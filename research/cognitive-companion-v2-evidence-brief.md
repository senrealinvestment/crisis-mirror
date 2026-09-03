# Cognitive Companion v1 — evidence brief (strengthened)

Date: 2026-08-18
Status: local research artifact. Extends, does not replace, `cognitive-companion-v1-evidence-brief.md`.
Product: camera-free HUD + audio cognitive companion for critical-care simulation.
Not a protocol. Not a buy order. Not a PR.

## Bottom line

**FACT.** Halo is a ~40 g open-source glasses product listed at $399.00 USD with dual mics and dual bone-conduction speakers [1].
**FACT.** Halo’s hardware docs specify a 640x480 front camera, 256x256 drawable area, stereo mics, stereo bone conduction, 300 mAh battery, and OTA firmware [3].
**FACT.** Those same docs say Halo is not verified for use where performance and accuracy would be critical to human health [3].
**FACT.** Even G2 is marketed as camera-free by design, 36 g, four microphones, 640*350, IP65 [4].
**FACT.** G2-A non-prescription list price is $599 [6].
**UNKNOWN.** G2 speakers / audio-out. Re-fetched Even pages have no speaker line [4] [5] [6].
**FACT.** MentraOS lists Even Realities as supported hardware; Mentra Live is a different, camera-enabled product [7].

**FACT.** Anesthesia HMD studies change detection or gaze in sim/OR process measures [18] [19] [20].
**FACT.** A 2021 systematic review of head-worn vital-sign displays found no clinical outcomes in its 7 clinical-context studies [35].
**FACT.** Crisis checklists in high-fidelity sim cut missed lifesaving steps (6% vs 23%) [34].
**FACT.** A 2023 tablet CDS app (PediAppRREST) cut guideline deviations vs a paper card or no aid [45].
Those two trials support the **content layer**, not glasses.

**INFERENCE.** Camera-free is the right privacy posture for a VCU sim pilot [unverified].
**INFERENCE.** Halo can be the pilot SKU only if “cam hard-off” is a documented disable, not a software mute next to an OTA camera [3].
**INFERENCE.** Phone/iPad-only is the honest control arm and the fallback [unverified].

## Decision

Keep v1 camera-free.
Treat Halo-with-camera-disabled as the procurement path **if and only if** disable is written down.
Treat G2 as the factory-camera-free alternative, pending speaker confirmation.
Treat phone/iPad-only as arm 3, not as a failure.

Do not claim outcome benefit from glasses.
Claim a test of whether HUD + short audio cues improve process adherence versus phone-only, using checklist-grade content [34] [45].

## What changed since the 2026-08-17 v1 brief

- Re-fetched Halo, Even, and Mentra pages on 2026-08-18. Prices unchanged: Halo $399 [1], G2-A $599 [6].
- Added phone/iPad-only as a first-class arm.
- Added Common Rule / HIPAA eCFR / VCU HRPP / VA recording / FDA CDS 2026 notes.
- Added Croskerry forcing-function papers as **content theory**, not hardware evidence [37] [38].
- G2 speakers remain unknown (same gap as v1).
- No citations pack existed on 2026-08-17. This pack adds one.

## Hardware (live)

Halo product page: regular price $399.00 USD [1].
Halo product page: the device weighs just over than 40g [1].
Halo product page: dual mics with audio activity detection and dual bone conduction speakers [1].
Halo product page: shipments beginning in early August [1].
Halo docs: 640x480 global shutter color camera; PixArt PAG7982J1 [3].
Halo docs: 256x256px drawable area [3].
Halo docs: stereo microphones and stereo bone conduction speakers [3].
Halo docs: 300mAh built-in rechargeable li-ion battery [3].
Halo docs: firmware fully updatable over the air [3].
Halo docs: not verified for health / safety / mission-critical use [3].

Even G2: camera-free by design; relies on the integrated microphone rather than a camera [4].
Even G2: just 36 grams [4].
Even G2: four microphones [4].
Even G2: resolution 640*350 [4].
Even G2: Conversate captures and transcribes every word [4].
Even G2: no data stored in the cloud without explicit consent [4].
Even tech: certified IP65; hinges 40,000 cycles; drop-tested from 2 metres [5].
Even G2-A: $599 [6].

Mentra: MentraOS supports Mentra Live, Even Realities, and Vuzix [7].
Mentra Live: camera-enabled; listed weight 43g [7].

Phone/iPad-only: no new vendor claim. It is the edge brain without a head-worn display.

**Conflict with committed copy.** Older funds/one-pager numbers used a cheaper Halo band. Live list is $399 [1].

## Evidence that transfers — and what does not

### Transfers to the *cue content*

