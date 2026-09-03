# Validated Structures Reference

Reverse-engineered ad structures with measured spend behind them. Unlike
`formulas.md` (canonical frameworks) and `hooks-library.md` (templates), every
pattern here is backed by observed Meta Ad Library data — so it tells you not
just what a structure looks like, but how much money it actually holds.

**How to use:** when a brief lands in a category covered here, start from the
validated skeleton rather than a generic PAS/PASTOR shell, then re-run the
result through `quality-checks.md`.

---

## Dataset 1 — DE health / gut-cleanse (Sept 2026)

**Source:** Meta Ad Library scrape, active ads only, German market.
**Scope:** 361 unique ads · 26 pages · 7.46M est. impressions · ~$89.5k est. spend.
**Raw data:** `data/meta-ad-library-de-health-2026-09.csv` (sorted by $/day).

⚠️ **Spend figures are scraper estimates derived from EU transparency ranges,
not billed spend.** Treat them as ordinal, not absolute — valid for ranking ads
against each other, invalid as a budget figure.

### Reading the metrics

Rank by **est_spend_per_day**, never by total spend. Total spend rewards age: a
mediocre ad running 135 days outranks a winner running 10. Daily burn is the
advertiser's live vote of confidence.

Three signals, in order of strength:

| Signal | What it means |
|---|---|
| High **$/day** on a **young** ad | Being scaled right now. Highest-value intel. |
| Same hook across **multiple pages** | Cross-validated. Survived more than one audience. |
| `creatives_sharing` > 1 | Advertiser is duplicating a proven asset, not testing a new idea. |

**The trap:** ad *count* is not strength. In this set, `Eliminiere Parasiten &
Pilze` runs 36 ads across 3 pages for 135 days — and peaks at $31/day. It is
cheap evergreen filler. The top earner runs as a **single** ad at $339/day.
Sorting by "most copies" picks the filler and misses the machine.

### Portfolio shape

One advertiser accounts for $77k of the $89.5k: **Carva Balance / Natuvi
Naturals** on `gesundheit-im-alltag.com`. The 26 "pages" are a network of
fake-media and fake-practitioner personas ("Apothekenjournal", "Deutsches
Gesundheitsblatt", "Medizin der Natur", "Dr. Markus Schneider") pointing at one
offer. Secondary players: Alimora OregaMix ($11.4k), Vitalira ($0.8k),
Naturavex ($0.6k).

### Top performers

| $/day | Total | Days | Library ID | Hook |
|---|---|---|---|---|
| **$339** | $9,142 | 27 | `1979449889375268` | "Wir haben alle Parasiten in uns (ja, auch Du!), lass mich erklären.." |
| **$260** | $6,749 | 26 | `1374898884815000` | "3 Jahre lang dachte meine Frau, sie würde verrückt werden. 4 Ärzte sagten ihr, es sei Stress. Sie lagen alle falsch." |
| **$245** | $2,446 | 10 | `27958249043840794` | "Reinige deinen Körper von innen‼️" (short-form benefit stack) |
| $167 | **$8,202** | **49** | `1684769269495401` | "Dein Körper sendet SOS-Signale 🚨" |

### Hook families

| Spend | Ads | Pages | LPs | Peak $/day | Family |
|---|---|---|---|---|---|
| $16,958 | 53 | 4 | 7 | $167 | SOS-Signale (symptom-alert) — the **control** |
| $14,128 | **4** | 2 | 3 | **$339** | "We all have parasites (yes, you too)" — best per-ad efficiency |
| $9,480 | 8 | 2 | 2 | $260 | Spouse-POV misdiagnosis story |
| $7,618 | 24 | 1 | 1 | $245 | Short-form "clean your body from within" |
| $5,803 | 36 | 3 | 4 | $31 | "Eliminate parasites & fungi" — evergreen filler |
| $4,540 | 18 | 3 | 3 | $52 | "137,000 customers trust…" (proof-led) |
| $3,732 | 19 | 3 | 1 | $125 | "Still not feeling right despite eating healthy?" |

Note the shape: **$14.1k from 4 ads** beats **$5.8k from 36 ads**. Per-ad
efficiency, not volume, separates the angles.

### Landing-page architecture

| Spend | Ads | Page |
|---|---|---|
| $25,933 | 86 | `carva-balance-angebot-limitiert-`**`v3`**`-01` |
| $18,909 | 40 | `carva-balance-angebot-limitiert-`**`v2`**`-01` |
| $15,823 | 47 | `5-gruende-warum-carva-balance-v1-01` (listicle) |
| $2,067 | 24 | `carva-balance-angebot-limitiert-`**`v1`**`-01` |

The version ladder is the real lesson: v1 → v2 → v3, with budget migrating to
each new version and v1 left nearly dead. **This advertiser won by rewriting the
landing page three times, not by producing more creatives.** A listicle variant
runs in parallel on the same script, so traffic gets sorted by reading style.

Corollary for testing order: `SKILL.md`'s testing hierarchy (hook 60-70% →
angle → format → offer) governs the creative. The LP is a separate axis, and in
this dataset it moved more money than any single creative.

---

## The Discredited-Diagnosis skeleton

The structure behind the two top earners. It is not a product pitch — it is an
argument that **the reader's existing diagnosis was wrong**, which makes the
product the only remaining option.

### Beats

1. **Hook** — universal provocation ("we all have X, yes you too") or
   third-person POV ("3 years my wife thought she was going crazy").
2. **Qualify + open loop** — name the symptoms, promise an explanation.
   *"If you're fighting bloating, fatigue or gut issues that just won't go
   away — keep reading. Because what came out of me explained everything."*
3. **Symptom list in domestic language** — concrete, not clinical.
   *"Salad? Bloated. Rice? Bloated. Water? Somehow still bloated."*
