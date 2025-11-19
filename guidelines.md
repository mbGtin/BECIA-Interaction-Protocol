# Annotation Guidelines — BECIA Interaction Protocol (BIP)
### Version: v1.1 (Intentionality Update)

These guidelines describe how to annotate text using the  
**BECIA Interaction Protocol (BIP)** — a multi-layer framework for interpreting emojis, tone, context, intention and emotional reaction.

All examples in v1.1 use **English (EN)**.

---

# 1. JSONL Schema

Each entry in `data/samples.jsonl` follows:

```json
{
  "id": "string",
  "text": "string",
  "language": "EN",
  "emojis": ["…", "😂"],
  "tone": ["sarcasm", "humour"],
  "intention": "string (optional)",
  "context_note": "string"
}
```

### Required fields

| Field | Description |
|-------|-------------|
| `id` | Unique identifier |
| `text` | Raw message |
| `language` | Language code (EN in v1.1) |
| `tone` | 1–3 tone labels |
| `context_note` | Short reasoning summary |

### Optional field

| Field | Description |
|-------|-------------|
| `intention` | Sender's communicative motive |

---

# 2. Minimal Emoji → Tone Mapping

See `emoji_semantics.md` for full descriptions.

| Emoji | Primary Tone | Notes |
|-------|--------------|-------|
| 😂 | humour | big laugh; high intensity |
| 😅 | micro-humour | polite embarrassment; tension release |
| 😏 | elegant mockery / tease | playful dominance or superiority |
| ❤️ | deep affection | emotional closeness |
| 🩷 | friendly warmth | soft support; feminine-coded |
| 💙 | symbolic positivity | neutral support, thematic colour |
| … | hesitation | pause, doubt, emotional space |

---

# 3. Tone Categories

Annotate **1–3 tones** per message.

| Tone | Description |
|------|-------------|
| humour | explicit amusement |
| micro-humour | small polite laugh |
| sarcasm | intent ≠ literal meaning |
| teasing | playful provocation |
| elegant mockery | polite superiority |
| warmth | emotional closeness |
| deep affection | intimate connection |
| symbolic positivity | neutral-good support |
| hesitation | emotional pause |
| mild frustration | soft irritation |
| dramatic humour | exaggerated joking |
| supportive | gentle encouragement |

**Valid combinations:**
- `["teasing", "humour"]`
- `["warmth", "deep affection"]`
- `["sarcasm", "elegant mockery"]`

---

# 4. Annotation Rules

1. **Emoji-first interpretation**  
   Emojis anchor tone and often override literal text.

2. **Maximum of 3 tone labels**  
   Keep annotations concise.

3. **Treat `…` as a nonverbal signal**  
   Always interpret ellipsis as emotional or relational, never neutral.

4. **Avoid sentiment-style labels**  
   No “joy/sadness/anger” unless directly expressed.

5. **Context note is mandatory**  
   Provide one short expert explanation.

6. **Use supporting documents**  
   - `emoji_semantics.md`  
   - `reaction_logic.md`  

7. **Consider relationship + history**  
   Tone changes depending on closeness and expectations.

8. **Document mismatches**  
   If sender intention ≠ expected receiver reaction, highlight it.

---

# 5. Interpretation Workflow (BIP)

Annotators should follow all seven steps:

### Step 1 — Identify emojis  
Extract all nonverbal tokens: emojis, ellipsis, repetition, emphasis.

### Step 2 — Identify relationship  
Friend, partner, stranger, authority, formal/informal, etc.

### Step 3 — Identify context  
Topic type: joke, apology, correction, disclosure, narrative, etc.

### Step 4 — Infer baseline emotional state  
Likelihood of stress, fatigue, calmness, loneliness, overload.

### Step 5 — Assign 1–3 tones  
Tone derives from interaction of signal × context × state.

### Step 6 — Add `context_note`  
Short (1–2 sentences) describing interpretation rationale.

### Step 7 — Validate  
Check consistency with:

- `emoji_semantics.md`  
- `reaction_logic.md`  

---

# 6. Purpose of BIP Guidelines

These guidelines aim to:

- improve annotation consistency  
- model human-level nuance  
- go beyond flat emotion categories  
- represent contextual emotional reasoning  
- support dataset creators and AI researchers  

---

# 7. Intentionality (v1.1)

The **intentionality field** captures *why* the sender shaped the message this way.

Examples of intentions:

- reassurance  
- distancing  
- softening a negative message  
- teasing to maintain closeness  
- masking vulnerability  
- signalling trust  

Annotate intention when:

- it is clear from the message, **and**
- context suggests a functional purpose behind the tone.

Intentionality is optional but recommended for advanced annotations in v1.1.
