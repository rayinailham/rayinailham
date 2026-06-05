# 13 — Security & Anti-Abuse

## Threat Model (UTBK-Specific)

| Vector | Risk |
|---|---|
| Multi-account school leaderboard manipulation | High |
| Referral abuse (self-refer) | Medium |
| Account sharing (1 Pro = whole class) | Medium |
| AI sidebar trial bypass | Medium |
| Question bank scraping | Medium |
| Tryout collusion (Discord answer-share) | High during event |
| Brute force MCQ bot | Medium |
| Payment fraud / chargeback | Medium |
| Leaderboard bot grinding | Medium |
| Fake school registration | Low (caught by Q15 stack) |
| Prompt injection AI | Low (Q17 layered defense) |
| DDoS during tryout | High during event |
| Account takeover (phishing) | Medium |
| PII leak (parent email, DOB) | High legal |

## Identity Layer

### Required uniqueness
- Phone OR email required at signup
- Phone unique constraint (one account per phone)
- Email unique constraint
- Email domain blocklist: known throwaway (10minutemail, guerrillamail, mailinator, etc) — public maintained list

### Device fingerprint
- FingerprintJS Pro (paid ~$100/mo at scale) OR self-host community version
- Hash stored on user creation + login
- Track: same fingerprint creating multiple account → rate limit max 3 account/fingerprint/30day

## CAPTCHA
**Cloudflare Turnstile** (free, privacy-better than hCaptcha)

### Gates
- Signup
- Login (after 3 fail)
- Password reset
- Referral redeem
- Mass-report submit

### NOT gated
- Tryout entry (would slow critical path)

## Rate Limit (Redis sliding window)

| Endpoint | Limit |
|---|---|
| Signup | 3/IP/hour, 10/IP/day |
| Login | 5/account/15min, 20/IP/hour |
| Battlefield answer submit | 60/min/user |
| AI message | 10/min/user |
| Report submit | 10/user/day |
| Tryout answer | No per-Q limit (event flow), just timeout |
| Generic API | 1000/user/min safety net |

## Bot Detection (Battlefield)

### Signals
- Response time variance <200ms across 10+ q (humans variance high)
- Response time avg <500ms (read+answer impossible <500ms)
- Zero tab focus loss across 50+ q (human switches)
- Identical answer pattern across users (collusion)

### Action ladder
1. **First detect**: silent log, no Elo update for that session
2. **Repeat**: shadowban (user sees own rank inflate, leaderboard shows real)
3. **Confirmed**: ban + appeal email

## Referral Fraud Guard
- Same fingerprint refer chain → void both side
- Referee must complete diagnostic + 7 day active before referral bonus apply
- Referrer rate limit: max 10 referral/month rewarded
- Audit trail: log fingerprint + IP + signup pattern

## Account Sharing Detection
- Max 3 active device per Pro account
- 5th login → kicks oldest device
- Simultaneous session different city (IP geo) → email alert + require re-auth on suspicious device
- Hard ban only if abuse extreme (10+ device + 5+ city)
- Family case considered mild, don't over-react

## AI Free Trial Bypass Defense
- 5 lifetime free message bound to **fingerprint + phone** (not just user_id)
- Phone same → already used → no new trial
- Phone change but fingerprint same → suspicious, warn + still no trial
- New fingerprint + new phone = legit new user, allow
- Manual override: support team grant trial case by case

## Question Bank Protection
- Hashed question_id per session (signed token, expires) — scraper can't bookmark direct ID
- Response payload includes hidden user-watermark in metadata — bank leak traceable to source user
- WAF rule: anomaly fetch rate (>200 q/min from one user) → challenge CAPTCHA
- Cloudflare bot fight mode for `/api/question/*`
- Accept ~5% leak unavoidable (screenshot share). Don't fight losing battle, focus high-volume scraper.

## Tryout Collusion Detection

### Post-event analysis
- Same answer pattern (all 100 question identical) cluster detect via cosine similarity
- Tab-switch + paste-attempt log per peserta
- Response time pattern anomaly

### Action
- **Soft**: flag for review + freeze leaderboard rank pending
- **Hard**: disqualify + refund (if paid event) + ban from next 3 event

### Public stance
"Kami pakai analisis pola untuk fairness leaderboard." — deterrent value.

## Brute Force MCQ Defense
- Sub-second uniform response + 75%+ accuracy across difficulty 5 = bot signature
- Shadowban Elo update + don't count toward leaderboard + log
- Inform user via support email "kami detect anomali, mohon konfirmasi"

