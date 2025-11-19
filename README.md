#  BECIA — Behavioral Emotion & Context Inference Architecture
### Version: v1.1 — Intentionality Update

The **BECIA Interaction Protocol (BIP)** is a human–AI communication framework for interpreting:

- emojis as nonverbal signals  
- tone and emotional attitude  
- sender intention  
- contextual meaning  
- relationship-driven nuance  
- physiological and environmental modifiers  

BECIA moves beyond flat emotion labels and models **dynamic emotional inference**, closer to real human interpretation.

---

##  Why BECIA?

Most NLP systems treat emojis as noise or simple sentiment markers.  
BECIA treats them as **compressed behavioural signals**, whose meaning depends on:

- context  
- relationship  
- emotional baseline  
- intention  
- environment  
- physiology  

This repository provides:

- a full interpretation protocol (BIP)  
- an annotation schema  
- detailed emoji semantics  
- reaction logic  
- a high-quality JSONL dataset with expert notes  
- examples of communicative intention (v1.1 update)

---

##  Repository Structure

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `BIP_overview.md` | Full protocol description (layers, reasoning) |
| `guidelines.md` | Annotation workflow (BIP steps) |
| `emoji_semantics.md` | Social meaning of emojis |
| `reaction_logic.md` | How context, state, physiology, environment modify tone |
| `intentionality_examples.md` | New v1.1 examples (sender motive) |
| `data/samples.jsonl` | High-quality annotated examples |
| `data/schema.json` | JSON schema for dataset entries |

---

##  What BECIA Models

BECIA interprets each message across interacting layers:

- **Signal** — emojis, punctuation, repetition, emphasis  
- **Context** — relationship, topic, conversational frame  
- **State** — emotional baseline of the receiver  
- **Physiology** — fatigue, stress, sensory load  
- **Environment** — noise, privacy, timing, pressure  
- **Intention** — what the sender tries to achieve socially  
- **Reaction** — how the message is likely to be felt  

This explains why the same emoji can shift between:

- humour → humiliation  
- teasing → hostility  
- affection → sadness  
- softening → passive-aggressiveness  

---

##  Example JSONL Entry

```json
{
  "id": "ex_005",
  "text": "Oh sure… I totally believe you 😏",
  "language": "EN",
  "emojis": ["…", "😏"],
  "tone": ["teasing", "elegant mockery"],
  "context_note": "Ellipsis indicates doubt; smirk adds polite superiority."
}
```

---

##  Intentionality Layer (v1.1)

BECIA v1.1 adds a new field: **intention**, describing *why* the sender uses a given emoji or tone pattern.

Examples:

- softening a negative message  
- reassurance through humour  
- distancing without rejection  
- teasing to maintain closeness  
- masking vulnerability  

This aligns BECIA with emerging research in contextual emotional modelling.

---

##  Using the Dataset (Python)

```python
from data_loader import load_becia_samples

samples = list(load_becia_samples("data/samples.jsonl"))

for s in samples[:5]:
    print(s["text"], s["tone"], s.get("intention"))
```

---

##  License

MIT License (or any other license you choose).

---

##  Citation

```
Benderyszyn, M. (2025). BECIA — Behavioral Emotion & Context Inference Architecture (v1.1).
GitHub Repository. https://github.com/mbGtin/BECIA-Interaction-Protocol
```

---

## ✔️ Status

**Stable — v1.1**  
Next planned update: v1.2 (extended intentionality, mismatch patterns, speaker profiles).
