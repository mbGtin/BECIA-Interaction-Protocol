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
