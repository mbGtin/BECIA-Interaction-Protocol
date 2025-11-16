# Annotation Guidelines — BECIA Interaction Protocol (BIP)

These guidelines explain how to annotate text with emojis under the  
**BECIA Interaction Protocol (BIP)**.

All examples in v0.1 use **English (EN)**.

---

## 1. JSONL Schema (Minimal)

Each entry in `data/samples.jsonl` follows:

```json
{
  "id": "string",
  "text": "string",
  "language": "EN",
  "emojis": ["…", "😂"],
  "tone": ["sarcasm", "humour"],
  "context_note": "string"
}
```
## Required Fields

| Field          | Type     | Description                                 |
|----------------|----------|---------------------------------------------|
| `id`           | string   | unique identifier                           |
| `text`         | string   | message content                             |
| `language`     | string   | always `"EN"` in v0.1                       |
| `emojis`       | string[] | list of emojis and markers                  |
| `tone`         | string[] | 1–3 tone labels                             |
| `context_note` | string   | short justification of interpretation       |

---

## 2. Minimal Emoji → Tone Mapping

See `emoji_semantics.md` for detailed meaning.

| Emoji | Primary Tone       | Description                                   |
|--------|---------------------|-----------------------------------------------|
| 😂     | humour              | strong laugh; big amusement                   |
| 😅     | micro-humour        | half-laugh; polite embarrassment              |
| 😏     | elegant mockery     | tease, flirt, controlled superiority          |
| ❤️     | deep affection      | strong emotional bond                         |
| 🩷     | friendly warmth     | soft affection; feminine-coded                |
| 💙     | symbolic support    | thematic/neutral positive                     |
| …      | hesitation          | pause, tension, doubt                         |

---

## 3. Tone Categories

Annotate **1–3 tones**.

| Tone label          | Description                                           |
|---------------------|-------------------------------------------------------|
| humour              | strong amusement                                      |
| micro-humour        | small, polite laugh                                   |
| sarcasm             | intent ≠ literal content                              |
| teasing             | playful provocation                                   |
| elegant mockery     | polite superiority                                    |
| warmth              | emotional closeness                                   |
| deep affection      | intimate emotional bond                               |
| symbolic positivity | neutral-good, thematic                                |
| hesitation          | emotional pause                                       |
| mild frustration    | small irritation                                      |
| dramatic humour     | exaggerated joking                                    |
| supportive          | encouragement, gentle care                            |

**Examples of combinations:**

- `["teasing", "humour"]`  
- `["warmth", "deep affection"]`  
- `["sarcasm", "elegant mockery"]`

---

## 4. Annotation Rules

1. **Emoji-first interpretation** — emojis anchor tone.  
2. **Max 3 tone labels** — avoid noise.  
3. **Treat `…` as a nonverbal signal**, not punctuation.  
4. **Avoid flat emotion labels** like “joy”, “sadness”.  
5. **Context note is mandatory** — always explain the reasoning.  
6. **Use supporting docs** (`emoji_semantics.md`, `reaction_logic.md`).  
7. **Reflect relationship + history** in tone.  
8. **Document mismatches** — sender intention ≠ receiver reaction.

---

## 5. Emotion Labels vs Nonverbal Meaning

Traditional sentiment uses flat labels:

- “joy”  
- “sadness”  
- “anger”  
- “love”

This ignores:

- intensity  
- direction  
- power dynamics  
- gender norms  
- cultural patterns  
- emotional state  
- politeness  
- closeness/distance  

**Emotion label = what**  
**Nonverbal meaning = how + why + social effect**

---

## 6. Example Annotations

### ex_001

```json
{
  "id": "ex_001",
  "text": "Sure, everything works… 😂",
  "language": "EN",
  "emojis": ["…", "😂"],
  "tone": ["sarcasm", "humour"],
  "context_note": "Ellipsis adds hesitation; 😂 reframes frustration as a joke."
}
```

```json
{
  "id": "ex_002",
  "text": "I'm not stressed, I'm just… thinking 😅",
  "language": "EN",
  "emojis": ["…", "😅"],
  "tone": ["hesitation", "micro-humour"],
  "context_note": "Downplaying stress with gentle embarrassment."
}
{
  "id": "ex_002",
  "text": "I'm not stressed, I'm just… thinking 😅",
  "language": "EN",
  "emojis": ["…", "😅"],
  "tone": ["hesitation", "micro-humour"],
  "context_note": "Downplaying stress with gentle embarrassment."
}
{
  "id": "ex_003",
  "text": "Thank you ❤️ That really helped.",
  "language": "EN",
  "emojis": ["❤️"],
  "tone": ["warmth", "deep affection"],
  "context_note": "Red heart shows real emotional closeness."
}
{
  "id": "ex_004",
  "text": "WHY would you do that 😭😂",
  "language": "EN",
  "emojis": ["😭", "😂"],
  "tone": ["dramatic humour", "playful exaggeration"],
  "context_note": "Cry + laugh combo signals dramatic joking."
}
{
  "id": "ex_005",
  "text": "Oh sure… I totally believe you 😏",
  "language": "EN",
  "emojis": ["…", "😏"],
  "tone": ["teasing", "elegant mockery"],
  "context_note": "Ellipsis indicates doubt; smirk adds polite superiority."
}
```
## 7. Interpretation Workflow

1. **Identify emojis**  
   - Extract all emoji tokens from the message.

2. **Identify relationship**  
   - Determine interlocutor type (friend, authority, stranger, AI, etc.).

3. **Identify context**  
   - Detect situational frame (joke, rant, request, narrative, meta-comment, etc.).

4. **Infer baseline emotional state**  
   - Based on patterns, history, and phrasing determine the initial state before message-specific modulation.

5. **Assign 1–3 tones**  
   - Combine immediate emotional tones derived from emojis + context + prosody.

6. **Add `context_note`**  
   - Provide one short note capturing the hidden or implied layer.

7. **Validate**  
   - Cross-check with:
     - `emoji_semantics.md`
     - `reaction_logic.md`


---

## 8. Purpose

The **BIP guidelines** aim to:

- improve annotation quality  
- capture human-level nuance  
- model dynamic emotional reactions  
- move beyond rigid emotion labels  
- support training of socially-aware AI models

### 9. Intentionality (Becia v1.1)

For v1.1, annotators may additionally fill the `intention` field with a short phrase describing the primary communicative motive (e.g. “reassurance”, “distancing”, “teasing”, “softening a negative message”).

* This field is optional in early experiments, but recommended when the annotator can clearly infer why the sender used a given emoji or tone pattern.
