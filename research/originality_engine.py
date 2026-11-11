"""
Master Anti-Repetition & 100% Video Originality Engine for Health Videos
Ensures every generated YouTube Short has completely unique storytelling, scientific angles,
scene visual sequences, and audio beds.
Enforces multi-layer semantic, n-gram, and visual sequence deduplication before rendering.
"""

import re
import math
import hashlib
import difflib
import logging
from typing import Dict, Any, List, Tuple, Optional
from collections import Counter

from database.db_manager import DatabaseManager

logger = logging.getLogger("health_videos.originality_engine")

class OriginalityEngine:
    """
    Evaluates new topics, scripts, hooks, and scene sequences against all historical
    productions in the SQLite master catalog to guarantee 100% originality.
    """
    def __init__(self, db: Optional[DatabaseManager] = None):
        self.db = db or DatabaseManager()
        self.max_topic_similarity_threshold = 0.50
        self.max_hook_similarity_threshold = 0.50
        self.max_script_similarity_threshold = 0.60
        self.max_visual_sequence_threshold = 0.55

    @staticmethod
    def _normalize_text(text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        return " ".join(text.split())

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        words = re.findall(r"\b\w{2,}\b", text.lower())
        stopwords = {
            "the", "is", "at", "which", "on", "and", "a", "an", "in", "to", "for",
            "of", "or", "by", "with", "this", "that", "hai", "ka", "ki", "ke", "ko",
            "mein", "se", "aur", "hota", "hoti", "hote", "bhi", "yeh", "kya", "kyun",
            "aap", "aapka", "aapki", "apne", "par"
        }
        return [w for w in words if w not in stopwords]

    @classmethod
    def _n_grams(cls, tokens: List[str], n: int = 2) -> set:
        if len(tokens) < n:
            return set(tokens)
        return set(tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1))

    @classmethod
    def jaccard_similarity(cls, text_a: str, text_b: str, n: int = 1) -> float:
        tokens_a = cls._tokenize(text_a)
        tokens_b = cls._tokenize(text_b)
        if not tokens_a or not tokens_b:
            return 0.0

        if n == 1:
            set_a, set_b = set(tokens_a), set(tokens_b)
        else:
            set_a = cls._n_grams(tokens_a, n)
            set_b = cls._n_grams(tokens_b, n)

        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))
        return intersection / union if union > 0 else 0.0

    @classmethod
    def cosine_similarity(cls, text_a: str, text_b: str) -> float:
        tokens_a = cls._tokenize(text_a)
        tokens_b = cls._tokenize(text_b)
        if not tokens_a or not tokens_b:
            return 0.0

        vec_a = Counter(tokens_a)
        vec_b = Counter(tokens_b)

        intersection = set(vec_a.keys()) & set(vec_b.keys())
        numerator = sum(vec_a[x] * vec_b[x] for x in intersection)

        sum1 = sum(vec_a[x] ** 2 for x in vec_a.keys())
        sum2 = sum(vec_b[x] ** 2 for x in vec_b.keys())
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        return float(numerator) / denominator

    @classmethod
    def sequence_similarity(cls, seq_a: List[str], seq_b: List[str]) -> float:
        """Measures similarity between two ordered sequences of visual asset paths/IDs."""
        if not seq_a or not seq_b:
            return 0.0
        matcher = difflib.SequenceMatcher(None, seq_a, seq_b)
        return matcher.ratio()

    @staticmethod
    def generate_video_fingerprint(title: str, script_text: str, visual_assets: List[str]) -> str:
        """Computes deterministic SHA-256 fingerprint for pre-render deduplication."""
        norm_title = " ".join(title.lower().split())
        norm_script = " ".join(script_text.lower().split())
        norm_assets = "|".join([str(a).lower().split("/")[-1] for a in visual_assets])
        payload = f"{norm_title}::{norm_script}::{norm_assets}".encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def check_originality(
        self,
        topic_title: str,
        script_text: str,
        hook_text: str = "",
        scenes: Optional[List[Dict[str, Any]]] = None,
        bgm_track_id: str = "",
        exclude_topic_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Runs the full 8-point Anti-Repetition & Originality Pre-Render Approval Gate.
        Returns a detailed report with overall passed status and individual gate scores.
        """
        past_topics = self.db.get_all_past_topics()
        past_videos = self.db.get_all_past_videos()
        recent_bgm_ids = self.db.get_recent_bgm_tracks(limit=5)

        asset_ids = []
        camera_moves = []
        if scenes:
            for s in scenes:
                asset_path = s.get("asset_path", "")
                if asset_path:
                    asset_ids.append(asset_path.split("/")[-1])
                camera_moves.append(s.get("camera_movement", "slow_push"))

        current_fingerprint = self.generate_video_fingerprint(topic_title, script_text, asset_ids)

        # ---------------- Gate 1: Topic Uniqueness ----------------
        max_topic_sim = 0.0
        matched_topic_title = ""
        for t in past_topics:
            if exclude_topic_id and t.get("topic_id") == exclude_topic_id:
                continue
            sim = max(
                self.cosine_similarity(topic_title, t.get("title", "")),
                self.jaccard_similarity(topic_title, t.get("title", ""))
            )
            if sim > max_topic_sim:
                max_topic_sim = sim
                matched_topic_title = t.get("title", "")

        gate1_pass = max_topic_sim < self.max_topic_similarity_threshold

        # ---------------- Gate 2: Hook Originality ----------------
        max_hook_sim = 0.0
        matched_hook_text = ""
        effective_hook = hook_text or (script_text.split(".")[0] if script_text else "")
        for t in past_topics:
            if exclude_topic_id and t.get("topic_id") == exclude_topic_id:
                continue
            past_hook = t.get("hook", "")
            if past_hook:
                sim = max(
                    self.cosine_similarity(effective_hook, past_hook),
                    self.jaccard_similarity(effective_hook, past_hook, n=2)
                )
                if sim > max_hook_sim:
                    max_hook_sim = sim
                    matched_hook_text = past_hook

        gate2_pass = max_hook_sim < self.max_hook_similarity_threshold

        # ---------------- Gate 3: Script Semantic Novelty ----------------
        max_script_sim = 0.0
        matched_script_id = ""
        for v in past_videos:
            if exclude_topic_id and v.get("topic_id") == exclude_topic_id:
                continue
            past_script = v.get("script_text", "")
            if past_script:
                cos_sim = self.cosine_similarity(script_text, past_script)
                jacc_sim = self.jaccard_similarity(script_text, past_script, n=2)
                sim = 0.6 * cos_sim + 0.4 * jacc_sim
                if sim > max_script_sim:
                    max_script_sim = sim
                    matched_script_id = v.get("video_id", "")

        gate3_pass = max_script_sim < self.max_script_similarity_threshold

        # ---------------- Gate 4: Visual Asset Sequence Distinction ----------------
        max_seq_sim = 0.0
        matched_seq_video_id = ""
        for v in past_videos:
            if exclude_topic_id and v.get("topic_id") == exclude_topic_id:
                continue
            past_assets = v.get("visual_asset_ids", [])
            if isinstance(past_assets, list) and past_assets:
                sim = self.sequence_similarity(asset_ids, past_assets)
                if sim > max_seq_sim:
                    max_seq_sim = sim
                    matched_seq_video_id = v.get("video_id", "")

        gate4_pass = max_seq_sim < self.max_visual_sequence_threshold

        # ---------------- Gate 5: Camera / Animation Variety ----------------
        unique_moves = len(set(camera_moves))
        gate5_pass = unique_moves >= min(2, len(camera_moves)) if camera_moves else True

        # ---------------- Gate 6: Background Music Rotation ----------------
        gate6_pass = bgm_track_id not in recent_bgm_ids if bgm_track_id and recent_bgm_ids else True

        # ---------------- Gate 7: Video Fingerprint Collision ----------------
        collision_found = any(
            v.get("video_fingerprint") == current_fingerprint
            for v in past_videos
            if not (exclude_topic_id and v.get("topic_id") == exclude_topic_id)
        )
        gate7_pass = not collision_found

        # ---------------- Gate 8: Rejected Ideas History Check ----------------
        recent_rejected = self.db.get_recent_rejected_attempts(limit=30)
        max_rejected_sim = 0.0
        for r in recent_rejected:
            sim = self.cosine_similarity(topic_title, r.get("content_payload", ""))
            if sim > max_rejected_sim:
                max_rejected_sim = sim
        gate8_pass = max_rejected_sim < 0.65

        # Overall Verdict
        gates = {
            "gate1_topic_uniqueness": {
                "passed": gate1_pass,
                "score": round(1.0 - max_topic_sim, 3),
                "similarity": round(max_topic_sim, 3),
                "threshold": self.max_topic_similarity_threshold,
                "matched_against": matched_topic_title
            },
            "gate2_hook_originality": {
                "passed": gate2_pass,
                "score": round(1.0 - max_hook_sim, 3),
                "similarity": round(max_hook_sim, 3),
                "threshold": self.max_hook_similarity_threshold,
                "matched_against": matched_hook_text[:60] if matched_hook_text else ""
            },
            "gate3_script_novelty": {
                "passed": gate3_pass,
                "score": round(1.0 - max_script_sim, 3),
                "similarity": round(max_script_sim, 3),
                "threshold": self.max_script_similarity_threshold,
                "matched_against": matched_script_id
            },
            "gate4_visual_sequence_distinction": {
                "passed": gate4_pass,
                "score": round(1.0 - max_seq_sim, 3),
                "similarity": round(max_seq_sim, 3),
                "threshold": self.max_visual_sequence_threshold,
                "matched_against": matched_seq_video_id
            },
            "gate5_camera_variety": {
                "passed": gate5_pass,
                "score": 1.0 if gate5_pass else 0.5,
                "details": f"{unique_moves} distinct camera movements in {len(camera_moves)} scenes"
            },
            "gate6_bgm_rotation": {
                "passed": gate6_pass,
                "score": 1.0 if gate6_pass else 0.0,
                "details": f"Track '{bgm_track_id}' not in last 5 used ({recent_bgm_ids})"
            },
            "gate7_fingerprint_unique": {
                "passed": gate7_pass,
                "fingerprint": current_fingerprint[:16],
                "details": "Zero fingerprint collisions" if gate7_pass else "DUPLICATE FINGERPRINT DETECTED"
            },
            "gate8_rejected_ideas_safe": {
                "passed": gate8_pass,
                "score": round(1.0 - max_rejected_sim, 3),
                "similarity": round(max_rejected_sim, 3),
                "details": f"Max similarity to rejected concepts: {max_rejected_sim:.2f}"
            }
        }

        passed_count = sum(1 for g in gates.values() if g["passed"])
        overall_originality_score = round(
            (gates["gate1_topic_uniqueness"]["score"] * 0.25) +
            (gates["gate2_hook_originality"]["score"] * 0.20) +
            (gates["gate3_script_novelty"]["score"] * 0.25) +
            (gates["gate4_visual_sequence_distinction"]["score"] * 0.20) +
            (gates["gate6_bgm_rotation"]["score"] * 0.10),
            3
        )
        approved = passed_count == 8 and overall_originality_score >= 0.70

        report = {
            "approved": approved,
            "overall_originality_score": overall_originality_score,
            "passed_gates": f"{passed_count}/8",
            "fingerprint": current_fingerprint,
            "gates": gates
        }

        if not approved:
            reason = f"Originality Gate Failure: {8 - passed_count} checks failed. Score={overall_originality_score}"
            self.db.record_rejected_attempt(
                attempt_type="similarity_gating",
                content_payload={"title": topic_title, "hook": effective_hook},
                rejection_reason=reason,
                similarity_score=max(max_topic_sim, max_script_sim, max_seq_sim),
                matched_entity_id=matched_topic_title or matched_script_id
            )
            logger.warning(f"Production Gated: {reason}")
        else:
            logger.info(f"Production Approved: 100% Originality Passed (Score: {overall_originality_score:.3f}, Fingerprint: {current_fingerprint[:12]})")

        return report