Croskerry 2003: clinicians can develop cognitive forcing strategies to abort latent error [38].
Croskerry 2013: forcing functions are a named debiasing strategy [37].
Arriaga 2013: 17 teams, 106 simulated crises; 6% vs 23% missed lifesaving steps with vs without checklists [34].
Harrison 2006: cognitive-aid use correlated with MH treatment score; best teams used the aid extensively [29].
Corazza 2023: tablet app, fewer guideline deviations than PALS card or no aid [45].

### Transfers to *HUD / audio packaging* (analog, not this product)

Sanderson 2008: audio mean 90% and audio+HMD mean 92% event detection vs visual 52%; HMD-alone 75% not significantly better [18].
Sanderson 2008 conclusion: advanced auditory displays helped; an HMD did not significantly improve performance [18].
Liu 2009: HMD helped when physically constrained, not when unconstrained [19].
Liu 2009: no conclusive extra inattentional blindness; display properties still change what is noticed [19].
Liu 2010: HMD 21.0% vs 25.3% gaze at workstation; 55.9% vs 51.5% gaze at patient/field [20].
Liu companion: faster event detection with HMD when busy, not during normal monitoring [22].
Elrose 2021: no clinical outcomes among 7 clinical-context HWD studies [35].
Elrose 2021: surrogate/process evidence limited and sometimes conflicting [35].

### Does **not** transfer

Google Glass / AR-video CPR papers are adjacent, not this product [23] [24].
Glass systematic reviews exist in surgical and nonsurgical settings [25] [26].
They assume a camera or video stack. Cognitive Companion v1 does not.

## Privacy / IRB / FDA (short)

PHI is individually identifiable health information at 45 CFR 160.103 [9].
A manikin is not an individual. A standardized patient’s voice can still identify a person [unverified].
45 CFR 46.104 names educational-practice and adult audiovisual-recording exemption paths [8].
VCU: research means a systematic investigation designed to contribute to generalizable knowledge [16].
VCU: most QI is not research; if unclear, submit in VIRBs [16].
VCU IRB system is VIRBs [15].
Virginia Code 19.2-62 is one-party consent for intercepting a communication [17].
FDA CDS guidance issued 29 January 2026 [13].
FDA: not all CDS is a device [13].
FDA: automation bias is over-reliance on an automated suggestion; it increases when action is urgent [13].

## What v1 should measure (inference, labeled)

Primary process endpoint: missed critical actions, Arriaga-style [34] [unverified].
Secondary: time-to-first-correct-action; gaze-away time if recorded from a room camera (room camera ≠ wearable camera) [unverified].
Safety: count of unnecessary interruptions and of accepted-wrong cues (automation bias [13]).
Arms: Halo cam-off vs G2 (if speakers exist) vs phone-only [unverified].

## Unknowns that block over-claim

- Halo camera disable method [3].
- G2 audio-out [4].
- Halo runtime on 300 mAh [3].
- Whether the first VCU cycle is QI or generalizable research [16].
- OpenEvidence / UpToDate license terms (not fetched).
- HHS OCR wearable-audio FAQ (HTTP 403 this session).

## Sources

[1] https://brilliant.xyz/products/halo — Brilliant Labs Halo product page
    > "Regular price $399.00 USD"
    > "The device weighs just over than 40g"
    > "dual mics with audio activity detection, a low-power AI processor, and dual bone conduction speakers"
    > "shipments beginning in early August"
[3] https://docs.brilliant.xyz/halo/hardware — Brilliant Labs Halo hardware docs
    > "640x480 global shutter color camera"
    > "256x256px drawable area"
    > "Stereo bone conduction speakers"
    > "300mAh built-in rechargeable li-ion battery"
    > "It is not verified for use where performance and accuracy would be critical to human health, safety or mission critical use."
    > "The firmware is fully updatable over the air (OTA)"
    > "The front facing camera on Halo is the PAG7982J1 from PixArt Imaging"
    > "Stereo microphones Stereo bone conduction speakers"
[4] https://www.evenrealities.com/smart-glasses — Even Realities G2 smart glasses
    > "Camera-free. By design."
    > "Just 36 grams."
    > "Even G2 relies on its integrated microphone for information input rather than a camera."
    > "Conversate captures and transcribes every word"
    > "No data is stored in the cloud without your explicit consent."
    > "Capabilities Four Microphones Auto brightness control"
    > "Even G2 resists to dust and water at IP65 rating"
    > "Resolution 640*350 FoV 27.5"
[5] https://www.evenrealities.com/tech — Even Realities G2 tech page
    > "Screwless hinges opened and closed 40,000 times."
    > "Drop-tested from 2 metres."
    > "Dust proof. Certified IP65."
[6] https://www.evenrealities.com/products/g2-a — Even Realities G2-A product
    > "Select frame shape and color$599 Even G2 A"
