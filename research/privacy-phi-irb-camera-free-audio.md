# Privacy / PHI / IRB framing: camera-free wearable audio in sim

Retrieved 2026-08-18. Framing notes, not legal advice and not an IRB submission.

Setting assumed: VCU critical-care **simulation**, manikin or standardized participant, Cognitive Companion mics + HUD, phone/iPad edge brain, Halo camera hard-off (or G2, which is camera-free by design [4]).

HHS OCR HTML pages returned HTTP 403 this session. HIPAA text below is from eCFR, not from an OCR FAQ.

## 1. Is this HIPAA?

**FACT.** Protected health information is individually identifiable health information held or transmitted by a covered entity / business associate in the forms 45 CFR 160.103 lists [9].
**FACT.** Individually identifiable health information is a subset of health information, including demographic information collected from an individual [9].

**INFERENCE (needs VCU privacy officer).** A manikin has no individual.
Standardized patients / confederates are people. Their voice is a biometric-ish identifier even if you never record a medical record number.
If the audio never includes a real patient’s IIHI, the HIPAA Privacy Rule may not be the binding regime. The Common Rule, state recording law, and VCU policy still are.

**Do not say “HIPAA does not apply, so we can record.”**
Say: “No real-patient IIHI is the working assumption; confirm with VCU privacy before any live-bay spillover.”

If a real EHR snippet, real name, or real case is ever piped into the edge brain, you are in PHI territory [9].
Research uses of PHI, when they apply, are addressed at 45 CFR 164.512 [10].
Minimum necessary still applies to PHI uses and disclosures [12].
De-identification / re-identification is 45 CFR 164.514 [11].

## 2. Common Rule: is this “research,” and is it exempt?

**FACT.** 45 CFR 46.104(d)(1) exempts research in established educational settings that specifically involves normal educational practices [8].
**FACT.** The same section names visual or auditory recording in other exemption text [8].
**FACT.** 46.104(d)(3) can cover benign behavioral interventions plus adult audiovisual recording if the subject prospectively agrees [8].

**FACT (VCU).** Research is a systematic investigation designed to develop or contribute to generalizable knowledge [16].
**FACT (VCU).** Most quality-improvement efforts do not meet that definition because they are not designed to be generalizable [16].
**FACT (VCU).** If a determination cannot clearly be made, submit the project in VIRBs [16].
**FACT (VCU).** VIRBs is the current IRB system [15].

**INFERENCE.** A local sim-curriculum QI cycle (no publication, no generalizable claim) may sit outside IRB.
A paper, abstract, multi-site protocol, or “we will publish usability” plan is research. Submit.

**Do not self-exempt in an email.** VCU’s own page says to submit when unclear [16].

Wearable audio of adult learners can still fit an exemption *if* the IRB says so under 46.104 [8].
That is an IRB determination, not a researcher slogan.

## 3. Virginia recording consent

**FACT.** Va. Code § 19.2-62 allows interception where the person is a party to the communication or one party has given prior consent [17].
Virginia is a one-party-consent statute on the text retrieved [17].

**INFERENCE.** One-party consent is the floor, not a sim-center policy.
Everyone in the bay (learners, confederate, tech, faculty) should still get a written notice that wearable mics are live.
G2’s Conversate feature “captures and transcribes every word” [4]. Treat that as a room-level recording, not a private memo.

## 4. Camera-free is not “privacy-complete”

**FACT.** Even G2 is marketed as camera-free by design and uses the microphone rather than a camera [4].
**FACT.** Halo ships a 640x480 front camera [3].
**FACT.** Halo firmware is OTA-updatable [3].

**INFERENCE.** Camera-off is a *mitigation*, not a guarantee.
IRB language should say: no video capture in the protocol; Halo camera disabled by documented method; G2 has no camera; audio *is* captured.

Audio risks that remain after the camera is off:

- Voice of learners and staff.
- Background speech from an adjacent bay.
- Accidental capture of a real-patient name if the device leaves the sim center.
- Transcripts stored on a phone, vendor cloud, or “Noa” memory [1] [4].

Even’s page says no cloud storage without explicit consent [4].
That is vendor marketing, not a BAA.

## 5. FDA CDS (software posture, not IRB)

**FACT.** FDA issued the Clinical Decision Support Software guidance on 29 January 2026 [13].
**FACT.** Not all CDS used in healthcare is a device under that guidance [13].
**FACT.** The guidance discusses the time-critical nature of the HCP’s decision [13].
**FACT.** It defines automation bias as over-reliance on an automated suggestion [13].
**FACT.** It states automation bias increases in situations that require urgent action [13].

**INFERENCE.** A crisis companion is exactly the time-critical, high-bias setting FDA flags [13].
For a **sim-only** pilot, device-regulation risk is lower than for live ICU use, but the *design* should still keep the human able to independently review the basis of a cue.
Do not market the pilot as an FDA-cleared device. Halo’s own docs already disclaim health-critical use [3].

## 6. Practical framing for Sergio / VCU ask

Safe protocol posture (inference, for counsel/IRB to accept or reject):

1. Sim-only. No live patients. No real EHR.
2. Adult learners; written prospective agreement if any audio is kept [8].
3. Default: no durable audio store. If stored, local encrypted, time-limited, no vendor cloud.
4. Halo: documented camera-off + physical cover. G2: camera-free SKU [4].
5. Decide QI vs generalizable *before* the first session [16].
6. If any chance of publication or external funding as “research,” submit VIRBs now [15] [16].
7. Phone-only arm is the lowest privacy novelty if IRB stalls.

## 7. Unknowns (do not invent)

- Whether VCU simulation center already has a standing recording consent that covers wearable mics.
- Whether Brilliant or Even will sign a BAA (probably irrelevant if no PHI; still ask).
- Whether “Noa” long-term memory can be disabled.
- Whether G2 Conversate can run fully on-device.
- HHS OCR’s wearable-audio FAQ text (page blocked this session).

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
[8] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.104 — 45 CFR 46.104 Exempt research
    > "Research, conducted in established or commonly accepted educational settings, that specifically involves normal educational practices"
    > "including visual or auditory recording"
    > "Research involving benign behavioral interventions in conjunction with the collection of information from an adult subject through verbal or written responses (including data entry) or audiovisual recording if the subject prospectively agrees"
[9] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103 — 45 CFR 160.103 PHI definitions
    > "Individually identifiable health information is information that is a subset of health information, including demographic information collected from an individual"
    > "Protected health information means individually identifiable health information"
[10] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.512 — 45 CFR 164.512 research disclosures
    > "A covered entity may use or disclose protected health information for research, regardless of the source of funding of the research"
[11] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514 — 45 CFR 164.514 de-identification
    > "to allow information de-identified under this section to be re-identified by the covered entity"
[12] https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502 — 45 CFR 164.502 minimum necessary
    > "When using or disclosing protected health information or when requesting protected health information from another covered entity"
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
