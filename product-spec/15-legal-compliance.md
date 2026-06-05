# 15 — Legal & Compliance

## Business Entity

### v1 (pre-revenue beta)
Operate as informal team, no entity yet OK if just testing.

### v2 (pre-launch)
Register PT (Perseroan Terbatas):
- Standard PT: min 2 founder
- PT Perorangan (since 2021): cheaper if solo
- Cost: ~5-15jt one-time via OSS / notaris
- Register before first revenue collection (month-3 latest)
- Bank account, NPWP, VAT registration follow

### v3 (raise foreign capital)
Convert to PT PMA — much later, ignore now.

## PDP Law (UU 27/2022) Compliance
Effective Oct 17 2024. Full enforcement ongoing 2025-2026.

### Must-do v1
- Publish privacy policy covering: data collected, purpose, legal basis, retention, sharing, user rights
- Explicit consent at signup (separate checkbox for marketing)
- Parent consent for <17 (UU 27 + UU 35/2014 child protection)
- Data subject rights handling (access / correct / delete / portability / withdraw consent) → SLA 7 day
- Data breach notification: 72 hour to user + KemKominfo
- Data minimization audit quarterly: store only what's needed

### Defer v2 (scale)
- DPO (Data Protection Officer) appointment — pragmatic: founder self-appoint v1, external consultant DPO from public launch
- DPIA (Data Protection Impact Assessment) for AI tutor + leaderboard
- Register as **Penyelenggara Sistem Elektronik (PSE) Privat** with KemKominfo before public launch — MANDATORY for ALL platform serving Indonesia user

## Terms of Service / T&C
Must publish. Cover:
- Service description
- Eligibility (16+ or with parent consent)
- Account responsibility
- Payment + subscription terms
- Refund policy (per UUPK + product policy §09)
- Intellectual property (your content, user-generated content license)
- Prohibited use (no scrape, no resell, no cheat)
- AI tutor disclaimer (§06)
- Warranty disclaimer + liability limit
- Dispute resolution: BANI arbitrasi or pengadilan negeri Jakarta
- Governing law: Republik Indonesia
- Modification policy

Budget: lawyer template + customization 5-15jt one-time.
**Avoid free generator** (hallucinate legal).

## Privacy Policy
Cover all PDP Law required elements (above) +
- Cookie policy
- Third-party data sharing list (Xendit, Resend, OpenRouter, Posthog, Sentry, Cloudflare, etc) with purpose
- Data retention table per data type
- Transfer outside Indonesia disclosure (vendor abroad)

Budget: bundle with T&C, 5-15jt one-time.

## Child Consent Mechanism

### Flow
1. Signup detect DOB <17 → block until parent consent
2. Enter parent email → parent receives link with summary
3. Parent click confirm → account active

### Audit log
Parent email + IP + timestamp stored.

### Revocation
Parent can revoke anytime via email or dashboard (v2 parent dashboard).

### NOT v1
Skip parent ID upload (too friction, email link standard for COPPA-equivalent compliance).

## Payment Regulation
- Xendit / Midtrans license aggregator (no separate BI/OJK license needed)
- Sub-merchant onboarding via Xendit handles KYC + AML
- Subscription disclosure mandatory (UUPK + Permendag): amount, period, renewal, cancel mechanism
- Receipt + tax invoice obligation if PKP (PPN-payer)

## Content Licensing

### Ghostwriter IP assignment
- Make-for-hire Indonesia recognized via UU Hak Cipta
- Template: works made for hire, IP belongs to company
- Non-compete: 6 month, narrow scope
- Indonesia legal: weaker enforcement than US, check with lawyer

### YouTube embed
- Standard YouTube ToS allows embed via official iframe (not download/re-host)
- Track creator + log embed ID

### Past UTBK question (A1 from §01)
- SNPMB releases public, fair-use/educational defensible
- Cite source

### Third-party media
- Photo: Unsplash + Pexels (free commercial)
- Lyrics / quotes: license proper before use

## Trademark

### Filing
- DJKI Indonesia: pdki-indonesia.dgip.go.id
- File **Class 41** (education service) + **Class 9** (downloadable software) + **Class 42** (SaaS)
- Cost: ~3-5jt per class
- 6-12mo process — file early

### Strategy
- File as soon as final name decided pre-launch
- Placeholder name "Tempa" working — confirm before final filing
- Domain reservation (cendika.id, lumina.id, wira.id, tempa.id) parallel to trademark check

