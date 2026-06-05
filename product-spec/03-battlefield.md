# 03 — Battlefield Feature

## Concept
Adaptive question grind. User picks subject → up to 3 BAB → infinite random question stream. Real mastery proof.

**Battlefield = the only feature that affects mastery.**

## Selection Flow
1. User picks subtest (1 of 7)
2. User picks 1-3 BAB within subtest
3. Question stream begins

## Question Stream Logic

### BAB rotation rule
Weighted random by user's **weakest BAB among 3** (force confront weakness).

### Anti-monotone constraint
- Same BAB question never appears 3× in a row
- 2× same BAB OK if random coincidence
- 3rd question after 2× same → force random different BAB
- Forcing events spaced ≥8 question apart (prevent forcing-near-forcing)

### Mode toggle
User override: "Balanced" mode = round-robin equal between 3 BAB.

### Question repeat
**Never within 7 day per user.** Cooldown queue per userID. Bank size 5000+ makes cooldown trivial.

## Wrong Answer Behavior
- **0 point** (no negative — discouraging for grind feature)
- Show explanation **immediately** + "lanjut" button
- Mark question for "Review Later" pile auto
- Surface "Review Later" recommendation in dashboard + battlefield + profile

## Session End
- User-quit only
- Soft prompt at 25 / 50 / 100 question ("istirahat dulu?")
- No hard cap
- Session length awareness: at 90 min → modal "udah 1.5 jam, istirahat 10 menit?"
- At 3 hour → stronger modal + auto-pause Elo for next 30min if continue (anti-burnout)

## Difficulty Progression — Adaptive Elo
- Each user has **hidden rating R per BAB** (start 1000)
- Each question has **rating D** (mapped from manual difficulty 1-5)
- Serve question within ±100 rating of user
- See `04-mastery-elo-system.md` for full formula

## Streak / Combo
- Visual streak counter per session
- +small bonus to mastery rolling avg on streak ≥5
- Break on wrong answer
- First 5 question of session = streak warmup, wrong does NOT break streak (beginner protection)
- Tab-switch detected → streak bonus that question NOT awarded + UI tells user "kami notice tab-switching"

## Anti-Cheat Philosophy
**Ignore (mostly).** Battlefield = practice, not graded. User cheat = user lose.

Soft signal:
- Detect tab-switch → no streak bonus that question
- Notify user "kami notice tab-switching"
- No hard ban from cheating in battlefield

(Hard anti-cheat reserved for tryout — see `04-tryout.md`.)

## Point System (radar chart fuel)

### Two radar chart on profile
1. **Mastery radar** (primary — honest skill signal)
2. **Raw count radar** (secondary — vanity dopamine)

### Mastery (per subtest)
- Range 0-100
- Derived from per-BAB Elo rating
- Log-weighted average across BAB in subtest
- See `04-mastery-elo-system.md`

### Raw count
- Simple counter: "soal dijawab benar: 425"
- Per BAB + per subtest
- Vanity counter — doesn't gate anything

### Hidden Elo per BAB
- Internal rating (~600-2000 range)
- Optionally exposed in detailed profile view

## Radar Chart Design
- **7 axes** = 7 subtest (matches UTBK scope)
- 100+ axis (per BAB) = unreadable garbage, never do
- Click subtest axis → **drill-down bar chart** of mastery per BAB within subtest
- Radar = overview, bar = detail

## Leaderboard
- Per-subtest **weekly mastery leaderboard**
- Top 100 + your rank
- Resets Senin 00:00 WIB
- Friends-only tab (v1, since friend system shipped)

## Free vs Paid Gate
- **Free**: 10 question/day battlefield, no leaderboard, no worked solution post-question
- **Pro**: unlimited, leaderboard access, worked solution + Review Pile

## Review Later Pile
Auto-populated from wrong-answer marks. Surfaced in:
- Battlefield dashboard
- Main dashboard widget
- Profile page section

User can:
- Review questions with worked solution
- Reset / clear pile
- Filter by BAB / subtest

## Recommendation Engine v1
Dashboard surface:
- "Review pile kamu: 47 soal" → click → review flow
- "Mastery terendah: [BAB Y] (32)" → click → battlefield with that BAB preselected
- Forward-looking framing (Q23): "fokus berikutnya" not "kamu lemah di"

## Cohort / Friend Tab
- Friend leaderboard (added Q21)
- Cohort tab (UTBK 2027 cohort) — auto-tagged by target_year_utbk

## Anti-Burnout Integration
See `09-retention-burnout.md` for:
- Session length warning
- Night grind detection
- Mastery framing (growth not deficit)
- Streak softening

## Anti-Bot Detection
- Sub-second uniform response variance <200ms across 10+ q → bot signature
- Action: shadowban (visible to self, hidden to leaderboard)
- Confirmed: ban + appeal email
- See `11-security.md` for full anti-abuse stack
