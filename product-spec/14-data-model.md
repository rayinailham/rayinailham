# 14 — Data Model & Key Entities

## Principle
- **Response log = source of truth**, everything else derived
- **Soft-delete user** (PDP "right to delete" → anonymize, keep aggregated)
- **Versioned content** (question + lesson) for retroactive integrity
- **Separate `tryout_response` from `response`** = in-event isolation
- **Append-only event log** for response → mastery recompute always possible
- **Partition response monthly** = scale + archive cheap

## Core Entities

### user
```
id, email, phone, oauth_provider, password_hash
name, username, dob, grade (10/11/12/lainnya)
target_year_utbk, school_id (FK), bimbel_id (FK nullable)
target_ptn (text array), target_jurusan (text), target_score (int)
preferred_study_time (pagi/siang/malam)
preferred_streak_target (1/3/5/7)
parent_email (nullable, encrypted), parent_consent_at (nullable)
pdp_consent_at, marketing_consent (bool)
display_name_public (bool, default false)
created_at, updated_at, last_active_at, deleted_at (soft)
```

### school
```
id, name, npsn (DAPODIK code), kabupaten, provinsi
type (SMA/MA/SMK), status (active/pending/rejected)
created_by_user_id (nullable, for user-added)
verified_at, created_at
```

### bimbel
```
id, name, kota, b2b_account_id (nullable, v2)
status (active/pending), created_at
```

### group (user-created, Q21)
```
id, name, description, invite_code (6-char unique)
leader_user_id (FK), privacy (public/private)
member_count, max_member (default 20)
created_at
```

### group_member
```
group_id, user_id, joined_at, role (member/leader)
```

### subtest
```
id, code, name, weight_in_score, sort_order
-- 7 fixed seed
```

### bab
```
id, subtest_id, code, name, sort_order
-- ~15/subtest
```

### lesson
```
id, bab_id, sort_order, title, content_markdown
video_url (nullable, curated YouTube)
estimated_minutes, version, created_at, updated_at
```

### question
```
id, version, status (active/suspended/retired)
bab_id, subtest_id, type (mcq/isian)
stem_markdown, options_json (for mcq)
answer_key, answer_normalized (for isian compare)
explanation_markdown
difficulty (1-5 manual), irt_difficulty (nullable v2)
source (uploaded/scraped/llm-draft-verified)
created_by, verified_by, created_at, retired_at
```

### question_version_history
```
question_id, version, change_type (kunci/typo/option/tag/retire)
old_payload_json, new_payload_json
changed_by, changed_at, reason
```

### user_bab_rating (Elo + mastery source of truth)
```
user_id, bab_id
elo_rating (default 1000)
question_answered_count, last_answered_at
mastery_display_cached (0-100, recompute on read or scheduled)
-- subtest mastery = derived view
```

### response (firehose, every answer logged)
```
id, user_id, question_id, question_version
context (battlefield/tryout/lesson_phase_a/b/c/diagnostic)
context_ref_id (session_id / tryout_id / lesson_id)
is_correct, answer_submitted, time_spent_ms
elo_before, elo_after, mastery_delta
tab_switch_count (anti-cheat signal)
created_at
-- partition monthly, archive >12mo to cold storage S3/R2
```

### battlefield_session
```
id, user_id, started_at, ended_at
selected_bab_ids (array of 1-3), question_count, correct_count
streak_max
```

### tryout_event
```
id, name, slug, scheduled_start, scheduled_end
duration_minutes_per_subtest, participant_cap
status (draft/upcoming/live/completed/archived)
scoring_method (weighted_raw_v1 / rasch_1pl / 2pl)
is_proctored (bool, v2)
price_idr (nullable, for non-subscriber per-event)
created_at
```

### tryout_participant
```
id, tryout_event_id, user_id, token (unique single-use)
registered_at, started_at, submitted_at
raw_score, scaled_score, percentile, rank_overall
status (registered/in_progress/submitted/disqualified)
```

