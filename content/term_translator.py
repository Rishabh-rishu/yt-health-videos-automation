"""
Scientific Language Simplification Engine (Scientific Term Translator)
Translates complex medical, anatomical, and biological terms into crystal-clear Hinglish.
Enforces the mandatory YouTube Shorts communication pattern:
[Simple Explanation] -> [Scientific Name] -> [Why It Matters]

Also provides:
- TTS-friendly phonetic spellings for Edge-TTS (hi-IN-SwaraNeural)
- On-screen terminology badge specifications (Title + Subtitle explanation pill)
"""

import re
import logging
from typing import Dict, Any, Optional, Tuple, List

logger = logging.getLogger("health_videos.term_translator")

# Comprehensive Medical & Biological Terminology Knowledge Base
SCIENTIFIC_DICTIONARY: Dict[str, Dict[str, Any]] = {
    "predictive_processing": {
        "term": "Predictive Processing",
        "tts_phonetic": "Predictive Processing",
        "simple_explanation": "Aapka brain har second aane wale signals ko pehle se guess karta hai",
        "why_it_matters": "Taaki aap bina delay ke tezi se react kar sakein",
        "script_phrase": "Aapka brain duniya ko real-time mein nahi, balki pehle se predict karke process karta hai. Science mein is mechanism ko Predictive Processing kehte hain, jisse aap instantly react kar paate hain.",
        "badge_title": "PREDICTIVE PROCESSING",
        "badge_sub": "Brain ka sensory guess mechanism"
    },
    "nasal_cycle": {
        "term": "Nasal Cycle",
        "tts_phonetic": "Nasal Cycle",
        "simple_explanation": "Aapki dono nostrils mein se ek waqt par sirf ek hi zyada khuli hoti hai",
        "why_it_matters": "Taaki ek side rest karke moisture recover kar sake aur smell receptors sharp rahein",
        "script_phrase": "Aapki ek nostril zyada hawa leti hai aur doosri rest karti hai, phir kuch ghanton baad ye switch ho jaati hain. Is natural body rhythm ko Nasal Cycle kehte hain.",
        "badge_title": "NASAL CYCLE",
        "badge_sub": "Nostrils ka alternating airflow"
    },
    "muscle_atonia": {
        "term": "REM Sleep Muscle Atonia",
        "tts_phonetic": "REM Muscle Atonia",
        "simple_explanation": "Sapne dekhte waqt brain temporary tor par body ke voluntary muscles ko switch off kar deta hai",
        "why_it_matters": "Taaki aap sapne mein bhaagte waqt sach mein bed se gir na jayein",
        "script_phrase": "Jab aap sapna dekh rahe hote hain, aapka brain motor signals ko block kar deta hai. Is temporary body freeze ko Muscle Atonia kehte hain, jo aapko physically safe rakhta hai.",
        "badge_title": "MUSCLE ATONIA",
        "badge_sub": "Sapne ke waqt temporary muscle paralysis"
    },
    "vestibular_system": {
        "term": "Vestibular System",
        "tts_phonetic": "Vestibular System",
        "simple_explanation": "Aapke kaan ke andar fluid se bhari tiny tubes hoti hain jo balance banaye rakhti hain",
        "why_it_matters": "Ghoomne ke baad fluid chalta rehta hai, isliye brain ko lagta hai ki aap abhi bhi ghoom rahe hain",
        "script_phrase": "Aapke inner ear ke andar semicircular canals hoti hain jisme liquid move karta hai. Is body balance system ko Vestibular System kehte hain.",
        "badge_title": "VESTIBULAR SYSTEM",
        "badge_sub": "Inner ear ka balance network"
    },
    "piloerection": {
        "term": "Piloerection",
        "tts_phonetic": "Pilo-erection",
        "simple_explanation": "Skin ke niche ki tiny muscles contract hokar hair follicles ko seedha khada kar deti hain",
        "why_it_matters": "Thand ya dar mein body heat trap karne aur alert hone ke liye",
        "script_phrase": "Dar ya thand lagte hi skin ke baal khade ho jaate hain. Science mein is automatic reflex ko Piloerection ya goosebumps kehte hain.",
        "badge_title": "PILOERECTION",
        "badge_sub": "Skin muscles ka tightening reflex"
    },
    "sa_node": {
        "term": "Sinoatrial (SA) Node",
        "tts_phonetic": "SA Node",
        "simple_explanation": "Heart ke andar ek natural electric generator hota hai jo har dhadkan ka current banata hai",
        "why_it_matters": "Isi electrical pulse ki wajah se heart brain ke bina bhi beat karta reh sakta hai",
        "script_phrase": "Aapke heart ke paas apna biological power station hai jo natural electrical current banata hai. Is natural pacemaker ko SA Node kehte hain.",
        "badge_title": "SA NODE",
        "badge_sub": "Heart ka natural electric pacemaker"
    },
    "gastric_mucus_barrier": {
        "term": "Gastric Mucus Barrier",
        "tts_phonetic": "Gastric Mucus Barrier",
        "simple_explanation": "Stomach ki walls par alkaline mucus ki ek thick shield hoti hai",
        "why_it_matters": "Jo razor blade melt karne wale hydrochloric acid ko pet ki walls tak pahunchne nahi deti",
        "script_phrase": "Aapke stomach mein powerful hydrochloric acid hota hai, lekin bicarbonate se bani ek thick protective gel layer use rokti hai. Ise Gastric Mucus Barrier kehte hain.",
        "badge_title": "MUCUS BARRIER",
        "badge_sub": "Acid se bachane wali protective shield"
    },
    "erythrocyte_clearance": {
        "term": "Red Blood Cell Lifecycle",
        "tts_phonetic": "RBC Lifecycle",
        "simple_explanation": "Har red blood cell lagbhag 120 din jeeti hai aur phir spleen use recycle kar deta hai",
        "why_it_matters": "Taaki purani damaged cells blood vessels ko block na karein aur fresh oxygen flow bana rahe",
        "script_phrase": "Aapke red blood cells sirf 120 din tak active rehti hain. Iske baad spleen in purani cells ko filter karke naye cells banne ki jagah deta hai.",
        "badge_title": "RBC LIFECYCLE",
        "badge_sub": "Blood cells ka 120-day replacement"
    },
    "doorway_effect": {
        "term": "Doorway Effect (Event Boundary)",
        "tts_phonetic": "Doorway Effect",
        "simple_explanation": "Jab aap ek room se doosre room mein jaate hain, brain purani information ka file band karke naya page open karta hai",
        "why_it_matters": "Is mental boundary ki wajah se working memory se previous task temporarily wipe ho jata hai",
        "script_phrase": "Doorway cross karte hi brain purane context ko reset karke naya memory folder khol deta hai. Psychology mein ise Doorway Effect ya Event Boundary kehte hain.",
        "badge_title": "DOORWAY EFFECT",
        "badge_sub": "Brain ka environment reset reflex"
    },
    "phosphenes": {
        "term": "Phosphenes",
        "tts_phonetic": "Fos-feens",
        "simple_explanation": "Aankh dabane par retina ke light sensors physically activate hokar flashes dikhate hain",
        "why_it_matters": "Bina kisi actual light ke bhi brain in mechanical signals ko roshni samajh leta hai",
        "script_phrase": "Aankhein rub karne par jo colorful lights aur stars dikhte hain, woh physical pressure se retina excite hone ki wajah se hote hain. Inhe Phosphenes kehte hain.",
        "badge_title": "PHOSPHENES",
        "badge_sub": "Bina light ke aankh mein flashes"
    },
    "hypnic_jerk": {
        "term": "Hypnic Jerk",
        "tts_phonetic": "Hip-nik Jerk",
        "simple_explanation": "Sote waqt jab muscles achanak relax hoti hain, toh brain ko lagta hai ki aap unchai se gir rahe hain",
        "why_it_matters": "Brain turant involuntary shock bhejta hai taaki aap girne se bach sakein",
        "script_phrase": "Neend mein achanak girne ka ehsaas hona aur jhatka lagna ek involuntary muscle twitch hai. Science mein ise Hypnic Jerk kehte hain.",
        "badge_title": "HYPNIC JERK",
        "badge_sub": "Sote waqt achanak jhatka"
    },
    "earworms": {
        "term": "Involuntary Musical Imagery (Earworm)",
        "tts_phonetic": "Earworm Effect",
        "simple_explanation": "Ek catchy tune aapke brain ke auditory memory loop mein fas kar baar baar repeat hoti hai",
        "why_it_matters": "Brain incomplete pattern ko poora karne ke liye use baar-baar replay karta rehta hai",
        "script_phrase": "Jab koi song dimaag mein continuously bajta rehta hai, toh ye auditory cortex ka ek mental loop hota hai. Ise Earworm ya Involuntary Musical Imagery kehte hain.",
        "badge_title": "EARWORM EFFECT",
        "badge_sub": "Dimag mein ghoomta repetitive song"
    },
    "alveoli": {
        "term": "Alveoli",
        "tts_phonetic": "Al-vee-o-lai",
        "simple_explanation": "Lungs ke andar grape-like clusters jaise millions of microscopic air sacs hote hain",
        "why_it_matters": "Yahin par blood mein oxygen add hoti hai aur carbon dioxide bahar nikalne ke liye transfer hoti hai",
        "script_phrase": "Aapke lungs ke andar lagbhag 500 million microscopic air sacs hote hain jahan gas exchange hota hai. In tiny spongy sacs ko Alveoli kehte hain.",
        "badge_title": "ALVEOLI",
        "badge_sub": "Lungs ki tiny oxygen-exchange sacs"
    },
    "memory_reconsolidation": {
        "term": "Memory Reconsolidation",
        "tts_phonetic": "Memory Reconsolidation",
        "simple_explanation": "Har baar jab aap kisi purani baat ko yaad karte hain, memory temporary tor par fragile ho jaati hai aur nayi details jud jaati hain",
        "why_it_matters": "Isliye purani memories exact camera recording nahi, balki rewrite hoti rehti hain",
        "script_phrase": "Aapki memory fixed CD recording ki tarah nahi hai; yaad karte waqt brain use dobara save karta hai. Is process ko Memory Reconsolidation kehte hain.",
        "badge_title": "RECONSOLIDATION",
        "badge_sub": "Har baar recall par memory ka rewrite hona"
    },
    "liver_regeneration": {
        "term": "Compensatory Hyperplasia (Liver Regeneration)",
        "tts_phonetic": "Liver Regeneration",
        "simple_explanation": "Liver ke cells apne original shape aur size ko restore karne ke liye tezi se divide ho sakte hain",
        "why_it_matters": "Agar liver ka 70% hissa nikal bhi diya jaye, toh bhi bacha hua hissa fully grow kar leta hai",
        "script_phrase": "Human body mein liver ek aisa unique organ hai jo tissue loss ke baad apne hepatocyte cells ko multiply karke full size mein regrow kar sakta hai. Ise Compensatory Hyperplasia kehte hain.",
        "badge_title": "LIVER REGROWTH",
        "badge_sub": "Organ ka apna tissue dobara grow karna"
    },
    "vagus_nerve": {
        "term": "Vagus Nerve",
        "tts_phonetic": "Vagus Nerve",
        "simple_explanation": "Brainstem se nikal kar pet, heart aur gut tak jaane wali body ki sabse lambi cranial communication wire",
        "why_it_matters": "Isi se gut ka digestion status aur mood chemicals brain tak pahunchte hain",
        "script_phrase": "Aapke brain aur digestive system ke beech 100,000 se zyada nerve fibers ka superfast highway hai. Is crucial biological link ko Vagus Nerve kehte hain.",
        "badge_title": "VAGUS NERVE",
        "badge_sub": "Brain aur gut ka communication highway"
    },
    "afterimages": {
        "term": "Photoreceptor Adaptation (Afterimages)",
        "tts_phonetic": "Afterimages",
        "simple_explanation": "Retina ke color sensors thak jaate hain, isliye aankhein hatane par opposite color ka ghost image dikhta hai",
        "why_it_matters": "Photoreceptors ko recharge hone ke liye kuch seconds ka waqt lagta hai",
        "script_phrase": "Bright light ya color dekhne ke baad aankhon ke aage bhoot jaisi image bani rehti hai. Eye sensors ki is chemical fatigue ko Afterimages kehte hain.",
        "badge_title": "AFTERIMAGES",
        "badge_sub": "Retina sensors ka temporary adaptation"
    },
    "proprioception": {
        "term": "Proprioception",
        "tts_phonetic": "Pro-pree-o-sep-shun",
        "simple_explanation": "Aankhein band hone par bhi body ko exactly pata hota hai ki haath ya pair kahan hai",
        "why_it_matters": "Muscles aur joints mein lage biological sensors continuous positional feedback bhejte hain",
        "script_phrase": "Aankhein band karke bhi aap bina dekhe apni naak ko touch kar sakte hain. Muscles aur joints ke is natural 3D position sense ko Proprioception kehte hain.",
        "badge_title": "PROPRIOCEPTION",
        "badge_sub": "Body position ka natural 6th sense"
    },
    "sensory_attenuation": {
        "term": "Sensory Attenuation (Self-Touch)",
        "tts_phonetic": "Sensory Attenuation",
        "simple_explanation": "Jab aap khud ko touch karte hain, brain cerebellum ke zariye us sensation ko pehle hi predict karke cancel kar deta hai",
        "why_it_matters": "Isi wajah se aap khud ko tickle karke zor se nahi has sakte",
        "script_phrase": "Aapka cerebellum aapke apne movements ko pehle se predict karke sensory signal ko suppress kar deta hai. Is protective brain filter ko Sensory Attenuation kehte hain.",
        "badge_title": "SELF-TOUCH CANCEL",
        "badge_sub": "Khud ko tickle na kar paane ka brain secret"
    },
    "glymphatic_system": {
        "term": "Glymphatic System",
        "tts_phonetic": "Glymphatic System",
        "simple_explanation": "Gehri neend ke waqt brain cells shrink hoti hain aur fluid channels expand ho jaate hain",
        "why_it_matters": "Cerebrospinal fluid metabolic waste aur beta-amyloid ko flush karke dimaag ko fresh rakhta hai",
        "script_phrase": "Sote waqt brain cells space banati hain taaki fluid tezi se flow karke neurotoxic waste ko clear kar sake. Is nightly cleaning network ko Glymphatic System kehte hain.",
        "badge_title": "GLYMPHATIC SYSTEM",
        "badge_sub": "Neend mein dimaag ka fluid waste flush"
    },
    "auditory_arousal": {
        "term": "Auditory Brain Processing During Sleep",
        "tts_phonetic": "Auditory Processing",
        "simple_explanation": "Aapka kaan so nahi raha hota, bas thalamus important aur un-important sounds ko filter karta rehta hai",
        "why_it_matters": "Isliye rona ya apna naam sunte hi aap turant jaag jaate hain lekin AC ki awaaz ignore ho jaati hai",
        "script_phrase": "Neend mein bhi aapka auditory system active rehta hai aur brain ka gatekeeper yaani thalamus sounds ko monitor karta hai taaki khatra hone par aap jag sakein.",
        "badge_title": "AUDITORY MONITOR",
        "badge_sub": "Sote waqt bhi active hearing sensors"
    },
    "cold_diuresis": {
        "term": "Cold-Induced Diuresis",
        "tts_phonetic": "Cold Diuresis",
        "simple_explanation": "Thand lagte hi blood vessels contract hokar blood ko core organs mein bhejti hain jisse blood pressure badh jata hai",
        "why_it_matters": "Kidneys extra fluid ko urine bana kar nikal deti hain taaki pressure normalize rahe",
        "script_phrase": "Thand lagte hi shareer internal organs ko garam rakhne ke liye peripheral blood vessels ko shrink karta hai. Is response ko Cold-Induced Diuresis kehte hain.",
        "badge_title": "COLD DIURESIS",
        "badge_sub": "Thand mein kidney ka extra fluid release"
    },
    "contagious_yawning": {
        "term": "Contagious Yawning (Mirror Neurons)",
        "tts_phonetic": "Contagious Yawning",
        "simple_explanation": "Kisi ko jamhai lete dekh kar brain ke social empathy aur mirror neuron circuits trigger ho jaate hain",
        "why_it_matters": "Ye primitive human communication aur group synchronization ka natural reflex hai",
        "script_phrase": "Dusre ko jamhai lete dekh kar aapko bhi jamhai aana social connection aur empathy se juda hai. Science mein ise Contagious Yawning kehte hain.",
        "badge_title": "MIRROR REFLEX",
        "badge_sub": "Social empathy aur contagious yawning"
    },
    "tear_types": {
        "term": "Basal, Reflex & Emotional Tears",
        "tts_phonetic": "Tear Types",
        "simple_explanation": "Har aansu alag hota hai; aankh ko geela rakhne wale alag, pyaaz kaatne par alag aur dukh mein alag",
        "why_it_matters": "Emotional tears mein stress hormones aur natural pain-reliever chemicals mixed hote hain",
        "script_phrase": "Har baar rone par nikalne wale tears alag chemical composition ke hote hain. Emotional tears mein stress hormone prolactin hota hai jo rone ke baad relief deta hai.",
        "badge_title": "TEAR BIOCHEMISTRY",
        "badge_sub": "Basal, reflex aur emotional tears ka fark"
    },
    "gut_microbiome": {
        "term": "Gut Microbiome",
        "tts_phonetic": "Gut Microbiome",
        "simple_explanation": "Aapke pet mein lagbhag 38 trillion friendly bacteria aur microorganisms ka ek poora jungle rehta hai",
        "why_it_matters": "Jo vitamins banate hain, immune system ko train karte hain aur 90% serotonin produce karte hain",
        "script_phrase": "Aapke digestive system mein trillions of helpful bacteria rehte hain jo body ke digestion aur immunity ke real hero hain. Is living ecosystem ko Gut Microbiome kehte hain.",
        "badge_title": "GUT MICROBIOME",
        "badge_sub": "38 trillion friendly bacteria ka ecosystem"
    },
    "brown_fat": {
        "term": "Brown Adipose Tissue (Brown Fat)",
        "tts_phonetic": "Brown Fat",
        "simple_explanation": "Ye normal fat ki tarah calories store nahi karta, balki iron-rich mitochondria se energy jala kar heat banata hai",
        "why_it_matters": "Thand mein body temperature ko bina shiver kiye warm rakhne ke liye",
        "script_phrase": "Normal white fat calories store karta hai, lekin ek aisa special brown fat hota hai jo calories burn karke body ko warm rakhta hai. Ise Brown Adipose Tissue kehte hain.",
        "badge_title": "BROWN FAT",
        "badge_sub": "Heat produce karne wala healthy fat"
    },
    "nociplastic_pain": {
        "term": "Nociplastic Pain (Central Sensitization)",
        "tts_phonetic": "Nociplastic Pain",
        "simple_explanation": "Bina kisi physical cut ya bone damage ke bhi brain pain pathways ke hypersensitive hone se dard generate kar sakta hai",
        "why_it_matters": "Dard imaginary nahi hota, lekin volume knob brain ke nervous system mein atka hota hai",
        "script_phrase": "Kabhi-kabhi kisi physical injury ke bina bhi nerves hyper-alert hokar pain generate karti hain. Science mein is altered pain signalling ko Nociplastic Pain kehte hain.",
        "badge_title": "NOCIPLASTIC PAIN",
        "badge_sub": "Bina injury ke nervous system ka pain response"
    },
    "bone_remodeling": {
        "term": "Bone Remodeling (Osteoblasts & Osteoclasts)",
        "tts_phonetic": "Bone Remodeling",
        "simple_explanation": "Aapki bones pathar nahi hain; osteoclasts purani bone dissolve karte hain aur osteoblasts nayi bone banate hain",
        "why_it_matters": "Har 10 saal mein aapka pura skeleton lagbhag naya ho jata hai",
        "script_phrase": "Aapki bones living dynamic tissue hain. Osteoclasts purani bone dissolve karte hain aur Osteoblasts nayi bone banate hain. Is continuous cycle ko Bone Remodeling kehte hain.",
        "badge_title": "BONE REMODELING",
        "badge_sub": "Skeleton ka 10-year regeneration cycle"
    },
    "sleep_paralysis": {
        "term": "Sleep Paralysis",
        "tts_phonetic": "Sleep Paralysis",
        "simple_explanation": "Aapka dimaag neend se jag jata hai lekin body ki REM muscle lock switch abhi bhi ON rehti hai",
        "why_it_matters": "Ye darawana zaroor lagta hai lekin medically temporary aur completely harmless hota hai",
        "script_phrase": "Neend se jaagne par aankhein khulna lekin body move na hona ek harmless brain transition gap hai. Ise Sleep Paralysis kehte hain.",
        "badge_title": "SLEEP PARALYSIS",
        "badge_sub": "Mind jaag gaya par body muscle switch off"
    },
    "misophonia": {
        "term": "Misophonia (Sound Sensitivity)",
        "tts_phonetic": "Miso-phonia",
        "simple_explanation": "Chewing ya breathing jaise normal sounds par brain ka emotional aur fight-or-flight center hyperactivate ho jata hai",
        "why_it_matters": "Ye sunne ki bimari nahi, balki auditory cortex aur emotional amygdala ka cross-connection hai",
        "script_phrase": "Kisi ke khane ya saans lene ki sound se severe gussa ya irritation aana ek brain connection issue hai. Science mein is extreme trigger ko Misophonia kehte hain.",
        "badge_title": "MISOPHONIA",
        "badge_sub": "Certain sounds se trigger hone wala emotional center"
    }
}

