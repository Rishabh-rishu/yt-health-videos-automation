"""
YouTube Metadata & SEO Engine for Health Videos
Generates high-CTR, SEO-optimized titles, descriptions, and hashtags.
Includes mandatory medical education disclaimer and NIH/PubMed source citations.
"""

from typing import Dict, Any, List

class MetadataGenerator:
    def generate_metadata(
        self,
        title: str,
        category: str,
        core_science: str,
        sources: List[str]
    ) -> Dict[str, Any]:
        """
        Creates publication-ready title, description, tags, and hashtags.
        """
        # Clean Short title under 60 chars
        clean_title = f"{title} 🧠 #Shorts #Health"
        if len(clean_title) > 95:
            clean_title = f"{title[:75]}... #Shorts"

        sources_formatted = "\n".join(f"• {s}" for s in sources)

        description = f"""{clean_title}

🔬 Scientific Insight:
{core_science}

📚 Medical References & Sources:
{sources_formatted}

⚠️ Medical Disclaimer:
This video is created solely for educational and science awareness purposes. It does not constitute medical advice. Always consult a qualified physician or healthcare professional for medical diagnoses.

#Shorts #Health #HumanBody #Science #Biology #BrainHealth #MedicalScience #HealthTips #HindiHealthTips
"""

        tags = [
            "health", "human body", "science documentary", "biology",
            "brain science", "sleep science", "medical animation",
            "3d anatomy", "health shorts", "shorts"
        ]

        return {
            "title": clean_title,
            "description": description,
            "tags": tags,
            "categoryId": "27"  # Education
        }
