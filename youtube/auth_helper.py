#!/usr/bin/env python3
"""
YouTube Channel Dedicated OAuth Authentication Helper
Authorizes the Google Account for the Health Videos channel.
Verifies channel identity, displays subscriber/video stats, and saves token.pickle securely.
"""

import sys
import os
from pathlib import Path

# Auto-bootstrap project virtual environment if executed via system Python
ROOT_PATH = Path(__file__).resolve().parent.parent
venv_python = ROOT_PATH / "venv" / "bin" / "python3"
if (sys.prefix == sys.base_prefix) and venv_python.exists():
    os.execv(str(venv_python), [str(venv_python)] + sys.argv)

import pickle
import argparse
import logging

# Add project root to sys.path
sys.path.insert(0, str(ROOT_PATH))

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

from config.settings import ROOT_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("health_videos.youtube_auth")

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube"
]

def verify_channel(creds):
    """Fetches and displays channel information to verify identity."""
    try:
        youtube = build("youtube", "v3", credentials=creds)
        response = youtube.channels().list(
            mine=True,
            part="snippet,statistics,contentDetails"
        ).execute()

        items = response.get("items", [])
        if not items:
            logger.warning("No YouTube channel found associated with this Google Account.")
            return False

        ch = items[0]
        snippet = ch.get("snippet", {})
        stats = ch.get("statistics", {})

        print("\n" + "=" * 60)
        print("  YOUTUBE CHANNEL AUTHENTICATION VERIFIED")
        print("=" * 60)
        print(f"  Channel Title:       {snippet.get('title', 'Unknown')}")
        print(f"  Channel ID:          {ch.get('id', 'Unknown')}")
        print(f"  Custom URL:          {snippet.get('customUrl', 'N/A')}")
        print(f"  Subscribers:         {stats.get('subscriberCount', '0')}")
        print(f"  Total Videos:        {stats.get('videoCount', '0')}")
        print(f"  Total Views:         {stats.get('viewCount', '0')}")
        print("=" * 60 + "\n")
        return True
    except Exception as e:
        logger.error(f"Error fetching channel information: {e}")
        return False

def authenticate(client_secrets_path: Path, token_output_path: Path, no_browser: bool = False):
    """Performs OAuth2 flow and saves credentials into token.pickle."""
    if not client_secrets_path.exists():
        logger.error(f"Client secrets file not found at: {client_secrets_path}")
        print("\n[ERROR] Missing client_secrets.json!")
        print("Please download OAuth 2.0 Client Credentials (Desktop application) from:")
        print("Google Cloud Console -> APIs & Services -> Credentials")
        print(f"And save it as: {client_secrets_path.resolve()}\n")
        return False

    creds = None
    if token_output_path.exists():
        try:
            with open(token_output_path, "rb") as f:
                creds = pickle.load(f)
            logger.info(f"Loaded existing token from {token_output_path}")
        except Exception as e:
            logger.warning(f"Could not load existing token: {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logger.info("Refreshing expired token...")
            try:
                creds.refresh(Request())
            except Exception as e:
                logger.warning(f"Token refresh failed: {e}. Re-authenticating.")
                creds = None

        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets_path), SCOPES)
            if no_browser:
                creds = flow.run_console()
            else:
                try:
                    creds = flow.run_local_server(port=8080, prompt="consent")
                except Exception as e:
                    logger.warning(f"Local server authorization failed ({e}). Falling back to console flow.")
                    creds = flow.run_console()

        # Save credentials with restrictive permissions
        with open(token_output_path, "wb") as f:
            pickle.dump(creds, f)
        os.chmod(str(token_output_path), 0o600)
        logger.info(f"Saved secure token to {token_output_path} (mode 0600)")

    # Verify channel
    success = verify_channel(creds)
    if success:
        logger.info("Authentication complete and channel verified!")
    return success

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Health Videos YouTube Channel OAuth Helper")
    parser.add_argument("--secrets", type=str, default=str(ROOT_DIR / "client_secrets.json"), help="Path to client_secrets.json")
    parser.add_argument("--token", type=str, default=str(ROOT_DIR / "token.pickle"), help="Output path for token.pickle")
    parser.add_argument("--no-browser", action="store_true", help="Use console URL copy-paste mode without starting local webserver")
    parser.add_argument("--check-only", action="store_true", help="Only verify current credentials without prompting login")

    args = parser.parse_args()

    token_p = Path(args.token)
    secrets_p = Path(args.secrets)

    if args.check_only:
        if not token_p.exists():
            print(f"No token found at {token_p}")
            sys.exit(1)
        with open(token_p, "rb") as f:
            c = pickle.load(f)
        ok = verify_channel(c)
        sys.exit(0 if ok else 1)

    authenticate(secrets_p, token_p, no_browser=args.no_browser)