class ScientificTermTranslator:
    """
    Intelligent term translator and simplifier for Health Videos.
    Matches scientific terms in topics and generates 3-step structured explanations.
    """
    def __init__(self):
        self.dictionary = SCIENTIFIC_DICTIONARY

    def find_terms(self, text: str) -> List[Tuple[str, Dict[str, Any]]]:
        """Finds any matching scientific concepts in text."""
        matched = []
        text_lower = text.lower()
        for key, info in self.dictionary.items():
            # Check for term name, key, or badge
            term_clean = info["term"].lower()
            key_clean = key.replace("_", " ")
            if key_clean in text_lower or any(word in text_lower for word in key_clean.split() if len(word) > 4):
                matched.append((key, info))
        return matched

    def get_term_info(self, key_or_term: str) -> Optional[Dict[str, Any]]:
        """Direct lookup by key or term name."""
        k = key_or_term.lower().replace(" ", "_").replace("-", "_")
        if k in self.dictionary:
            return self.dictionary[k]
        for key, val in self.dictionary.items():
            if val["term"].lower() == key_or_term.lower() or val["badge_title"].lower() == key_or_term.lower():
                return val
        return None

    def simplify_sentence(self, term_key: str) -> str:
        """Returns the pre-crafted 3-step simplified Hinglish sentence."""
        info = self.get_term_info(term_key)
        if info:
            return info["script_phrase"]
        return ""

    def get_badge(self, term_key: str) -> Tuple[str, str]:
        """Returns (badge_title, badge_subtitle)."""
        info = self.get_term_info(term_key)
        if info:
            return info["badge_title"], info["badge_sub"]
        return "MEDICAL SCIENCE", "Verified Human Physiology"
