# BECIA Interaction Protocol v1

**BECIA Interaction Protocol (BIP)** is a small, focused specification and dataset for teaching AI models how to interpret emojis, ellipses (`…`) and subtle cues as **nonverbal signals** in text.

Most NLP pipelines treat emojis and punctuation as *noise* and strip them during preprocessing.  
BIP assumes the opposite:

> Emojis are compressed nonverbal signals.  
> They carry emotional intensity, social roles, relationship cues and cultural patterns.

This repository defines:

- a **base protocol** for emoji-as-tone interpretation (Becia v1),
- a **minimal JSONL schema** for examples,
- a set of **annotated samples** in English.

Higher-level concepts like **emotional modes**, **overload detection** and **regulation** are out of scope for v1 and belong to a future **Becia v2**.

---

## 1. Concept: Behavioral Emotion & Context Inference Architecture

BIP is based on a simple idea:

> Meaning of an emoji is not just the icon.  
> It is the result of an interaction between  
> **Intention × Relationship × Context × State × Physiology × Environment**.

Instead of mapping:

- `😂` → “joy”  
- `😅` → “nervousness”  
- `😏` → “sarcasm”  
- `❤️` → “love”

…BIP treats emojis and `…` as **nonverbal markers**, similar to:

- facial expressions  
- micro-expressions  
- gaze and tension  
- tone of voice  
- social distance (close vs formal)  

The protocol aims to reconstruct the kind of inference a human social observer would make, not force emojis into flat sentiment labels.

---

## 2. Goals

Becia v1 focuses on five core goals:

1. **Nonverbal-first view**  
   Treat emojis, hearts, smirks and ellipses as primary tone carriers.

2. **Dynamic interpretation**  
   Show how the same emoji can flip meaning depending on relationship and context.

3. **Explicit tone labels**  
   Provide clear, human-readable tone tags (e.g. `["teasing", "elegant mockery"]`).

4. **Compact JSONL format**  
   Offer a simple schema that can be ingested directly by models and tools.

5. **Readable specification**  
   Keep the protocol small enough to read in one sitting and easy to extend.

---

## 3. Repository Structure

```text
becia-interaction-protocol/
├── README.md
├── BIP_overview.md
├── emoji_semantics.md
├── reaction_logic.md
├── guidelines.md
└── data/
    └── samples.json
