# How to turn this packet into a Notebook LM explainer video

Date: 2026-08-27
Audience: department leadership (chair / boss), then possibly the dean and School of Medicine research leadership
Product: Cognitive Companion — camera-free HUD + short audio cues for critical-care simulation

## What to upload

Upload **only** these four sources, as PDFs if you have them, otherwise the matching `.md` files:

1. `01-the-problem-and-the-product.pdf`
2. `02-how-we-build-it.pdf`
3. `03-team-and-engineering-backing.pdf`
4. `04-the-ask-seed-and-springboard.pdf`

Do **not** upload `VCU-ANESTHESIOLOGY-FUNDS-REQUEST.md`, `FUNDING.md`, or `ONEPAGER.md`. Those still carry the old $12,500 / $7,500 departmental numbers and will fight this packet.

Do **not** upload this how-to file. It is for you, not for the model.

## Notebook LM settings

- Create a new notebook named **Cognitive Companion — leadership explainer**
- Source type: uploaded PDFs
- Generate **Video Overview**
- Length: default / longer if offered (aim spoken 6–8 minutes)
- Visual style: professional, academic, not startup-pitch
- Paste the custom prompt below into the Video Overview custom-instructions box

## Custom prompt for Video Overview (paste this)

```
You are making a 6–8 minute explainer for a department chair in anesthesiology, not a consumer product ad and not a grant-review panel.

Voice: calm, specific, academic. Speak as if Sergio Navarrete is briefing his chair. First person plural is fine (“we”). Do not sound like a startup. Do not use words like disrupt, revolutionary, game-changer, or unique in the world.

Open with the clinical problem in simulation and the OR/ICU: cognitive load, missed critical actions, paper and tablet checklists that compete with hands and eyes. Then say what Cognitive Companion is in one breath: a camera-free pair of glasses plus a nearby phone or iPad that delivers short HUD and audio cues during high-fidelity critical-care simulation. It is not a diagnostic model. It is not watching the patient. It is not a live-patient device in version 1.

Be honest about evidence. Crisis checklists and tablet cognitive aids improve process adherence in simulation. Head-worn vital-sign displays have not shown clinical outcome benefit. We are testing packaging of known-good content, not claiming glasses save lives.

Describe the 12-month build: camera-free hardware, local protocol content, simulation sessions, process measures, then a write-up that unlocks the next dollar. Name the three hardware arms: Halo with the camera documented hard-off, Even G2 as factory camera-free, and phone/iPad-only as a real control arm and fallback — not a failure.

Team: Sergio Navarrete, with Brian Kazior and Lorena Beltoja as clinical collaborators. Engineering: we have already spoken with Dr. Rodrigo Spínola at the VCU College of Engineering. He has reviewed this project and judges it to have a substantial likelihood of true implementation success. He already runs ongoing AI-in-healthcare work with Dr. Daniel Falcão, a VCU neurologist, including an NSF-funded living-lab program for multimodal AI in medical applications. Do not say Dr. Falcão has reviewed this specific project. Do not say this project is funded by that NSF award. The point is: the engineering partner is real, local, and already working with clinicians.

Money: the honest year-one program to build and test this is about $155,000. We are NOT asking the department for $155,000. We are asking for a substantial seed of $50,000 so Anesthesiology can stand up hardware, start engineering with the College of Engineering, and run the first simulation cycle. That seed is a springboard for the rest of the year-one envelope.

The other ask of the chair is introductions, which matter as much as the seed: the dean, the School of Medicine research office or research group that can fund this kind of work more specifically, and any other contacts she thinks can help. Industry money is being evaluated only as a last resort because of conflict of interest.

Close on what 12 months of seed buys: a working camera-free prototype in sim, process data, an engineering partnership already in motion, and a clean story for the next internal or society dollar — without selling the department, the patients, or the residents to a vendor.

Do not invent IRB approval, FDA clearance, outcome data, purchased hardware, hired staff, or letters we have not described. Do not show a wearable camera as part of the product. Do not request the full $155,000 from the chair.
```

## After the video renders

Watch once for these failure modes before you send it:

- It asks the chair for $155,000 (wrong — seed is $50,000)
- It says Falcão reviewed the project (wrong — Spínola did)
- It shows or describes a glasses camera as the product (wrong — camera-free v1)
- It claims the glasses improve mortality or are an FDA device (wrong)
- It leads with industry partnership (wrong — last resort)

If any of those appear, delete that source of confusion and regenerate. Do not “fix it in the email.”
