# Literature notes: cognitive forcing, HUD cues, sim CDS, interruptibility

Retrieved 2026-08-18. Abstracts from Europe PMC. This is not a systematic review.

**Scope lock.** Camera-free Cognitive Companion is HUD + audio + optional phone CDS.
Google Glass / AR-video papers are **adjacent**, not evidence that a camera-free HUD works.
Crisis-checklist RCTs support the **content layer** (checklists, apps), not the glasses.

## 1. Cognitive forcing and debiasing (content theory)

Croskerry 2003 describes cognitive forcing strategies as a metacognitive way to abort latent diagnostic error [38].
Croskerry 2000 names heuristics as a principal source of abbreviated thinking that leads to error [39].
Croskerry et al. 2013 put forcing functions among the major debiasing strategies drawn from social science and medicine [37].
A 2024 “adaptive toolbox” paper still lists cognitive forcing functions next to heuristics and fast-and-frugal trees [36].

**What this is.** A theory of *when* to interrupt the clinician with a cue.
**What this is not.** Evidence that a 256x256 glasses HUD implements a forcing function.

**INFERENCE.** If Cognitive Companion ships a “consider X / do not skip Y” cue, the intellectual parent is this literature, not Halo’s camera.

## 2. Head-mounted / head-worn displays in anesthesia (closest hardware analog)

These studies used vital-sign HMDs, not camera-free AI companions. They are the closest published analog for “keep the numbers in the line of sight.”

Sanderson et al. 2008 (full-scale sim, n=16): event detection was higher with advanced audio (mean 90%) and audio+HMD (mean 92%) than visual-only (mean 52%); HMD-alone (mean 75%) was not significantly better than visual [18].
The same abstract’s conclusion: advanced auditory displays helped the distracted anesthesiologist; an HMD did not significantly improve performance [18].

Liu et al. 2009: the HMD helped when the anesthesiologist was physically constrained, not when unconstrained [19].
The same paper found no conclusive worsening of inattentional blindness, but said HMD perceptual properties influence which events are detected [19].

Liu et al. 2010 (clinical OR, 6 attendings, 36 rigid-cystoscopy cases): HMD use cut gaze to the workstation (21.0% vs 25.3%) and increased gaze to patient/field (55.9% vs 51.5%) [20].
That paper reports process/gaze outcomes, not patient outcomes [20].

A 2009 companion abstract states anesthesiologists detect events faster with an HMD when busy doing procedures, but not during normal monitoring [22].

Elrose et al. 2021 systematic review of head-worn displays for continuous vital signs: none of the 7 clinical-context studies reported clinical outcomes [35].
The same review: evidence on surrogate/process outcomes is limited and sometimes conflicting; clinical-outcome evidence is lacking [35].

Via et al. 1995 is an early “head-up” anesthesia-data display (existence) [33].
Schlosser 2019 is an exploratory multi-patient head-worn app (existence) [21].
Arevalo 2021 reviews wearable monitoring human factors in critical care (existence) [28].

**Implication for Cognitive Companion.**
A HUD that only relocates a monitor may buy gaze time [20] and may help only when hands are busy [19] [22].
Audio cues may be the stronger detection channel in a distracted operator [18].
Do not promise outcome benefit from a glasses HUD. Elrose already flagged that gap [35].

## 3. Crisis checklists and cognitive aids in simulation (content layer)

Arriaga et al. 2013 (17 OR teams, 106 simulated surgical crises): failure to adhere to lifesaving processes was 6% of steps with checklists vs 23% from memory (P<0.001) [34].
Every team did better with the checklist than without [34].

Harrison et al. 2006 (malignant-hyperthermia sim): frequency of cognitive-aid use correlated with the MH treatment score; the best teams used the aid extensively [29].

Marshall 2013: it has been suggested that cognitive aids improve performance in anesthetic emergencies, but a systematic assessment of the evidence was then lacking [30].
Later reviews still treat checklists/algorithms as proposed tools for decision-making and non-technical skills [41].
A 2025/26 emergency-medicine paper says little is known about cognitive-aid use inside EM [40].
Goldhaber-Fiebert 2016 frames emergency manuals as context-relevant cognitive aids / crisis checklists, still nascent in health care relative to other high-hazard industries [32].
Lelaidier / related 2019: cognitive aids can counteract crisis effects and support anesthesiologists [31].

Digital / tablet descendants (still not glasses):

Corazza et al. 2023 PediAppRREST RCT (100 resident teams): a tablet app produced fewer guideline deviations than a PALS card or no aid [45].
eGENA is described as an app offering digital support in anesthesiological emergencies [42].
App *design* can change speed of action in a critical event (existence; do not invent the effect size) [43].
Other sim checklist papers exist for emergency anesthetic prep [47] and RSI training [46].
A neonatal UVC cognitive-aid sim hypothesis paper exists [44].

