# 09 — Monetization & Pricing

## Tier Structure (locked)
**Two tier only: Free + Pro.** No Boot Camp v1, no trial v1.

Single-paid-tier philosophy: clearer yes/no decision = higher conversion. Multi-tier confuses.

## Tier 1 — Free
Cost: Rp 0

### Free includes
- All 7 subtest accessible (lesson access)
- **Linear hard gate**: lesson 1→2→3→4 sequential, phase A→B→C sequential per lesson
- 10 question/day battlefield
- 1 tryout/month entry
- 5 message **lifetime trial** AI sidebar (not per day, lifetime total)
- Profile + radar chart (mastery + raw count)
- Daily streak + freeze (2/month earned)
- School/bimbel/group/cohort leaderboard view (read-only)
- Diagnostic at signup
- Public profile URL `/u/{username}`
- Friend system + share card
- Tryout token receive

### Free EXCLUDES
- Leaderboard active rank participation (no, free user does compete on leaderboard)
- Wait — correction: free user appears on leaderboard, just can't view full top 100
- Worked solution post-question (battlefield + tryout review)
- Review Pile flow
- Recommendation engine surface (limited)
- AI sidebar daily quota
- Lesson free-roam (locked behind linear gate)
- Unlimited streak freeze
- Premium tryout

## Tier 2 — Pro

### Pricing
| Period | Price | Per-month equiv | Save |
|---|---|---|---|
| Monthly | Rp 79.000 | Rp 79.000 | — |
| Quarterly | Rp 199.000 / 3mo | Rp 66.333 | 16% |
| **Semester (HERO)** | **Rp 349.000 / 6mo** | **Rp 58.166** | **26%** |
| Annual | Rp 599.000 / yr | Rp 49.916 | 37% |

### Hero offer
**Semester (Rp 349.000 / 6mo)** = primary push.

Reason: UTBK is time-bounded — kid prep Aug → exam Apr-May. Semester pack matches actual timeline + biggest perceived savings + locks revenue.

Annual = for kelas 11 starting early.

### Pro includes
Everything in Free, plus:
- All lesson **free-roam**, all phase unlocked
- Battlefield **unlimited**
- Tryout **unlimited entry**
- AI sidebar **50 message/day** soft cap (unlimited fair-use)
- Leaderboard **full top 100 view** + position tracking
- Worked solution **+ review pile + recommendation engine**
- Tryout post-event review + worked solution
- Cosmetic gold variant badge
- Early access to new BAB content
- Priority support response

### Pro hard rate limit
AI sidebar 10 message/min/user (regardless of plan, anti-abuse).

## Per-Event Tryout (Non-Subscriber)
**Rp 35.000/event** for one-time access without subscription.

- Includes: leaderboard + review for that single event
- Drives top-of-funnel capture for big national tryout marketing event
- Non-paying user joins event → sees leaderboard locked + worked solution locked → friction-driven upgrade

### Premium Proctored (v2 only)
- Rp 75.000-100.000/event
- Webcam proctor + ID verification
- Credible leaderboard for serious aspirant
- 6mo+ post-launch

## Referral Program

### Mechanic
Refer friend → both get **14 day Pro extension**.

### Anti-fraud
- Same fingerprint refer chain → void both side
- Referee must complete diagnostic + 7 day active before referral bonus apply (forces real engagement)
- Referrer rate limit: max 10 referral/month rewarded
- Audit trail: log fingerprint + IP + signup pattern

## NO Trial
**Skip free trial v1.** Free tier already generous (full lesson content, sample features). Trial add complexity.

If data shows demand: add 7-day Pro trial in v2.

## NO Student Discount
Skip — whole product is for student, no leverage.

## NO Boot Camp v1
Skip — premium upsell can be added v2 if user demand validated.

## B2B Tier (much later)
- Rp 25rb/student/mo with admin dashboard
- Min 50 student
- Targeted at bimbel + sekolah
- v3+ priority, after PMF + B2B sales process

## Cancellation & Refund
- **Cancel anytime**, prorate not refunded
- **Refund only if**: technical issue + within 7 day → support manual review
- Cooling-off period per UUPK Indonesia: 7 day refund right honored
- Per-event tryout: no refund after event starts

## Payment Failure & Grace
- 3-day grace period after failed renewal
- Account stays Pro during grace
- Day 3 → auto-downgrade to Free
- Retry payment: notification email + WA
- Account data preserved (no data loss on downgrade, just feature gating)

## Payment Method Support
Indonesia-specific via Xendit (primary):
- QRIS (covers GoPay, OVO, DANA, LinkAja, ShopeePay)
- Virtual Account (BCA, BNI, BRI, Mandiri, Permata)
- Credit card (3DS mandatory)
- E-wallet direct (GoPay, OVO, DANA)
- Convenience store (Alfamart, Indomaret)

Fallback: Midtrans

International / Stripe: skip v1.

## Tax & Invoicing
- PPN 11% if PKP threshold (revenue >4.8M IDR/yr) — applies once revenue scale up
- Tax invoice for B2B + on-request individual
- Withholding for ghostwriter freelance: PPh 21 / 23

## Chargeback Policy
- Auto-suspend account on chargeback dispute
- Manual review with Xendit fraud score
- Permanent ban if confirmed fraud
- Refund issued only if legit issue (per refund policy)

## Conversion Funnel KPI
- Visit → Signup: 5%
- Signup → Activated: 60%
- Activated → Engaged: 40%
- **Engaged → Paid: 10%** (aspirational, with semester hero)
- Paid → Retained (week 4): 70%
- 60d → Champion (referrer): 5%

## Pricing Test Plan v2
A/B test post-launch:
- Price point sensitivity (79rb vs 89rb vs 69rb monthly)
- Hero offer framing (semester vs annual primary push)
- Free tier quota (10 q/day vs 5 q/day vs 20 q/day)

## Anti-Account-Sharing
- Max 3 active device per Pro account
- 5th login → kicks oldest device
- Simultaneous session different city (IP geo) → email alert + require re-auth
- Hard ban only if abuse extreme (10+ device + 5+ city)

Family case considered mild, don't over-react.

## Free Tier Strategy Reasoning
Free tier deliberately generous on lesson access (full content, just slower via linear gate). 

Reasoning:
- Lesson = SEO + word-of-mouth + class-of-friends-tell-friends
- Battlefield + tryout + AI = where conversion happens (active grind = reveals need for unlimited)

## Revenue Math (rough)
ARPU v1 avg: ~70rb/mo (mix of 79rb monthly + 58rb semester equivalent + 50rb annual equivalent + per-event amortized)

Break-even monthly burn estimate Phase 3+: 250-400jt/mo small team + infra + content.

Break-even paid user count: 350-600rb paid user.
Total user (assume 5% conversion): 7k-12k user.

Feasible by UTBK 2027 (Apr-May) with referral + school leaderboard viral.