## Payment Fraud
- Xendit built-in fraud score (use it)
- 3DS mandatory for card
- Velocity: max 3 payment attempt/user/hour
- Chargeback: auto-suspend account + manual review + permanent ban if confirmed fraud
- High-value (>1jt single transaction) manual review queue before auto-fulfill (semester + annual)

## Leaderboard Bot Defense
- Headless browser detect: Cloudflare bot management (Pro plan) + JS challenge on suspicious user
- Server-side validation: Elo gain anomaly (e.g. 500 elo gain in 1 hour from rest baseline) → flag
- Session-based: must have legit referer + cookie + CSRF token + valid session token to count answer

## Fake School Defense (recap from Q15)
- 14-day pending + min 10 user threshold + admin queue
- Geo-cluster anomaly detect

## DDoS Protection

### Layers
- Cloudflare in front (free plan adequate v1, Pro $20/mo at scale)
- WAF custom rule
- Tryout entry queue: 5000 cap + waiting-room page if traffic spike
- DB connection pool limit + circuit breaker on heavy query
- Separate read replica for leaderboard query (v2 scale)

## Account Takeover

### 2FA
- Opt-in TOTP (Google Auth / Authy)
- Encourage during Pro upgrade flow

### Session security
- Email alert on new device login (with device + city + time)
- Session list in setting + "logout from all device"
- Force re-auth on suspicious device

### Password requirements
- Min 8 char
- Not in HIBP top 10k breached
- Force password reset if email appears in HIBP breach (haveibeenpwned API)

## PII Protection

### Encryption
- All PII encrypted at rest (Supabase default)
- Parent_email + phone field-level encrypt (extra layer for minor)

### Access control
- Access log: any admin read of user record logged with reason
- Quarterly access review: who has prod DB access, rotate credential

### Data minimization
- Store DOB year only if granular age not needed
- Cached `is_minor` boolean for permission check (don't query DOB repeatedly)

### Retention
- Soft delete: `deleted_at` field
- 30 day cooldown
- Hard purge with anonymization after cooldown
- Anonymize: strip user_id + PII, keep aggregated content for eval

## Operational Security (Founder Discipline)
- Secret management: never commit to repo, use Vercel env + Supabase Vault
- Admin panel: 2FA mandatory + IP allowlist for super admin
- Dependency audit: weekly Snyk / npm audit
- Penetration test: 1× before public launch, 1×/yr after — budget ~30-50jt
- Bug bounty: HackerOne starter or self-host page, ~5jt-50jt payout per report
- Incident response plan: who get called, communication template, timeline target (notify user within 72 hour per UU 27/2022)

## Friction-vs-Security Balance

### v1 strict
- Signup CAPTCHA
- Email verify only

### v2 escalate
- 2FA on Pro (when revenue start, justify friction)
- Device limit enforcement
- Mandatory 2FA for super-admin

### Never
- Over-friction free tier signup (PMF first)
- Captcha on every page (too aggressive)

## Privacy Disclosure (PDP Compliance)
Fingerprint use disclosed in privacy policy explicit:
- Framing: "device security" not "tracking"
- Purpose: account security, fraud prevention, multi-account detection
- Retention: per data type table

## False Positive Mitigation
**Always combine 3+ signal before action.** Bot detection false positive = legit fast student banned = bad UX.

Hierarchy:
- Shadowban > hardban (reversible if false positive)
- Email warning before action
- Appeal flow with human review

## Specific to UTBK Risk Stack
**Multi-account school leaderboard manipulation** = top risk to combat from day 1.

Mitigation stack:
1. Fingerprint
2. Phone unique
3. 14-day account age before count toward school
4. 7-day school assignment cooldown
5. Min 10 active user school threshold
6. Admin audit top-10 weekly
7. Geo-cluster anomaly

Without these → leaderboard becomes meaningless → social moat dies.

## Incident Response Plan (Outline)
- Written IR plan v1
- Who-call list (founder, eng lead, legal advisor, PR)
- Communication template (user notification, KemKominfo notification, public statement)
- Timeline target: 72-hour notification to user + KemKominfo per UU 27/2022
- Quarterly tabletop drill v2
- Cyber insurance v3 (when revenue >1B/yr)

## Vendor Due Diligence (DPA mandatory)
All vendor handling user data must have Data Processing Agreement signed:
- Xendit
- Resend
- Supabase
- OpenRouter
- Cloudflare
- Posthog
- Sentry

Keep DPA log.