**Implication.** The content (checklist / algorithm / tablet CDS) has sim evidence.
Putting that content on glasses is an untested packaging choice.

## 4. AR / Google Glass / video glasses (adjacent; do not over-claim)

Siebert 2017: AR glasses adapted for assisted pediatric CPR (existence; adherence numbers not pulled beyond the title this session) [23].
Drummond 2017: Google Glass for residents in pediatric cardiopulmonary arrest (existence) [24].
Systematic reviews of Glass in surgical [25] and nonsurgical [26] settings exist.
A 2022 prehospital AR paper says research in that setting is limited [27].

**These papers assume a camera or optical-see-through video stack.**
They are not evidence for Halo-cam-off or G2.

## 5. Interruptibility and human factors (why a cue can harm)

Direct “wearable mic + HUD interruptibility in ICU sim” trials were not found in this retrieval.
Use adjacent findings, labeled as adjacent.

Sanderson 2008 is an interruptibility paper in all but name: a reading distractor + resident actor, measuring whether displays keep peripheral awareness [18].
Liu 2009 explicitly worries that cockpit HUD literature predicts worse inattentional blindness; they did not conclusively find that, but they warn that display properties change what is noticed [19].
Elrose 2021: most HWD studies that asked found the device “easy to use,” and participants would consider using it, while asking for hardware/display improvements; still no clinical outcomes [35].

FDA’s 2026 CDS guidance (not a trial) names automation bias and says it increases when action is urgent [13].

**INFERENCE.** A companion that talks or flashes during a pause-sensitive task can recreate the interruption problem the product claims to solve.
Design the *silence* policy with the same seriousness as the cue library.

## 6. What the literature does *not* contain (this retrieval)

- No RCT of camera-free consumer glasses as a critical-care cognitive companion.
- No patient-level outcome for HWD vital-sign monitoring [35].
- No head-to-head Halo vs G2 vs phone in sim.
- No validated interruptibility metric for a glasses-mounted LLM.
- Classic Westbrook 2010 medication-interruption citation was not landed (wrong PMID on first lookup). Do not invent its numbers.

## How to cite this in a deck

Safe: “Checklists and tablet CDS reduce process failures in sim [34] [45]. Anesthesia HMD studies change gaze and sometimes detection, not outcomes [18] [20] [35]. Audio may beat HUD-alone for a distracted operator [18].”

Unsafe: “Smart glasses improve crisis performance.”

## Sources

[13] https://www.fda.gov/media/109618/download — FDA CDS Software guidance PDF 2026-01-29
    > "Document issued on January 29, 2026."
    > "Not all clinical decision support software used in healthcare settings are devices and therefore subject to FDA oversight as a device."
    > "time-critical nature of the HCP"
    > "Automation bias is the propensity of humans to over-rely on a suggestion from an automated system."
    > "In situations that require urgent action, automation bias increases"
[18] https://europepmc.org/article/MED/18499611 — Europe PMC 18499611
    > "Participants detected significantly more events with Audio (mean = 90%, median = 100%, P < 0.02) and Both (mean = 92%, median = 100%, P < 0.05) but not with HMD (mean = 75%, median = 67%, ns) compared with the Visual condition (mean = 52%, median = 50%)."
    > "Advanced auditory displays help the distracted anesthesiologist maintain peripheral awareness of a simulated patient's status, whereas a HMD does not significantly improve performance."
[19] https://europepmc.org/article/MED/19762741 — Europe PMC 19762741
    > "The HMD helped anesthesiologists detect events when physically constrained, but not when physically unconstrained."
    > "Although there was no conclusive evidence of worsened inattentional blindness, found in aviation, the perceptual properties of the HMD display appear to influence whether events are detected."
[20] https://europepmc.org/article/MED/20357147 — Europe PMC 20357147
    > "When participants were using the HMD, compared with standard monitoring, they spent less time looking toward the anesthesia workstation (21.0% vs 25.3%, P = 0.003) and more time looking toward the patient and surgical field (55.9% vs 51.5%, P = 0.014)."
[21] https://europepmc.org/article/MED/30721389 — Europe PMC 30721389
    > "An exploratory clinical evaluation of a head-worn display based multiple-patient monitoring application"
[22] https://europepmc.org/article/MED/19770643 — Europe PMC 19770643
    > "Anesthesiologists can detect patient events faster with an HMD when they are busy performing procedures, but not during normal monitoring."
[23] https://europepmc.org/article/MED/28554878 — Europe PMC 28554878
    > "Adherence to AHA Guidelines When Adapted for Augmented Reality Glasses for Assisted Pediatric Cardiopulmonary Resuscitation"
[24] https://europepmc.org/article/MED/28165347 — Europe PMC 28165347
    > "Google Glass for Residents Dealing With Pediatric Cardiopulmonary Arrest"
