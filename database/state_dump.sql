BEGIN TRANSACTION;
CREATE TABLE bgm_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    track_id TEXT NOT NULL,
    track_category TEXT NOT NULL,
    topic_id TEXT,
    used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duration_seconds REAL
);
CREATE TABLE content_calendar (
    day_number INTEGER NOT NULL,
    video_number INTEGER NOT NULL,
    topic_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    core_concept TEXT NOT NULL,
    hook_text TEXT NOT NULL,
    term_key TEXT NOT NULL,
    scientific_term TEXT NOT NULL,
    term_badge_title TEXT NOT NULL,
    term_badge_sub TEXT NOT NULL,
    research_sources TEXT, -- JSON array of medical citations
    visual_style_prompt TEXT,
    bgm_category TEXT DEFAULT 'medical_documentary',
    research_status TEXT DEFAULT 'VERIFIED',
    script_status TEXT DEFAULT 'PLANNED',
    voice_status TEXT DEFAULT 'PLANNED',
    visual_status TEXT DEFAULT 'PLANNED',
    render_status TEXT DEFAULT 'PLANNED',
    qc_status TEXT DEFAULT 'PLANNED',
    approval_status TEXT DEFAULT 'STAGED',
    video_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "content_calendar" VALUES(1,1,'day01_video01','Your Brain Is Always One Step Ahead','Brain and Psychology','Predictive processing: the brain creates a continuous internal hypothesis of reality rather than passively processing raw sensory input in real-time.','Aapka brain duniya ko exactly waise nahi dekhta jaise woh actually hai!','predictive_processing','Predictive Processing','PREDICTIVE PROCESSING','Brain ka sensory guess mechanism','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6400842/", "https://www.nature.com/articles/nrn3404"]','3D holographic glowing brain in dark slate studio with pulsating orange neural predictive pathways','cinematic_technology','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','UPLOADED','/home/rishabh/Heath Videos/output/videos/day01_video01_health_short.mp4','2026-11-11 10:57:11','2026-11-11 12:12:29');
INSERT INTO "content_calendar" VALUES(1,2,'day01_video02','Your Nose Secretly Switches Sides','Human Body Secrets','The nasal cycle: autonomic alternating congestion and decongestion of nasal erectile tissue every 2 to 6 hours.','Aapki ek nostril zyada active hoti hai, phir kuch ghanton baad doosri!','nasal_cycle','Nasal Cycle','NASAL CYCLE','Nostrils ka alternating airflow','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4944485/", "https://www.nidcd.nih.gov/health/smell-disorders"]','3D anatomical nasal cavity cross-section showing luminous blue airflow switching from left to right nostril','medical_documentary','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','UPLOADED','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day01_video02_health_short.mp4','2026-11-11 10:57:11','2026-11-11 13:10:34');
INSERT INTO "content_calendar" VALUES(2,3,'day02_video03','Why Your Body Freezes During Dreams','Sleep Science','REM sleep muscle atonia: the brainstem inhibits spinal somatic motor neurons via glycine and GABA to prevent acting out vivid dreams.','Sapne mein bhaagna chahte ho, lekin body move kyun nahi karti?','muscle_atonia','REM Sleep Muscle Atonia','MUSCLE ATONIA','Sapne ke waqt temporary muscle paralysis','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403735/", "https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-understanding-sleep"]','Person sleeping peacefully with 3D brainstem glowing and descending blue motor inhibitory signals','deep_ambient','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_FAILED','UPLOADED','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day02_video03_health_short.mp4','2026-11-11 10:57:11','2026-11-12 05:08:16');
INSERT INTO "content_calendar" VALUES(2,4,'day02_video04','Why You Feel Dizzy After Spinning','Eyes and Human Senses','The vestibular system: endolymph fluid inertia in the inner ear semicircular canals continues deflecting the cupula even after the body stops rotating.','Ghoomna band karne ke baad bhi duniya kyun ghoomti rehti hai?','vestibular_system','Vestibular System','VESTIBULAR SYSTEM','Inner ear ka balance network','["https://www.ncbi.nlm.nih.gov/books/NBK10819/", "https://medlineplus.gov/ency/anatomyvideos/000008.htm"]','3D macro view of inner ear labyrinth and semicircular canals showing luminous fluid swirling inside','suspense_science','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','UPLOADED','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day02_video04_health_short.mp4','2026-11-11 10:57:11','2026-11-12 12:19:36');
INSERT INTO "content_calendar" VALUES(3,5,'day03_video05','Why Does Your Skin Get Goosebumps?','Skin and Hair Science','Piloerection: sympathetic adrenergic activation causes tiny arrector pili smooth muscles to contract, pulling hair upright.','Dar ya thand lagte hi body ke baal khade kyun ho jaate hain?','piloerection','Piloerection','PILOERECTION','Skin muscles ka tightening reflex','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7439050/", "https://www.nih.gov/news-events/nih-research-matters/how-goosebumps-stimulate-stem-cells"]','3D microscopic cross-section of skin dermis showing arrector pili muscle tightening around hair follicle','mystery_discovery','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','UPLOADED','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day03_video05_health_short.mp4','2026-11-11 10:57:11','2026-11-12 20:14:51');
INSERT INTO "content_calendar" VALUES(3,6,'day03_video06','Your Heart Has Its Own Electrical System','Heart and Blood Circulation','Cardiac conduction system: the sinoatrial (SA) node generates intrinsic spontaneous electrical action potentials independently of brain input.','Aapka heart apni electrical signals generate karke beat kar sakta hai!','sa_node','Sinoatrial (SA) Node','SA NODE','Heart ka natural electric pacemaker','["https://www.ncbi.nlm.nih.gov/books/NBK459233/", "https://www.cdc.gov/heartdisease/facts.htm"]','Pulsating 3D anatomical heart in dark studio with bright golden electrical currents branching from the SA node','medical_documentary','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','UPLOADED','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day03_video06_health_short.mp4','2026-11-11 10:57:11','2026-11-13 11:58:11');
INSERT INTO "content_calendar" VALUES(4,7,'day04_video07','Why Doesn''t Your Stomach Digest Itself?','Gut Health','Gastric mucosal barrier: surface mucous cells secrete an alkaline, bicarbonate-rich gelatinous mucus layer protecting against pH 1.5 hydrochloric acid.','Aapke stomach mein powerful acid hota hai, phir woh khud ko digest kyun nahi karta?','gastric_mucus_barrier','Gastric Mucus Barrier','MUCUS BARRIER','Acid se bachane wali protective shield','["https://www.ncbi.nlm.nih.gov/books/NBK535425/", "https://medlineplus.gov/ency/anatomyvideos/000007.htm"]','3D interior cross-section of stomach rugae with glowing green gastric acid repelled by a luminous protective mucus gel barrier','suspense_science','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','APPROVED','/home/rishabh/Heath Videos/output/videos/day04_video07_health_short.mp4','2026-11-11 10:57:11','2026-11-11 11:20:54');
INSERT INTO "content_calendar" VALUES(4,8,'day04_video08','Your Blood Cells Have an Expiry Date','Heart and Blood Circulation','Erythrocyte lifespan: red blood cells circulate for approximately 120 days before losing membrane flexibility and getting engulfed by splenic macrophages.','Aapke blood ke red cells hamesha nahi jeete!','erythrocyte_clearance','Red Blood Cell Lifecycle','RBC LIFECYCLE','Blood cells ka 120-day replacement','["https://www.ncbi.nlm.nih.gov/books/NBK2263/", "https://www.nih.gov/news-events/nih-research-matters/how-spleen-filters-blood"]','Microscopic view of biconcave red blood cells navigating narrow capillary filters with spleen macrophage breakdown','informational_education','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(5,9,'day05_video09','Why Do You Forget Why You Entered a Room?','Brain and Psychology','The Doorway Effect: passing through physical doorways creates event boundaries in episodic working memory, triggering mental file compartmentalization.','Room mein enter karte hi yaad kyun nahi rehta ki aaye kis kaam se the?','doorway_effect','Doorway Effect (Event Boundary)','DOORWAY EFFECT','Brain ka environment reset reflex','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3212853/", "https://www.scientificamerican.com/article/why-walking-through-doorways-makes-us-forget/"]','Person walking through cinematic doorway transition into illuminated 3D brain hippocampus memory pathways resetting','mystery_discovery','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(5,10,'day05_video10','Why Do You See Flashes After Rubbing Your Eyes?','Eyes and Human Senses','Phosphenes: mechanical pressure on the eyeball directly depolarizes retinal ganglion cells, which the visual cortex interprets as light bursts.','Aankhein band karne par bhi light jaisi cheezein kyun dikhti hain?','phosphenes','Phosphenes','PHOSPHENES','Bina light ke aankh mein flashes','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656113/", "https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases"]','Macro 3D cross-section of human eye retina showing mechanical pressure generating vibrant geometric light flashes','cinematic_technology','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(6,11,'day06_video11','Why Do You Suddenly Jerk While Falling Asleep?','Sleep Science','Hypnic jerks: involuntary myoclonic twitches occurring during the transition from wakefulness to NREM sleep when motor signals misfire.','Sote-sote achanak aisa lagta hai jaise gir rahe ho?','hypnic_jerk','Hypnic Jerk','HYPNIC JERK','Sote waqt achanak jhatka','["https://www.ncbi.nlm.nih.gov/books/NBK560720/", "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-science-of-sleep"]','Sleeping person in dark cinematic room with sudden synaptic flash in motor cortex triggering full-body muscle twitch','deep_ambient','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(6,12,'day06_video12','Why Does a Song Keep Playing Inside Your Head?','Brain and Psychology','Involuntary Musical Imagery (earworms): spontaneous reactivation of phonological loops in the auditory cortex without conscious effort.','Ek song dimag mein baar-baar kyun bajta rehta hai?','earworms','Involuntary Musical Imagery (Earworm)','EARWORM EFFECT','Dimag mein ghoomta repetitive song','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440618/", "https://www.apa.org/monitor/2016/10/music-earworms"]','3D auditory cortex with rhythmic soundwaves forming a closed continuous glowing loop inside the temporal lobe','informational_education','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(7,13,'day07_video13','Your Lungs Have Millions of Tiny Air Sacs','Human Body Secrets','Pulmonary alveoli: 480 million microscopic spherical sacs providing 100 square meters of surface area for passive capillary diffusion of O2 and CO2.','Aapke lungs ke andar millions of tiny air sacs hote hain!','alveoli','Alveoli','ALVEOLI','Lungs ki tiny oxygen-exchange sacs','["https://www.ncbi.nlm.nih.gov/books/NBK542318/", "https://www.nhlbi.nih.gov/health/lungs/respiratory-system"]','3D bronchus branching into microscopic grape-like alveoli clusters showing blue/red capillary gas exchange','medical_documentary','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(7,14,'day07_video14','Why Do Memories Change Every Time You Recall Them?','Brain and Psychology','Memory reconsolidation: retrieving an episodic memory renders its synaptic trace labile and susceptible to modification before it is re-stabilized.','Aapki memory video recording ki tarah fixed nahi hoti!','memory_reconsolidation','Memory Reconsolidation','RECONSOLIDATION','Har baar recall par memory ka rewrite hona','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3789138/", "https://www.nature.com/articles/nn.3503"]','3D neural network synapses lighting up, dissolving slightly, and re-weaving with subtle color variations','mystery_discovery','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(8,15,'day08_video15','The Organ That Can Regrow Part of Itself','Human Body Secrets','Compensatory hyperplasia: quiescent hepatocytes re-enter the cell cycle upon partial hepatectomy to restore 100% of functional liver mass.','Human body ka ek organ apna lost tissue dobara grow kar sakta hai!','liver_regeneration','Compensatory Hyperplasia (Liver Regeneration)','LIVER REGROWTH','Organ ka apna tissue dobara grow karna','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836881/", "https://medlineplus.gov/ency/article/002237.htm"]','3D anatomical human liver regenerating glowing healthy tissue lobes with microscopic hepatocyte cell division','emotional_science','VERIFIED','SCRIPT_READY','VOICE_READY','ASSETS_READY','RENDERED','QC_PASSED','APPROVED','/home/rishabh/Heath Videos/output/videos/day08_video15_health_short.mp4','2026-11-11 10:57:11','2026-11-11 11:28:08');
INSERT INTO "content_calendar" VALUES(8,16,'day08_video16','The Nerve That Connects Your Brain to Your Gut','Gut Health','The vagus nerve (Cranial Nerve X): bidirectional electrical superhighway carrying 80% sensory afferent signals from the gut microbiome to the brain.','Aapke stomach aur brain ke beech ek communication highway hai!','vagus_nerve','Vagus Nerve','VAGUS NERVE','Brain aur gut ka communication highway','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5808284/", "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-brain-gut-connection"]','3D transparent human torso showing glowing golden vagus nerve cable connecting the brainstem down to the stomach and intestines','medical_documentary','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(9,17,'day09_video17','Why Do You Still See an Image After Looking Away?','Eyes and Human Senses','Negative afterimages: prolonged photic stimulation bleaches photopigments in retinal cone photoreceptors, causing rebound signals in opponent color channels.','Bright object ko dekhne ke baad bhi uski image aankhon ke saamne kyun rehti hai?','afterimages','Photoreceptor Adaptation (Afterimages)','AFTERIMAGES','Retina sensors ka temporary adaptation','["https://www.ncbi.nlm.nih.gov/books/NBK11532/", "https://www.britannica.com/science/afterimage"]','Retina photoreceptors cones adapting to bright stimulus and rendering negative inverted ghost afterimage','cinematic_technology','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(9,18,'day09_video18','How Can You Touch Your Nose With Closed Eyes?','Human Body Secrets','Proprioception: muscle spindles, Golgi tendon organs, and joint mechanoreceptors continuously send spatial coordinates to the parietal cortex.','Aankhein band hone ke baad bhi aapko apne haath ki location kaise pata hoti hai?','proprioception','Proprioception','PROPRIOCEPTION','Body position ka natural 6th sense','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5070002/", "https://www.nih.gov/news-events/nih-research-matters/how-mechanoreceptors-sense-body-position"]','Person touching nose with closed eyes while 3D skeletal muscular sensors fire glowing spatial wireframe pulses','mystery_discovery','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(10,19,'day10_video19','Why Can''t You Properly Tickle Yourself?','Brain and Psychology','Sensory attenuation: the cerebellum computes an efference copy of motor commands to predict and cancel self-generated tactile stimulation.','Khud ko tickle karne par waise hasi kyun nahi aati?','sensory_attenuation','Sensory Attenuation (Self-Touch)','SELF-TOUCH CANCEL','Khud ko tickle na kar paane ka brain secret','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2832870/", "https://www.nature.com/articles/nn876"]','3D cerebellum highlighted in magenta, predicting motor movement and muting tactile somatosensory signals','informational_education','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(10,20,'day10_video20','What Happens to Your Brain During Deep Sleep?','Sleep Science','Glymphatic system: interstitial space expands by 60% during deep NREM sleep, allowing CSF influx to clear beta-amyloid (current research limitations noted).','Sote waqt brain ke andar fluid movement aur waste clearance kaise hota hai?','glymphatic_system','Glymphatic System','GLYMPHATIC SYSTEM','Neend mein dimaag ka fluid waste flush','["https://www.nih.gov/news-events/nih-research-matters/how-sleep-clears-brain", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/"]','3D brain cross-section during sleep with luminous blue CSF fluid cleansing metabolic waste between neural spaces','deep_ambient','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(11,21,'day11_video21','Your Ears Never Really Stop Working','Eyes and Human Senses','Nocturnal auditory gating: acoustic soundwaves convert to electrical signals continuously; the thalamic reticular nucleus filters threats during sleep.','Aap so rahe hote ho, lekin brain sounds ko monitor karta rehta hai!','auditory_arousal','Auditory Brain Processing During Sleep','AUDITORY MONITOR','Sote waqt bhi active hearing sensors','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6265731/", "https://www.nidcd.nih.gov/health/how-do-we-hear"]','Cochlea hair cells vibrating in dark bedroom, sending acoustic electrical impulses to the sleeping thalamus','soft_atmosphere','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(11,22,'day11_video22','Why Does Cold Weather Make You Pee More?','Hormones and Metabolism','Cold-induced diuresis: cutaneous vasoconstriction diverts blood to the central core, raising arterial pressure and triggering renal filtration of excess fluid.','Thand mein washroom zyada kyun jana padta hai?','cold_diuresis','Cold-Induced Diuresis','COLD DIURESIS','Thand mein kidney ka extra fluid release','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6481107/", "https://www.kidney.org/atoz/content/howkidneyswork"]','3D human silhouette in cold air showing peripheral blood vessels contracting and kidneys filtering urine faster','medical_documentary','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(12,23,'day12_video23','Why Is Yawning Contagious?','Brain and Psychology','Contagious yawning: action-perception coupling mediated by mirror neuron networks and motor empathy circuits in the frontoparietal cortex.','Kisi ko jamhai lete dekhkar aapko bhi kyun aati hai?','contagious_yawning','Contagious Yawning (Mirror Neurons)','MIRROR REFLEX','Social empathy aur contagious yawning','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3678674/", "https://www.frontiersin.org/articles/10.3389/fneur.2020.00890/full"]','Human yawning trigger activating mirror neuron circuits across two communicating silhouettes','informational_education','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(12,24,'day12_video24','Your Tears Are Not All the Same','Human Body Secrets','Tear biochemistry: basal tears maintain corneal refraction, reflex tears flush irritants with lysozyme, and emotional tears excrete prolactin and ACTH.','Har baar rone par nikalne wale aansu same type ke nahi hote!','tear_types','Basal, Reflex & Emotional Tears','TEAR BIOCHEMISTRY','Basal, reflex aur emotional tears ka fark','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6457075/", "https://www.aao.org/eye-health/tips-prevention/all-about-emotional-tears"]','Macro 3D eye and lacrimal gland showing 3 distinct microscopic molecular crystal structures of tears','emotional_science','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "content_calendar" VALUES(13,25,'day13_video25','The Tiny World Living Inside Your Gut','Immunity and Microbiology','Gut microbiome: 38 trillion symbiotic microbes synthesize vitamins (K, B12), train immune lymphocytes, and ferment dietary fiber into short-chain fatty acids.','Aapke intestine mein trillions of microorganisms rehte hain!','gut_microbiome','Gut Microbiome','GUT MICROBIOME','38 trillion friendly bacteria ka ecosystem','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4290017/", "https://www.nih.gov/news-events/nih-research-matters/human-microbiome-health-disease"]','Luminous 3D microscopic view of vibrant symbiotic beneficial bacteria colonies on healthy intestinal villi','medical_documentary','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "content_calendar" VALUES(13,26,'day13_video26','Your Body Has Fat That Burns Energy to Make Heat','Hormones and Metabolism','Brown adipose tissue (BAT): mitochondria-dense fat expressing uncoupling protein 1 (UCP1) uncouples oxidative phosphorylation to generate heat directly.','Body mein ek aisa fat bhi hota hai jo heat produce karne mein help karta hai!','brown_fat','Brown Adipose Tissue (Brown Fat)','BROWN FAT','Heat produce karne wala healthy fat','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3593105/", "https://www.nih.gov/news-events/nih-research-matters/how-brown-fat-improves-metabolic-health"]','3D cellular view of brown fat cell packed with iron-rich mitochondria burning lipid droplets into radiant golden thermal heat','cinematic_technology','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "content_calendar" VALUES(14,27,'day14_video27','Can Your Brain Create Pain Without an Injury?','Brain and Psychology','Nociplastic pain & central sensitization: altered central nociceptive processing causes real pain sensations without ongoing tissue damage.','Kabhi-kabhi pain ka experience injury ke bina bhi ho sakta hai!','nociplastic_pain','Nociplastic Pain (Central Sensitization)','NOCIPLASTIC PAIN','Bina injury ke nervous system ka pain response','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8186584/", "https://www.iasp-pain.org/resources/terminology/"]','3D nervous system spine and brain with pain processing pathways glowing without peripheral tissue damage','suspense_science','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "content_calendar" VALUES(14,28,'day14_video28','Your Bones Are Constantly Rebuilding Themselves','Fitness and Muscle Science','Bone remodeling: coordinated balance between osteoclasts (resorbing old bone mineral) and osteoblasts (synthesizing new collagen bone matrix).','Aapki bones dead structures nahi hain, ye continuously change hoti rehti hain!','bone_remodeling','Bone Remodeling (Osteoblasts & Osteoclasts)','BONE REMODELING','Skeleton ka 10-year regeneration cycle','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3179341/", "https://medlineplus.gov/bonediseases.html"]','3D microscopic bone trabecular cross-section with osteoclasts clearing mineral pits and osteoblasts depositing fresh glowing matrix','medical_documentary','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "content_calendar" VALUES(15,29,'day15_video29','Sleep Paralysis – When Your Mind Wakes Before Your Body','Sleep Science','Sleep paralysis: conscious cortical awakening occurs while cholinergic REM muscle atonia is still active, causing brief harmless motor block.','Aankhein khul gayi, lekin body move nahi ho rahi... aisa kyun?','sleep_paralysis','Sleep Paralysis','SLEEP PARALYSIS','Mind jaag gaya par body muscle switch off','["https://www.ncbi.nlm.nih.gov/books/NBK562303/", "https://www.sleepfoundation.org/parasomnias/sleep-paralysis"]','Person lying in bed in deep twilight lighting with active 3D conscious brain while muscle pathways remain safely offline','suspense_science','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "content_calendar" VALUES(15,30,'day15_video30','Why Do Some Sounds Make You Extremely Irritated?','Brain and Psychology','Misophonia: hyper-reactivity between the auditory cortex and the anterior insular cortex triggers acute autonomic fight-or-flight arousal to specific oral/nasal sounds.','Kisi ke chewing ki awaaz se itna irritation kyun hota hai?','misophonia','Misophonia (Sound Sensitivity)','MISOPHONIA','Certain sounds se trigger hone wala emotional center','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5321671/", "https://www.cell.com/current-biology/fulltext/S0960-9822(16)31530-5"]','Soundwaves entering the ear triggering acute fiery connection into the emotional insular cortex and amygdala','mystery_discovery','VERIFIED','PLANNED','PLANNED','PLANNED','PLANNED','PLANNED','STAGED','','2026-11-11 10:57:12','2026-11-11 10:57:12');
CREATE TABLE publication_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id TEXT NOT NULL,
    youtube_video_id TEXT,
    visibility TEXT,
    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT,
    response_metadata TEXT,
    FOREIGN KEY(topic_id) REFERENCES topics(topic_id)
);
CREATE TABLE rejected_attempts (
    attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    attempt_type TEXT NOT NULL, -- 'topic', 'script', 'hook', 'visual_sequence', 'similarity_gating'
    content_payload TEXT NOT NULL,
    rejection_reason TEXT NOT NULL,
    similarity_score REAL,
    matched_entity_id TEXT,
    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "rejected_attempts" VALUES(1,'similarity_gating','{"title": "Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?", "hook": "Jab aap gehri neend mein sote hain, aapka brain shrink hota hai."}','Originality Gate Failure: 3 checks failed. Score=0.314',1.0,'Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?','2026-11-11 10:23:10');
INSERT INTO "rejected_attempts" VALUES(2,'similarity_gating','{"title": "Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?", "hook": "Jab aap gehri neend mein sote hain, aapka dimaag shrink ho jata hai."}','Originality Gate Failure: 2 checks failed. Score=0.683',1.0,'Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?','2026-11-11 10:26:39');
INSERT INTO "rejected_attempts" VALUES(3,'similarity_gating','{"title": "Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?", "hook": "Jab aap gehri neend mein sote hain, aapka dimaag shrink ho jata hai."}','Originality Gate Failure: 2 checks failed. Score=0.683',1.0,'Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?','2026-11-11 10:27:56');
INSERT INTO "rejected_attempts" VALUES(4,'similarity_gating','{"title": "Mitochondria: Cell Ka Powerhouse Energy Kaise Banata Hai?", "hook": "Aapke shareer ke har cell mein hazaron tiny factories hain."}','Originality Gate Failure: 1 checks failed. Score=0.808',5.71428571428571396e-01,'Dimag ki Safai: Neend mein brain kaise clean hota hai?','2026-11-11 10:28:35');
INSERT INTO "rejected_attempts" VALUES(5,'similarity_gating','{"title": "Mitochondria: Cell Ka Powerhouse Energy Kaise Banata Hai?", "hook": "Aapke shareer ke har cell mein hazaron tiny factories hain."}','Originality Gate Failure: 1 checks failed. Score=0.922',1.66666666666666685e-01,'Dimag ki Safai: Neend mein brain kaise clean hota hai?','2026-11-11 10:28:49');
INSERT INTO "rejected_attempts" VALUES(6,'similarity_gating','{"title": "Why Your Body Freezes During Dreams", "hook": "Sapne mein bhaagna chahte ho, lekin body move kyun nahi karti?"}','Originality Gate Failure: 1 checks failed. Score=0.802',3.69274472937998254e-01,'Sleep Paralysis – When Your Mind Wakes Before Your Body','2026-11-12 05:08:13');
CREATE TABLE sentence_scenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id TEXT NOT NULL,
    sentence_idx INTEGER NOT NULL,
    sentence_text TEXT NOT NULL,
    start_sec REAL NOT NULL,
    end_sec REAL NOT NULL,
    visual_description TEXT,
    visual_type TEXT, -- '3d_anatomy', 'microscopic', 'relatable_footage', 'infographic'
    camera_movement TEXT,
    animation_notes TEXT,
    overlay_text TEXT,
    asset_path TEXT,
    FOREIGN KEY(topic_id) REFERENCES topics(topic_id)
);
INSERT INTO "sentence_scenes" VALUES(1,'health_1b27e62b',0,'Sote waqt aapka dimag khud ki safai kaise karta hai?',0.0,3.438,'3D glowing translucent human brain suspended in deep dark studio with neon blue and golden particles shimmering around it.','3d_anatomy','slow_push_in','','DIMAG KI SAFAI','');
INSERT INTO "sentence_scenes" VALUES(2,'health_1b27e62b',1,'Jab hum gehri neend mein jaate hain, toh hamara dimag ek hidden dishwasher ki tarah kaam karta hai.',3.438,9.983,'Cinematic close-up of a human skull fading into a glowing holographic brain pulsing with a rhythmic soothing light.','3d_anatomy','cinematic_orbit','','HIDDEN DISHWASHER','');
INSERT INTO "sentence_scenes" VALUES(3,'health_1b27e62b',2,'Asal mein, deep sleep ke dauran hamare brain cells lagbhag sixty percent chote ho jaate hain, jisse cerebrospinal fluid tezi se beh kar saare toxic waste ko flush out kar deta hai.',9.983,21.883,'Microscopic view of cellular tissue where star-shaped astrocytes dramatically shrink, and crystal-clear fluid washes away glowing red Alzheimer-linked beta-amyloid plaques.','microscopic','microscopic_zoom','','60% SHRINKAGE','');
INSERT INTO "sentence_scenes" VALUES(4,'health_1b27e62b',3,'Agar aap roz raat ko poori neend nahi lete, toh yeh kachra aapke brain mein jama hota rehta hai, jo aage chalkar memory loss aur Alzheimer''s ka khatra badha sakta hai.',21.883,32.923,'A tired person sitting under warm desk lamp glow at 3 AM looking at a laptop screen, rubbing their heavy eyes in a moody cinematic room.','relatable_footage','slow_push_in','','TOXIC BUILDUP','');
INSERT INTO "sentence_scenes" VALUES(5,'health_1b27e62b',4,'Isliye, rozana saat se aath ghante ki deep sleep lena kisi medicine se kam nahi hai.',32.923,38.476,'Clean minimalist infographic animation on dark slate background showing a rising sleep timer counter hitting the 8-hour optimal mark with a glowing green checkmark.','infographic','cinematic_orbit','','7-8 HOURS SLEEP','');
INSERT INTO "sentence_scenes" VALUES(6,'health_1b27e62b',5,'Toh aaj raat aap kitne ghante sone wale hain? Humein comments mein zaroor batayein!',38.476,43.963,'Glowing 3D brain smiling slightly with a bright pulse of light radiating outwards as interactive comment icon floats gently nearby.','3d_anatomy','slow_push_in','','COMMENT BELOW','');
INSERT INTO "sentence_scenes" VALUES(7,'health_84878fc1',0,'Sote waqt aapka dimag khud ki safai kaise karta hai?',0.0,3.485,'3D holographic glowing brain in dark cinematic space with fluid pulsing through it.','3d_anatomy','slow_push_in','','BRAIN SECRET','');
INSERT INTO "sentence_scenes" VALUES(8,'health_84878fc1',1,'Jab hum gehri neend mein hote hain, toh hamare dimag ke cells lagbhag saath percent chhote ho jate hain.',3.485,10.456,'Microscopic view of glowing neurons shrinking and expanding in a synchronized rhythm.','microscopic','microscopic_zoom','','CELLS SHRINK','');
INSERT INTO "sentence_scenes" VALUES(9,'health_84878fc1',2,'Iske beech ki jagah mein cerebrospinal fluid tezi se behkar beta-amyloid jaise zehrele toxins ko bahar nikal deta hai.',10.456,18.365,'Bioluminescent cleaning fluid rushing through neural pathways, flushing out toxic debris.','3d_anatomy','cinematic_orbit','','TOXIN FLUSH','');
INSERT INTO "sentence_scenes" VALUES(10,'health_84878fc1',3,'Isko glymphatic system kehte hain, aur agar aapki neend poori nahi hoti, toh dimag mein kachra jama hone lagta hai.',18.365,26.073,'Exhausted person rubbing eyes in a dimly lit room, glowing digital hud overlay of sluggish brain activity.','relatable_footage','slow_push_in','','BAD SLEEP','');
INSERT INTO "sentence_scenes" VALUES(11,'health_84878fc1',4,'Yeh zehrele proteins age chalkar Alzheimer''s jaisi khatarnak bimariyon ki wajah ban sakte hain.',26.073,32.44,'Clean anatomical brain transitioning to a faded, clouded state with warning hud elements.','infographic','cinematic_orbit','','DISEASE RISK','');
INSERT INTO "sentence_scenes" VALUES(12,'health_84878fc1',5,'Toh aaj raat gehri neend lena mat bhuliye, kyuki aapka dimag apni safai khud karta hai. Aap kitne ghante sote hain?',32.44,40.148,'Peaceful glowing brain resting inside a starry cosmos, fading out smoothly.','3d_anatomy','slow_push_in','','SLEEP WELL','');
INSERT INTO "sentence_scenes" VALUES(13,'health_8ebe6906',0,'Aapka dil bina ruke 5 litre blood kaise pump kar leta hai?',0.1,4.383,'A photorealistic 3D human head in a dark cinematic environment with glowing golden brain activity','3d_anatomy','slow_push_in','','BRAIN CLEANING','');
INSERT INTO "sentence_scenes" VALUES(14,'health_8ebe6906',1,'Jab aap deep sleep mein hote hain, aapka brain ek extraordinary cleaning process shuru karta hai.',4.333,10.43,'Translucent 3D brain showing cerebrospinal fluid channels expanding between cerebral gyri','3d_anatomy','cinematic_orbit','','GLYMPHATIC SYSTEM','');
INSERT INTO "sentence_scenes" VALUES(15,'health_8ebe6906',2,'Isse kehte hain Glymphatic System, jahan fluid din bhar ka toxic waste aur beta-amyloid proteins wash out kar deta hai.',10.43,18.061,'Microscopic view of luminous blue fluid washing toxic protein aggregates away from neurons','microscopic','microscopic_zoom','','TOXIN FLUSH','');
INSERT INTO "sentence_scenes" VALUES(16,'health_8ebe6906',3,'Lekin agar aap regular 7 se 8 ghante ki sleep nahi lete, toh ye toxins accumulate hone lagte hain.',18.061,25.05,'Split screen of person sleeping peacefully vs tired person rubbing eyes with morning sunlight','relatable_footage','slow_push_in','','SLEEP DEPRIVATION','');
INSERT INTO "sentence_scenes" VALUES(17,'health_8ebe6906',4,'Jisse brain fog, memory loss aur long term neuro issues ka risk badh sakta hai.',25.05,30.702,'3D neural network with synapses fading and losing electrical connectivity','3d_anatomy','slow_push_in','','BRAIN FOG','');
INSERT INTO "sentence_scenes" VALUES(18,'health_8ebe6906',5,'Toh apne brain ko recover karne ka poora time dijiye, aur har raat ek peaceful sleep lijiye!',30.702,37.007,'Photorealistic 3D brain glowing with vibrant cyan and golden synapses surrounded by orbital telemetry','3d_anatomy','cinematic_orbit','','PRIORITIZE SLEEP','');
INSERT INTO "sentence_scenes" VALUES(19,'health_cafd6809',0,'Aapke sote hi dimag ka khud ka vacuum cleaner on ho jata hai!',0.1,4.665,'3D holographic glowing translucent brain in dark cinematic studio with golden synaptic firing','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(20,'health_cafd6809',1,'Jab aap gehri neend mein hote hain, tab aapka Glymphatic System activate hota hai.',4.615,10.017,'Deep slow-wave sleep state visualized with calming blue neural waves flowing across the cortex','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(21,'health_cafd6809',2,'Glial cells 60% tak shrink ho jaate hain, jisse Cerebrospinal Fluid Flush neural tissue ke andar tezi se flow karta hai.',10.017,18.235,'Extreme close-up microscopic view of brain cells shrinking as glowing cerebrospinal fluid washes away cellular debris','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(22,'health_cafd6809',3,'Yeh powerful mechanism din bhar jama hue toxic Beta-Amyloid proteins ko puri tarah wash out kar deta hai.',18.235,24.941,'Fluorescent glowing toxic beta-amyloid plaque proteins being swept away by rushing fluid currents','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(23,'health_cafd6809',4,'Agar aap roz 7-8 ghante ki deep sleep nahi lete, toh yeh dangerous toxins dimag mein accumulate hone lagte hain.',24.941,32.702,'Sleek HUD graphics showing sleep duration timeline and neurotoxin accumulation warning meters','infographic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(24,'health_cafd6809',5,'Toh kya aap aaj raat apne brain ko proper Neural Regeneration ka mauka denge?',32.702,37.757,'Radiant glowing human brain pulsing with healthy, balanced light waves against a starry cosmos background','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(25,'health_1de09cc9',0,'Sote waqt aapka dimag ek secret dishwasher chalu karta hai!',0.1,5.024,'3D holographic glowing translucent brain in dark cinematic studio with golden synaptic firing','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(26,'health_1de09cc9',1,'Jaise hi hum deep sleep mein jaate hain, hamara Glymphatic System activate ho jata hai.',4.974,10.626,'Microscopic view of brain tissue cells shifting and making space in deep blue and purple hues','microscopic','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(27,'health_1de09cc9',2,'Astrocytes shrink ho kar interstitial spaces ko lagbhag sixty percent tak bada kar dete hain, jisse cerebrospinal fluid tezi se flow karta hai.',10.626,19.648,'Detailed 3D cellular network expanding rapidly as crystal-clear fluid surges through neural pathways','3d_anatomy','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(28,'health_1de09cc9',3,'Ye powerful Cerebrospinal Fluid Flush din bhar ka sara metabolic waste aur neurotoxic beta-amyloid proteins ko bahar nikal deta hai.',19.648,28.572,'Glowing fluid washing away toxic dark protein clusters from delicate neural synapses','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(29,'health_1de09cc9',4,'Agar aap roz saat se aath ghante ki gehri neend nahi lete, toh ye toxic buildup aapke cognitive health ko severely affect kar sakta hai.',28.572,37.257,'Cinematic low-light shot of a person sleeping peacefully in a calm, aesthetic room','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(30,'health_1de09cc9',5,'Toh aap aaj raat kitne ghante sone wale hain, taaki aapka Brain Detox complete ho sake?',37.257,43.387,'Glowing 3D brain pulsing with soft cyan light against a dark minimalist background','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(31,'health_38303f90',0,'Aapka brain raat ko rest nahi, balki toxic waste flush karta hai!',0.1,4.98,'3D holographic glowing brain in dark cinematic studio with golden synaptic firing.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(32,'health_38303f90',1,'Jab aap gehri neend mein hote ho, toh aapka central nervous system ek powerful mechanism activate karta hai jise glymphatic system kehte hain.',4.93,13.496,'Microscopic view of glial cells shrinking and expanding in deep blue tissue matrix.','microscopic','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(33,'health_38303f90',2,'Is process ke dauran glial cells shrink ho jaate hain, jisse cerebrospinal fluid ka ek tez surge brain tissue ke andar flow karta hai.',13.496,21.898,'Luminous cerebrospinal fluid rapidly surging through translucent neural pathways.','3d_anatomy','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(34,'health_38303f90',3,'Yeh fluid din bhar jam hue beta-amyloid proteins ko puri tarah se wash out kar deta hai, jo Alzheimer''s disease se jude hote hain.',21.898,37.996,'Glowing fluid clearing away toxic dark protein plaque clusters from neural networks.','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(35,'health_38303f90',4,'Isliye, rozana saat se aath ghante ki neural regeneration neend lena aapki long-term cognitive health ke liye behad zaroori hai.',37.996,44.191,'Serene cinematic portrait of peaceful deep sleep with soft ambient moonlight filtering in.','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(36,'health_38303f90',5,'Kya aapko lagta hai ki aapki current sleep schedule aapke brain ko properly detox kar pa rahi hai? Comment mein zaroor batayein!',44.191,46.539,'Clean, modern minimalist UI overlay on a dark brain graphic prompting viewer engagement.','infographic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(37,'health_c356fe6d',0,'Kya aapko pata hai, sote waqt bhi aapka dimaag ek zaroori kaam karta hai?',0.0,4.918,'3D holographic glowing brain in dark cinematic studio with golden synaptic firing','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(38,'health_c356fe6d',1,'Jab hum deep sleep me hote hain, tab hamara Glymphatic System activate ho jata hai.',4.918,10.51,'Extreme close-up of glial cells shrinking in real-time, opening up neural tissue pathways','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(39,'health_c356fe6d',2,'Is process ke dauran, cerebrospinal fluid rapid flush ki tarah brain tissue me se guzarta hai aur saari metabolic waste ko wash out kar deta hai.',10.51,20.279,'Bioluminescent cerebrospinal fluid surging through microscopic interstitial spaces of glowing neural networks','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(40,'health_c356fe6d',3,'Yahi woh mechanism hai jo beta-amyloid proteins ko clear karta hai, jo ki Alzheimer''s jaisi neurodegenerative diseases se jude hote hain.',20.279,29.509,'Microscopic view of toxic beta-amyloid protein plaques being swept away by fluid currents','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(41,'health_c356fe6d',4,'Agar aap daily 7-8 hours ki sound sleep nahi lete, toh yeh neural regeneration process disrupt ho sakti hai.',29.509,36.785,'Cinematic ambient shot of a peaceful person sleeping deeply in a serene, dimly lit modern bedroom','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(42,'health_c356fe6d',5,'Toh agli baar jab aap late night tak jagoge, sochna ki aapka dimaag apna sabse zaroori safai abhi miss kar raha hai. Aap kitne ghante sote hain?',36.785,46.486,'Stunning macro shot of a fully revitalized, glowing neural network pulsing with vibrant blue energy','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(43,'health_d273fc65',0,'Kya aapko pata hai, sote waqt bhi aapka dimaag ek zaroori kaam karta hai?',0.1,5.361,'3D holographic glowing brain in dark cinematic studio with golden synaptic firing','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(44,'health_d273fc65',1,'Jaise hi aap gehri neend mein jaate hain, aapka dimaag ek powerful cleaning process shuru karta hai.',5.311,11.691,'Cinematic orbit around a translucent human brain showing deep internal structural lighting shifts as sleep begins','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(45,'health_d273fc65',2,'Is process ke dauran, aapke brain ke glial cells shrink ho jaate hain, jisse Cerebrospinal Fluid tezi se neural tissue ke beech flush hota hai.',11.691,20.854,'Microscopic view of shrinking glial cells widening intercellular gaps while clear cerebrospinal fluid washes through neurons','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(46,'health_d273fc65',3,'Ye convective flow din bhar jama hue toxic waste products aur Beta-Amyloid proteins ko effectively clear kar deta hai.',20.854,28.398,'High-detail cellular visualization of toxic beta-amyloid protein plaques being swept away by fluid current','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(47,'health_d273fc65',4,'Agar aap roz poori 7 se 8 ghante ki neend nahi lete, toh ye neurological waste dimaag mein hi jama hota rehta hai.',28.398,36.17,'Atmospheric cinematic shot of a person resting peacefully in a dimly lit modern bedroom at night','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(48,'health_d273fc65',5,'Toh agli baar jab aap late night scrolling ka sochein, khud se poochein—kya aap apne dimaag ko flush hone se rokna chahte hain?',36.17,44.517,'Glowing 3D brain pulsing with vibrant blue light against a deep slate background, signifying optimal neural health','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(49,'health_7febd121',0,'Aapka brain raat ko rest nahi, balki toxic waste flush karta hai!',0.1,4.98,'3D holographic glowing brain in dark cinematic studio with golden synaptic firing','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(50,'health_7febd121',1,'Jab hum deep sleep mein jaate hain, toh hamare central nervous system ki glial cells shrink ho jaati hain.',4.93,11.202,'Microscopic view of glial cells contracting and creating wide intercellular pathways in neural tissue','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(51,'health_7febd121',2,'Isse intercellular space widen hota hai aur Glymphatic System activate ho jata hai, jisse Cerebrospinal Fluid ka ek powerful surge brain tissue ke through flow karta hai.',11.202,21.778,'Brilliant cyan cerebrospinal fluid surging rapidly through the translucent pathways of the cerebral cortex','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(52,'health_7febd121',3,'Ye fluid din bhar jam hue beta-amyloid proteins—jo neurodegeneration ka karan bante hain—unhe efficiently clear kar deta hai.',21.778,29.854,'Glowing blue fluid washing away toxic amber protein aggregates from microscopic neural synapses','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(53,'health_7febd121',4,'Agar aap roz 7 se 8 hours ki quality sleep nahi lete, toh ye toxic waste accumulate hone lagta hai.',29.854,36.996,'Cinematic side profile of a person sleeping peacefully under soft warm studio lighting','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(54,'health_7febd121',5,'Toh batayiye, aaj raat aap apne brain ko proper Brain Detox dene ke liye kitne ghante soyenge?',36.996,43.387,'Radiant 3D human brain pulsing with calm, steady cyan light against a deep obsidian background','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(55,'health_81ee3387',0,'Aapka brain raat ko rest nahi, balki toxic waste flush karta hai!',0.1,4.98,'3D holographic glowing brain in dark cinematic studio with golden synaptic firing','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(56,'health_81ee3387',1,'Jaise hi hum deep sleep mein enter karte hain, hamara glymphatic system active ho jata hai.',4.93,10.724,'Microscopic view of glial cells shrinking by about 60 percent inside dark cerebral tissue','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(57,'health_81ee3387',2,'Cerebrospinal fluid yaani CSF, brain parenchyma ke andar tezi se surge karta hai.',10.724,16.789,'Luminescent blue cerebrospinal fluid rushing smoothly through neural pathways and blood vessels','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(58,'health_81ee3387',3,'Yeh powerful mechanism din bhar jama hue neurotoxic beta-amyloid proteins ko puri tarah wash out kar deta hai.',16.789,23.778,'Close-up of glowing protein plaque particles being swept away by rushing fluid currents','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(59,'health_81ee3387',4,'Agar aap roz 7 se 8 hours ki quality sleep nahi lete, toh yeh metabolic waste brain mein hi accumulate hota rehta hai.',23.778,31.746,'Minimalist graphic showing declining fluid clearance curves during sleep deprivation','infographic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(60,'health_81ee3387',5,'Toh apne glymphatic system ko optimize karne ke liye, aaj raat aap kitne baje so rahe hain?',31.746,37.615,'Cinematic warm bedroom lighting with person resting peacefully as dawn approaches','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(79,'day04_video07',0,'Aapke stomach mein powerful acid hota hai, phir woh khud ko digest kyun nahi karta?',0.1,5.611,'3D glowing translucent human stomach in a dark slate studio with subtle amber and blue highlights.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(80,'day04_video07',1,'Stomach ki inner walls par alkaline mucus aur bicarbonate ki ek thick shield hoti hai.',5.561,11.735,'Extreme close-up microscopic view of surface mucous cells secreting a glistening, gelatinous alkaline layer.','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(81,'day04_video07',2,'Is protective mechanism ko hum Gastric Mucus Barrier kehte hain.',11.735,15.996,'Clean anatomical cross-section graphic highlighting the exact mucosal cell lining with glowing text overlays.','infographic','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(82,'day04_video07',3,'Yeh specialized layer hydrochloric acid ko direct stomach tissue tak pahunchne nahi deti.',15.996,21.767,'Close-up 3D render showing corrosive acid molecules bouncing off the thick, glowing mucus gel surface.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(83,'day04_video07',4,'Is barrier ki continuous cellular division har kuch dino mein mucosal lining ko renew karti hai.',21.767,27.593,'Fast-paced microscopic timelapse of epithelial cells dividing rapidly to regenerate the stomach lining.','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(84,'day04_video07',5,'Aapke gut ki yeh defensive chemistry kitni fascinating hai, hai na?',27.593,32.365,'Cinematic full view of glowing human digestive system pulsing with soft bioluminescent light against a dark background.','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(85,'day01_video01',0,'Aapka brain duniya ko exactly waise nahi dekhta jaise woh actually hai!',0.0,4.983,'3D glowing translucent human skull and brain model in dark slate studio with pulsating neon blue neural highlights.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(86,'day01_video01',1,'Aapka brain har second aane wale visual aur sensory signals ko pehle se guess karta hai.',4.983,11.159,'Cinematic first-person perspective tracking rapidly moving traffic and pedestrians with subtle predictive motion trail overlays.','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(87,'day01_video01',2,'Is complex neurological mechanism ko science mein Predictive Processing kehte hain.',11.159,16.984,'Macro view of firing neural pathways sending synchronized electrical impulses across the cerebral cortex.','3d_anatomy','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(88,'day01_video01',3,'Ye survival mechanism isliye evolve hua taaki aap bina delay ke tezi se react kar sakein.',16.984,23.23,'Athletic hand catching a fast-moving object in slow motion, highlighting instant motor cortex coordination.','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(89,'day01_video01',4,'Jab aapki receptor sensitivity strong hoti hai, toh aapke neural pathways aur bhi fast kaam karte hain.',23.23,30.458,'Close-up microscopic simulation of synaptic cleft neurotransmitters transferring signals between neurons.','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(90,'day01_video01',5,'Kya aapko lagta hai ki aapka brain is waqt aapke aage chal raha hai? Comments mein bataiye!',30.458,36.844,'Rotating glowing holographic brain gently fading into dark minimal background with subtle UI data points.','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(91,'day08_video15',0,'Human body ka ek organ apna lost tissue dobara grow kar sakta hai!',0.0,4.467,'3D glowing translucent human torso with the liver highlighted in warm amber and gold light against a dark slate background.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(92,'day08_video15',1,'Liver ke cells apne original shape aur size ko restore karne ke liye tezi se divide ho sakte hain.',4.467,11.099,'Cinematic macro shot focusing on healthy human abdominal cross-section with pulsing arterial blood flow.','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(93,'day08_video15',2,'Ise kehte hain Compensatory Hyperplasia yaani Liver Regeneration, jahan quiescent hepatocytes dobara cell cycle mein enter karte hain.',11.099,20.168,'Stunning microscopic CGI showing individual liver cells dividing rapidly with glowing DNA strands and active cellular receptors.','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(94,'day08_video15',3,'Agar liver ka 70% hissa surgically nikal bhi diya jaye, toh bhi bacha hua tissue apna 100% mass wapas gain kar leta hai.',20.168,28.289,'Clean anatomical split-screen graphic illustrating a 70 percent organ resection seamlessly transforming back into a full-sized liver.','infographic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(95,'day08_video15',4,'Yeh incredible mechanism hamari body ko toxins se protect karta hai aur harsh metabolic stress mein bhi survival ensure karta hai.',28.289,37.087,'Close-up 3D render of hepatic blood filtration pathways neutralizing glowing toxin particles in real-time.','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(96,'day08_video15',5,'Kya aapko pata tha ki human liver bina kisi surgical help ke khud ko heal kar sakta hai? Comments mein batao!',37.087,44.464,'Polished BBC-style presenter studio backdrop with soft depth-of-field and glowing biological infographics.','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(97,'day01_video02',0,'Aapki ek nostril zyada active hoti hai, phir kuch ghanton baad doosri!',0.0,4.751,'Close-up 3D holographic render of a human nose in a dark slate studio with subtle ambient lighting.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(98,'day01_video02',1,'Aapki dono nostrils mein se ek waqt par sirf ek hi zyada khuli hoti hai.',4.751,9.638,'Clean, cinematic macro shot showing airflow dynamics and subtle nasal tissue movement.','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(99,'day01_video02',2,'Is rhythmic switching of autonomic erectile tissue inside the nose ko Nasal Cycle kehte hain.',9.638,15.95,'Cross-section 3D medical visualization highlighting alternating nasal turbinates and vascular congestion.','3d_anatomy','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(100,'day01_video02',3,'Taaki ek side rest karke moisture recover kar sake aur receptor sensitivity maintain rahe.',15.95,22.059,'Microscopic view of olfactory receptor cells and mucosal lining glowing under optimal humidity.','microscopic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(101,'day01_video02',4,'Ye automatic neural pathways ke through control hota hai bina aapke dhyan ke.',22.059,27.285,'Glowing neural pathways connecting the autonomic nervous system directly to the nasal cavity.','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(102,'day01_video02',5,'Kya aapne kabhi notice kiya ki kis waqt aapki kaunsi nostril zyada active hoti hai?',27.285,32.919,'Clean minimalist infographic interface displaying alternating nostril activity metrics in real-time.','infographic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(103,'day02_video03',0,'Sapne mein bhaagna chahte ho, lekin body move kyun nahi karti?',0.1,4.665,'Cinematic slow-motion shot of a person sleeping restfully in dim blue lighting, subtle dynamic lighting shifts.','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(104,'day02_video03',1,'Jab aap deep REM sleep mein hote hain, aapka brainstem temporary tor par voluntary muscles ke neural pathways ko block kar deta hai.',4.615,12.626,'3D glowing translucent human brain focusing on the brainstem pulsing with bioluminescent neural signals.','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(105,'day02_video03',2,'Is exact physiological mechanism ko hum REM Sleep Muscle Atonia kehte hain, jahan glycine aur GABA neurotransmitters motor neurons ko suppress karte hain.',12.626,22.235,'Microscopic animation of neurotransmitter molecules binding to cellular receptors across a synaptic cleft in vibrant purple and cyan.','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(106,'day02_video03',3,'Ye evolutionary defense mechanism hai taaki aap vivid dreams ke dauran physically react karke khud ko ya apne partner ko injure na kar dein.',22.235,31.126,'3D skeletal and muscular system of the human body glowing softly in a defensive posture.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(107,'day02_video03',4,'Jab ye system kabhi-kabhi premature disable ho jata hai, tab aapko sleep paralysis ka experience hota hai.',31.126,38.072,'Clean minimalist infographic overlay showing sleep stage transition timelines and motor neuron activity graphs.','infographic','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(108,'day02_video03',5,'Aapke brain ki ye safety coding kitni fascinating hai, niche comment karke bataiye?',38.072,43.713,'Cinematic close-up of peaceful human eyes resting during REM sleep with subtle ambient starfield backdrop.','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(109,'day02_video04',0,'Ghoomna band karne ke baad bhi duniya kyun ghoomti rehti hai?',0.0,3.915,'3D anatomical visual for Why You Feel Dizzy After Spinning in dark slate studio','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(110,'day02_video04',1,'Aapki body mein Aapke kaan ke andar fluid se bhari tiny tubes hoti hain jo balance banaye rakhti hain.',3.915,10.461,'Relatable everyday footage illustrating bodily sensation','relatable_footage','slow_drift','','','');
INSERT INTO "sentence_scenes" VALUES(111,'day02_video04',2,'Science mein is biological process ko Vestibular System kehte hain, jo body ko dynamically regulate karta hai.',10.461,17.521,'Microscopic cellular mechanisms in action','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(112,'day02_video04',3,'Yeh mechanism isliye zaroori hai ghoomne ke baad fluid chalta rehta hai, isliye brain ko lagta hai ki aap abhi bhi ghoom rahe hain.',17.521,25.928,'3D physiological anatomical system operating smoothly','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(113,'day02_video04',4,'Is natural system ko healthy rakhne ke liye balanced daily routine aur body awareness behad zaroori hai.',25.928,32.602,'Healthy lifestyle and wellness application','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(114,'day02_video04',5,'Toh kya aap Why You Feel Dizzy After Spinning ke is secret science ke baare mein jaante the? Humein comments mein batayein!',32.602,40.496,'Illuminated anatomical scan with closing engagement question','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(115,'day03_video05',0,'Dar ya thand lagte hi body ke baal khade kyun ho jaate hain?',0.0,3.878,'Close-up 3D render of human skin pores with fine hairs instantly springing upright on a dark slate background.','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(116,'day03_video05',1,'Jab humein thand lagti hai ya sudden fear hota hai, toh skin ke niche ki tiny smooth muscles contract ho jaati hain.',3.878,11.376,'Microscopic cross-section of skin showing involuntary muscle fibers pulling tightly against a hair follicle.','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(117,'day03_video05',2,'Science mein is automatic sympathetic nervous system reflex ko Piloerection kehte hain.',11.376,17.0,'Glowing neural pathways lighting up along the spine, transmitting rapid electrical signals to the skin tissue.','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(118,'day03_video05',3,'Yeh evolution ka ek brilliant survival mechanism hai jo thand mein body heat trap karne aur dar ke waqt bade dikh kar threat ko intimidate karne ke liye design hua tha.',17.0,27.86,'Cinematic side-by-side visualization of heat insulation layers forming around the skin surface.','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(119,'day03_video05',4,'Aaj ke modern humans mein iska practical use kam ho gaya hai, lekin hamari receptor sensitivity aaj bhi waise hi react karti hai.',27.86,36.199,'Sleek biometric HUD overlay displaying real-time receptor sensitivity and nervous system activation data.','infographic','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(120,'day03_video05',5,'Aapko aakhri baar goosebumps kis movie ya gaane ki wajah se aaye the? Comments mein batao!',36.199,42.017,'Stunning macro shot of skin reacting to a sudden wave of emotional goosebumps in ambient studio light.','relatable_footage','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(121,'day03_video06',0,'Aapka heart apni electrical signals generate karke beat kar sakta hai!',0.0,4.538,'3D anatomical visual for Your Heart Has Its Own Electrical System in dark slate studio','3d_anatomy','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(122,'day03_video06',1,'Aapki body mein Heart ke andar ek natural electric generator hota hai jo har dhadkan ka current banata hai.',4.538,11.475,'Relatable everyday footage illustrating bodily sensation','relatable_footage','slow_drift','','','');
INSERT INTO "sentence_scenes" VALUES(123,'day03_video06',2,'Science mein is biological process ko Sinoatrial (SA) Node kehte hain, jo body ko dynamically regulate karta hai.',11.475,18.801,'Microscopic cellular mechanisms in action','microscopic','microscopic_zoom','','','');
INSERT INTO "sentence_scenes" VALUES(124,'day03_video06',3,'Yeh mechanism isliye zaroori hai isi electrical pulse ki wajah se heart brain ke bina bhi beat karta reh sakta hai.',18.801,26.257,'3D physiological anatomical system operating smoothly','3d_anatomy','cinematic_orbit','','','');
INSERT INTO "sentence_scenes" VALUES(125,'day03_video06',4,'Is natural system ko healthy rakhne ke liye balanced daily routine aur body awareness behad zaroori hai.',26.257,33.0,'Healthy lifestyle and wellness application','relatable_footage','slow_push_in','','','');
INSERT INTO "sentence_scenes" VALUES(126,'day03_video06',5,'Toh kya aap Your Heart Has Its Own Electrical System ke is secret science ke baare mein jaante the? Humein comments mein batayein!',33.0,41.429,'Illuminated anatomical scan with closing engagement question','3d_anatomy','slow_push_in','','','');
CREATE TABLE topics (
    topic_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    hook TEXT,
    hook_style TEXT,
    research_summary TEXT,
    research_sources TEXT, -- JSON array of URLs and medical journals
    evidence_status TEXT DEFAULT 'verified', -- 'verified', 'emerging', 'established'
    script_text TEXT,
    duration_estimated REAL,
    duration_actual REAL,
    voice_file_path TEXT,
    video_path TEXT,
    thumbnail_path TEXT,
    status TEXT DEFAULT 'discovered', -- 'discovered', 'scripted', 'voiced', 'rendered', 'qc_passed', 'published', 'rejected'
    qc_passed BOOLEAN DEFAULT 0,
    qc_report TEXT,
    upload_id TEXT,
    publication_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "topics" VALUES('health_50832fcb','Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?','Sleep Science','Sote waqt aapka dimag ek hidden washing machine ban jata hai!','Curiosity',NULL,'["https://www.nih.gov/news-events/nih-research-matters/how-sleep-clears-brain", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'hook_approved',0,NULL,NULL,NULL,'2026-11-11 07:17:51','2026-11-11 07:17:53');
INSERT INTO "topics" VALUES('health_bceef8e5','Dimag ki Safai: Neend mein brain kaise clean hota hai?','Sleep Science','Sote waqt aapka dimag ek secret cleaning machine ban jata hai!','Curiosity',NULL,'[]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'hook_approved',0,NULL,NULL,NULL,'2026-11-11 07:19:10','2026-11-11 07:19:12');
INSERT INTO "topics" VALUES('health_1b27e62b','Dimag ki Safai: Glymphatic System Kaise Kaam Karta Hai?','Sleep Science','Sote waqt aapka dimag khud ki safai kaise karta hai?','Curiosity',NULL,'[]','verified',NULL,NULL,43.963,NULL,'/home/rishabh/Heath Videos/output/videos/health_1b27e62b_health_short.mp4',NULL,'qc_failed',0,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_1b27e62b`  
**Title**: Dimag ki Safai: Glymphatic System Kaise Kaam Karta Hai?  
**Category**: Sleep Science  
**Overall Verdict**: **REJECTED (REQUIRES REPAIR)**  
**Score**: 14/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 43.94s, Audio duration: 43.99s, Delta: 0.05s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with assigned visual specifications. |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (19511 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 60133786 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 43.94s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ❌ FAIL | 0 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Dimag ki Safai: Glymphatic System Kaise Kaam Karta Hai?'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_1b27e62b_health_short.mp4`  
',NULL,NULL,'2026-11-11 07:20:38','2026-11-11 07:23:05');
INSERT INTO "topics" VALUES('health_84878fc1','Dimag ki Safai: Glymphatic System Kaise Kaam Karta Hai?','Sleep Science','Sote waqt aapka dimag khud ki safai kaise karta hai?','Curiosity','During deep NREM sleep, brain cells shrink by about 60%, allowing cerebrospinal fluid (CSF) to rush through the tissue and flush out neurotoxic waste products like beta-amyloid proteins. This nocturnal cleansing mechanism, known as the glymphatic system, is primarily driven by glial cells and is essential for preventing neurodegenerative diseases.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/", "https://www.nih.gov/news-events/nih-research-matters/how-sleep-clears-brain"]','verified',NULL,NULL,40.148,NULL,'/home/rishabh/Heath Videos/output/videos/health_84878fc1_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_84878fc1_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_84878fc1`  
**Title**: Dimag ki Safai: Glymphatic System Kaise Kaam Karta Hai?  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 40.13s, Audio duration: 40.18s, Delta: 0.05s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with assigned visual specifications. |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (16847 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 44468248 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 40.13s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Dimag ki Safai: Glymphatic System Kaise Kaam Karta Hai?'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_84878fc1_health_short.mp4`  
',NULL,NULL,'2026-11-11 07:26:44','2026-11-11 07:28:58');
INSERT INTO "topics" VALUES('health_8ebe6906','Har Dhadkan Ke Peeche: 1 Minute Mein 5 Litre Blood!','Heart and Blood Circulation','Aapka dil bina ruke 5 litre blood kaise pump kar leta hai?','Curiosity','A human heart beats approximately 100,000 times a day, pumping around 5 liters of oxygen-rich blood through 60,000 miles of blood vessels in just 60 seconds.','["https://medlineplus.gov/ency/anatomyvideos/000023.htm", "https://www.cdc.gov/heartdisease/facts.htm"]','verified',NULL,NULL,37.007,NULL,'/home/rishabh/Heath Videos/output/videos/health_8ebe6906_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_8ebe6906_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_8ebe6906`  
**Title**: Har Dhadkan Ke Peeche: 1 Minute Mein 5 Litre Blood!  
**Category**: Heart and Blood Circulation  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 36.97s, Audio duration: 37.03s, Delta: 0.07s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with assigned visual specifications. |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (16080 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 41562039 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 36.97s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Har Dhadkan Ke Peeche: 1 Minute Mein 5 Litre Blood!'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_8ebe6906_health_short.mp4`  
',NULL,NULL,'2026-11-11 07:32:55','2026-11-11 07:35:02');
INSERT INTO "topics" VALUES('health_cafd6809','Dimag Ka Vacuum Cleaner: Glymphatic System Kaise Safai Karta Hai?','Sleep Science','Aapke sote hi dimag ka khud ka vacuum cleaner on ho jata hai!','Curiosity','During deep slow-wave sleep, glial cells in the brain shrink by up to 60%, dramatically increasing interstitial space. This allows cerebrospinal fluid (CSF) to flush through the neural tissue, clearing out neurotoxic waste products accumulated during waking hours, including beta-amyloid proteins associated with Alzheimer''s disease.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/", "https://www.nih.gov/news-events/news-releases/nih-funded-scientists-explain-how-sleep-cleans-toxins-brain"]','verified',NULL,NULL,37.757,NULL,'/home/rishabh/Heath Videos/output/videos/health_cafd6809_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_cafd6809_thumb.jpg','qc_failed',0,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_cafd6809`  
**Title**: Dimag Ka Vacuum Cleaner: Glymphatic System Kaise Safai Karta Hai?  
**Category**: Sleep Science  
**Overall Verdict**: **REJECTED (REQUIRES REPAIR)**  
**Score**: 14/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 37.73s, Audio duration: 37.78s, Delta: 0.05s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with assigned visual specifications. |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (22759 bytes) |
| 07 | Zero Black Frames | ❌ FAIL | Detected black frames: 3 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 41043489 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 37.73s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Dimag Ka Vacuum Cleaner: Glymphatic System Kaise Safai Karta Hai?'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_cafd6809_health_short.mp4`  
',NULL,NULL,'2026-11-11 08:38:50','2026-11-11 08:40:37');
INSERT INTO "topics" VALUES('health_1de09cc9','Aapka brain raat ko khud ko kaise CLEAN karta hai? The Glymphatic System!','Sleep Science','Sote waqt aapka dimag ek secret dishwasher chalu karta hai!','Curiosity','During deep slow-wave sleep, astrocytes shrink, widening the interstitial spaces in the brain by roughly 60%. This allows cerebrospinal fluid (CSF) to surge through the brain tissue, flushing out metabolic waste products accumulated during waking hours, including neurotoxic beta-amyloid proteins.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/", "https://www.nih.gov/news-events/news-releases/how-sleep-clears-toxins-brain"]','verified',NULL,NULL,43.387,NULL,'/home/rishabh/Heath Videos/output/videos/health_1de09cc9_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_1de09cc9_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_1de09cc9`  
**Title**: Aapka brain raat ko khud ko kaise CLEAN karta hai? The Glymphatic System!  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 43.37s, Audio duration: 43.42s, Delta: 0.05s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with assigned visual specifications. |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (24764 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 74558540 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 43.37s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Aapka brain raat ko khud ko kaise CLEAN karta hai? The Glymphatic System!'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_1de09cc9_health_short.mp4`  
',NULL,NULL,'2026-11-11 08:43:46','2026-11-11 08:46:23');
INSERT INTO "topics" VALUES('health_38303f90','Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨','Sleep Science','Aapka brain raat ko rest nahi, balki toxic waste flush karta hai!','Counter-Intuitive Truth','During deep sleep, glial cells in the central nervous system shrink, widening the intercellular space and activating the glymphatic system. This allows cerebrospinal fluid (CSF) to surge through the brain tissue, flushing out neurotoxic waste products accumulated during wakefulness, including beta-amyloid proteins associated with Alzheimer''s disease.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/", "https://www.nih.gov/news-events/news-releases/nih-funded-scientists-explain-how-sleep-cleans-toxins-brain"]','verified',NULL,NULL,46.539,NULL,'/home/rishabh/Heath Videos/output/videos/health_38303f90_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_38303f90_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_38303f90`  
**Title**: Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 43.64s, Audio duration: 43.68s, Delta: 0.04s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (28256 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 33009400 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 43.64s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_38303f90_health_short.mp4`  
',NULL,NULL,'2026-11-11 09:43:54','2026-11-11 09:45:50');
INSERT INTO "topics" VALUES('health_c356fe6d','Aapka brain sote waqt khud ko kaise clean karta hai? (Glymphatic System)','Sleep Science','Kya aapko pata hai, sote waqt bhi aapka dimaag ek zaroori kaam karta hai?','Engaging Question','During deep sleep, glial cells in the brain shrink, widening the interstitial spaces and allowing cerebrospinal fluid (CSF) to flush rapidly through the tissue. This ''glymphatic clearance'' process uses convective flow to wash away neurotoxic waste products accumulated during waking hours, including beta-amyloid proteins linked to Alzheimer''s disease.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636972/", "https://www.nih.gov/news-events/news-releases/how-sleep-clears-mind"]','verified',NULL,NULL,46.486,NULL,'/home/rishabh/Heath Videos/output/videos/health_c356fe6d_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_c356fe6d_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_c356fe6d`  
**Title**: Aapka brain sote waqt khud ko kaise clean karta hai? (Glymphatic System)  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 43.59s, Audio duration: 43.63s, Delta: 0.04s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (27483 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 34457875 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 43.59s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Aapka brain sote waqt khud ko kaise clean karta hai? (Glymphatic System)'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_c356fe6d_health_short.mp4`  
',NULL,NULL,'2026-11-11 09:51:43','2026-11-11 09:53:52');
INSERT INTO "topics" VALUES('health_d273fc65','Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨','Sleep Science','Kya aapko pata hai, sote waqt bhi aapka dimaag ek zaroori kaam karta hai?','Engaging Question','During deep sleep, glial cells in the brain shrink, dramatically increasing the intercellular space and allowing cerebrospinal fluid (CSF) to flush through neural tissue via the glymphatic system. This convective flow clears out neurotoxic waste products accumulated during wakefulness, including beta-amyloid proteins associated with neurodegeneration.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/", "https://www.nih.gov/news-events/news-releases/how-sleep-clears-mind"]','verified',NULL,NULL,44.517,NULL,'/home/rishabh/Heath Videos/output/videos/health_d273fc65_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_d273fc65_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_d273fc65`  
**Title**: Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 41.62s, Audio duration: 41.66s, Delta: 0.04s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (27272 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 24705459 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 41.62s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_d273fc65_health_short.mp4`  
',NULL,NULL,'2026-11-11 09:57:26','2026-11-11 09:59:14');
INSERT INTO "topics" VALUES('health_7febd121','Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨','Sleep Science','Aapka brain raat ko rest nahi, balki toxic waste flush karta hai!','Counter-Intuitive Truth','During deep sleep, glial cells in the central nervous system shrink, widening the intercellular space and activating the glymphatic system. This allows cerebrospinal fluid (CSF) to surge through the brain tissue, efficiently flushing out neurotoxic waste products accumulated during wakefulness, including beta-amyloid proteins associated with neurodegeneration.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/", "https://www.nih.gov/news-events/news-releases/nih-funded-scientists-explain-how-sleep-cleans-toxins-brain"]','verified',NULL,NULL,43.387,NULL,'/home/rishabh/Heath Videos/output/videos/health_7febd121_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_7febd121_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_7febd121`  
**Title**: Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 40.49s, Audio duration: 40.54s, Delta: 0.04s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (25628 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 18633868 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 40.49s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Aapka brain raat ko khud ko kaise WASH karta hai? 🧠✨'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_7febd121_health_short.mp4`  
',NULL,NULL,'2026-11-11 10:01:33','2026-11-11 10:03:18');
INSERT INTO "topics" VALUES('health_81ee3387','Aapka brain sote waqt khud ko kaise clean karta hai? (Glymphatic System)','Sleep Science','Aapka brain raat ko rest nahi, balki toxic waste flush karta hai!','Counter-Intuitive Truth','During deep slow-wave sleep, glial cells in the central nervous system shrink by about 60%, drastically increasing the interstitial space. This allows cerebrospinal fluid (CSF) to surge through the brain parenchyma via the glymphatic system, efficiently washing away metabolic waste products accumulated during wakefulness, including neurotoxic beta-amyloid proteins.','["https://pubmed.ncbi.nlm.nih.gov/24137970/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/"]','verified',NULL,NULL,37.615,NULL,'/home/rishabh/Heath Videos/output/videos/health_81ee3387_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/health_81ee3387_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `health_81ee3387`  
**Title**: Aapka brain sote waqt khud ko kaise clean karta hai? (Glymphatic System)  
**Category**: Sleep Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 15/15 Gates Passed  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 34.71s, Audio duration: 34.75s, Delta: 0.04s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (22440 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 34397413 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-20dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 34.71s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Deduplication | ✅ PASS | Topic ''Aapka brain sote waqt khud ko kaise clean karta hai? (Glymphatic System)'' verified unique in SQLite catalog. |

---
**Verified Output**: `/home/rishabh/Heath Videos/output/videos/health_81ee3387_health_short.mp4`  
',NULL,NULL,'2026-11-11 10:05:36','2026-11-11 10:07:28');
INSERT INTO "topics" VALUES('day04_video08','Your Blood Cells Have an Expiry Date','Heart and Blood Circulation','Aapke blood ke red cells hamesha nahi jeete!','Curiosity Question','Erythrocyte lifespan: red blood cells circulate for approximately 120 days before losing membrane flexibility and getting engulfed by splenic macrophages.','["https://www.ncbi.nlm.nih.gov/books/NBK2263/", "https://www.nih.gov/news-events/nih-research-matters/how-spleen-filters-blood"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day05_video09','Why Do You Forget Why You Entered a Room?','Brain and Psychology','Room mein enter karte hi yaad kyun nahi rehta ki aaye kis kaam se the?','Curiosity Question','The Doorway Effect: passing through physical doorways creates event boundaries in episodic working memory, triggering mental file compartmentalization.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3212853/", "https://www.scientificamerican.com/article/why-walking-through-doorways-makes-us-forget/"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day05_video10','Why Do You See Flashes After Rubbing Your Eyes?','Eyes and Human Senses','Aankhein band karne par bhi light jaisi cheezein kyun dikhti hain?','Curiosity Question','Phosphenes: mechanical pressure on the eyeball directly depolarizes retinal ganglion cells, which the visual cortex interprets as light bursts.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656113/", "https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day06_video11','Why Do You Suddenly Jerk While Falling Asleep?','Sleep Science','Sote-sote achanak aisa lagta hai jaise gir rahe ho?','Curiosity Question','Hypnic jerks: involuntary myoclonic twitches occurring during the transition from wakefulness to NREM sleep when motor signals misfire.','["https://www.ncbi.nlm.nih.gov/books/NBK560720/", "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-science-of-sleep"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day06_video12','Why Does a Song Keep Playing Inside Your Head?','Brain and Psychology','Ek song dimag mein baar-baar kyun bajta rehta hai?','Curiosity Question','Involuntary Musical Imagery (earworms): spontaneous reactivation of phonological loops in the auditory cortex without conscious effort.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440618/", "https://www.apa.org/monitor/2016/10/music-earworms"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day07_video13','Your Lungs Have Millions of Tiny Air Sacs','Human Body Secrets','Aapke lungs ke andar millions of tiny air sacs hote hain!','Curiosity Question','Pulmonary alveoli: 480 million microscopic spherical sacs providing 100 square meters of surface area for passive capillary diffusion of O2 and CO2.','["https://www.ncbi.nlm.nih.gov/books/NBK542318/", "https://www.nhlbi.nih.gov/health/lungs/respiratory-system"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day07_video14','Why Do Memories Change Every Time You Recall Them?','Brain and Psychology','Aapki memory video recording ki tarah fixed nahi hoti!','Curiosity Question','Memory reconsolidation: retrieving an episodic memory renders its synaptic trace labile and susceptible to modification before it is re-stabilized.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3789138/", "https://www.nature.com/articles/nn.3503"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day08_video16','The Nerve That Connects Your Brain to Your Gut','Gut Health','Aapke stomach aur brain ke beech ek communication highway hai!','Curiosity Question','The vagus nerve (Cranial Nerve X): bidirectional electrical superhighway carrying 80% sensory afferent signals from the gut microbiome to the brain.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5808284/", "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-brain-gut-connection"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day09_video17','Why Do You Still See an Image After Looking Away?','Eyes and Human Senses','Bright object ko dekhne ke baad bhi uski image aankhon ke saamne kyun rehti hai?','Curiosity Question','Negative afterimages: prolonged photic stimulation bleaches photopigments in retinal cone photoreceptors, causing rebound signals in opponent color channels.','["https://www.ncbi.nlm.nih.gov/books/NBK11532/", "https://www.britannica.com/science/afterimage"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day09_video18','How Can You Touch Your Nose With Closed Eyes?','Human Body Secrets','Aankhein band hone ke baad bhi aapko apne haath ki location kaise pata hoti hai?','Curiosity Question','Proprioception: muscle spindles, Golgi tendon organs, and joint mechanoreceptors continuously send spatial coordinates to the parietal cortex.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5070002/", "https://www.nih.gov/news-events/nih-research-matters/how-mechanoreceptors-sense-body-position"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day10_video19','Why Can''t You Properly Tickle Yourself?','Brain and Psychology','Khud ko tickle karne par waise hasi kyun nahi aati?','Curiosity Question','Sensory attenuation: the cerebellum computes an efference copy of motor commands to predict and cancel self-generated tactile stimulation.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2832870/", "https://www.nature.com/articles/nn876"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day10_video20','What Happens to Your Brain During Deep Sleep?','Sleep Science','Sote waqt brain ke andar fluid movement aur waste clearance kaise hota hai?','Curiosity Question','Glymphatic system: interstitial space expands by 60% during deep NREM sleep, allowing CSF influx to clear beta-amyloid (current research limitations noted).','["https://www.nih.gov/news-events/nih-research-matters/how-sleep-clears-brain", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4636982/"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day11_video21','Your Ears Never Really Stop Working','Eyes and Human Senses','Aap so rahe hote ho, lekin brain sounds ko monitor karta rehta hai!','Curiosity Question','Nocturnal auditory gating: acoustic soundwaves convert to electrical signals continuously; the thalamic reticular nucleus filters threats during sleep.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6265731/", "https://www.nidcd.nih.gov/health/how-do-we-hear"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day11_video22','Why Does Cold Weather Make You Pee More?','Hormones and Metabolism','Thand mein washroom zyada kyun jana padta hai?','Curiosity Question','Cold-induced diuresis: cutaneous vasoconstriction diverts blood to the central core, raising arterial pressure and triggering renal filtration of excess fluid.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6481107/", "https://www.kidney.org/atoz/content/howkidneyswork"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day12_video23','Why Is Yawning Contagious?','Brain and Psychology','Kisi ko jamhai lete dekhkar aapko bhi kyun aati hai?','Curiosity Question','Contagious yawning: action-perception coupling mediated by mirror neuron networks and motor empathy circuits in the frontoparietal cortex.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3678674/", "https://www.frontiersin.org/articles/10.3389/fneur.2020.00890/full"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:11','2026-11-11 10:57:11');
INSERT INTO "topics" VALUES('day12_video24','Your Tears Are Not All the Same','Human Body Secrets','Har baar rone par nikalne wale aansu same type ke nahi hote!','Curiosity Question','Tear biochemistry: basal tears maintain corneal refraction, reflex tears flush irritants with lysozyme, and emotional tears excrete prolactin and ACTH.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6457075/", "https://www.aao.org/eye-health/tips-prevention/all-about-emotional-tears"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day13_video25','The Tiny World Living Inside Your Gut','Immunity and Microbiology','Aapke intestine mein trillions of microorganisms rehte hain!','Curiosity Question','Gut microbiome: 38 trillion symbiotic microbes synthesize vitamins (K, B12), train immune lymphocytes, and ferment dietary fiber into short-chain fatty acids.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4290017/", "https://www.nih.gov/news-events/nih-research-matters/human-microbiome-health-disease"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day13_video26','Your Body Has Fat That Burns Energy to Make Heat','Hormones and Metabolism','Body mein ek aisa fat bhi hota hai jo heat produce karne mein help karta hai!','Curiosity Question','Brown adipose tissue (BAT): mitochondria-dense fat expressing uncoupling protein 1 (UCP1) uncouples oxidative phosphorylation to generate heat directly.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3593105/", "https://www.nih.gov/news-events/nih-research-matters/how-brown-fat-improves-metabolic-health"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day14_video27','Can Your Brain Create Pain Without an Injury?','Brain and Psychology','Kabhi-kabhi pain ka experience injury ke bina bhi ho sakta hai!','Curiosity Question','Nociplastic pain & central sensitization: altered central nociceptive processing causes real pain sensations without ongoing tissue damage.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8186584/", "https://www.iasp-pain.org/resources/terminology/"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day14_video28','Your Bones Are Constantly Rebuilding Themselves','Fitness and Muscle Science','Aapki bones dead structures nahi hain, ye continuously change hoti rehti hain!','Curiosity Question','Bone remodeling: coordinated balance between osteoclasts (resorbing old bone mineral) and osteoblasts (synthesizing new collagen bone matrix).','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3179341/", "https://medlineplus.gov/bonediseases.html"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day15_video29','Sleep Paralysis – When Your Mind Wakes Before Your Body','Sleep Science','Aankhein khul gayi, lekin body move nahi ho rahi... aisa kyun?','Curiosity Question','Sleep paralysis: conscious cortical awakening occurs while cholinergic REM muscle atonia is still active, causing brief harmless motor block.','["https://www.ncbi.nlm.nih.gov/books/NBK562303/", "https://www.sleepfoundation.org/parasomnias/sleep-paralysis"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day15_video30','Why Do Some Sounds Make You Extremely Irritated?','Brain and Psychology','Kisi ke chewing ki awaaz se itna irritation kyun hota hai?','Curiosity Question','Misophonia: hyper-reactivity between the auditory cortex and the anterior insular cortex triggers acute autonomic fight-or-flight arousal to specific oral/nasal sounds.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5321671/", "https://www.cell.com/current-biology/fulltext/S0960-9822(16)31530-5"]','verified',NULL,NULL,NULL,NULL,NULL,NULL,'planned',0,NULL,NULL,NULL,'2026-11-11 10:57:12','2026-11-11 10:57:12');
INSERT INTO "topics" VALUES('day04_video07','Why Doesn''t Your Stomach Digest Itself?','Gut Health','Aapke stomach mein powerful acid hota hai, phir woh khud ko digest kyun nahi karta?','Curiosity Question','Gastric mucosal barrier: surface mucous cells secrete an alkaline, bicarbonate-rich gelatinous mucus layer protecting against pH 1.5 hydrochloric acid.','["https://www.ncbi.nlm.nih.gov/books/NBK535425/", "https://medlineplus.gov/ency/anatomyvideos/000007.htm"]','verified',NULL,NULL,32.365,NULL,'/home/rishabh/Heath Videos/output/videos/day04_video07_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/day04_video07_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day04_video07`  
**Title**: Why Doesn''t Your Stomach Digest Itself?  
**Category**: Gut Health  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.833)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 32.35s, Audio duration: 32.38s, Delta: 0.02s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (14987 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 45893879 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 32.35s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.67 (Similarity: 0.33) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.76, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 0.82 (Overlap: 0.18) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/rishabh/Heath Videos/output/videos/day04_video07_health_short.mp4`  
**Originality Fingerprint**: `4255c2015069b771...`  
',NULL,NULL,'2026-11-11 11:18:48','2026-11-11 11:20:54');
INSERT INTO "topics" VALUES('day01_video01','Your Brain Is Always One Step Ahead','Brain and Psychology','Aapka brain duniya ko exactly waise nahi dekhta jaise woh actually hai!','Curiosity Question','Predictive processing: the brain creates a continuous internal hypothesis of reality rather than passively processing raw sensory input in real-time.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6400842/", "https://www.nature.com/articles/nrn3404"]','verified',NULL,NULL,36.844,NULL,'/home/rishabh/Heath Videos/output/videos/day01_video01_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/day01_video01_thumb.jpg','published',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day01_video01`  
**Title**: Your Brain Is Always One Step Ahead  
**Category**: Brain and Psychology  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.805)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 36.82s, Audio duration: 36.84s, Delta: 0.02s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (16557 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 76179179 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 36.82s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.57 (Similarity: 0.43) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.75, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 0.82 (Overlap: 0.18) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/rishabh/Heath Videos/output/videos/day01_video01_health_short.mp4`  
**Originality Fingerprint**: `3ed1ff7a9aa53626...`  
','ldNSyXB5-8A','2026-11-11T12:12:24Z','2026-11-11 11:21:36','2026-11-11 12:12:29');
INSERT INTO "topics" VALUES('day08_video15','The Organ That Can Regrow Part of Itself','Human Body Secrets','Human body ka ek organ apna lost tissue dobara grow kar sakta hai!','Curiosity Question','Compensatory hyperplasia: quiescent hepatocytes re-enter the cell cycle upon partial hepatectomy to restore 100% of functional liver mass.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2836881/", "https://medlineplus.gov/ency/article/002237.htm"]','verified',NULL,NULL,44.464,NULL,'/home/rishabh/Heath Videos/output/videos/day08_video15_health_short.mp4','/home/rishabh/Heath Videos/output/thumbnails/day08_video15_thumb.jpg','qc_passed',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day08_video15`  
**Title**: The Organ That Can Regrow Part of Itself  
**Category**: Human Body Secrets  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.878)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 44.45s, Audio duration: 44.47s, Delta: 0.02s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (21133 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 71443343 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 44.45s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.82 (Similarity: 0.18) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.80, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 0.82 (Overlap: 0.18) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/rishabh/Heath Videos/output/videos/day08_video15_health_short.mp4`  
**Originality Fingerprint**: `3f1720cc637e491c...`  
',NULL,NULL,'2026-11-11 11:24:55','2026-11-11 11:28:08');
INSERT INTO "topics" VALUES('day01_video02','Your Nose Secretly Switches Sides','Human Body Secrets','Aapki ek nostril zyada active hoti hai, phir kuch ghanton baad doosri!','Curiosity Question','The nasal cycle: autonomic alternating congestion and decongestion of nasal erectile tissue every 2 to 6 hours.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4944485/", "https://www.nidcd.nih.gov/health/smell-disorders"]','verified',NULL,NULL,32.919,NULL,'/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day01_video02_health_short.mp4','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/thumbnails/day01_video02_thumb.jpg','published',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day01_video02`  
**Title**: Your Nose Secretly Switches Sides  
**Category**: Human Body Secrets  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.891)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 32.90s, Audio duration: 32.93s, Delta: 0.02s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (15716 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 41935492 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 32.90s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.68 (Similarity: 0.32) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.85, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 1.00 (Overlap: 0.00) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day01_video02_health_short.mp4`  
**Originality Fingerprint**: `bce8268881c2d04d...`  
','EiAR0IE0zWc','2026-11-11T13:10:32Z','2026-11-11 13:08:51','2026-11-11 13:10:34');
INSERT INTO "topics" VALUES('day02_video03','Why Your Body Freezes During Dreams','Sleep Science','Sapne mein bhaagna chahte ho, lekin body move kyun nahi karti?','Curiosity Question','REM sleep muscle atonia: the brainstem inhibits spinal somatic motor neurons via glycine and GABA to prevent acting out vivid dreams.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403735/", "https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-understanding-sleep"]','verified',NULL,NULL,43.713,NULL,'/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day02_video03_health_short.mp4','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/thumbnails/day02_video03_thumb.jpg','published',0,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day02_video03`  
**Title**: Why Your Body Freezes During Dreams  
**Category**: Sleep Science  
**Overall Verdict**: **REJECTED (REQUIRES REPAIR)**  
**Score**: 17/18 Gates Passed (Originality Score: 0.802)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.10s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 43.70s, Audio duration: 43.70s, Delta: 0.00s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (20637 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 61356774 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 43.70s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.63 (Similarity: 0.37) |
| 16 | Script & Hook Novelty Gate | ❌ FAIL | Hook novelty: 0.47, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 1.00 (Overlap: 0.00) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day02_video03_health_short.mp4`  
**Originality Fingerprint**: `617f1e0220ee4752...`  
','SMF77AFvIU0','2026-11-12T05:08:14Z','2026-11-12 05:05:39','2026-11-12 05:08:16');
INSERT INTO "topics" VALUES('day02_video04','Why You Feel Dizzy After Spinning','Eyes and Human Senses','Ghoomna band karne ke baad bhi duniya kyun ghoomti rehti hai?','Curiosity Question','The vestibular system: endolymph fluid inertia in the inner ear semicircular canals continues deflecting the cupula even after the body stops rotating.','["https://www.ncbi.nlm.nih.gov/books/NBK10819/", "https://medlineplus.gov/ency/anatomyvideos/000008.htm"]','verified',NULL,NULL,40.496,NULL,'/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day02_video04_health_short.mp4','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/thumbnails/day02_video04_thumb.jpg','published',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day02_video04`  
**Title**: Why You Feel Dizzy After Spinning  
**Category**: Eyes and Human Senses  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.829)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 40.49s, Audio duration: 40.49s, Delta: 0.00s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (20250 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 36553911 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 40.49s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.53 (Similarity: 0.47) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.73, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 1.00 (Overlap: 0.00) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day02_video04_health_short.mp4`  
**Originality Fingerprint**: `d3cffe78b5dac6f8...`  
','fKW7DqWOzRk','2026-11-12T12:19:33Z','2026-11-12 12:17:54','2026-11-12 12:19:36');
INSERT INTO "topics" VALUES('day03_video05','Why Does Your Skin Get Goosebumps?','Skin and Hair Science','Dar ya thand lagte hi body ke baal khade kyun ho jaate hain?','Curiosity Question','Piloerection: sympathetic adrenergic activation causes tiny arrector pili smooth muscles to contract, pulling hair upright.','["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7439050/", "https://www.nih.gov/news-events/nih-research-matters/how-goosebumps-stimulate-stem-cells"]','verified',NULL,NULL,42.017,NULL,'/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day03_video05_health_short.mp4','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/thumbnails/day03_video05_thumb.jpg','published',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day03_video05`  
**Title**: Why Does Your Skin Get Goosebumps?  
**Category**: Skin and Hair Science  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.852)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 42.02s, Audio duration: 42.02s, Delta: 0.00s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (21519 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 50499201 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 42.02s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.57 (Similarity: 0.43) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.80, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 1.00 (Overlap: 0.00) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day03_video05_health_short.mp4`  
**Originality Fingerprint**: `06340de4b982dd2d...`  
','af2Fyo9UbdI','2026-11-12T20:14:48Z','2026-11-12 20:12:13','2026-11-12 20:14:51');
INSERT INTO "topics" VALUES('day03_video06','Your Heart Has Its Own Electrical System','Heart and Blood Circulation','Aapka heart apni electrical signals generate karke beat kar sakta hai!','Curiosity Question','Cardiac conduction system: the sinoatrial (SA) node generates intrinsic spontaneous electrical action potentials independently of brain input.','["https://www.ncbi.nlm.nih.gov/books/NBK459233/", "https://www.cdc.gov/heartdisease/facts.htm"]','verified',NULL,NULL,41.429,NULL,'/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day03_video06_health_short.mp4','/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/thumbnails/day03_video06_thumb.jpg','published',1,'# HEALTH VIDEOS — QUALITY CONTROL AUDIT REPORT
**Topic ID**: `day03_video06`  
**Title**: Your Heart Has Its Own Electrical System  
**Category**: Heart and Blood Circulation  
**Overall Verdict**: **PASSED (APPROVED FOR PRODUCTION)**  
**Score**: 18/18 Gates Passed (Originality Score: 0.893)  

---

### Audit Inspection Matrix

| Gate # | Quality Gate Name | Status | Inspection Details |
|:---:|:---|:---:|:---|
| 01 | Female Narration Enforced | ✅ PASS | Voice: hi-IN-SwaraNeural, Female-only enforced: True |
| 02 | Playback Speed 1.15x | ✅ PASS | Speed factor: 1.15x (Target: 1.15x) |
| 03 | 0-2s Immediate Hook | ✅ PASS | Hook starts at: 0.00s (Threshold: <= 0.2s) |
| 04 | Audio-Video Synchronization | ✅ PASS | Video duration: 41.42s, Audio duration: 41.42s, Delta: 0.00s |
| 05 | Sentence-to-Visual Alignment | ✅ PASS | 6 scenes verified with distinct visuals (No adjacent duplicates: True). |
| 06 | Word Subtitle Synchronization | ✅ PASS | Subtitles file verified (20107 bytes) |
| 07 | Zero Black Frames | ✅ PASS | Detected black frames: 0 |
| 08 | Media File Integrity | ✅ PASS | Output video file size: 41543058 bytes |
| 09 | Audio Clipping & Headroom | ✅ PASS | Audio levels normalized within broadcast limits. |
| 10 | Ambient BGM Ducking (-22dB) | ✅ PASS | BGM sidechain compressed at -20dB under vocal envelope. |
| 11 | Aspect Ratio 9:16 (1080x1920) | ✅ PASS | Resolution: 1080x1920 (Target: 1080x1920) |
| 12 | Duration (30–50 Seconds) | ✅ PASS | Duration: 41.42s (Allowed: 30.0-50.0s) |
| 13 | Scientific Evidence Citations | ✅ PASS | 2 scientific sources verified (NIH/PubMed/MedlinePlus) |
| 14 | Asset Licensing Compliance | ✅ PASS | All visual and audio assets sourced under Pexels CC0 / Pixabay / Procedural license. |
| 15 | Catalog Topic Deduplication | ✅ PASS | Topic uniqueness score: 0.73 (Similarity: 0.27) |
| 16 | Script & Hook Novelty Gate | ✅ PASS | Hook novelty: 0.80, Script novelty: 1.00 |
| 17 | Visual Sequence Distinction | ✅ PASS | Sequence distinction: 1.00 (Overlap: 0.00) |
| 18 | Shorts Audio Ready Export | ✅ PASS | Shorts audio picker ready in shorts_audio_ready/ (Guide verified) |

---
**Verified Master Output**: `/home/runner/work/yt-health-videos-automation/yt-health-videos-automation/output/videos/day03_video06_health_short.mp4`  
**Originality Fingerprint**: `5affd322b8db7e13...`  
','_GkH2YW46Bk','2026-11-13T11:58:09Z','2026-11-13 11:55:57','2026-11-13 11:58:11');
CREATE TABLE video_history (
    video_id TEXT PRIMARY KEY,
    topic_id TEXT NOT NULL,
    main_topic TEXT NOT NULL,
    subtopic TEXT,
    core_scientific_concept TEXT NOT NULL,
    script_text TEXT NOT NULL,
    hook_text TEXT NOT NULL,
    title TEXT NOT NULL,
    scene_descriptions TEXT, -- JSON array of scene visual descriptions
    visual_asset_ids TEXT,   -- JSON array of asset paths/IDs used
    models_animations TEXT,  -- JSON array of 3D models or animation clips used
    camera_angles_movements TEXT, -- JSON array of camera trajectories
    lighting_style TEXT,
    subtitle_text TEXT,
    bgm_track_id TEXT,
    rendered_path TEXT,
    clean_shorts_path TEXT,
    video_fingerprint TEXT UNIQUE, -- SHA256 of normalized text + visual sequence
    originality_score REAL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    publishing_status TEXT DEFAULT 'draft',
    FOREIGN KEY(topic_id) REFERENCES topics(topic_id)
);
INSERT INTO "video_history" VALUES('vid_health_81ee3387_c','health_81ee3387','Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?','Glymphatic Waste Clearance','Cerebrospinal fluid flushes beta-amyloid proteins during deep slow-wave sleep via glymphatic influx.','Jab aap gehri neend mein sote hain, aapka dimaag shrink ho jata hai taaki cerebrospinal fluid metabolic waste saaf kar sake.','Jab aap gehri neend mein sote hain, aapka dimaag shrink ho jata hai.','Glymphatic System: Sote Waqt Brain Kaise Clean Hota Hai?','["Jab aap gehri neend mein sote hain, aapka dimaag shrink ho jata hai.", "Ye magical process Glymphatic System kehlata hai.", "Beta-amyloid jaise harmful toxins ko cerebrospinal fluid flush out karta hai.", "Taaki aapki memory sharp aur brain youthful bana rahe.", "Health science updates ke liye Swasth Snap ko subscribe karein!"]','["sleep_bed_relax_night.mp4", "cells_microscopic_laboratory.mp4", "liquid_fluid_flow_microscopic.mp4", "human_brain_glowing_synapses.mp4", "human_eye_macro_blink.mp4"]','["sleep_bed_relax_night.mp4", "cells_microscopic_laboratory.mp4", "liquid_fluid_flow_microscopic.mp4"]','["slow_push", "slow_zoom_in", "pan_right", "orbit_slow", "slow_push"]','cinematic_dark_glow_cyan','Jab aap gehri neend mein sote hain, aapka dimaag shrink ho jata hai taaki cerebrospinal fluid metabolic waste saaf kar sake.','bgm_deep_ambient_01','output/videos/health_81ee3387_mix_c_soft_ambient.mp4','output/shorts_audio_ready/health_81ee3387_clean_shorts.mp4','766ee4d86675d20b8713392fcf4f4a4e691799189db9a9812227135bf4e561f6',0.933,'2026-11-11 10:26:39','qc_passed');
CREATE INDEX idx_topics_category ON topics(category);
CREATE INDEX idx_topics_status ON topics(status);
CREATE INDEX idx_topics_title ON topics(title);
CREATE INDEX idx_video_history_topic ON video_history(main_topic);
CREATE INDEX idx_video_history_fingerprint ON video_history(video_fingerprint);
CREATE INDEX idx_bgm_history_track ON bgm_history(track_id);
CREATE INDEX idx_rejected_type ON rejected_attempts(attempt_type);
CREATE INDEX idx_calendar_day ON content_calendar(day_number);
CREATE INDEX idx_calendar_video ON content_calendar(video_number);
CREATE INDEX idx_calendar_status ON content_calendar(render_status);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('sentence_scenes',126);
INSERT INTO "sqlite_sequence" VALUES('rejected_attempts',6);
COMMIT;
