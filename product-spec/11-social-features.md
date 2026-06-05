# 11 — Social Features

## Scope (locked v1)
**Lean v1, expand v2.**

v1 ships: friend system, user-created group + group leaderboard, custom avatar, public profile URL, share card.

v1 SKIPS: DM, chat, post/feed, co-op battlefield, versus battlefield, mentor Q&A, watch party, achievement broadcast.

## Friend System

### Mechanic
- Add friend by **username search** OR **friend-code** (6-char unique per user)
- **Mutual confirm required** (no follower model — both sides accept)
- Max 100 friend (soft cap, prevent farming)

### Friend used for
- Friend-only leaderboard tab
- Profile visit
- Cohort filter (your friend + your school cohort)

### Not in v1
- DM / chat / message
- Friend activity notification feed (noise control)
- Friend overtake leaderboard push (v2)

## Public Profile

### URL
`/u/{username}` — public, indexable.

### Profile shows
- Username + display name (if opted public)
- School (if opted public)
- Grade
- Target PTN (if opted)
- **Mastery radar** (opt-in only, default OFF for privacy)
- **Raw count radar** (opt-in only, default OFF)
- Badge wall (collection of earned badge)
- Display badges (user picks 3 to feature)
- Streak count (current only, longest hidden private)
- Member since
- "Tambah teman" button (if logged in viewer + not already friend)

### Default privacy
- Most fields public
- Mastery radar opt-in (privacy-sensitive)

### Profile = SEO + Viral Surface
- Indexable URL → "siapa peringkat 1 UTBK [brand]" → google → land on profile → signup CTA
- Cheap to build, big SEO compound

### NOT on profile
- Comment / message / follow (not in v1)
- Email / phone / DOB (PDP)
- Activity timeline
- AI conversation history

## Custom Avatar

### Options
- Upload picture (max 2MB, square crop tool)
- Pick from **12 preset illustration** (consistent style with brand identity)

### Moderation
- Image upload → Cloudflare Image AI / Sightengine moderation
- Auto-flag NSFW + violent + face-mismatch
- User can report avatar via "laporkan profile"

## Bio (140 char text)
- Optional
- Profanity filter
- Admin queue if flagged

## Cohort Auto-Tag
- Auto-tag user by `target_year_utbk` → "UTBK 2027 cohort"
- Dashboard widget: "12.482 pejuang UTBK 2027 aktif minggu ini"
- Cohort leaderboard tab as 5th leaderboard scope (see `08-leaderboards.md`)

## Share Card (Viral Fuel)

### Concept
Server-side render PNG → user shares to IG / WA / TikTok / Twitter / X.

### Templates (5-10 designed by brand designer)
- "Aku Master Aljabar di [brand]" + radar chart preview
- "Streak ku 47 hari" + flame visual
- "Peringkat #3 di SMA-ku minggu ini" + school badge
- "Tryout score X percentile Y" + score card
- "Belajar [BAB] di [brand], yuk join" + topic visual
- "Sekolah-ku peringkat #5 minggu ini" + school flag visual
- "Aku udah jawab 425 soal Matematika" + raw count milestone
- "[Brand] Cohort UTBK 2027" + cohort visual
- Tryout Akbar event recap card
- Quarterly progress card

### Card Includes
- Subtle brand watermark
- QR code or short URL link to signup
- Referral code embedded → conversion track

### Share Triggers (in-app prompts)
- After badge earn → "share badge ini?"
- After streak milestone → "share streak kamu?"
- After tryout result → "share hasil tryout?"
- Post-leaderboard rank improvement → "share rank baru kamu?"
- Manual share button always available on profile

## Group System (user-created)

### Create Group
- Group leader (creator) sets:
  - Group name (profanity filter + admin queue if flagged)
  - Description (optional, 200 char)
  - Privacy: public discoverable / private invite-only
- Generates 6-char invite code

### Member Management
- Max 20 member
- Group leader can:
  - Rename group
  - Kick member
  - Transfer leadership
  - Delete group
- One user can join max 5 group

### Group Leaderboard
- Same metric as school (top-10 avg mastery)
- If member <10 → adjust to top-5 avg
- Internal-only (not on global leaderboard)
- Resets weekly Senin

### Group Features (v1 minimal)
- Member list with rank
- Group leaderboard
- Shared streak target (optional, group leader sets)
- Leader-only announcement (single message text, max 280 char)

### NOT in v1 group
- Real-time chat
- File sharing
- Voice / video call
- Group challenges (v2 maybe)

## SKIPPED Features (v1)

### DM / Chat (skip permanent or near-permanent)
Reason:
- UTBK kid age + privacy + grooming risk + mod cost = liability mountain
- Encourage external Discord / WA group where you're not liable

### Post / Feed (never)
- Too much moderation cost
- No clear value
- Reddit / TikTok already do this better

### Co-op Battlefield ("Sparring Mode") — v2
2-4 friend, same 3 BAB, race 20 question. Real-time sync via Realtime channel.

### Versus Battlefield (1v1) — v2
Matchmaking by Elo ±100. 10 question side-by-side timer. Daily 5 match limit free, 20 paid.

### Mentor / Alumni Q&A — v2-3
Paid feature, alumni PTN answer in 24h SLA. 50rb-100rb per question, alumni 70% revshare.

### Tryout Watch Party — v2
Post-event live stream solution discussion by tutor. Paid Pro feature, recorded for replay.

### Achievement Broadcast — v2
Opt-in only, throttled (max 1 friend notif/day). Friend got rare badge → small in-app notif, no push.

## Moderation Budget
- v1: 1 part-time moderator (4h/day) handles profile reports + bio/avatar abuse + erratum triage backup
- v2: 2-3 moderator full-time once chat / group ship

### Tools
- Built-in word filter (Indonesian profanity list maintained)
- Image moderation (Cloudflare Image AI / Sightengine)
- User report queue
- Admin dashboard with bulk action

## External Community Strategy
Encourage external Discord community (volunteer-led, free, deniable liability, organic).

Provide:
- Official Discord invite link in dashboard
- Volunteer mod recognition
- Channel suggestions (per subtest, per cohort)

Platform NOT liable for external chat content.

## Privacy & PDP Compliance
- All profile fields opt-in for public display (default off for sensitive: mastery, real name)
- Profile public removable on request (PDP "right to delete" → 7 day SLA)
- Username changeable once per 6 month
- Friend list PRIVATE, only user sees own list

## Friend Limit Reasoning
100 friend cap = prevent farming + keeps "friend" meaningful. Indonesia teen often has dozens of school friends → 100 enough headroom.

## Group Limit Reasoning
- 20 member per group: bimbel-class-sized, intimate
- 5 group per user: school + bimbel + cohort + study-circle + family enough
- More = noise + grouping for grouping sake
