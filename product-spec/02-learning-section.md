# 02 — Learning Section Feature

## Concept
Structured lesson per BAB. User reads concept → embedded video → AI tutor sidebar (RAG) → 3-phase challenge → badge.

**Critical principle: Lesson = teach + badge ONLY. Lesson does NOT affect mastery. Mastery proof = battlefield only.**

## Module Structure
```
subtest (7) → BAB (~15/subtest) → lesson (~4/BAB)
each lesson 15-25 min self-contained
```

## Lesson Sequence Gating

### Free user — hard linear gate
- Must finish lesson 1 → unlock lesson 2 → unlock lesson 3 → 4
- Within lesson: phase A → B → C sequential
- BAB to BAB: any order (free roam across BAB)

### Paid (Pro) user — free roam
- All lesson always accessible
- All phase always accessible
- No gating

## Lesson Content Format
- GitHub-flavored Markdown
- KaTeX math (inline `$x^2$` + block `$$\int$$`)
- Mermaid diagram (text-based, version-able)
- Hand-drawn complex diagram → PNG/SVG upload to Storage
- Image alt text mandatory (a11y + SEO)
- Curated YouTube embed via official iframe

## Lesson Template (ghostwriter)
1. **Tujuan Pembelajaran** (3 bullet, behavioral verb)
2. **Pra-syarat** (link to prerequisite lesson)
3. **Konsep Inti** (max 800 word)
4. **Contoh + Worked Example** (2-3 contoh)
5. **Latihan Cek Pemahaman** (link to question pool)
6. **Ringkasan** (5 bullet)
7. **Kaitan UTBK** (kisi-kisi reference)

## Challenge Structure (3 Phase per Lesson)

### Phase A — "Cek Pemahaman"
- 3 MCQ low difficulty (D=1-2)
- During/after content read
- Inline interspersed with lesson content
- Pass: complete all 3
- Reward: small mastery bump → wait NO. **Lesson zero effect on mastery.** Just badge progress.

### Phase B — "Latihan"
- 5 MCQ medium difficulty (D=3)
- Mix from question bank, curated subset for this lesson
- Pass: ≥60% correct
- Reward: badge "Latihan Lulus"

### Phase C — "Tantangan Boss"
- 1-3 hard multi-step (D=4-5)
- Unlock after phase B ≥60% (free user) / always (Pro)
- Pass: ≥60% correct
- Reward: badge "Boss Down" + streak bonus + unlock "Latihan Lanjutan" pile (extra hard question for that BAB in battlefield)

## Difficulty Curve
**Static curve A→B→C**, NOT adaptive.

Reason: Lesson = teaching, not assessment. Adaptive belongs in battlefield. Static curve = predictable + designed pedagogically.

Same engine as battlefield Q5 bank, just curated subset preselected per lesson.

## End-of-Lesson CTA
**"Udah paham? Coba battlefield BAB ini sekarang?"**

Direct funnel teach → assess. Forces user to battlefield = real mastery proof + more engagement loop.

## Badges (level system replacement)
**Drop "level" abstraction.** Replace with mastery + 4-tier badge.

### Badge tiers per BAB (derived from mastery)
- **Pemula**: mastery 0-20
- **Pelajar**: mastery 20-50
- **Mahir**: mastery 50-80
- **Master**: mastery 80-100

### Phase badges per lesson
- "Cek Pemahaman Lulus" (phase A done)
- "Latihan Lulus" (phase B ≥60%)
- "Boss Down" (phase C ≥60%)
- "Lulus Jalur Lurus" (linear sequence within BAB)

## AI Tutor Sidebar
See `05-ai-tutor.md` for full guardrail spec.

### Access tier
- **Free user**: 5 message lifetime trial total (not per day, lifetime)
- **Pro user**: 50 message/day soft cap (unlimited fair-use)
- **Hard rate limit all**: 10 message/min/user

### Trigger
Visible in lesson page sidebar. Organic discovery — no forced tutorial use.

### First-time disclaimer
1-time modal on first AI sidebar open: "ini AI, bisa salah, selalu cross-check materi" → acknowledge once, never re-show.

### Per-message footer
Persistent small text "AI bisa salah" per response.

## Revisit / Review
- Redo lesson anytime
- **No mastery decay** (UTBK is bounded exam, decay annoying)
- Show "terakhir kerjakan: 12 hari lalu" hint
- Separate "Review Pile" feature (from Q7 wrong-answer auto-mark)

## Content Discovery v1
Dashboard widget:
- **"Lanjutkan Belajar"** — last opened lesson
- **"Rekomendasi"** — lowest-mastery BAB user has touched (force confront weakness)
- **"Next Lesson"** — next in soft-linear order within current BAB
- Manual browse: subtest tree always available

## Integration with Other Features
- Lesson mastery merge with battlefield mastery → **same per-BAB Elo rating**, one source of truth
- Lesson phase B/C question = same as battlefield bank, just preselected curated
- All BAB unlocked from start in **battlefield + tryout** (UTBK kid need flexibility)
- Tryout score does NOT affect lesson mastery (separate concern)
- Lesson does NOT affect mastery (locked decision)

## Streak
Daily streak. Open AND complete ≥1 phase = streak count. See `09-retention-burnout.md`.

## Decoupling Logic Summary
| Action | Mastery Impact |
|---|---|
| Complete lesson phase A/B/C | None — badge only |
| Battlefield correct answer | Yes — Elo update |
| Battlefield wrong answer | Yes — Elo update |
| Tryout response | None on mastery — tryout has own scoring |
| Diagnostic response | Yes — initial Elo seed only |
