# Product Spec — Tempa (placeholder name)

UTBK/SNBT prep platform for grade 12 SMA. Adaptive learning + RAG AI tutor + ranked battlefield + scheduled tryout events.

**Tagline**: Fight Your Way to PTN.

## How to Read

Files numbered by domain. Read in order for full context, or jump to topic.

| # | File | Topic |
|---|---|---|
| 00 | `00-overview.md` | Brand, USP, positioning, tagline, visual direction |
| 01 | `01-scope-content.md` | Curriculum scope (7 subtest), video strategy, RAG corpus, question bank |
| 02 | `02-learning-section.md` | Lesson feature, 3-phase challenge, badge, free vs Pro gating |
| 03 | `03-battlefield.md` | Adaptive grind feature, BAB selection, streak, radar chart |
| 04 | `04-mastery-elo-system.md` | Elo formula, asymmetric K-factor, mastery cap, beginner protection |
| 05 | `05-tryout.md` | Scheduled event, token, anti-cheat, IRT scoring migration |
| 06 | `06-ai-tutor.md` | Sidebar guardrail, mental health protocol, citation mandatory |
| 07 | `07-onboarding.md` | Signup, parent consent, diagnostic CAT-lite, goal setting |
| 08 | `08-leaderboards.md` | School + bimbel + group + cohort + global leaderboard |
| 09 | `09-monetization.md` | Free + Pro tier, semester hero offer, referral, payment |
| 10 | `10-retention-burnout.md` | Streak system, notification, anti-burnout, weekly mood check |
| 11 | `11-social-features.md` | Friend, group, public profile, share card, scope discipline |
| 12 | `12-erratum-quality.md` | Report flow, version history, retroactive recompute, transparency changelog |
| 13 | `13-security.md` | Anti-abuse, fingerprint, rate limit, PII, DDoS |
| 14 | `14-data-model.md` | Entity schema, source-of-truth principle, materialization |
| 15 | `15-legal-compliance.md` | PT, PDP, PSE, T&C, trademark, vendor DPA |

## Feature Pillars
1. **Learning Section** — structured lesson + AI tutor sidebar (§02, §06)
2. **Battlefield** — adaptive grind, Elo, radar mastery (§03, §04)
3. **Tryout** — scheduled exam, leaderboard, percentile (§05)

## Locked Decisions Quick Reference

### Curriculum
- All 7 UTBK SNBT subtests at launch
- ~420 lesson + 5000 question seed

### Mastery
- Elo-based, asymmetric K-factor (gain easy, loss hard for newbie)
- Lesson does NOT affect mastery — battlefield + tryout only
- Hard cap mastery 100 per BAB

### AI Tutor
- 5 lifetime free message (Free), 50/day (Pro)
- Mandatory citation for RAG-grounded response
- Mental health 3-tier escalation, never pretend therapist

### Tryout
- 5000 cap per event
- Fixed start time, mirror real UTBK timing
- Accept-cheat freemium (no webcam v1)
- IRT migration after first event

### Pricing
- Free + Pro only (no trial v1)
- Hero: Semester Rp 349.000/6mo
- Per-event tryout Rp 35.000

### Social
- Friend (mutual confirm) + user-created group + public profile + share card
- NO chat / DM / feed v1
- School + bimbel + group + cohort + global leaderboard

### Onboarding
- 35 q diagnostic CAT-lite (skippable)
- Parent consent for <17 (PDP UU 27/2022)
- School field required (DAPODIK list)

### Compliance
- PT before revenue
- PSE registration before public launch
- 30-50jt legal budget v1
- Trademark filing day-1 of brand commit

### Anti-Burnout
- Streak softened: rest day, auto-freeze, growth framing
- Weekly mood check
- D-day countdown tone shifts per stage
- Night grind detection

## Deferred to Specialists
| Topic | Owner | When |
|---|---|---|
| Tech stack architecture | Engineer team | Post-spec lock |
| Tooling (CMS, admin, project mgmt) | Engineer team | Post-spec lock |
| Content production pipeline ops | Content lead | Phase 0 hire |
| Metric system & KPI dashboard | Analyst | Post-PMF |
| Roadmap & launch sequence | Product manager | Post-team formation |
| Founding team & capital | Founder | Now-ongoing |

## Specs NOT Covered (User Explicitly Skipped)
- Tech stack (frontend, backend, database, deploy) → engineer
- Tooling (CMS, project management) → tech team
- Roadmap phases & launch timing → product manager
- Metric system → analyst
- Founding team & capital → founder management

## Naming Status
- Working name: **Tempa** (forge yourself, academic + battle subtext)
- User candidate "Edufield" rejected: descriptive mark, weak trademark, likely collision
- Action: domain check + DJKI trademark check before commit

## Brand Direction
- Dark mode primary
- Deep navy + electric green/cyan accent + warm orange highlight
- Geist Sans / Inter UI, serif for editorial
- No mascot v1, wordmark-first logo
- Tone: tutor yang percaya + dukung kamu, kayak trainer untuk warrior — bakar semangat, tegas suportif
- Hero metaphor: athlete training, not soldier

## Critical Path to v1 Public Launch
1. Confirm brand name + trademark filing
2. Hire content lead + ghostwriter team (Phase 0)
3. Hire founding engineer (parallel)
4. Content production: 3 subtest priority (Penalaran Mat + Lit Inggris + Penalaran Umum)
5. PT + PSE + T&C + Privacy Policy
6. Closed beta 200 user
7. Tryout feature ship (defer if needed to v1.5)
8. Pro tier + payment infra
9. Public launch with Pro semester hero offer

(Actual phasing & timeline = product manager / founder decision, not in spec.)

## Decision Log Format
Each major decision in spec marked **(locked)** at point of definition. If revisit, update + add date + reason.

## Spec Update Discipline
When implementing:
- Discrepancy from spec → either update spec OR fix implementation
- Never let spec drift from reality
- New decision = add to relevant file with date

## Spec Owner
Product founder. Engineer / content / design teams reference, not edit without product approval.
