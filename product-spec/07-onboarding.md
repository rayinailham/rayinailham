# 07 — Onboarding & Diagnostic

## Goal
First 5 min after signup determine retention. Capture compliance data + seed mastery + show value.

## Step 1 — Signup (30 sec)

### Auth options
- Email + password
- Google OAuth
- Phone OTP

### Required fields
- Email
- Name
- Grade (10 / 11 / 12)
- Target year UTBK (2027 / 2028 / 2029)
- DOB (full date for PDP compliance)

### Conditional required (PDP UU 27/2022)
If DOB <17:
- Parent email collected
- Parent consent flow triggered (see below)

### Required (Q15 — school leaderboard)
- **School** (select from preloaded DAPODIK list ~14k SMA + sederajat)
- "Sekolah saya tidak ada" → user-add → admin moderate queue before active on leaderboard
- School can be changed once per 6 month (anti-gaming)

### Optional fields
- School (above is required actually — moved to required)
- Target PTN (text array, e.g. "ITB", "UI", "UGM")
- Target jurusan (text)
- Target score (e.g. 600, 700+)
- Bimbel name (optional, user-add)
- Referral code field

## Parent Consent Flow (Minor Users)
1. Detect DOB <17 → block account activation
2. Enter parent email
3. System sends email link with summary of platform + data usage
4. Parent clicks confirm link
5. Account active
6. Audit log: parent email + IP + timestamp stored

Parent can revoke anytime via email or future parent dashboard.

Skip parent ID upload v1 (too friction, email link standard COPPA-equivalent).

## Step 2 — Goal Setting (30 sec)
- "Berapa hari/minggu mau belajar?" 1 / 3 / 5 / 7 day → daily streak target
- "Jam belajar tipikal?" pagi (7AM) / siang (1PM) / malam (7PM) → reminder timing
- "Target nilai UTBK?" 500 / 600 / 700+ → personalize tone

Skip-able with "atur nanti". Defaults: 3 day target, malam, 600.

Used in:
- Daily reminder timing
- Email greeting personalization ("12 hari menuju target ITB kamu")
- Streak target visualization

## Step 3 — Diagnostic (skippable but recommended, ~10 min)

### Framing
"Mau tau level kamu sekarang? 10 menit = mastery awal terisi"

Skip option: "Lewati — semua mastery mulai 0%, isi nanti via Battlefield"

### Format
- 5 question per subtest × 7 subtest = 35 question total
- Adaptive within subtest (CAT-lite):
  - Start medium (D=3)
  - Correct → next harder
  - Wrong → next easier
- Each subtest ~1.5 min, total ~10 min

### Post-Diagnostic
- Per-BAB Elo seeded from subtest avg + (optional self-rate fallback for granular BAB)
- Radar chart pre-filled
- Result page: "kamu kuat di X, lemah di Y, mulai di Y?"

### Future (v2)
- Full IRT-calibrated CAT once question bank IRT-calibrated
- Per-BAB granular diagnostic

### If skipped
- All BAB start default Elo 1000
- Mastery shows "belum cukup data — terus latihan" until 10 question per BAB answered

## Step 4 — Tour (30 sec, skippable)
3-tooltip walkthrough on dashboard:
1. "Ini Battlefield — latihan bebas, mastery naik di sini"
2. "Ini Lesson — belajar terstruktur, dapat badge"
3. "Ini Tryout — event terjadwal, simulasi UTBK asli"

Dismissible, never re-show after dismiss.

## Step 5 — First Action CTA
- If diagnostic taken → "Mulai dari [weakest BAB]" → Lesson direct
- If skipped → "Pilih subtest mau dipelajari dulu" → Lesson tree
- Persistent "Lewati ke dashboard" always available

## NOT Forced
- AI sidebar use (organic discovery — sidebar visible in lesson page, user click when curious)
- Profile photo (add later via gentle nudge)

## Conversion Target
- ~60-70% take diagnostic if framed well
- ~80%+ complete signup post diagnostic prompt
- D7 retention >25% baseline

## Diagnostic Length Tradeoff (locked)
**35 question — 10 min — full subtest coverage** (recommended).

Alternatives considered + rejected:
- 14 q (2 q/subtest) = less signal
- 1 subtest = no radar fill
- Skip entirely = cold-start problem

## PDP Consent Capture
At signup, explicit checkbox separate for:
1. Privacy Policy + T&C (required)
2. Data processing for AI tutor (required for product)
3. Marketing communication (optional, default unchecked)

Granular consent log stored. User can revoke anytime via setting.

## UTM + Referral Tracking
- UTM params from landing → store at signup
- Referral code at signup → bind referrer relationship
- Both feed marketing attribution + referral reward (Q11)

## Onboarding Conversion Funnel (KPI)
1. Visit landing → signup form: ~5%
2. Signup form → submit: ~70%
3. Submit → diagnostic complete: ~60-70%
4. Diagnostic complete → first lesson opened: ~80%
5. First lesson → week-2 active (engaged): ~40%

Activation defined: diagnostic complete OR ≥30 question answered week-1.

## Re-onboarding (returning user post-inactive)
If user inactive 30+ day → re-engage flow:
- Welcome back banner
- "Gimana kabar? Mau lihat progress kamu?" → dashboard
- Suggest "Mini Diagnostic" 5-min refresh diagnostic to recalibrate Elo

## Tech Notes (deferred)
- Auth: Supabase Auth (email + Google OAuth + phone OTP)
- DOB validation server-side
- Parent consent email via Resend
- Diagnostic question pool curated subset of main bank
