# 08 — Leaderboards & Social Ranking

## Layered Leaderboard System
Multiple scope, weekly cadence (mostly).

### Scope tabs
1. **Global** — top 100 by per-subtest mastery + your rank
2. **School** — top 100 schools + intra-school top 50
3. **Bimbel** — top 100 bimbel + intra-bimbel top 50
4. **Friends** — friend-only ranking (after friend system)
5. **Group** — user-created group internal leaderboard
6. **Cohort** — UTBK 2027 cohort etc

## Reset Cadence
- **Weekly**: Senin 00:00 WIB → previous week archived
- "Hall of fame" page = top school + bimbel each historical week
- **Special event**: Tryout Akbar = own one-off leaderboard (overlay on weekly)
- **UTBK D-30**: "Sprint Final" 4-week aggregate special leaderboard

## School Leaderboard

### School assignment (Q15)
- Required field at signup
- Select from preloaded DAPODIK list (~14k SMA + sederajat)
- "Sekolah saya tidak ada" → user-add → admin moderate queue
- 14-day pending before counted in leaderboard
- Min 10 active user before school appears in main leaderboard
- School can be changed once per 6 month (anti-gaming)

### Special pseudo-schools
- Homeschooler / gap year / kelas 13 → "lainnya" pseudo-school
- Own bucket, won't pollute SMA leaderboard

### School verification (v1)
- Trust + soft heuristic (e.g. ≥5 user same school + similar location IP cluster = legit)
- No .sch.id email gate (most SMA student no school email)
- Admin random audit top-10 schools weekly (manual until tooling)
- Report-fake button on school page

### Aggregation Metric — Top-10 Average
**Top-10 avg mastery per school** = the school's score.

```
school_score = avg(top_10_mastery_subtest_user_in_school)
```

Reason: small + big school both compete fair. Top-10 = "varsity team" concept = bragging rights without forcing whole school active.

### Min participation threshold
- School needs ≥10 active user this week to qualify
- "Active": answered ≥30 battlefield question OR completed ≥1 tryout this week

### My School tab
Always shown if user has school assigned:
- School rank globally + week-over-week change arrow
- Top 50 user in school (intra-school competition)
- Your personal rank in school

## Bimbel Leaderboard
- Same logic as school
- Min threshold: ≥5 active user (smaller than school)
- Top-10 avg mastery (or top-5 if member <10)
- Optional bimbel field at signup
- v1 user-add bimbel → admin moderate
- v2 B2B: bimbel admin claim listing + premium dashboard

### B2B Hook
Bimbel ranks #1 → "klaim listing bimbel ini, dapat dashboard monitoring siswa" CTA → email lead capture → sales follow-up.

This = B2B lead engine even before B2B product ships.

## Group Leaderboard (user-created)
- Create group → 6-char invite code → max 20 member
- Group leader (creator) can rename, kick, transfer leadership
- Same metric as school (top-10 avg mastery, but small group adjust to top-5 if member <10)
- Group name moderation: profanity filter + admin queue if flagged
- No chat (consistent with privacy-first philosophy)
- One user can join max 5 group

## Active User Definition (this week)
- Answered ≥30 battlefield question OR completed ≥1 tryout this week
- 30 = high enough to filter noise, low enough achievable in 1 day

## Leaderboard Pressure Mitigation (Q23)
- Dashboard widget highlights **personal progress** (mastery WoW +5%) BEFORE leaderboard rank
- Leaderboard tab not on main dashboard — separate page, 1 click away
- Rank decline notification: opt-in only, default off
- "Kamu naik X rank" notify yes (positive only push)
- "Kamu turun X rank" → no push, only visible if user clicks leaderboard

## Privacy
- Default display: username (not real name) + grade + school initial
- User can opt show full name in setting (off default)
- School page shows aggregate, individual user only via opt-in
- PDP Law: student can request removal anytime (7 day SLA delete)

## Metric Source Weights
- **Battlefield**: 60% weight (volume engagement)
- **Tryout**: 40% weight (high-stakes assessment)
- **Lesson**: 0% (lesson zero effect on mastery — locked)

Mastery snapshot Sunday 23:59 → ranking computed.

## Anti-Fake & Abuse
- New school added → 14-day "pending" before counted
- ≥10 active user before school appears in main leaderboard
- Manual flag + audit on suspicious rank surge (>50 rank/week jump)
- Account age ≥7 day to count toward school metric
- Multi-account detection via fingerprint + phone uniqueness (see `14-security.md`)

## Prizes / Motivation v1
- Bragging rights + badge ("Top 10 School Week 23")
- School page public, shareable URL → social viral
- Top school user gets cosmetic profile flair next week
- No monetary prize v1 (operational headache)
- v2: sponsored prize (bimbel/PTN as sponsor)

## Hall of Fame Archive
- Weekly archived snapshot
- Public page: historical winners
- "Top Sniper Bulan Ini" mention for trusted erratum reporter (Q18)

## Dashboard Integration
- Main dashboard widget: "Sekolah kamu peringkat #X minggu ini" + WoW arrow → click → leaderboard
- Profile page: school badge + bimbel badge visible
- Share button: "SMA-ku peringkat #5 di [platform], gabung sekarang [link]" → viral coefficient boost

## Sprint Final (D-30 UTBK)
4-week aggregate special leaderboard during UTBK pre-exam window.
- Cohort-specific (UTBK 2027 only)
- Highlights weekly top + cumulative
- Drives push toward exam day

## Cohort Auto-Tag
- Auto-tag user by `target_year_utbk` → "UTBK 2027 cohort"
- Dashboard widget: "12.482 pejuang UTBK 2027 aktif minggu ini"
- Cohort leaderboard tab as 5th leaderboard scope

## Tryout-Specific Leaderboard
See `05-tryout.md`. Per-event leaderboard, post-event, full ranking + percentile, all leaderboard scopes (global/school/bimbel/friend/group/cohort) overlay on event.
