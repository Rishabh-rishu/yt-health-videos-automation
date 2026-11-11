"""
Hook Generation Agent for Health Videos
Generates 3 scientifically accurate, compelling 0-2 second hook variations.
Styles: Curiosity, Mystery, Question, Unexpected Science, Relatable.
Picks the strongest hook with immediate visual synergy.
"""

import json
import logging
import requests
from typing import Dict, Any, List

from config.settings import GEMINI_API_KEY, GEMINI_MODEL

logger = logging.getLogger("health_videos.hook_generator")

class HookGeneratorAgent:
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.model = GEMINI_MODEL

    def generate_hooks(self, title: str, category: str, core_science: str) -> Dict[str, Any]:
        """
        Generates 3 hook variations and selects the strongest scientifically accurate hook.
        """
        prompt = f"""
        Act as an award-winning Medical Documentary Director and YouTube Hook Specialist.
        Generate 3 distinct 0-2 second viral opening hooks for a health documentary YouTube Short.
        
        Topic: {title}
        Category: {category}
        Core Science: {core_science}

        Hook Requirements:
        - Must be spoken in natural conversational Hinglish.
        - Exactly 1 to 2 short punchy sentences (under 12 words total).
        - Hook Style 1: Curiosity / Mystery (e.g., "Aapka brain sote waqt bhi ek secret kaam karta hai!")
        - Hook Style 2: Direct Question (e.g., "Kabhi socha hai jab aap sote hain toh dimag ke andar kya hota hai?")
        - Hook Style 3: Relatable / Unexpected Science (e.g., "Agar aap 7 ghante se kam sote hain, toh ye science zaroor dekhiye.")
        - NO 'Hello friends', NO 'Welcome back', NO medical scare tactics or fake claims.
        - Opening visual must be dynamic (e.g. 3D holographic brain flare, beating heart cutaway).

        Return strictly valid JSON:
        {{
            "hooks": [
                {{"style": "Curiosity", "text": "...", "opening_visual": "3D holographic glowing brain in dark cinematic space"}},
                {{"style": "Question", "text": "...", "opening_visual": "Close-up of human eyes closing into microscopic neuron zoom"}},
                {{"style": "Relatable", "text": "...", "opening_visual": "Person sleeping peacefully with glowing synaptic HUD overlay"}}
            ],
            "selected_index": 0,
            "selection_rationale": "Strongest curiosity loop with immediate 3D anatomical impact."
        }}
        """

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        try:
            resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                if "```json" in text:
                    text = text.split("```json")[1].split("```")[0].strip()
                elif "```" in text:
                    text = text.split("```")[1].split("```")[0].strip()
                res = json.loads(text)
                return res
        except Exception as e:
            logger.warning(f"Hook generation API call failed: {e}. Using deterministic high-performing hooks.")

        # Deterministic fallback hooks
        hooks = [
            {
                "style": "Curiosity",
                "text": "Jab aap sote hain, aapka brain bilkul shaant nahi hota!",
                "opening_visual": "3D holographic translucent human head with glowing brain synaptic activation"
            },
            {
                "style": "Question",
                "text": "Kabhi socha hai neend mein aapke dimag ka kachra kaise saaf hota hai?",
                "opening_visual": "Microscopic CSF fluid rushing through cerebral tissue flushing waste particles"
            },
            {
                "style": "Relatable",
                "text": "Agar aap roz late night sote hain, toh aapka brain ye critical kaam miss kar deta hai.",
                "opening_visual": "Split screen of sleeping person contrasting with glowing 3D neural network"
            }
        ]
        return {
            "hooks": hooks,
            "selected_index": 0,
            "selection_rationale": "High engagement curiosity hook with instant 3D anatomical support."
        }
