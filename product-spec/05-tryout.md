# 05 — Tryout Event Feature

## Concept
Scheduled large-scale tryout exam. Mirror real UTBK feel: fixed start time, hard timer per subtest, leaderboard, percentile. Online but feels like real-life event.

## Token System
- Token auto-generated on **event registration + payment** (or free for Pro)
- Single-use per user × event
- Different token per user
- Tied to userID + eventID (not transferable)
- Generated at registration, sent via in-app inbox + email

## Capacity
**5000 peserta cap per event v1.** Waitlist after cap. Scale ceiling later.

## Scheduling
**Fixed start time, all participants same UTC moment.**

Reason: real UTBK feel = whole point. Rolling 24h window kills "battle" energy + leaderboard meaningless.

WIB timezone v1, single zone for all.

## Duration
**Mirror real UTBK timing per subtest.**

Hard cutoff per subtest. Auto-submit when time runs out per subtest. Cannot return to previous subtest.

Real UTBK reference (subject to update per official SNPMB):
- TPS: 30-37min per sub-component (4 components)
- Literasi Indonesia: 42min
- Literasi Inggris: 30min
- Penalaran Matematika: 42min

## Anti-Cheat (v1, technical only)
- Tab-switch warning + count tracked per peserta
- Fullscreen lock
- Paste disabled
- Copy disabled
- Right-click disabled
- Screenshot watermark with hidden userID
- **No webcam proctor v1** (privacy + infra cost)

User who pays to learn yet still cheats = their loss. Outliers curated manually post-event.

## Anti-Cheat Philosophy
**Accept-cheat freemium model v1.** Market as "self-assessment ranking among honest participants". Outlier disqualified manually.

v2 optional: paid tier "Tryout Premium Proctored" with webcam — defer 6mo+ post-launch.

## Scoring
**v1: weighted raw by manual difficulty tag.**

```
score_subtest = sum(difficulty_weight × is_correct) / sum(difficulty_weight × all_question)
                × 100  (or scaled 200-800 UTBK-like)
```

### IRT Migration
- After event #1 (5000 response/question collected): switch **1-PL Rasch model**
- After event #6+ (25k+ response/question): **2-PL Rasch**
- 1-PL stable from 100-200 peserta per question (research-backed)
- Skip 3-PL — noisy on MCQ-4option

UI shows score + percentile, engine transparent to user.

## Leaderboard
**Post-event only**, full ranking with percentile.

Released ~1 hour after event close (allow grading + sanity check).

Live ranking during event = laggy + cheating signal + stress. Skip.

Leaderboard scope (per event):
- Global top 100 + your rank
- School ranking (per Q15 logic)
- Bimbel ranking
- Friend tab
- Cohort tab

## Review Flow
**Post-event only**, after leaderboard release.

Immediate review during event = cheat vector for late starter. Skip.

User can:
- See own answer per question
- See correct answer + worked solution
- See difficulty tag + percentile correct
- Mark question for "Review Pile" (carry to learning + battlefield)

Review access:
- **Free user**: score only, no review
- **Pro user**: full review + worked solution

## Grading
- **MCQ**: auto, exact match
- **Isian Penalaran Matematika**: exact-match string compare with normalization
  - Trim whitespace
  - Lowercase
  - Accept "1/2" == "0.5" (numeric equivalence)
  - Accept "0,5" == "0.5" (Indonesia decimal)
- Edge cases auto-flag for **manual review** by content team

## Monetization
**Freemium tryout model:**

### Free user
- 1 tryout/month free entry
- Score only (no leaderboard, no review)

### Pro user
- Unlimited tryout entry
- Leaderboard access
- Worked solution + review post-event

### Per-Event (non-subscriber)
- **Rp 35.000/event**
- One-time access to specific event
- Leaderboard + review unlocked for that event
- Drives top-of-funnel capture for big national events

### Premium Proctored (v2)
- Rp 75.000-100.000/event
- Webcam proctor + ID verification
- Credible leaderboard for serious aspirant

## Erratum During & Post Event

### Mid-event question correction
- Question suspended → all peserta who reached question get full credit + skip (no replace)
- Emergency in-event banner announces "soal X dihapus karena error"
- 1-hour SLA for content moderator on duty during event

### Post-event correction
- Re-grade all affected peserta
- Leaderboard re-rank
- Email + in-app notify all peserta about correction
- "Leaderboard tryout [event] diperbarui karena perbaikan soal X"

## Event Lifecycle Status
```
draft → upcoming → live → completed → archived
```

- Draft: admin creating
- Upcoming: registration open
- Live: event in progress, no new registration
- Completed: event ended, grading/review
- Archived: 30+ day post-event, leaderboard frozen, archived to cold storage

## Event Tier (v1+)
- **Mini Tryout**: 1 subtest, weekly schedule
- **Tryout Akbar**: full 7 subtest, monthly schedule
- **Tryout Akbar Nasional**: special event, 5000 cap, marketing peak (Nov 2026 launch event)
- **Sprint Final Tryout**: UTBK D-30 special, weekly intensive

## Special: Sprint Final (D-30)
4-week aggregate special leaderboard during UTBK pre-exam window. See `09-leaderboards.md` for cohort-special ranking.

## DDoS / Infra Concern
- Cloudflare WAF in front
- Tryout entry queue: 5000 cap + waiting-room page if traffic spike
- Separate read replica for leaderboard query
- DB connection pool + circuit breaker on heavy query

See `14-security.md` for full DDoS spec.

## Token Anti-Abuse
- Token bound to userID + fingerprint at generation
- Cannot be transferred / sold
- Single-use enforced server-side
- Refund on chargeback fraud → token void

## Tryout Does NOT Affect Mastery
Tryout = high-stakes assessment, separate from battlefield Elo.

Reason: tryout response one-time burst with stress condition ≠ steady mastery practice. Conflating pollutes battlefield Elo signal.

Tryout response stored in **separate table** `tryout_response` (not battlefield `response` table) for in-event isolation. Allows full re-grade post-event without touching battlefield mastery.
