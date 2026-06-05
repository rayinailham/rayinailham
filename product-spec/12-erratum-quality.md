# 12 — Erratum & Quality Feedback Flywheel

## Concept
User-driven QA. Real users spot wrong answers, ambiguity, AI hallucination. Without report flow + fix loop → trust dies. Embrace user reports as free QA labor at scale.

**Public errata changelog = trust signal moat.** Competitor hides errors; we publish weekly fix log.

## Report Channel

### Per-question report
Button per question (battlefield + tryout review + lesson challenge): "laporkan soal" icon corner.

### Per AI message report
Button per AI message: "👍 / 👎 / laporkan".

### In-app inbox
"Laporanku" tab shows user's report status (pending / verified / rejected with reason).

### NOT used
- No email
- No external form
- Single channel consolidation

## Report Categories (per question)
- Kunci jawaban salah (most common)
- Soal ambigu / pertanyaan tidak jelas
- Typo / format error
- Opsi jawaban salah (e.g. duplicate option)
- Tagging salah (BAB / subtest / difficulty)
- Lain-lain (free text)

Free text field optional, max 500 char.

## Report Categories (per AI message)
- Jawaban salah faktual
- Tidak menjawab pertanyaan
- Sumber kutipan tidak sesuai
- Bahasa terlalu sulit / mudah
- Lain-lain free text

## Handling SLA
- **Acknowledge**: instant ("laporan diterima, kami review dalam 72 jam")
- **Triage**: 72 hour to first verdict (verified / rejected / needs more info)
- **Fix**: 7 day to deploy correction if verified
- **Response to reporter**: in-app inbox notification with verdict + reason
- **Emergency** (during tryout event): 1 hour SLA, dedicated mod on duty

## Incentive Structure

### Verified report rewards (no cash)
- **Question report verified** (kunci salah / typo): +5 mastery point in relevant BAB + badge "Sniper Soal"
- **AI feedback verified**: +1 mastery point + badge "AI Helper"
- **Rejected report**: no penalty, polite explanation

### Sniper Soal Badge Tiers
- Tier 1: 1 verified report
- Tier 2: 5 verified reports
- Tier 3: 25 verified reports
- Tier 4: 100 verified reports

Cash bounty = abuse magnet, not v1.

## Mass-Report Detection
- Same question_id → 5+ report in 24h → auto-flag priority queue for content team
- Same question_id → 10+ report → auto-suspend question (don't serve until reviewed)
- Pattern detect: question accuracy <60% → auto-flag for review (likely kunci salah)

## Versioning

### Question schema
- `id` + `version` + `status` (active / suspended / retired)
- On fix: increment version, old responses linked to old version

### Mastery recompute logic on fix
| Fix type | Action |
|---|---|
| Kunci changed | Re-grade all past response → adjust user Elo retroactively |
| Soal retired (ambiguous) | Annul all response (no Elo impact) + refund 1 mastery point each affected user |
| Typo only | No recompute, soft patch |
| Opsi error | Re-grade if option correctness changed |
| Tagging error | No mastery impact, just metadata fix |

## Tryout In-Progress Erratum
- Question suspended mid-event → award full credit to all peserta who reached question + skip instead of replace
- Emergency in-event banner: "soal X dihapus karena error"
- 1-hour SLA for content moderator on duty

## Tryout Post-Event Correction
- Re-grade all affected peserta
- Leaderboard re-rank
- Email + in-app notify all peserta
- Announce: "leaderboard tryout [event] diperbarui karena perbaikan soal X"

## Communication Strategy

### Silent patch
- Typo fixes only
- No announcement

### In-app banner notification
- Kunci change: "soal X di BAB Y telah diperbaiki, mastery kamu disesuaikan"
- Affected user only

### Email notification
- Tryout retroactive correction: "leaderboard tryout [event] diperbarui karena perbaikan soal X"
- All peserta of that event

### Public Errata & Update Page
**Weekly transparency changelog**:
- "Minggu 23: 12 soal diperbaiki (8 kunci, 3 typo, 1 retire), 4 BAB diperbarui, 2 lesson revisi"
- Public URL, indexable
- Inspired by: Anthropic safety reports, Notion changelog

**Rationale**: turn errata from weakness into strength signal ("kami serius soal kualitas, transparan").

## AI Response Feedback

### Thumbs up
- Log positive
- No action

### Thumbs down
- Require category select
- Optional free text
- High-volume on same query pattern → trigger eval team review → update RAG corpus chunk OR adjust system prompt

### Top 50 thumbs-down weekly
Manual review queue.

## Internal Triage Queue

### Roles
- 1 dedicated content moderator
- Content team rotation backup
- Lead editor sign-off for kunci change (avoid wrong-fix cascade)

### Tooling (deferred)
Admin dashboard with:
- Report queue sorted by priority (mass-report first)
- Action button: verify / reject / escalate
- Bulk action support
- Audit log per change

## Question Retire vs Fix Decision Tree
- **Typo + opsi error + tagging error**: fix in place
- **Kunci salah**: fix in place + retroactive recompute
- **Soal ambigu** (≥3 expert reviewer disagree): retire + backfill replacement question same BAB difficulty
- **Never silently delete**: audit log + version history mandatory

## Eval Feedback Loop (the flywheel)
1. User report → tagged into eval set
2. Eval set growth: target +50 entry/week from real user signal
3. Quarterly: re-run eval suite → measure improvement → publish in transparency page
4. Improvement compounds over time

This is the moat — user report = free QA labor. Embrace not fight.

## Anti-Abuse

### Rate limit
- Max 10 report/user/day

### Quality score per user
- `false_report_count / total_report`
- <30% accuracy → throttle (max 3/day) + warning
- <10% accuracy over 5+ report → ban from report system

### Manual override
Lead editor can whitelist serial-correct reporter as "trusted" → priority queue.

## Trusted Reporter Tier
Power user who reliably catches errors = free QA labor + community asset.

### Public recognition (with permission)
- "Top Sniper Bulan Ini" mention on errata changelog page
- Profile flair: "Trusted Reporter" badge
- Builds community + incentive without cash

## Question Version History Table
```
question_version_history:
  question_id, version, change_type (kunci/typo/option/tag/retire),
  old_payload_json, new_payload_json,
  changed_by, changed_at, reason
```

## Audit Trail Mandatory
- Any content team change logged
- Who + when + what + before/after
- Lead editor approval required for kunci changes
- Cannot delete history (immutable log)

## Expected Volume (rough)
- 1000 question grind/day average user → ~5-10 wrong-flag/day per active user
- ~1% of those = legit errors
- ~10-20 legit errata reports/day at 1k WAU
- Scales linearly with user count

## Trust Position
Public stance: "Kami pakai analisis pola untuk fairness leaderboard. Kami publish errata mingguan. Kami serius soal kualitas."

Counter-intuitive flex: transparency = trust = retention = referral.