4. **Graveyard of spend** — every failed attempt, itemized with prices:
   dozens of probiotics, influencer gut powders, elimination diets, a €200
   intolerance test, doctor visits. Each failure pre-answers an objection.
5. **The junk diagnosis** ⭐ — the label doctors hand out instead of an answer.
   *"IBS. The diagnosis you get when nobody knows what's actually wrong."*
6. **The 2 a.m. discovery** — found via "a real scientific study", not a forum.
   Reframes the reader's own late-night searching as legitimate research.
7. **Why your test came back clean** ⭐ — the load-bearing beat. Explains away
   the single strongest counter-argument the reader holds (a doctor said I'm
   fine). *"Standard stool tests miss up to 90% of infections. Parasites don't
   lay eggs every day."*
8. **Named mechanism** — a molecule, not an herb. Carvacrol destroys the cell
   membrane; thymoquinone attacks eggs and larvae. Specificity does the
   persuading.
9. **DIY failure** ⭐ — why the cheap version can't work, on dosage grounds.
   *"Health-store oregano oil: maybe 15-20% carvacrol. Some bottles almost none
   — just olive oil that tastes like oregano."* Kills self-treatment and the
   entire competing category in one move.
10. **Brand as the only correct dose** — 165 mg carvacrol, standardized.
11. **Offer block** — 30-day money-back, "20,000+ customers", "4.8/5 Trustpilot",
    certified German production, independent lab testing.
12. **Scarcity with a reason** — *"Sold out last month after the viral rush.
    Stock is back, but demand is high."*

### Why it transfers

Beats **5, 7 and 9** are the transferable asset, and none of them are
category-specific:

- **5** — every chronic condition has a junk diagnosis ("it's age", "it's
  stress", "it's wear and tear", "it's chronic, you'll manage it for years").
- **7** — every condition has a test that can be framed as blind to the real
  cause.
- **9** — every category has a cheap pharmacy version that can be attacked on
  dosage or bioavailability.

Swap the topic, keep beats 5/7/9, and the argument holds.

### Structural variants worth testing

- **Third-person POV** (spouse, adult child) outperforms first-person illness
  narration in this set: $260/day. It converts complaint into testimony and
  lets the narrator be angry on the sufferer's behalf.
- **Counted authority failures** — "4 doctors", "4 minutes with me", "third
  misdiagnosis". Numbers make the indictment auditable.
- **Named pre-emptive worsening** — a scripted "it gets worse in week three,
  that's the sign it's working" turns the top refund trigger into proof. (Seen
  in the Spanish-market equivalent of this offer.)
- **Anti-CTA** — "oh, I almost forgot the link" reads as testimony, not ad.

---

## Cross-vertical mapping

Applying the skeleton to adjacent DR health verticals. `Personal attributes`
refers to Meta's prohibition on copy that asserts or implies the viewer has a
condition.

| Vertical | Junk diagnosis (beat 5) | Blind test (beat 7) | DIY failure (beat 9) | Notes |
|---|---|---|---|---|
| **Parasites / gut** | "It's IBS" | Stool test misses intermittent shedding | Health-store oregano oil is under-dosed | 1:1 fit. Beat-1 provocation is safe here because "everyone has them" asserts nothing about the individual viewer. |
| **Joints** | "It's your age", "cartilage wear", "take NSAIDs" | X-ray images bone, not the soft tissue driving pain | Pharmacy chondroitin at sub-therapeutic dose | Largest audience of the group. Strong fit; the reader arrives already medicated, so beat 9 must also explain why the NSAID only masks. |
| **Prostatitis** | "It's chronic, you'll manage it for years" | PSA/standard panel doesn't explain symptoms | Saw palmetto extract standardization varies wildly | High intent, narrow audience (M 45+). Personal-attributes risk is real. |
| **Incontinence** | "It's normal after childbirth / at your age" | Nobody tested the actual muscle function | Pelvic-floor apps ignore the underlying cause | ⚠️ Do **not** port beat-1 verbatim. "You have this" about parasites is universal; the same construction about incontinence is a direct assertion about the viewer and trips personal attributes. Use third-person POV or a situational open. |
| **Hypertension** | — | — | — | ⛔ Not recommended for cold traffic. BP claims are treated as medical claims, the audience is on prescription medication, and any implication of replacement is both a policy violation and a genuine safety problem. Low ceiling, high domain risk. |

**Priority when the vertical is open:** parasites first (validated structure
copies over with near-zero adaptation, readable results in 2-3 days), joints
second (largest volume, but the angle is untested and needs its own hook round).

---

## What not to copy from this dataset

The observed advertiser's persuasion rests substantially on fabrications. These
are the parts to leave behind, and they are also the parts that get a domain and
business manager killed rather than a single ad rejected:

- **Invented practitioners and media brands** — a page network posing as
  pharmacy journals, health gazettes and named doctors.
- **Fabricated testimonials and case names.**
- **Unverifiable proof numbers** — "20,000+ customers", "137,000 satisfied
  customers", "4.8/5 on Trustpilot" repeated verbatim across 53 ads.
- **Disease-treatment claims on a food supplement** — under Reg. (EC) 1924/2006
  and the Unfair Commercial Practices Directive, health claims not on the EU
  permitted list, invented health professionals and fake reviews are all
  prohibited outright in the EU.
- **Inconsistent guarantees** — 30 days in most creatives, 90 in others.
  Whatever the compliance posture, this alone drives chargebacks.

The structure is legitimately reusable. The fabricated authority layer is not —
and beats 5/7/9 are what actually carry the argument, so replacing invented
credentials with a real or clearly-labelled voice costs less performance than
it looks like it should.