### Pre-filing check
1. Domain check (.id + .co.id + .com)
2. AHU/DJKI trademark check kelas 41
3. IG/TikTok handle availability
4. Global Google check (avoid TM cease-and-desist from foreign EdTech)

## Tax

### Corporate (PT)
- PPh badan 22% on net profit

### VAT (PPN)
- 11%, PKP threshold 4.8M IDR/yr revenue
- Above threshold: charge VAT on subscription

### Withholding
- Ghostwriter freelance: PPh 21 / 23 depending contract type

### Bookkeeping
- Mandatory from PT registration
- Hire bookkeeper / accounting firm month-1 of revenue (~3-5jt/mo retainer)

## Consumer Protection (UUPK)
- Clear disclosure: features, price, limit, cancel mechanism
- Cooling-off / refund: 7 day refund per §09 policy = compliant
- Complaint handling: max 7 day response (recommended SLA)
- Prohibition: misleading claim, false testimonial, hidden fee

## Education Accreditation
- "Platform persiapan ujian" generally NOT subject to Kemdikbud accreditation (you're not awarding diploma/ijazah)
- If expand to "kursus berakreditasi" v2-3 → reconsider
- No formal permit needed v1
- Clear disclaimer: "kami platform persiapan, bukan lembaga pendidikan formal"

## AI Ethics / Regulation

### Current
- SE MenKominfo No 9/2023 AI ethics guideline (non-binding but referenced)
- Principles: human-centered, transparency, accountability, safety, privacy
- §06 AI guardrail = aligns

### Future
- Indonesia AI Bill (in progress 2025-2026) — prepare to comply
- Disclosure mandatory: "konten ini dibantu AI" tag for AI output (already §06)

## Data Localization
- PSE Privat strategis classification = data localization required
- EdTech with minor user = arguably strategic
- **Prudent**: primary DB in Indonesia (Supabase Singapore region nearest, alternatively self-host AWS Jakarta region)
- Vendor abroad (LLM API, email, analytics) = disclose + contractual safeguard
- Revisit when reach 100k user

## Incident Response Plan

### Written IR plan v1
- Who-call: founder, eng lead, legal advisor, PR
- Communication template: user notification, KemKominfo notification, public statement
- Timeline target: 72-hour notification per UU 27/2022

### Drill cadence
- Quarterly tabletop drill v2

### Insurance
- Cyber insurance v3 (when revenue >1B/yr)

## Defamation / UU ITE Risk

### Vector
User-generated content: bio, group name, report free-text — potential vector.

### Defense
- Moderation queue + report flow (§11 + §12)
- Takedown mechanism: clear contact + 24h SLA for clear violation
- UU ITE risk mainly with public broadcast — your platform private mostly, low risk if mod active

## Vendor Due Diligence (DPA mandatory)
All vendor handling user data must have **Data Processing Agreement** signed:
- Xendit (payment)
- Resend (email)
- Supabase (DB + auth)
- OpenRouter (LLM)
- Cloudflare (CDN + WAF)
- Posthog (analytics)
- Sentry (error monitoring)

Standard DPA available from each. Sign before launch.

Keep DPA log + renewal reminder.

## Legal Budget Summary
| Item | Cost (one-time / annual) |
|---|---|
| PT registration | 5-15jt one-time |
| T&C + Privacy Policy lawyer | 5-15jt one-time |
| DPA review | bundled with above |
| Trademark (3 class) | ~10-15jt one-time |
| Bookkeeper / accounting | 3-5jt/mo recurring (post-revenue) |
| Penetration test | 30-50jt/yr |
| External DPO consultant | 5-10jt/mo (v2+) |
| Lawyer retainer | 3-5jt/mo (v2+) |

**Total v1 legal setup: ~30-50jt one-time, amortize over 1 year manageable.**

## Critical Path Items
1. PT registration before first revenue
2. PSE registration before public launch (KemKominfo OSS)
3. Lawyer-reviewed T&C + Privacy Policy before public launch
4. Trademark filing day-1 of brand commit
5. Parent consent flow before any minor signup
6. DPA signed with all vendor before production
7. PDP audit checklist: explicit consent + retention + breach notification ready

## Founder Discipline
- Don't DIY T&C from template generator
- Don't operate post-revenue without PT
- Don't skip PSE registration (service can be blocked)
- Don't ignore breach notification SLA (legal exposure)
- Hire lawyer once, save 100× downside
