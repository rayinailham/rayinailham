# 10 — Retention, Streak & Anti-Burnout

## Retention Engine Stack
1. Daily streak (Duolingo-style, softened)
2. Notification system (email + push + in-app)
3. Comeback ladder (3 / 7 / 14 / 30 day inactive)
4. Exam D-day countdown widget
5. Anti-burnout safeguards
6. Weekly mood check
7. Leaderboard pressure mitigation

## Streak System

### Trigger
Open AND complete ≥1 phase (battlefield ≥10 q OR lesson phase complete OR tryout participation) = streak day count.

### Visual
Flame icon with current count. "Streak: 47 hari".

### Display
- Current streak: dashboard prominent
- **Longest streak: PRIVATE (profile self-view only)**, NOT public on profile
  - Reason: comparison fuel = anxiety, removed from public display

### Streak Freeze
Earned: 1 freeze every 7 day streak. Stack max 2.
- Free user: 2 freeze/month total cap
- Pro user: auto-freeze always-on (never manually deploy)

Use: skip 1 day, streak preserved. Auto-deploys at midnight if available + streak ≥3.

### Rest Day Built-In
**1 day/week chosen by user (e.g. Sabtu) doesn't break streak even with zero activity.**

Framing: "Hari istirahat — kamu butuh recharge."

User selects rest day in settings, can change weekly.

### Streak Warmup (Battlefield)
First 5 question of session → wrong does NOT break streak.

### Streak Break Message — Reframed
NOT: "Kamu gagal."
INSTEAD: "Streak reset — yuk mulai lagi besok."

### Streak Milestone
Notification at 7 / 14 / 30 / 60 / 100 day. Badge earned per milestone.

## Notification System

### Channels
- **Email** (primary, Resend) — transactional + light marketing
- **Web Push** (PWA opt-in for desktop, browser support varies)
- **In-app inbox** (always on, source of truth)
- **WhatsApp** = v2+ only (cost + WA Business API approval 2-4 week)
- **SMS** = skip entirely

### Opt-in Model
- Email: opted-in by default at signup (transactional + soft marketing legal in Indonesia under UU ITE if disclosed in T&C)
- Web push: prompt after first lesson complete (high-intent moment, not spam-prompt at signup)
- In-app inbox: always on

### Notification Catalog

#### Transactional (always on, no opt-out)
- Signup confirmation
- Parent consent confirmation (minor)
- Payment success/fail
- Subscription renewal D-3
- Tryout registration confirm + token + reminder D-1 + start time
- Password reset

#### Engagement (opt-out)
- Streak danger (8 PM if today no activity yet, only if streak ≥3)
- Streak milestone (7/14/30/60/100 day reached)
- Daily reminder at user-chosen slot (pagi/siang/malam)
- New badge earned
- Friend overtake leaderboard (v2 once friend activity ship)
- New BAB content drop
- Tryout event upcoming (D-7, D-1, D-day)
- Exam countdown (D-100, D-50, D-30, D-14, D-7, D-3, D-1)

#### Comeback (opt-out, throttled)
- 3-day inactive → "kangen — ada [N] soal baru di [weakest BAB]"
- 7-day inactive → "udah seminggu, target [target PTN] masih nunggu"
- 14-day inactive → "exam D-[N], yuk lanjut dari [last lesson]"
- 30-day inactive → final email + auto-pause subscription billing

### Timing
- Daily reminder: user-chosen slot (pagi 7AM / siang 1PM / malam 7PM), single timezone WIB v1
- Streak danger: 8PM if no activity today + streak ≥3
- Exam countdown: 7AM on milestone day
- Tryout reminder: D-1 at 7PM, D-day 30min before start
- Smart-time per-user: v2 (need behavioral data)

### Frequency Cap
- Max 1 engagement push/day + 1 email/day
- Transactional unlimited
- Comeback throttled: max 4 in 30 day inactive run

### Preference Center
- Granular per-category toggle
- Single-click "matikan semua engagement" mute
- Transactional always on (T&C disclosed)

### Email Provider
**Resend** — $20/mo for 50k email, deliverability handled, 5min setup.

Don't build own email server. SPF/DKIM/DMARC + IP reputation = ops nightmare. Use managed.

