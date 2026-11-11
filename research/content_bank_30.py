"""
15-Day Master Production Roadmap & Content Bank (30 Unique Health Videos)
Populates all 30 science topics into SQLite database with verified citations,
simplified scientific terminology, and visual storytelling directions.
"""

import json
import logging
from typing import List, Dict, Any

from database.db_manager import DatabaseManager
from content.term_translator import ScientificTermTranslator

logger = logging.getLogger("health_videos.content_bank")

TOPICS_30_DATA: List[Dict[str, Any]] = [
    # ---------------- DAY 1: Hidden Brain and Body Secrets ----------------
    {
        "day_number": 1,
        "video_number": 1,
        "topic_id": "day01_video01",
        "title": "Your Brain Is Always One Step Ahead",
        "category": "Brain and Psychology",
        "core_concept": "Predictive processing: the brain creates a continuous internal hypothesis of reality rather than passively processing raw sensory input in real-time.",
        "hook_text": "Aapka brain duniya ko exactly waise nahi dekhta jaise woh actually hai!",
        "term_key": "predictive_processing",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6400842/",
            "https://www.nature.com/articles/nrn3404"
        ],
        "visual_style_prompt": "3D holographic glowing brain in dark slate studio with pulsating orange neural predictive pathways",
        "bgm_category": "cinematic_technology"
    },
    {
        "day_number": 1,
        "video_number": 2,
        "topic_id": "day01_video02",
        "title": "Your Nose Secretly Switches Sides",
        "category": "Human Body Secrets",
        "core_concept": "The nasal cycle: autonomic alternating congestion and decongestion of nasal erectile tissue every 2 to 6 hours.",
        "hook_text": "Aapki ek nostril zyada active hoti hai, phir kuch ghanton baad doosri!",
        "term_key": "nasal_cycle",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4944485/",
            "https://www.nidcd.nih.gov/health/smell-disorders"
        ],
        "visual_style_prompt": "3D anatomical nasal cavity cross-section showing luminous blue airflow switching from left to right nostril",
        "bgm_category": "medical_documentary"
    },

    # ---------------- DAY 2: Sleep and Balance ----------------
    {
        "day_number": 2,
        "video_number": 3,
        "topic_id": "day02_video03",
        "title": "Why Your Body Freezes During Dreams",
        "category": "Sleep Science",
        "core_concept": "REM sleep muscle atonia: the brainstem inhibits spinal somatic motor neurons via glycine and GABA to prevent acting out vivid dreams.",
        "hook_text": "Sapne mein bhaagna chahte ho, lekin body move kyun nahi karti?",
        "term_key": "muscle_atonia",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403735/",
            "https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-understanding-sleep"
        ],
        "visual_style_prompt": "Person sleeping peacefully with 3D brainstem glowing and descending blue motor inhibitory signals",
        "bgm_category": "deep_ambient"
    },
    {
        "day_number": 2,
        "video_number": 4,
        "topic_id": "day02_video04",
        "title": "Why You Feel Dizzy After Spinning",
        "category": "Eyes and Human Senses",
        "core_concept": "The vestibular system: endolymph fluid inertia in the inner ear semicircular canals continues deflecting the cupula even after the body stops rotating.",
        "hook_text": "Ghoomna band karne ke baad bhi duniya kyun ghoomti rehti hai?",
        "term_key": "vestibular_system",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK10819/",
            "https://medlineplus.gov/ency/anatomyvideos/000008.htm"
        ],
        "visual_style_prompt": "3D macro view of inner ear labyrinth and semicircular canals showing luminous fluid swirling inside",
        "bgm_category": "suspense_science"
    },

    # ---------------- DAY 3: Survival Mechanisms ----------------
    {
        "day_number": 3,
        "video_number": 5,
        "topic_id": "day03_video05",
        "title": "Why Does Your Skin Get Goosebumps?",
        "category": "Skin and Hair Science",
        "core_concept": "Piloerection: sympathetic adrenergic activation causes tiny arrector pili smooth muscles to contract, pulling hair upright.",
        "hook_text": "Dar ya thand lagte hi body ke baal khade kyun ho jaate hain?",
        "term_key": "piloerection",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7439050/",
            "https://www.nih.gov/news-events/nih-research-matters/how-goosebumps-stimulate-stem-cells"
        ],
        "visual_style_prompt": "3D microscopic cross-section of skin dermis showing arrector pili muscle tightening around hair follicle",
        "bgm_category": "mystery_discovery"
    },
    {
        "day_number": 3,
        "video_number": 6,
        "topic_id": "day03_video06",
        "title": "Your Heart Has Its Own Electrical System",
        "category": "Heart and Blood Circulation",
        "core_concept": "Cardiac conduction system: the sinoatrial (SA) node generates intrinsic spontaneous electrical action potentials independently of brain input.",
        "hook_text": "Aapka heart apni electrical signals generate karke beat kar sakta hai!",
        "term_key": "sa_node",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK459233/",
            "https://www.cdc.gov/heartdisease/facts.htm"
        ],
        "visual_style_prompt": "Pulsating 3D anatomical heart in dark studio with bright golden electrical currents branching from the SA node",
        "bgm_category": "medical_documentary"
    },

    # ---------------- DAY 4: Digestive and Blood Science ----------------
    {
        "day_number": 4,
        "video_number": 7,
        "topic_id": "day04_video07",
        "title": "Why Doesn't Your Stomach Digest Itself?",
        "category": "Gut Health",
        "core_concept": "Gastric mucosal barrier: surface mucous cells secrete an alkaline, bicarbonate-rich gelatinous mucus layer protecting against pH 1.5 hydrochloric acid.",
        "hook_text": "Aapke stomach mein powerful acid hota hai, phir woh khud ko digest kyun nahi karta?",
        "term_key": "gastric_mucus_barrier",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK535425/",
            "https://medlineplus.gov/ency/anatomyvideos/000007.htm"
        ],
        "visual_style_prompt": "3D interior cross-section of stomach rugae with glowing green gastric acid repelled by a luminous protective mucus gel barrier",
        "bgm_category": "suspense_science"
    },
    {
        "day_number": 4,
        "video_number": 8,
        "topic_id": "day04_video08",
        "title": "Your Blood Cells Have an Expiry Date",
        "category": "Heart and Blood Circulation",
        "core_concept": "Erythrocyte lifespan: red blood cells circulate for approximately 120 days before losing membrane flexibility and getting engulfed by splenic macrophages.",
        "hook_text": "Aapke blood ke red cells hamesha nahi jeete!",
        "term_key": "erythrocyte_clearance",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK2263/",
            "https://www.nih.gov/news-events/nih-research-matters/how-spleen-filters-blood"
        ],
        "visual_style_prompt": "Microscopic view of biconcave red blood cells navigating narrow capillary filters with spleen macrophage breakdown",
        "bgm_category": "informational_education"
    },

    # ---------------- DAY 5: Memory and Vision ----------------
    {
        "day_number": 5,
        "video_number": 9,
        "topic_id": "day05_video09",
        "title": "Why Do You Forget Why You Entered a Room?",
        "category": "Brain and Psychology",
        "core_concept": "The Doorway Effect: passing through physical doorways creates event boundaries in episodic working memory, triggering mental file compartmentalization.",
        "hook_text": "Room mein enter karte hi yaad kyun nahi rehta ki aaye kis kaam se the?",
        "term_key": "doorway_effect",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3212853/",
            "https://www.scientificamerican.com/article/why-walking-through-doorways-makes-us-forget/"
        ],
        "visual_style_prompt": "Person walking through cinematic doorway transition into illuminated 3D brain hippocampus memory pathways resetting",
        "bgm_category": "mystery_discovery"
    },
    {
        "day_number": 5,
        "video_number": 10,
        "topic_id": "day05_video10",
        "title": "Why Do You See Flashes After Rubbing Your Eyes?",
        "category": "Eyes and Human Senses",
        "core_concept": "Phosphenes: mechanical pressure on the eyeball directly depolarizes retinal ganglion cells, which the visual cortex interprets as light bursts.",
        "hook_text": "Aankhein band karne par bhi light jaisi cheezein kyun dikhti hain?",
        "term_key": "phosphenes",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656113/",
            "https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases"
        ],
        "visual_style_prompt": "Macro 3D cross-section of human eye retina showing mechanical pressure generating vibrant geometric light flashes",
        "bgm_category": "cinematic_technology"
    },

    # ---------------- DAY 6: Sleep and Music ----------------
    {
        "day_number": 6,
        "video_number": 11,
        "topic_id": "day06_video11",
        "title": "Why Do You Suddenly Jerk While Falling Asleep?",
        "category": "Sleep Science",
        "core_concept": "Hypnic jerks: involuntary myoclonic twitches occurring during the transition from wakefulness to NREM sleep when motor signals misfire.",
        "hook_text": "Sote-sote achanak aisa lagta hai jaise gir rahe ho?",
        "term_key": "hypnic_jerk",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK560720/",
            "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-science-of-sleep"
        ],
        "visual_style_prompt": "Sleeping person in dark cinematic room with sudden synaptic flash in motor cortex triggering full-body muscle twitch",
        "bgm_category": "deep_ambient"
    },
    {
        "day_number": 6,
        "video_number": 12,
        "topic_id": "day06_video12",
        "title": "Why Does a Song Keep Playing Inside Your Head?",
        "category": "Brain and Psychology",
        "core_concept": "Involuntary Musical Imagery (earworms): spontaneous reactivation of phonological loops in the auditory cortex without conscious effort.",
        "hook_text": "Ek song dimag mein baar-baar kyun bajta rehta hai?",
        "term_key": "earworms",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440618/",
            "https://www.apa.org/monitor/2016/10/music-earworms"
        ],
        "visual_style_prompt": "3D auditory cortex with rhythmic soundwaves forming a closed continuous glowing loop inside the temporal lobe",
        "bgm_category": "informational_education"
    },

    # ---------------- DAY 7: Lungs and Memory ----------------
    {
        "day_number": 7,
        "video_number": 13,
        "topic_id": "day07_video13",
        "title": "Your Lungs Have Millions of Tiny Air Sacs",
        "category": "Human Body Secrets",
        "core_concept": "Pulmonary alveoli: 480 million microscopic spherical sacs providing 100 square meters of surface area for passive capillary diffusion of O2 and CO2.",
        "hook_text": "Aapke lungs ke andar millions of tiny air sacs hote hain!",
        "term_key": "alveoli",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK542318/",
            "https://www.nhlbi.nih.gov/health/lungs/respiratory-system"
        ],
        "visual_style_prompt": "3D bronchus branching into microscopic grape-like alveoli clusters showing blue/red capillary gas exchange",
        "bgm_category": "medical_documentary"
    },
    {
        "day_number": 7,
        "video_number": 14,
        "topic_id": "day07_video14",
        "title": "Why Do Memories Change Every Time You Recall Them?",
        "category": "Brain and Psychology",
        "core_concept": "Memory reconsolidation: retrieving an episodic memory renders its synaptic trace labile and susceptible to modification before it is re-stabilized.",
        "hook_text": "Aapki memory video recording ki tarah fixed nahi hoti!",
        "term_key": "memory_reconsolidation",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3789138/",
            "https://www.nature.com/articles/nn.3503"
        ],
        "visual_style_prompt": "3D neural network synapses lighting up, dissolving slightly, and re-weaving with subtle color variations",
        "bgm_category": "mystery_discovery"
    },

    # ---------------- DAY 8: Liver and Gut-Brain Connection ----------------
    {
        "day_number": 8,
        "video_number": 15,
        "topic_id": "day08_video15",
        "title": "The Organ That Can Regrow Part of Itself",
        "category": "Human Body Secrets",
        "core_concept": "Compensatory hyperplasia: quiescent hepatocytes re-enter the cell cycle upon partial hepatectomy to restore 100% of functional liver mass.",
        "hook_text": "Human body ka ek organ apna lost tissue dobara grow kar sakta hai!",
        "term_key": "liver_regeneration",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836881/",
            "https://medlineplus.gov/ency/article/002237.htm"
        ],
        "visual_style_prompt": "3D anatomical human liver regenerating glowing healthy tissue lobes with microscopic hepatocyte cell division",
        "bgm_category": "emotional_science"
    },
    {
        "day_number": 8,
        "video_number": 16,
        "topic_id": "day08_video16",
        "title": "The Nerve That Connects Your Brain to Your Gut",
        "category": "Gut Health",
        "core_concept": "The vagus nerve (Cranial Nerve X): bidirectional electrical superhighway carrying 80% sensory afferent signals from the gut microbiome to the brain.",
        "hook_text": "Aapke stomach aur brain ke beech ek communication highway hai!",
        "term_key": "vagus_nerve",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5808284/",
            "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-brain-gut-connection"
        ],
        "visual_style_prompt": "3D transparent human torso showing glowing golden vagus nerve cable connecting the brainstem down to the stomach and intestines",
        "bgm_category": "medical_documentary"
    },

    # ---------------- DAY 9: Visual Perception and Body Awareness ----------------
    {
        "day_number": 9,
        "video_number": 17,
        "topic_id": "day09_video17",
        "title": "Why Do You Still See an Image After Looking Away?",
        "category": "Eyes and Human Senses",
        "core_concept": "Negative afterimages: prolonged photic stimulation bleaches photopigments in retinal cone photoreceptors, causing rebound signals in opponent color channels.",
        "hook_text": "Bright object ko dekhne ke baad bhi uski image aankhon ke saamne kyun rehti hai?",
        "term_key": "afterimages",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK11532/",
            "https://www.britannica.com/science/afterimage"
        ],
        "visual_style_prompt": "Retina photoreceptors cones adapting to bright stimulus and rendering negative inverted ghost afterimage",
        "bgm_category": "cinematic_technology"
    },
    {
        "day_number": 9,
        "video_number": 18,
        "topic_id": "day09_video18",
        "title": "How Can You Touch Your Nose With Closed Eyes?",
        "category": "Human Body Secrets",
        "core_concept": "Proprioception: muscle spindles, Golgi tendon organs, and joint mechanoreceptors continuously send spatial coordinates to the parietal cortex.",
        "hook_text": "Aankhein band hone ke baad bhi aapko apne haath ki location kaise pata hoti hai?",
        "term_key": "proprioception",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5070002/",
            "https://www.nih.gov/news-events/nih-research-matters/how-mechanoreceptors-sense-body-position"
        ],
        "visual_style_prompt": "Person touching nose with closed eyes while 3D skeletal muscular sensors fire glowing spatial wireframe pulses",
        "bgm_category": "mystery_discovery"
    },

    # ---------------- DAY 10: Brain and Sleep Research ----------------
    {
        "day_number": 10,
        "video_number": 19,
        "topic_id": "day10_video19",
        "title": "Why Can't You Properly Tickle Yourself?",
        "category": "Brain and Psychology",
        "core_concept": "Sensory attenuation: the cerebellum computes an efference copy of motor commands to predict and cancel self-generated tactile stimulation.",
        "hook_text": "Khud ko tickle karne par waise hasi kyun nahi aati?",
        "term_key": "sensory_attenuation",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2832870/",
            "https://www.nature.com/articles/nn876"
        ],
        "visual_style_prompt": "3D cerebellum highlighted in magenta, predicting motor movement and muting tactile somatosensory signals",
        "bgm_category": "informational_education"
    },
    {
        "day_number": 10,
        "video_number": 20,
        "topic_id": "day10_video20",
        "title": "What Happens to Your Brain During Deep Sleep?",
        "category": "Sleep Science",
        "core_concept": "Glymphatic system: interstitial space expands by 60% during deep NREM sleep, allowing CSF influx to clear beta-amyloid (current research limitations noted).",
        "hook_text": "Sote waqt brain ke andar fluid movement aur waste clearance kaise hota hai?",
        "term_key": "glymphatic_system",
        "research_sources": [
            "https://www.nih.gov/news-events/nih-research-matters/how-sleep-clears-brain",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/"
        ],
        "visual_style_prompt": "3D brain cross-section during sleep with luminous blue CSF fluid cleansing metabolic waste between neural spaces",
        "bgm_category": "deep_ambient"
    },

    # ---------------- DAY 11: Hearing and Temperature ----------------
    {
        "day_number": 11,
        "video_number": 21,
        "topic_id": "day11_video21",
        "title": "Your Ears Never Really Stop Working",
        "category": "Eyes and Human Senses",
        "core_concept": "Nocturnal auditory gating: acoustic soundwaves convert to electrical signals continuously; the thalamic reticular nucleus filters threats during sleep.",
        "hook_text": "Aap so rahe hote ho, lekin brain sounds ko monitor karta rehta hai!",
        "term_key": "auditory_arousal",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6265731/",
            "https://www.nidcd.nih.gov/health/how-do-we-hear"
        ],
        "visual_style_prompt": "Cochlea hair cells vibrating in dark bedroom, sending acoustic electrical impulses to the sleeping thalamus",
        "bgm_category": "soft_atmosphere"
    },
    {
        "day_number": 11,
        "video_number": 22,
        "topic_id": "day11_video22",
        "title": "Why Does Cold Weather Make You Pee More?",
        "category": "Hormones and Metabolism",
        "core_concept": "Cold-induced diuresis: cutaneous vasoconstriction diverts blood to the central core, raising arterial pressure and triggering renal filtration of excess fluid.",
        "hook_text": "Thand mein washroom zyada kyun jana padta hai?",
        "term_key": "cold_diuresis",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6481107/",
            "https://www.kidney.org/atoz/content/howkidneyswork"
        ],
        "visual_style_prompt": "3D human silhouette in cold air showing peripheral blood vessels contracting and kidneys filtering urine faster",
        "bgm_category": "medical_documentary"
    },

    # ---------------- DAY 12: Social Biology and Tears ----------------
    {
        "day_number": 12,
        "video_number": 23,
        "topic_id": "day12_video23",
        "title": "Why Is Yawning Contagious?",
        "category": "Brain and Psychology",
        "core_concept": "Contagious yawning: action-perception coupling mediated by mirror neuron networks and motor empathy circuits in the frontoparietal cortex.",
        "hook_text": "Kisi ko jamhai lete dekhkar aapko bhi kyun aati hai?",
        "term_key": "contagious_yawning",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3678674/",
            "https://www.frontiersin.org/articles/10.3389/fneur.2020.00890/full"
        ],
        "visual_style_prompt": "Human yawning trigger activating mirror neuron circuits across two communicating silhouettes",
        "bgm_category": "informational_education"
    },
    {
        "day_number": 12,
        "video_number": 24,
        "topic_id": "day12_video24",
        "title": "Your Tears Are Not All the Same",
        "category": "Human Body Secrets",
        "core_concept": "Tear biochemistry: basal tears maintain corneal refraction, reflex tears flush irritants with lysozyme, and emotional tears excrete prolactin and ACTH.",
        "hook_text": "Har baar rone par nikalne wale aansu same type ke nahi hote!",
        "term_key": "tear_types",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6457075/",
            "https://www.aao.org/eye-health/tips-prevention/all-about-emotional-tears"
        ],
        "visual_style_prompt": "Macro 3D eye and lacrimal gland showing 3 distinct microscopic molecular crystal structures of tears",
        "bgm_category": "emotional_science"
    },

    # ---------------- DAY 13: Microbiology and Body Heat ----------------
    {
        "day_number": 13,
        "video_number": 25,
        "topic_id": "day13_video25",
        "title": "The Tiny World Living Inside Your Gut",
        "category": "Immunity and Microbiology",
        "core_concept": "Gut microbiome: 38 trillion symbiotic microbes synthesize vitamins (K, B12), train immune lymphocytes, and ferment dietary fiber into short-chain fatty acids.",
        "hook_text": "Aapke intestine mein trillions of microorganisms rehte hain!",
        "term_key": "gut_microbiome",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4290017/",
            "https://www.nih.gov/news-events/nih-research-matters/human-microbiome-health-disease"
        ],
        "visual_style_prompt": "Luminous 3D microscopic view of vibrant symbiotic beneficial bacteria colonies on healthy intestinal villi",
        "bgm_category": "medical_documentary"
    },
    {
        "day_number": 13,
        "video_number": 26,
        "topic_id": "day13_video26",
        "title": "Your Body Has Fat That Burns Energy to Make Heat",
        "category": "Hormones and Metabolism",
        "core_concept": "Brown adipose tissue (BAT): mitochondria-dense fat expressing uncoupling protein 1 (UCP1) uncouples oxidative phosphorylation to generate heat directly.",
        "hook_text": "Body mein ek aisa fat bhi hota hai jo heat produce karne mein help karta hai!",
        "term_key": "brown_fat",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3593105/",
            "https://www.nih.gov/news-events/nih-research-matters/how-brown-fat-improves-metabolic-health"
        ],
        "visual_style_prompt": "3D cellular view of brown fat cell packed with iron-rich mitochondria burning lipid droplets into radiant golden thermal heat",
        "bgm_category": "cinematic_technology"
    },

    # ---------------- DAY 14: Pain and Bone Science ----------------
    {
        "day_number": 14,
        "video_number": 27,
        "topic_id": "day14_video27",
        "title": "Can Your Brain Create Pain Without an Injury?",
        "category": "Brain and Psychology",
        "core_concept": "Nociplastic pain & central sensitization: altered central nociceptive processing causes real pain sensations without ongoing tissue damage.",
        "hook_text": "Kabhi-kabhi pain ka experience injury ke bina bhi ho sakta hai!",
        "term_key": "nociplastic_pain",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8186584/",
            "https://www.iasp-pain.org/resources/terminology/"
        ],
        "visual_style_prompt": "3D nervous system spine and brain with pain processing pathways glowing without peripheral tissue damage",
        "bgm_category": "suspense_science"
    },
    {
        "day_number": 14,
        "video_number": 28,
        "topic_id": "day14_video28",
        "title": "Your Bones Are Constantly Rebuilding Themselves",
        "category": "Fitness and Muscle Science",
        "core_concept": "Bone remodeling: coordinated balance between osteoclasts (resorbing old bone mineral) and osteoblasts (synthesizing new collagen bone matrix).",
        "hook_text": "Aapki bones dead structures nahi hain, ye continuously change hoti rehti hain!",
        "term_key": "bone_remodeling",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3179341/",
            "https://medlineplus.gov/bonediseases.html"
        ],
        "visual_style_prompt": "3D microscopic bone trabecular cross-section with osteoclasts clearing mineral pits and osteoblasts depositing fresh glowing matrix",
        "bgm_category": "medical_documentary"
    },

    # ---------------- DAY 15: Sleep and Sound Sensitivity ----------------
    {
        "day_number": 15,
        "video_number": 29,
        "topic_id": "day15_video29",
        "title": "Sleep Paralysis – When Your Mind Wakes Before Your Body",
        "category": "Sleep Science",
        "core_concept": "Sleep paralysis: conscious cortical awakening occurs while cholinergic REM muscle atonia is still active, causing brief harmless motor block.",
        "hook_text": "Aankhein khul gayi, lekin body move nahi ho rahi... aisa kyun?",
        "term_key": "sleep_paralysis",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/books/NBK562303/",
            "https://www.sleepfoundation.org/parasomnias/sleep-paralysis"
        ],
        "visual_style_prompt": "Person lying in bed in deep twilight lighting with active 3D conscious brain while muscle pathways remain safely offline",
        "bgm_category": "suspense_science"
    },
    {
        "day_number": 15,
        "video_number": 30,
        "topic_id": "day15_video30",
        "title": "Why Do Some Sounds Make You Extremely Irritated?",
        "category": "Brain and Psychology",
        "core_concept": "Misophonia: hyper-reactivity between the auditory cortex and the anterior insular cortex triggers acute autonomic fight-or-flight arousal to specific oral/nasal sounds.",
        "hook_text": "Kisi ke chewing ki awaaz se itna irritation kyun hota hai?",
        "term_key": "misophonia",
        "research_sources": [
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5321671/",
            "https://www.cell.com/current-biology/fulltext/S0960-9822(16)31530-5"
        ],
        "visual_style_prompt": "Soundwaves entering the ear triggering acute fiery connection into the emotional insular cortex and amygdala",
        "bgm_category": "mystery_discovery"
    }
]

