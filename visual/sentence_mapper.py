"""
Sentence-to-Visual Synchronization Engine
Maps every individual spoken narration sentence to a bespoke, contextually matched visual:
- Photorealistic 3D anatomical models
- Microscopic cellular / fluid dynamics
- Relatable real-life human scenes
- High-tech medical HUD overlays
Grounded directly in the 7 reference photos.
"""

import os
import logging
from pathlib import Path
from typing import List, Dict, Any

from config.settings import OUTPUT_DIR, ASSETS_DIR
from visual.pexels_client import PexelsClient
from visual.medical_hud import MedicalHUDGenerator

logger = logging.getLogger("health_videos.sentence_mapper")

class SentenceVisualMapper:
    def __init__(self):
        self.pexels = PexelsClient()
        self.hud_gen = MedicalHUDGenerator()
        self.ref_dir = ASSETS_DIR / "references"
        self.cache_dir = ASSETS_DIR / "visual_cache"

    def map_scenes_to_visuals(
        self,
        topic_id: str,
        category: str,
        scenes: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Assigns bespoke visual footage, HUD overlays, and camera movement to each sentence scene.
        """
        visuals_dir = OUTPUT_DIR / "visuals" / topic_id
        visuals_dir.mkdir(parents=True, exist_ok=True)
        mapped_scenes = []

        # Available reference images for anatomical fallbacks
        ref_images = sorted(list(self.ref_dir.glob("media_*.png")))

        used_assets = set()

        for idx, scene in enumerate(scenes):
            sc = dict(scene)
            v_type = sc.get("visual_type", "3d_anatomy")
            desc = sc.get("visual_description", "").lower()
            is_hook = (idx == 0) or sc.get("is_hook_scene", False)
            
            # Extract structured title hierarchy (Issue A & V3 fix)
            main_title = sc.get("main_title") or sc.get("text_overlay") or "MEDICAL SCAN"
            concept_badge = sc.get("concept_badge")
            statistic = sc.get("statistic")
            hook_text = sc.get("sentence") if is_hook else None
            hook_keywords = ["brain", "dimaag", "toxic", "waste", "flush", "wash", "raat", "sleep", "rest", "danger", "secret", "truth"]
            highlight_words = sc.get("highlight_words") or []
            if is_hook:
                highlight_words = list(set(highlight_words + hook_keywords))
            elif not highlight_words:
                highlight_words = ["brain", "heart", "cells", "fluid", "body", "sleep"]

            # 1. Generate clean overlay image (Netflix style)
            hud_path = visuals_dir / f"hud_scene_{idx:02d}.png"
            self.hud_gen.generate_hud_overlay(
                main_title=main_title,
                category=category,
                output_path=hud_path,
                concept_badge=concept_badge,
                statistic=statistic,
                is_hook_scene=is_hook,
                hook_text=hook_text,
                highlight_words=highlight_words
            )
            sc["hud_overlay_path"] = str(hud_path)

            # 2. Determine best video/visual asset (Ensure ZERO repeated visuals across scenes)
            asset_path = None
            if idx == 0:
                # Scene 0 (Hook): Contextual 3D anatomical organ/system visual
                if any(k in desc for k in ["stomach", "gastric", "acid", "digestive"]):
                    stomach_clip = self.cache_dir / "stomach_anatomy.mp4"
                    if stomach_clip.exists():
                        asset_path = str(stomach_clip)
                elif any(k in desc for k in ["liver", "regrowth", "regeneration", "hyperplasia", "hepatocyte"]):
                    liver_clip = self.cache_dir / "human_anatomy_cells.mp4"
                    if liver_clip.exists():
                        asset_path = str(liver_clip)
                elif any(k in desc for k in ["brain", "neural", "mind", "predictive", "synapse", "head"]):
                    ref_brain = self.ref_dir / "media_1794379567781.png"
                    if ref_brain.exists():
                        asset_path = str(ref_brain)
            elif idx == 1 and any(k in desc for k in ["sleep", "bed", "night", "rest"]):
                # Scene 1 (Sleep Transition): Real person sleeping peacefully in bed
                sleep_clip = self.cache_dir / "person_sleeping_in_bed.mp4" if hasattr(self, 'cache_dir') else None
                if sleep_clip and sleep_clip.exists():
                    asset_path = str(sleep_clip)
                else:
                    clip_path = self.pexels.search_video(query="person sleeping in bed")
                    if clip_path and Path(clip_path).exists():
                        asset_path = clip_path

            if not asset_path or asset_path in used_assets:
                # Direct scientific concept matching against local verified 3D assets
                cache_candidates = []
                if any(k in desc for k in ["stomach", "gastric", "acid", "digestive"]):
                    cache_candidates.append("stomach_anatomy.mp4")
                if any(k in desc for k in ["liver", "regrowth", "regeneration", "hepatocyte"]):
                    cache_candidates.append("human_anatomy_cells.mp4")
                if any(k in desc for k in ["fluid", "flush", "cerebrospinal", "csf", "interstitial", "wash"]):
                    cache_candidates.append("liquid_fluid_flow_microscopic.mp4")
                if any(k in desc for k in ["cell", "glial", "cellular", "pathway", "shrink", "neuron", "synapse", "protein", "plaque", "mitosis"]):
                    cache_candidates.extend(["cells_microscopic_laboratory.mp4", "cellular_biology_microscopic_laboratory.mp4"])
                if any(k in desc for k in ["brain", "neural", "glymphatic", "head", "mind", "predictive"]):
                    cache_candidates.extend(["human_brain_3d.mp4", "human_brain_medical_animation_3d.mp4", "human_brain_medical_animation.mp4"])
                if any(k in desc for k in ["sleep", "bed", "night", "rest"]):
                    cache_candidates.append("person_sleeping_in_bed.mp4")
                if any(k in desc for k in ["water", "drink", "hydrate", "health"]):
                    cache_candidates.append("person_drinking_water_fitness.mp4")
                if any(k in desc for k in ["heart", "cardio", "pulse", "blood pressure"]):
                    cache_candidates.append("human_heart_3d_medical.mp4")

                for cc in cache_candidates:
                    cp = self.cache_dir / cc
                    if cp.exists() and str(cp) not in used_assets:
                        asset_path = str(cp)
                        break

            if not asset_path or asset_path in used_assets:
                # Query Pexels based on narrative role
                if v_type == "3d_anatomy":
                    if any(k in desc for k in ["brain", "neural", "glymphatic", "head", "mind"]):
                        query = "human brain medical animation 3d"
                    elif any(k in desc for k in ["heart", "cardio", "pulse", "blood pressure"]):
                        query = "human heart 3d medical animation"
                    elif any(k in desc for k in ["spine", "spinal", "nerve"]):
                        query = "human spine medical animation"
                    else:
                        query = "human anatomy 3d medical animation"
                elif v_type == "microscopic":
                    if any(k in desc for k in ["blood", "vessel", "artery"]):
                        query = "blood cells microscopic flow"
                    elif any(k in desc for k in ["fluid", "flush", "toxin", "water"]):
                        query = "liquid fluid flow microscopic"
                    elif any(k in desc for k in ["neuron", "synapse"]):
                        query = "neurons synaptic firing microscopic"
                    else:
                        query = "cellular biology microscopic laboratory"
                elif v_type == "relatable_footage":
                    if any(k in desc for k in ["sleep", "bed", "night", "rest"]):
                        query = "person sleeping in bed"
                    elif any(k in desc for k in ["water", "drink", "hydrate"]):
                        query = "person drinking clean water"
                    elif any(k in desc for k in ["stress", "tired", "headache"]):
                        query = "person tired resting face"
                    else:
                        query = "healthy person morning wellness"
                else:
                    query = "medical technology laboratory"

                clip_path = self.pexels.search_video(query=query)
                if clip_path and Path(clip_path).exists() and clip_path not in used_assets:
                    asset_path = clip_path

            # If still None or duplicate, cycle through distinct 3D reference images
            if not asset_path or asset_path in used_assets:
                for cand in ref_images:
                    if str(cand) not in used_assets:
                        asset_path = str(cand)
                        break

            # Absolute fallback
            if not asset_path:
                asset_path = str(ref_images[idx % len(ref_images)]) if ref_images else None

            used_assets.add(asset_path)
            sc["asset_path"] = asset_path
            mapped_scenes.append(sc)

        logger.info(f"Mapped {len(mapped_scenes)} sentence scenes to tailored visual assets.")
        return mapped_scenes