## Comeback Ladder
- 3-day → "kangen" + weakest BAB nudge
- 7-day → "target masih nunggu" + last activity recap
- 14-day → "exam D-[N]" + lesson resume CTA
- 30-day → final email + auto-pause Pro billing (ethical, don't charge ghost)

## Exam D-Day Countdown

### Persistent UI Widget
"UTBK D-127" with progress bar. Dashboard top.

### Tone Shift Per Stage
- **D-100+**: "Masih panjang. Bangun fondasi konsep."
- **D-50 to D-30**: "Sprint terstruktur. Fokus BAB lemah."
- **D-30 to D-7**: "Konsolidasi. Latihan tryout penuh."
- **D-7 to D-0**: "Persiapan mental + tidur cukup. Kamu udah usaha keras."
- **UTBK day**: app banner "semangat pejuang. yang udah dipersiapkan, tinggal jalankan." + temporary feature pause (no battlefield available during exam hour)

### Opt-out Toggle
User can hide widget if anxious. Settings option.

## Anti-Burnout Safeguards

### Session Length Awareness
- 25 / 50 / 100 question prompt: "istirahat dulu?"
- 90 min continuous in battlefield → modal: "udah 1.5 jam, istirahat 10 menit?"
- 3 hour: stronger modal + auto-pause Elo for next 30min if continue
- Never hard force, always allow override

### Mastery Framing — Growth Not Deficit
- Replace "kamu lemah di X" with "fokus berikutnya: X"
- Profile radar: "ruang berkembang" overlay (gap to 100), not "kekurangan"
- Weakest BAB highlighted as "next opportunity" not red alarm
- Copy audit: every mastery-string reviewed deficit→growth framing

### Target Score Reality Check
- Onboarding: user sets target → no judgment, accept any
- Every 4 week: dashboard widget "Rencana Sprint" shows realistic projection
- "Kalau lanjut pace ini, prediksi UTBK kamu: 580. Target kamu 700. Mau adjust target atau tambah jam?"
- Allow target adjust anytime, no penalty

### Comparison Toxicity Mitigation
- Friend mastery NOT shown by default on friend profile
- Friend can opt show, viewer can also opt hide all friend mastery
- Leaderboard shows username + school + rank only (no granular mastery per user)
- Aggregate fine, individual granular = toxic

### Night Grind Detection
If user activity >50% logs between 11PM-3AM consistently 7+ day:
- Soft notification next morning: "tidur cukup juga bagian belajar — coba mulai earlier?"
- No force, no penalty, just gentle awareness
- Single light nudge then stop (respect autonomy)

### Failure Recovery (post-tryout low score)
Dashboard intercept after low tryout (<percentile 30):
- "Score belum sesuai harapan? Wajar — tryout = latihan menemukan gap. Let's break down hasil kamu."
- Guided flow: review wrong answer, identify weak BAB, suggest 3-day mini sprint plan
- Prevent freeze: don't show big red "skor rendah" — show breakdown + actionable next step
- Email follow-up (Pro user): tutor team note (template) "hai, lihat hasil tryout kamu — yuk diskusi rencana"

### Recovery Sunday (optional feature)
Pick subject → light review only mode (no Elo update, just re-read worked solution) → counts toward streak as active.

### Mindfulness / Meditation
Skip in-app v1.
Alternative: link to free resource on dashboard wellness card:
- Riliv app
- Bantu Mental
- Kemenkes BicaraDiri

Don't pretend to be wellness app.

## Weekly Mood Check
**1x/week (Senin pagi) modal**: "Minggu ini gimana? [great / oke / struggling]"

If "struggling" → gentle: "wajar. UTBK marathon, bukan sprint. Mau pause 1 hari? Freeze streak otomatis aktif."

Aggregate data → product team see cohort mood week-over-week (anonymized).

Tier 3 distress signal (Q17) → triggered separately via AI sidebar mental health protocol.

## Parent Dashboard (v2-3, deferred)
Parent of minor sees:
- Weekly summary of activity + mastery trend + tryout result

DO NOT show:
- AI conversation
- Individual question detail
- Daily granular activity (privacy + parent over-pressure)

Parent gets anxious-too-much email if not designed careful.

## Cohort-Based Blast (admin)
- Send segmented blast (e.g. "all kelas 12 active 7d")
- Rate-limit: 1 blast/week max, manual approval per blast
- Use case: tryout event, content drop, urgent UTBK info

## In-App Inbox
- Postgres table + Realtime channel
- Per-user notification log (cap 30 day) for debug + dedup
- "Laporanku" tab (erratum reports status)
- "Aktivitasmu" tab (badges, streak, leaderboard updates)
