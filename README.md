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
