# Hardware comparison: Halo cam-off vs Even G2 vs phone-only

Retrieved 2026-08-18 from live vendor pages. This is a research note, not a buy order.

Labels: **FACT** = quoted from a fetched page. **INFERENCE** = labeled. **UNKNOWN** = not on the fetched pages.

## Why three arms

Cognitive Companion v1 is camera-free HUD + audio, not wearable video [unverified].
The committed product path is Halo with camera hard-off for the VCU sim pilot [unverified].
G2 is the camera-free-by-design alternative [4].
Phone/iPad-only is the no-glasses control and the fallback if glasses fail procurement, IRB, or wear-time [unverified].

## Comparison (vendor claims)

| Dimension | Brilliant Labs Halo | Even Realities G2 / G2-A | Phone / iPad only |
| --- | --- | --- | --- |
| List price (2026-08-18) | $399.00 USD [1] | $599 non-prescription G2-A [6] | Device already in pocket / cart. Cost = $0 incremental hardware if a phone/iPad is already used. |
| Mass | “just over than 40g” [1] | “Just 36 grams.” [4] | N/A (handheld) |
| Camera | 640x480 global shutter color; PixArt PAG7982J1 [3] | “Camera-free. By design.” [4] | Device camera exists; keep it unused for this protocol |
| Microphones | Dual / stereo mics [1] [3] | Four microphones [4] | Phone/iPad mics |
| Audio out | Dual / stereo bone-conduction speakers [1] [3] | **UNKNOWN** (no speaker line on fetched G2 pages) | Phone speaker / AirPods / cart speaker |
| Display | 256x256 px drawable area [3] | 640*350 stated resolution [4] | Full phone/iPad screen |
| Battery (vendor) | 300 mAh built-in Li-ion [3] | **UNKNOWN** (not extracted this session) | Hours, but hands and gaze leave the patient |
| Durability | **UNKNOWN** (no IP rating on fetched Halo pages) | IP65; 40,000 hinge cycles; 2 m drop [4] [5] | Consumer phone ratings vary |
| Cloud / consent copy | Conversational agent “Noa” on product page [1] | “No data is stored in the cloud without your explicit consent.” [4] | Depends on app, not fetched |
| Health-critical disclaimer | “not verified for use where performance and accuracy would be critical to human health” [3] | Not seen on fetched G2 pages | Consumer device, not a medical device |
| Firmware / lock | OTA firmware updates [3] | **UNKNOWN** | OS updates |
| OS / app path | Brilliant / Noa stack; camera is on the board | MentraOS lists Even Realities as a supported platform [7] | Native iOS/iPadOS app is the edge brain in all arms |

Mentra Live is **not** a camera-free candidate [7].
Mentra Live is sold as camera-enabled glasses at 43 g [7].

## Halo: what “cam hard-off” actually is

**FACT.** Halo ships with a front-facing 640x480 color camera [3].

**FACT.** Brilliant’s own hardware docs say the device is not verified for health-critical use [3].

**UNKNOWN.** Fetched docs do not describe a hardware kill-switch, camera-module removal SKU, or a documented “camera off” firmware flag [unverified].

**INFERENCE.** “Hard-off” for a VCU pilot is a protocol + firmware + physical-cover problem, not a factory SKU. If the camera can be re-enabled by OTA [3], a one-time software mute is not hard-off.

Pilot implications (inference, not vendor text):

1. Prefer a physical cover plus a firmware image that never initializes the sensor [unverified].
2. Photograph / inventory that image before first sim [unverified].
3. Do not call Halo “camera-free.” Call it “camera present, disabled for this study” [unverified].

## Even G2: camera-free, audio-out still open

**FACT.** Even’s marketing page says the product is camera-free by design and uses the microphone rather than a camera for input [4].

**FACT.** Four microphones and a Conversate “captures and transcribes every word” feature are on the same page [4].

**FACT.** G2-A list price on 2026-08-18 is $599 [6].

**UNKNOWN.** Speakers, bone conduction, or any audio-out path [unverified].
Re-fetched Even pages still have no speaker line [4] [5] [6].

**INFERENCE.** If G2 cannot play a short audio cue, the companion’s output collapses to the HUD plus the phone speaker. That is a different human-factors product than Halo’s bone-conduction path [1] [3].

Do not write “G2 has no speakers.” Absence of a spec line is unknown, not a negative finding [unverified].

## Phone / iPad only

No new vendor page is required [unverified].
This arm is the edge brain without a head-worn display [unverified].

What it buys:

- Zero wearable camera / wearable-mic IRB novelty.
- Full screen for a PediAppRREST-style checklist (content-layer evidence; see literature notes).
- Instant fallback if glasses procurement slips.

What it loses:

- Hands and gaze leave the manikin whenever the operator reads the phone.
- No HUD in the line of sight.
- Cart-mounted tablet is a third sub-arm (hands-free-ish, still not head-worn).

## Mentra as OS, not as glasses

**FACT.** MentraOS lists Even Realities among supported hardware [7].

**FACT.** Mentra Live is a different, camera-enabled product [7].

**INFERENCE.** Mentra is relevant as a possible app runtime for G2, not as the VCU pilot headset [unverified].

## Cost collision with committed docs

Committed funds/one-pager copy has used a cheaper Halo band ($299–$349 in older notes) [unverified].
Live list price 2026-08-18 is $399 [1].

Do not silently “split the difference.” Update the budget or footnote the date [unverified].

G2 at $599 [6] is the more expensive glasses SKU if the team abandons Halo over the camera.

## What this note does not decide

- Which SKU to buy.
- Whether Halo firmware can legally/technically disable the camera.
- Battery life in a 15–20 minute sim (300 mAh is a capacity, not a runtime [3]).
- Whether G2 HUD is readable in a bright sim bay (no lux/contrast numbers retrieved).

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
