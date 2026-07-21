# Crisis Mirror — One-Pager

**Smart glasses ambient AI — cognitive companion for clinical medicine**  
Real-time cost + cue quality feedback loop  
*From Sergio’s whiteboard sketch → product brief*

---

## One sentence

Ambient video + audio from clinician smart glasses feed an OpenEvidence-class reasoner that delivers a **discrete multimodal cue** (tone / haptic / HUD). The clinician acts; we log whether the cue was **helpful** and **accurate** for post-hoc training.

---

## Loop (physics of the product)

| Stage | What happens | Non-negotiable |
|---|---|---|
| **Sense** | POV video ambient context + ambient listening | On-device gate when possible; minimize continuous cloud stream |
| **Reason** | Cognitive-forcing suggestion (not autopilot orders) | Grounded in evidence API / local protocol pack |
| **Cue** | Tone / vibration + short visual text | Discrete in ICU; no patient-facing spectacle |
| **Act** | Natural verbal response or clinical action | Human remains decision-maker |
| **Label** | Was cue helpful? Accurate? Cost/latency? | Required for every fired cue eventually |
| **Train** | Offline policy / model update | Never silent online self-modification at bedside |

---

## What this is / is not

**Is**
- Cognitive forcing function for decompensations (sim + learners first)
- Ambient co-pilot with a closed quality loop
- Candidate hardware path for Tx ICU excellence / Crisis Mirror

**Is not**
- Autodiagnosis or automatic order entry
- Always-on cloud wiretap of the unit
- A replacement for board-certified judgment

---

## Hardware map (candidates you named)

Sources: Brilliant Labs public Halo materials / reviews (2025–2026); Even Realities G2 reviews & support specs (2025–2026). Verify price/availability before buy.

### Scorecard vs sketch requirements

| Requirement from sketch | Brilliant Labs **Halo** | Even Realities **G2** |
|---|---|---|
| **Visual cue (HUD text)** | Yes — color microOLED ~20° FoV, glance/tilt to see; +2 to −6 diopter optic | Yes — binocular waveguide, mono green 640×350, **27.5° FoV**, ~1200 nits (strong daylight text) |
| **Tone / audio out** | Yes — dual bone-conduction speakers | **No speakers** on core G2 A/B (reviews) |
| **Vibration / haptic** | IMU + tap; true haptic weak/unclear — may need phone/ring | Optional **Even R1 ring** (~$249) for control/haptic-ish UX |
| **Ambient listening (mics)** | Yes — dual mics + audio activity detection | Limited / app-dependent; not the design center |
| **Video ambient context** | Yes — onboard optical/POV sensing (low-power AI camera path) | **No camera** on standard G2 (privacy-forward, breaks full sketch alone) |
| **On-device AI headroom** | Strong — Alif B1 CPU+NPU, ZephyrOS, open HW/SW, Noa agent | Phone-centric stack; less open hack surface |
| **All-day clinical wear** | ~40 g, up to ~**14 h** claimed | **~36 g**, up to **~2 days** regular use + case (7× recharges) |
| **Prescription** | Optic + lens options (stock AR coat; Rx path) | Full Rx frames (extra cost) |
| **Price (street/MSRP ballpark)** | ~**$299–349** (launch/preorder band; limited drops) | **$599** frames (+ Rx; ring extra) |
| **Open / buildable** | **Best-in-class** for this project (GitHub / Lua / Zephyr) | Closed consumer product + app store |
| **Fit to full Crisis Mirror sketch** | **Primary hardware** — sense + cue on one device | **Secondary / display specialist** — needs phone or second sensor for A/V |

### Recommendation

1. **Build prototype on Halo** (or Halo-class open glasses): only candidate that natively covers *video + listen + tone + visual* without bolting on a second body-worn camera. Open stack matches “post-hoc training + custom cognitive forcing.”
2. **Keep G2 as display reference / alternate form factor** if discrete daylight text and multi-day battery matter more than onboard sensing — pair with phone mic/camera **only in sim**, not as the long-term bedside architecture unless privacy policy forbids glass cameras.
3. **Do not buy both yet.** Spike sim-lab cue UX on Halo first; rent/borrow G2 only if Halo HUD readability fails under ICU lighting.

### Hard gaps on both

- Neither is a medical device. Clinical use = research / QI / education framing + IRB/ethics as required.
- PHI: prefer on-device redaction, short buffers, BAA’d cloud only for evidence queries stripped of identifiers.
- Haptics on Halo may be too weak for “tap the shoulder” cues → fallback: bone-conduction earcon patterns + HUD flash.

---

## MVP slice (4 weeks of real work, not theater)

1. **Sim only** — scripted decompensation scenarios (hypotension post-reperfusion, rising lactate, airway risk, etc.).
2. **Cue types v0** — 3 earcons + ≤8-word HUD text; no free-form speech to clinician during crisis.
3. **Reasoner v0** — protocol card pack + OpenEvidence (or equivalent) behind a strict schema: `{trigger, differential_nudge, next_check, confidence}`.
4. **Label UI** — after scenario: 2 taps — Helpful Y/N, Accurate Y/N, optional 5-sec voice note.
5. **Metrics** — cue latency p50/p95, $/cue, %helpful, %accurate, clinician interruptibility score.

**Exit criterion:** learners prefer Crisis Mirror on vs off on ≥1 scenario class with no increase in harmful actions.

---

## Safety / ethics firewall (carry into every build)

- Advisory language only (“consider”, “check”, “diff includes”).
- No automatic documentation into EMR without explicit commit.
- Role separation if donor / prior-recipient edge cases appear in ambient audio (align with Prior Recipient→Donor Ethical Firewall).
- Full audit log of cues shown + labels; deletable retention policy.

---

## Artifact index

| File | Purpose |
|---|---|
| `crisis-mirror-architecture.html` | Dark tech architecture diagram (open in browser) |
| `crisis-mirror-flow.excalidraw` | Editable hand-drawn flow (drop on excalidraw.com) |
| `ONEPAGER.md` | This brief |

---

## Next decisions for Sergio

1. Halo preorder / unit for sim lab — yes/no?
2. First scenario pack: liver reperfusion instability vs generic ICU decompensation?
3. Evidence backend: OpenEvidence API vs local protocol YAML first?

---

*Crisis Mirror • Tx ICU • Link / Hermes*