### tryout_response (separate from response for in-event isolation)
```
id, tryout_participant_id, question_id, question_version
answer_submitted, is_correct, time_spent_ms, flagged_for_review
answered_at
```

### lesson_progress
```
user_id, lesson_id
phase_a_done_at, phase_b_done_at, phase_c_done_at
phase_b_score, phase_c_score
badge_earned (text array)
```

### ai_conversation
```
id, user_id, lesson_id (nullable, scope context)
started_at, ended_at, message_count
retained_until (created_at + 90 day)
```

### ai_message
```
id, conversation_id, role (user/assistant/system)
content, citations_json (RAG chunk ID array)
flag_category (nullable: factual_wrong/off_topic/safety)
user_feedback (nullable: up/down + category)
tokens_in, tokens_out, model_used, created_at
```

### streak
```
user_id, current_streak, longest_streak, last_active_date
freezes_available (max 2), freezes_used_total
rest_day_of_week (0-6, user-chosen)
```

### badge (catalog)
```
id, code, name, description, tier (1-4 if tiered), icon_url
```

### user_badge
```
user_id, badge_id, earned_at, context_ref (e.g. bab_id)
```

### notification
```
id, user_id, type (catalog from §10)
channel (email/push/inapp), payload_json
scheduled_at, sent_at, read_at, clicked_at
```

### report (erratum flow §12)
```
id, reporter_user_id, target_type (question/ai_message)
target_id, category, free_text
status (pending/verified/rejected)
triaged_by, resolution_action, resolved_at, created_at
```

### subscription
```
user_id, plan (free/pro)
tier_period (monthly/quarterly/semester/annual)
status (active/grace/cancelled/expired)
current_period_start, current_period_end
xendit_subscription_id, last_payment_at
```

### payment
```
id, user_id, subscription_id (nullable)
amount_idr, type (subscription/per_event_tryout)
ref_id (e.g. tryout_event_id for per-event)
xendit_payment_id, status (pending/paid/failed/refunded)
created_at, paid_at
```

### diagnostic_result
```
user_id, taken_at
per_subtest_score_json
initial_elo_seed_json (per_bab_id → rating)
```

### friend
```
user_id, friend_user_id, status (pending/accepted/blocked)
created_at, accepted_at
```

### admin_user
```
id, email, role (lead_editor/content_mod/support/super)
created_at
```

### content_audit_log
```
who, when, what (entity), action, before_json, after_json
-- mandatory for any content team change
```

### dapodik_school_seed
```
id, npsn, name, type, kabupaten, provinsi
last_synced_at
-- preloaded ~14k SMA + sederajat
```

### referral
```
id, referrer_user_id, referee_user_id
referral_code, redeemed_at
referee_activated_at (post 7-day active)
referrer_reward_at, referee_reward_at
status (pending/qualified/rewarded/voided)
```

### error_log_internal (admin)
```
event_id, type, severity, payload, created_at, resolved_at
```

## Materialization Strategy
- **v1**: compute mastery on read (live Elo from rating table) — simple, slower at scale
- **v2 (5k+ MAU)**: cache + scheduled refresh hourly — faster, slight stale
- **v3**: write-through cache on every answer — fastest, most code

Premature optimization rejected v1.

## AI Conversation Retention
Automated job to anonymize after 90 day expiry:
- Delete user_id reference
- Keep aggregated content for eval

## PDP Compliance Mapping
- Soft delete `deleted_at` on user → 30 day cooldown → hard purge with anonymization
- Right to delete: 7 day SLA from request
- Right to access: export user data as JSON
- Right to portability: data export endpoint
- Marketing consent separate field, default false
- Audit log on admin read of user record

## Index & Performance Notes (deferred to engineer)
- `response` partition by month
- Heavy index on `user_id, bab_id` for Elo lookup
- `question` partial index on `status='active'`
- Read replica for leaderboard query at scale

## Tech Notes (deferred)
- Postgres via Supabase
- pgvector for RAG embeddings
- pg_cron for scheduled job
- Drizzle ORM (TS-first)
- Realtime channel for tryout sync + leaderboard live update v2
