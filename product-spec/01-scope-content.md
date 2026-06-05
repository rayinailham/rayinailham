# 01 — Scope & Content Strategy

## Curriculum Scope (locked)
**UTBK/SNBT 2026-2027, all 7 subtests at launch.**

7 subtests:
1. Penalaran Umum (TPS)
2. Pengetahuan Kuantitatif (TPS)
3. Pengetahuan & Pemahaman Umum (TPS)
4. Kemampuan Memahami Bacaan & Menulis (TPS)
5. Literasi Bahasa Indonesia
6. Literasi Bahasa Inggris
7. Penalaran Matematika

Tradeoff accepted: content team burn higher, launch slower vs phased 3-subtest. Founder accepts.

## Module Structure
```
subtest (7) → BAB (~15/subtest) → lesson (~4/BAB) = ~420 lesson total
~5000 question seed across all BAB
```

Each lesson 15-25 min self-contained. Stop at lesson granularity v1, no sub-BAB layer.

## Video Strategy (Q3 — locked)
**Hybrid B + E: text-first lesson + curated YouTube embed v1, prepare A (own production) for v2.**

- Text-first lesson (markdown + diagram + worked example)
- Embedded curated YouTube (Kognita, Pak Anto, Jerome Polin, Eduwall — public + good quality)
- RAG sidebar = real differentiation, not video
- Skip own video production until PMF + funding
- Add own video when know which BAB convert best

Video curation rule:
- Creator credible (alumni PTN, dosen, established channel)
- Content accurate (tutor verify)
- Upload date <3 year
- Indonesian language preferred
- Re-check 6 month + broken-link checker cron

## RAG Corpus Strategy (Q4 — locked)
**Hybrid C+B: ghostwritten skeleton + enriched with translated open source.**

### Corpus production
- Skeleton per BAB ghostwritten by subject expert
- Team: ~20 ghostwriter (1 dosen + 1 alumni PTN per subtest)
- Bounded scope: ~150 BAB × 3000 word = 450k word, 3-4mo work
- Enrich with OpenStax / Khan / MIT OCW translation for depth + worked example

### RAG technical
- Storage: chunked markdown + embeddings
- Embedding: BGE-M3 (Indonesian-strong) self-host on Modal/Replicate, or Cohere multilingual
- NOT OpenAI embedding (poor Indonesian)
- Vector store: pgvector (Supabase)

### Pedagogical guardrail (system prompt enforce)
- Socratic mode default, never give direct answer to graded question
- Always cite chunk source
- Render math as KaTeX
- Cap explanation at SMA-level vocab
- Master-level depth, simplified delivery

### Eval framework
- 200 question/subtest = 1400 total eval set
- Score weekly: faithfulness + helpfulness + difficulty match + citation quality
- Tutor team grade 50 random response sample weekly
- Target: <5% factual error v1, <2% v2

### Budget
~20 ghostwriter × 5jt/mo × 4mo = **400jt** (largest single line item)

## Question Bank Strategy (Q5 — locked)
**A1 → E hybrid: scrape past official UTBK as LLM seed → human verify.**

### Source
- **A1 only**: past official UTBK/SBMPTN (LTMPT/SNPMB public release post-exam)
- ~10yr × 150 soal = ~1500 seed
- A2 (competitor bank Zenius/Ruangguru/etc) = REJECTED legal risk

### Generation pipeline
1. LLM (Gemini 2.5 Pro) draft 5000 question from corpus + seed pattern
2. Tutor verify + rewrite stem + write step-by-step explanation
3. Tag: BAB / subtest / difficulty (1-5 manual)
4. Cost: 5000 × 15rb verify-fee = **75jt** + ~2mo

### Quality requirements
- **Worked solution mandatory** per question (3× cost but feeds RAG + differentiator)
- 1 unambiguous correct answer
- Plausible distractors (not joke options)
- Common misconception in distractor design
- Free of typo, no cultural/political bias

### Difficulty calibration
- v1: human-labeled 1-5
- v2: swap to **1-PL Rasch IRT** after first event collects 100-200 response/question
- v3: 2-PL Rasch after 5+ events (25k+ response/question)
- Skip 3-PL — guessing param noisy on 4-option MCQ

### Freshness
- Ship 500 new question/month after launch (~7.5jt/mo)

### Anti-leak
- Hash question_id per session (signed token, expires)
- Randomize option order
- Watermark screenshot with userID hidden in metadata
- Accept some leak unavoidable, focus high-volume scraper

## Question Format
Structured JSON per question:
- BAB tag + subtest + difficulty
- Stem markdown (max 200 word + image if needed)
- Options array (4 for MCQ, distractor logic note for reviewer)
- Answer key + answer_normalized (for isian compare)
- Explanation markdown (step-by-step mandatory)
- Common misconception used in distractor design
- Source (UTBK 20XX / original)

## Content Format Standards
- **Lesson**: GitHub-flavored Markdown + KaTeX math + Mermaid diagram
- **Math notation**: desimal koma "0,5" Indonesia standard (exception: code → "0.5")
- **Persen**: "50%" not "50 persen"
- **Sapa user**: "kamu" (formal-friendly), bukan "anda"
- **Istilah teknis**: keep English when standard (e.g. "function" in coding context)

## Style Guide Distribution
1-page document distributed to all ghostwriter day 1, covering bahasa + notasi + tone + UTBK terminology align official SNPMB.