[7] https://mentra.glass — Mentra OS / Mentra Live
    > "support for multiple hardware platforms including Mentra Live, Even Realities, and Vuzix"
    > "Mentra Live gives enterprise teams and developers camera-enabled smart glasses"
    > "Frame Dimensions 162 L X 148 W x 47 H Weight 43g"
[8] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.104 — 45 CFR 46.104 Exempt research
    > "Research, conducted in established or commonly accepted educational settings, that specifically involves normal educational practices"
    > "including visual or auditory recording"
    > "Research involving benign behavioral interventions in conjunction with the collection of information from an adult subject through verbal or written responses (including data entry) or audiovisual recording if the subject prospectively agrees"
[9] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103 — 45 CFR 160.103 PHI definitions
    > "Individually identifiable health information is information that is a subset of health information, including demographic information collected from an individual"
    > "Protected health information means individually identifiable health information"
[13] https://www.fda.gov/media/109618/download — FDA CDS Software guidance PDF 2026-01-29
    > "Document issued on January 29, 2026."
    > "Not all clinical decision support software used in healthcare settings are devices and therefore subject to FDA oversight as a device."
    > "time-critical nature of the HCP"
    > "Automation bias is the propensity of humans to over-rely on a suggestion from an automated system."
    > "In situations that require urgent action, automation bias increases"
[15] https://research.vcu.edu/integrity-and-compliance/hrpp-irb — VCU HRPP/IRB home
    > "New IRB review system: VIRBs (VCU IRB system)"
[16] https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review — VCU activities requiring IRB review
    > "Most quality improvement efforts do not meet the definition of research because they are not designed to be generalizable."
    > "Research is a systematic investigation designed to develop or contribute to generalizable knowledge."
    > "If a determination cannot clearly be made, submit the project to the VCU IRB using VIRBs"
[17] https://law.lis.virginia.gov/vacode/title19.2/chapter6/section19.2-62 — Virginia Code 19.2-62 recording consent
    > "where such person is a party to the communication or one of the parties to the communication has given prior consent to such interception"
[18] https://europepmc.org/article/MED/18499611 — Europe PMC 18499611
    > "Participants detected significantly more events with Audio (mean = 90%, median = 100%, P < 0.02) and Both (mean = 92%, median = 100%, P < 0.05) but not with HMD (mean = 75%, median = 67%, ns) compared with the Visual condition (mean = 52%, median = 50%)."
    > "Advanced auditory displays help the distracted anesthesiologist maintain peripheral awareness of a simulated patient's status, whereas a HMD does not significantly improve performance."
[19] https://europepmc.org/article/MED/19762741 — Europe PMC 19762741
    > "The HMD helped anesthesiologists detect events when physically constrained, but not when physically unconstrained."
    > "Although there was no conclusive evidence of worsened inattentional blindness, found in aviation, the perceptual properties of the HMD display appear to influence whether events are detected."
[20] https://europepmc.org/article/MED/20357147 — Europe PMC 20357147
    > "When participants were using the HMD, compared with standard monitoring, they spent less time looking toward the anesthesia workstation (21.0% vs 25.3%, P = 0.003) and more time looking toward the patient and surgical field (55.9% vs 51.5%, P = 0.014)."
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
[29] https://europepmc.org/article/MED/16931660 — Europe PMC 16931660
    > "The frequency of cognitive aid use correlated significantly with the MH treatment score"
    > "The teams that performed the best in treating MH used a cognitive aid extensively throughout the simulation."
[34] https://europepmc.org/article/MED/23323901 — Europe PMC 23323901
    > "Failure to adhere to lifesaving processes of care was less common during simulations when checklists were available (6% of steps missed when checklists were available vs. 23% when they were unavailable, P<0.001)."
    > "Every team performed better when the crisis checklists were available than when they were not."
[35] https://europepmc.org/article/MED/33973863 — Europe PMC 33973863
    > "Of the 7 studies conducted in clinical contexts, none reported any clinical outcomes."
    > "Although there is limited and sometimes conflicting evidence about the benefits of HWDs from certain surrogate and process outcomes, evidence for clinical outcomes is lacking."
[37] https://europepmc.org/article/MED/23996094 — Europe PMC 23996094
    > "We then examine the major strategies that have been developed in the social sciences and in medicine to achieve cognitive and affective debiasing, including the important concept of forcing functions."
[38] https://europepmc.org/article/MED/12514691 — Europe PMC 12514691
    > "Through the process of metacognition, clinicians can develop cognitive forcing strategies to abort such latent errors."
[45] https://europepmc.org/article/MED/37535352 — Europe PMC 37535352
    > "The number of deviations from guidelines was significantly lower in the PediAppRREST group than in the control groups"