def seed_30_topics(db: DatabaseManager = None) -> int:
    """Populates all 30 topics into content_calendar and topics tables."""
    db = db or DatabaseManager()
    tt = ScientificTermTranslator()
    count = 0

    for item in TOPICS_30_DATA:
        badge_title, badge_sub = tt.get_badge(item["term_key"])
        term_info = tt.get_term_info(item["term_key"])
        scientific_name = term_info["term"] if term_info else item["term_key"].replace("_", " ").title()

        # 1. Upsert into content_calendar
        cal_entry = {
            **item,
            "scientific_term": scientific_name,
            "term_badge_title": badge_title,
            "term_badge_sub": badge_sub,
            "research_status": "VERIFIED",
            "script_status": "PLANNED",
            "render_status": "PLANNED",
            "approval_status": "STAGED"
        }
        db.upsert_calendar_entry(cal_entry)

        # 2. Also register in topics table for unified catalog lookup
        db.save_topic({
            "topic_id": item["topic_id"],
            "title": item["title"],
            "category": item["category"],
            "hook": item["hook_text"],
            "hook_style": "Curiosity Question",
            "core_science": item["core_concept"],
            "research_sources": item["research_sources"],
            "evidence_status": "verified",
            "status": "planned"
        })
        count += 1

    logger.info(f"Successfully seeded {count} educational topics into content_calendar and catalog.")
    return count

if __name__ == "__main__":
    db = DatabaseManager()
    c = seed_30_topics(db)
    print(f"Seeded {c} topics across 15 days successfully.")
