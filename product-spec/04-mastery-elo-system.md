# 04 — Mastery & Elo System

## Source of Truth
**Per-BAB Elo rating** = single source of truth. All mastery, radar, leaderboard derive from here.

Lesson does NOT update Elo. Battlefield + tryout response + diagnostic = update sources.

## Elo Formula

### Setup
- User per-BAB rating R: start 1000, range 400-2000
- Question difficulty D mapped from manual 1-5:
  - D=1 → 600
  - D=2 → 800
  - D=3 → 1000
  - D=4 → 1200
  - D=5 → 1400
- Later: swap manual D to IRT-calibrated rating

### Update on answer
```
expected = 1 / (1 + 10^((D - R) / 400))
R_new = R + K × (actual - expected)
  where actual = 1 if correct, 0 if wrong
```

### K-factor — Asymmetric Tier-Based
Beginner-friendly: gain easier, loss harder. Dopamine for low-level user. Earn stays hard for high-level.

| Tier | Rating R | K_gain (correct) | K_loss (wrong) |
|---|---|---|---|
| Newbie | R < 900 | 40 | 16 |
| Mid | 900-1100 | 24 | 24 |
| Advanced | R > 1100 | 16 | 32 |

Newbie tier: 2.5× faster gain than loss → fast onboarding satisfaction.

### Calibration phase
First 30 question per BAB: K boosted +50% on top of tier value (faster initial convergence).

## Beginner Protection Stack
1. **Grace period**: first 10 question per BAB = gain only, no loss. After 10 → Elo loss kicks in.
2. **Rating floor**: R clamp ≥600. User never goes negative.
3. **Streak warmup**: wrong in first 5 question of session = no streak break.
4. **Wrong-answer tone**: UI never red/X. Use neutral color + "belum tepat — yuk pelajari".
5. **Asymmetric K (above)** at low rating tier.

## Mastery Display Score (0-100)

### Per BAB
```
mastery_BAB = clamp((R - 600) / (1400 - 600) × 100, 0, 100)
```
- R=600 → 0%
- R=1000 → 50%
- R=1400 → 100%
- Clipped at boundary

### Per Subtest (radar chart axis)
```
mastery_subtest = weighted_avg(mastery_BAB, weight = log(1 + question_answered_BAB))
```
Log weight prevents one over-grinded BAB from dominating subtest score.

### Display gating
Mastery shown only if user answered ≥10 question in that BAB. Otherwise: "belum cukup data — terus latihan".

## Mastery Cap
**Hard cap 100.** UTBK is bounded — 100 = "siap". User reaches → badge "Master" earned, mastery freezes at 100 in display.

Internal Elo R can keep climbing past 1400 (uncapped) for matchmaking purpose, but display caps.

## No Mastery Decay
**No decay over time.** UTBK is bounded exam, decay annoying for self-paced learner.

Show "terakhir kerjakan: 12 hari lalu" hint instead of decay penalty.

## 4-Tier Mastery Badge (per BAB, derived)
- **Pemula**: 0-20 mastery
- **Pelajar**: 20-50
- **Mahir**: 50-80
- **Master**: 80-100

## Two Radar Chart on Profile
1. **Mastery radar** — primary, honest skill signal, 7 axes (subtest), values 0-100 from formula above
2. **Raw count radar** — secondary, vanity dopamine, 7 axes (subtest), values = total correct count per subtest

Both visible on profile page. Dashboard shows mastery primary, raw count tucked smaller.

Click subtest axis on mastery radar → drill-down bar chart of mastery per BAB within subtest.

## Recompute Logic on Erratum
When question kunci salah is fixed (Q18):
- Re-grade all past response on this question_id
- Reverse Elo change for affected user (per question affected)
- Recompute mastery cache
- Notify user via in-app banner

When question retired due to ambiguity:
- Annul all response (no Elo impact either direction)
- Refund 1 mastery point each affected user (compensation for confusion)

## IRT Migration Path
- v1 launch: hardcoded `score = sum(difficulty_weight × correct)` with manual D
- After event #1 (5000 response/question): switch **1-PL Rasch** using py-irt or mirt R package
- After event #6+ (25k+ response/question): upgrade **2-PL Rasch** (difficulty + discrimination)
- Skip 3-PL — guessing parameter noisy on 4-option MCQ, marginal gain

UI just shows score + percentile. Engine swap underneath transparent to user.

## Materialization Strategy
- v1: compute mastery on read (live from rating table) — simple
- v2 (5k+ MAU): cache + scheduled refresh hourly — faster
- v3: write-through cache on every answer — fastest

Premature optimization rejected v1.

## Internal Storage Recap
```
[user_bab_rating] table
  user_id, bab_id, elo_rating (default 1000),
  question_answered_count, last_answered_at,
  mastery_display_cached (0-100, recompute on read or scheduled)
```

Subtest mastery = derived view from this table, not stored.

## Diagnostic Seed
On signup diagnostic completion (see `07-onboarding.md`):
- Per-subtest avg score → per-BAB Elo seeded
- 5 question/subtest × 7 = 35 question total
- CAT-lite within subtest (correct → harder next, wrong → easier next)
- Skip diagnostic → all BAB start at default 1000
