> **BECIA — Behavioral Emotion & Context Inference Architecture  
> Version: v1.1 (Intentionality Update)**

# BECIA Interaction Protocol, BIP (**Behavioral Emotion & Context Inference Architecture**) 
The **BECIA Interaction Protocol (BIP)** is a human–AI communication protocol for interpreting emojis, tone, nonverbal cues, and contextual meaning in digital text.

BIP is based on the:


A human-inspired approach to understanding emotional signals, relational context, and dynamic interpretation.

---

## Goals

- Define a clear protocol for reading emojis as nonverbal cues  
- Show how tone, context and relationship shape meaning  
- Provide annotation rules for emotional nuance  
- Offer a JSONL micro-dataset with rich context notes  
- Demonstrate how AI can move beyond flat “emotion labels”  

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `BIP_overview.md` | The protocol layers and model reasoning |
| `guidelines.md` | Annotation rules + JSONL schema |
| `emoji_semantics.md` | Meaning and social usage of emojis |
| `reaction_logic.md` | How emojis trigger different reactions |
| `data/samples.jsonl` | Example dataset entries |
| `intentionality-examples.md` | Focused examples for the intentionality layer |

---

## Emoji as Nonverbal Communication

Emojis imitate human nonverbal signals:

- facial expressions  
- micro-expressions  
- emotional intensity  
- pauses, hesitation  
- relational cues  
- softened tone  
- social alignment  

They are not decorations.  
They are **compressed nonverbal communication**.

---

## Emotion Labels vs Nonverbal Meaning

Traditional sentiment → “joy”, “sadness”, “anger”.  
This is flat.

Nonverbal meaning includes:

- tone  
- attitude  
- intensity  
- relationship  
- state of the receiver  
- social norms  
- emotional mismatch  

BIP focuses on **dynamic interpretation**, not static categories.

---

## Example JSONL Entry

```json
{
  "id": "ex_005",
  "text": "Oh sure… I totally believe you 😏",
  "language": "EN",
  "emojis": ["…", "😏"],
  "tone": ["teasing", "elegant mockery"],
  "context_note": "Polite sarcastic disbelief; smirk used as controlled superiority."
}
```

## 9. Intentionality (New in BECIA v1.1)

BECIA v1.1 introduces an explicit layer for intention inference — a structured way of capturing *why* the sender used a specific tone, emoji or punctuation pattern.

Unlike emotion labels, intention focuses on the communicative function of the message:
- reassurance
- distancing
- teasing
- softening
- avoidance
- seeking closeness
- masking tension
- signalling vulnerability

Intentionality is not extracted from emoji alone, but from the full interaction between:

**Intention × Relationship × Context × State × Environment**

This upgrade aligns BECIA with next-generation conversational AI research, where the goal is to recover the underlying motive, not the surface emotion.

---
---

## 10. New in BECIA v1.1

Version 1.1 adds:

- an explicit **Intentionality Layer**  
- the `intention` field in the core JSON schema  
- extended logic in `reaction_logic.md`  
- dedicated examples in `intentionality_examples.md`  

These changes allow the protocol to capture *why* the sender uses a specific emoji or tone marker, not only *how* it sounds.
---

## 11. Using BECIA data in Python

Below is a minimal example of how to load and iterate over BECIA samples stored in `data/samples.jsonl`.

### 11.1. Loading JSONL samples

```python
import json
from typing import Iterator, Dict, Any


def load_becia_samples(path: str) -> Iterator[Dict[str, Any]]:
    """
    Stream BECIA samples from a JSONL file.
    Each line is a separate JSON object.
    """
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


if __name__ == "__main__":
    samples = list(load_becia_samples("data/samples.jsonl"))

    # Print a few samples with tone and intention
    for sample in samples[:5]:
        sample_id = sample.get("id")
        text = sample.get("text")
        tone = sample.get("tone")
        intention = sample.get("intention")  # may be None for older examples

        print(f"{sample_id}: {text}")
        print(f"  tone      : {tone}")
        print(f"  intention : {intention}")
        print()
```

### 11.2. Typical usage in a training pipeline

In a real model-training setup, `tone`, `intention` and `context_note` can be used as supervision signals:

```python
for sample in load_becia_samples("data/samples.jsonl"):
    text = sample["text"]
    emojis = sample.get("emojis", [])
    tone = sample["tone"]
    intention = sample.get("intention")
    context_note = sample["context_note"]

    # Example: build an input/output pair for a model
    model_input = {
        "text": text,
        "emojis": emojis,
    }

    supervision = {
        "tone": tone,
        "intention": intention,
        "explanation": context_note,
    } 

    # Here you would pass model_input and supervision into your
    # favourite training or evaluation pipeline.
```

This keeps BECIA usage simple:  
**JSONL in → Python dicts → model input + supervision.**

---
---

## Release Notes — BECIA v1.1 (Intentionality Update)

**Date:** 2025-11  
**Status:** Stable  
**Changes introduced:**

- Added the `intention` field to the JSON schema  
- Added intentionality examples (`intentionality_examples.md`)  
- Updated `reaction_logic.md` with mismatch patterns  
- Expanded emoji semantics with communicative intention  
- Added three intentionality samples to `samples.jsonl`  
- Added version headers across documentation  
- Minor cleanup and consistency fixes  

**Summary:**  
BECIA v1.1 extends the protocol beyond surface-level tone markers by integrating *communicative intention* as a core interpretive dimension.  
This update strengthens the protocol's ability to model human social inference.