[25] https://europepmc.org/article/MED/29510969 — Europe PMC 29510969
    > "Using Google Glass in Surgical Settings: Systematic Review."
[26] https://europepmc.org/article/MED/29051136 — Europe PMC 29051136
    > "Using Google Glass in Nonsurgical Medical Settings: Systematic Review."
[27] https://europepmc.org/article/MED/35225816 — Europe PMC 35225816
    > "limited research has investigated its application in prehospital operations"
[28] https://europepmc.org/article/MED/34032574 — Europe PMC 34032574
    > "Augmenting Critical Care Patient Monitoring Using Wearable Technology: Review of Usability and Human Factors."
[29] https://europepmc.org/article/MED/16931660 — Europe PMC 16931660
    > "The frequency of cognitive aid use correlated significantly with the MH treatment score"
    > "The teams that performed the best in treating MH used a cognitive aid extensively throughout the simulation."
[30] https://europepmc.org/article/MED/24029855 — Europe PMC 24029855
    > "It has been suggested that the use of cognitive aids improves performance and patient outcomes during anesthetic emergencies; however, a systematic assessment of the evidence is lacking."
[31] https://europepmc.org/article/MED/31033445 — Europe PMC 31033445
    > "Cognitive aids can counteract these effects and support anesthesiologists in their crisis management."
[32] https://europepmc.org/article/MED/27541721 — Europe PMC 27541721
    > "Emergency manuals (EMs), context-relevant sets of cognitive aids or crisis checklists, have been used in high-hazard industries for decades, although this is a nascent field in health care."
[33] https://europepmc.org/article/MED/7782663 — Europe PMC 7782663
    > "Clinical evaluation of the 'head-up' display of anesthesia data. Preliminary communication."
[34] https://europepmc.org/article/MED/23323901 — Europe PMC 23323901
    > "Failure to adhere to lifesaving processes of care was less common during simulations when checklists were available (6% of steps missed when checklists were available vs. 23% when they were unavailable, P<0.001)."
    > "Every team performed better when the crisis checklists were available than when they were not."
[35] https://europepmc.org/article/MED/33973863 — Europe PMC 33973863
    > "Of the 7 studies conducted in clinical contexts, none reported any clinical outcomes."
    > "Although there is limited and sometimes conflicting evidence about the benefits of HWDs from certain surrogate and process outcomes, evidence for clinical outcomes is lacking."
[36] https://europepmc.org/article/MED/38588820 — Europe PMC 38588820
    > "Additionally, the adaptive toolbox includes situational-specific tools such as heuristics, narratives, cognitive forcing functions, and fast and frugal trees."
[37] https://europepmc.org/article/MED/23996094 — Europe PMC 23996094
    > "We then examine the major strategies that have been developed in the social sciences and in medicine to achieve cognitive and affective debiasing, including the important concept of forcing functions."
[38] https://europepmc.org/article/MED/12514691 — Europe PMC 12514691
    > "Through the process of metacognition, clinicians can develop cognitive forcing strategies to abort such latent errors."
[39] https://europepmc.org/article/MED/11073470 — Europe PMC 11073470
    > "Principal among them is the use of heuristics, a form of abbreviated thinking that often leads to"
[40] https://europepmc.org/article/MED/42131898 — Europe PMC 42131898
    > "little is known about their use within emergency medicine"
[41] https://europepmc.org/article/MED/39851796 — Europe PMC 39851796
    > "Cognitive aids, such as checklists and algorithms, have been proposed as tools to improve decision-making, procedural competency, and non-technical skills"
[42] https://europepmc.org/article/MED/39794633 — Europe PMC 39794633
    > "The electronic cognitive aid for emergencies in anesthesia (eGENA) is an app that offers digital support in anesthesiological emergency situations"
[43] https://europepmc.org/article/MED/39508414 — Europe PMC 39508414
    > "Does cognitive aid app design influence the speed of actions during a critical event?"
[44] https://europepmc.org/article/MED/38876930 — Europe PMC 38876930
    > "We hypothesized that reading a cognitive aid for UVC placement in the delivery room during neonatal resuscitation simulation scenarios"
[45] https://europepmc.org/article/MED/37535352 — Europe PMC 37535352
    > "The number of deviations from guidelines was significantly lower in the PediAppRREST group than in the control groups"
[46] https://europepmc.org/article/MED/36545368 — Europe PMC 36545368
    > "A Simulation-Based Training Program in Rapid Sequence Induction for Novice Anesthesiology Trainees Using a Novel Checklist."
[47] https://europepmc.org/article/MED/34946372 — Europe PMC 34946372
    > "Cognitive Aid for Anesthetic Preparation in An Emergency Situation: A Simulation-Based Study."
