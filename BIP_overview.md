# BECIA Interaction Protocol (BIP) – Overview

The **BECIA Interaction Protocol (BIP)** is a human–AI communication protocol based on the:

**Behavioral Emotion & Context Inference Architecture**

It defines how an AI model should interpret:
- emojis as nonverbal cues  
- tone and emotional attitude  
- contextual meaning  
- relationship-driven nuance  
- dynamic reactions shaped by human state and environment  

BIP moves beyond static “emotion labels” into **dynamic human-like reasoning**.

---

# 1. Design Principles

### 1.1 Emojis are nonverbal signals  
They mirror:
- facial expressions  
- micro-expressions  
- tension  
- attitude  
- emotional intensity  

### 1.2 Context is required, not optional  
Meaning depends on:
- relationship  
- social history  
- topic sensitivity  
- cultural and gender norms  

### 1.3 Sender ≠ receiver  
The sender’s intention is not the same as the receiver’s emotional reaction.

### 1.4 Physiology and environment matter  
Fatigue, illness, stress, weather, discomfort → all change interpretation.

### 1.5 Interpretation is dynamic  
Emojis are not static labels.  
Meaning is computed from interacting factors.

### 1.6 Human-aligned reasoning  
The protocol reconstructs how humans infer tone and emotional context.

---

# 2. Layers of the Protocol

BIP is a four-layer process.

---

## 2.1 Signal Layer  
**Input:** text + emojis + punctuation  
Tasks:
- detect emojis  
- detect ellipsis `…` as emotional marker  
- detect repetition (😂😂😂 vs 😂)  
- detect emphasis (ALL CAPS, “???”)  
- detect softeners and intensifiers  

**Output:** structured list of nonverbal markers

---

## 2.2 Context Layer  
**Input:** signals + conversational context  
Context includes:
- relationship (friend, partner, stranger, authority)  
- history (conflict, closeness, neutrality)  
- gender norms (e.g., heart colors)  
- social expectations  
- sensitivity of the topic  

**Output:** contextual interpretation frame

---

## 2.3 State Layer (Receiver)  
**Input:** context + text tone  
Estimates:
- emotional baseline (stressed, calm, lonely, overloaded)  
- inferred physiological modifiers (fatigue, illness, comfort)  
- environmental modifiers (weather, noise, cold, discomfort)  

**Output:** sensitivity profile of the receiver

---

## 2.4 Reaction Layer  
**Input:** signals + context + state  
Tasks:
- infer tone  
- predict emotional impact  
- detect mismatch between intention & reaction  
- generate 1–3 tone labels  
- produce a concise context note  

**Output:** BIP annotation entry

---

# 3. Core Interpretation Equation

Simplified:

**Reaction ≈  
Intention × Relationship × Context × Emotional State × Physiology × Environment**

A change in any element can flip meaning:
- humour → humiliation  
- affection → sadness  
- teasing → hostility  
- flirt → contempt  

---

# 4. File Roles

| File | Purpose |
|------|---------|
| `guidelines.md` | How to annotate using BIP |
| `emoji_semantics.md` | Social meaning of emojis |
| `reaction_logic.md` | How context and state modify reactions |
| `data/samples.jsonl` | Example annotated entries |

---

# 5. Intended Use

BIP is a conceptual and practical prototype designed to:

- inspire richer emoji handling in NLP  
- support tone/emotion annotation  
- demonstrate contextual emotional reasoning  
- guide dataset creators and alignment researchers  

It is intentionally small, readable, and extendable.

---
## 6. Intentionality Layer (added in BECIA v1.1)

This layer captures the sender's underlying communicative motive:
not what the emoji expresses, but what the sender *tries to achieve* with it.

Examples of common intention types:
- reassurance
- protecting the receiver’s feelings
- softening a negative message
- hiding tension behind humour
- distancing without rejecting
- signalling closeness or trust
- playful challenge or teasing
- showing vulnerability indirectly

The key idea:
**Emojis and tone markers reveal the function of the message, not its emotional category.**

This layer is evaluated together with:
Intention × Relationship × Context × State × Predicted Reaction.
