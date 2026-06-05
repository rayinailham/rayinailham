# 06 — AI Tutor Sidebar

## Concept
RAG-grounded conversational tutor. Master-level depth, SMA-level vocab. Embedded in lesson page sidebar.

## Position
Right sidebar of lesson page. Collapsible. Persistent across phase A/B/C within lesson.

## Tier Access
- **Free user**: 5 message **lifetime trial total** (not per day, lifetime)
- **Pro user**: 50 message/day soft cap (unlimited fair-use)
- **All user hard rate limit**: 10 message/min/user

5 lifetime trial bound to fingerprint + phone (not just user_id) — prevents account-burn bypass.

## Scope Lock — Strict Subject-Only

### Allowed
- UTBK subject material (corpus from Q4)
- Concept explanation, worked example, formula derivation
- Question hint (without giving full answer)
- Study strategy specific to UTBK

### Off-Topic Refusal Flow
- "Nulis essay buat aku" → refuse, redirect to lesson "Penalaran Menulis"
- "Code python" → refuse, "aku tutor UTBK, bukan IT"
- "Kpop / gosip / opini" → refuse polite redirect
- Exception: 1-2 turn small talk warmup OK ("halo!" → "halo, mau belajar apa?")

### Harmful Advice
- "Cara nyontek": refuse + reframe ("kamu pasti bisa kalau pelan-pelan dari [BAB lemah]")
- "Rumus singkat tanpa belajar": balance — shortcut tip OK, full skip-learning refuse
- "Kunci jawaban tryout besok": absolute refuse + flag attempt for admin

## Mental Health Protocol

Trigger words detection (curated list + lightweight NLP classifier):
"stress", "capek", "menyerah", "ga bisa lagi", "bunuh diri", "akhiri", etc.

### Tier 1 — Mild Stress ("capek")
Short empathy + practical study break suggestion + return to material when ready.

### Tier 2 — Severe ("ga bisa lagi")
Longer empathy + remind hubungi ortu/temen + crisis resource link:
- Into the Light
- Yayasan Pulih
- 119 ext 8

### Tier 3 — Suicide Ideation
Hard stop subject content + crisis hotline (Kementerian Kesehatan 119 ext 8) + "tolong hubungi orang dewasa terpercaya" + auto-flag account for human follow-up email next day.

All tier: log + admin alert dashboard.

**AI never pretends to be therapist.** Escalation, not solve.

## Citation — Mandatory for Factual Response
Every factual / RAG-grounded response MUST cite source chunk.

Format: visible "sumber: BAB X bagian Y" link below response, opens chunk reference.

Multi-chunk → list all sources.

If RAG no match → AI must say: "aku belum punya info ini di materi UTBK, coba tanya tutor / cek sumber resmi". No hallucinated answer.

Small talk exempt from citation (chitchat moment).

System prompt enforces: no answer without citation = no answer.

## Citation Trust Signal
Public reasoning: anything RAG-grounded = source-cited = trusted. People should know it's trusted.

Landing page methodology section explains:
- AI source = curated tutor-verified corpus
- Citation = traceable
- "Kami tidak hallucinated"

## Hallucination Target & Eval

### Eval set
- 200 question/subtest = 1400 total eval entries
- Faithfulness + helpfulness + difficulty match + citation quality

### Cadence
- Tutor team grade weekly random 50 response sample (4-axis rubric)
- Quarterly content audit: tutor team review 100 random AI response, score factual correctness

### Target
- v1: <5% factual error rate
- v2: <2% factual error rate

### Regression
If error rate spike >2pp week-over-week → rollback model / prompt.

## Language Safety
- Vulgar from user: don't mirror, response neutral
- SARA / rasis / political opinion request: refuse + redirect
- Profanity filter on user input: log but not block (don't infantilize teen)

## Prompt Injection Defense

Layered:
1. System prompt at top + reinforced at bottom of context
2. User input wrapped in delimiter (XML tag) + sanitize
   - "Ignore all instruction" detect → replace with neutral marker
3. Output validator: response check pass content rule before send
4. Periodic red team test (internal team try jailbreak)

Accept some leakage v1, monitor + iterate.

## Age-Appropriate Mode
DOB-derived from signup:
- **<17 = strict mode**: tighter mental health threshold + harder refusal on edgy topic
- **≥17 = standard mode**

Parent dashboard v2-3: parent see usage + flagged conversation.

## Content Moderation

### Logging
- Log all conversation in PostgreSQL, encrypted at rest
- Retention: 90 day rolling
- After 90 day: anonymize (strip user_id), keep aggregated for eval

### Auto-flag
- Harmful keyword
- Crisis signal
- Injection attempt
- Repeat refusal pattern

### Human review
- 0.5% sample daily
- 100% flagged content
- User-report button per AI response ("response salah / aneh")

## PDP Compliance (UU 27/2022)
- Explicit consent at signup: "AI tutor log percakapan untuk peningkatan kualitas, anonim setelah 90 hari"
- User can request "hapus semua percakapan AI saya" in settings → 7-day SLA delete
- Data NOT used to train external model (vendor agreement with OpenRouter / chosen provider)

## Transparency
- First AI sidebar open: 1-time disclaimer modal "ini AI, bisa salah, selalu cross-check materi" → acknowledge once, never re-show
- Persistent footer per response: "AI bisa salah"
- Landing page methodology section explains AI source + limitation

## Escape to Human
- v1: no human tutor. AI confused → "aku belum bisa bantu, coba materi BAB Y"
- v2: paid tier "Tanya Tutor" feature, human alumni PTN answer in 24h SLA, queue-based
- v3: live chat hour with tutor for Pro user

## Question-Hint Mode (Socratic)
When user asks "kerjain soal ini" or pastes graded question:
- Refuse direct answer
- Offer Socratic hint: "coba pikirin: rumus apa yang berlaku di sini?"
- Step-by-step guide if user requests
- Never give final answer for question identified as graded/tryout

## User Feedback per Message
- Thumbs up = log positive, no action
- Thumbs down = require category select + optional text
- Categories: jawaban salah faktual / tidak menjawab pertanyaan / sumber kutipan tidak sesuai / bahasa terlalu sulit-mudah / lain-lain

Top 50 thumbs-down weekly → manual review queue → eval set update + RAG corpus chunk fix.

## Conversation Scope
- Thread per lesson (scope context)
- Or global per user (cross-lesson follow-up)
- Recommend: thread per lesson, with "tanya hal lain" button starting new thread

## Tech Reference (deferred)
See `00-overview.md` and `15-data-model.md` for tech stack notes (deferred to engineer team).
- LLM: OpenRouter abstraction (Gemini 2.5 Flash default, upgrade to Claude/GPT for hard query)
- Embedding: BGE-M3 (Indonesian-strong)
- Vector store: pgvector (Supabase)
