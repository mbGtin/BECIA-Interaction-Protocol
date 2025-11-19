# BECIA Interaction Protocol — Overview  
### Version: v1.1 (Intentionality Update)

The **BECIA Interaction Protocol (BIP)** defines how an AI system interprets  
**emojis, tone, contextual cues, sender intention, and emotional reactions**  
in a human-aligned way.

BIP is based on the:

**Behavioral Emotion & Context Inference Architecture**

It models the full chain of human emotional reasoning rather than relying on flat sentiment labels.

---

# 1. Design Principles

### 1.1 Emojis are nonverbal signals  
Emojis mimic real-world nonverbal behaviour:

- facial expressions  
- micro-expressions  
- hesitation or tension  
- emotional intensity  
- social alignment  
- playful vs serious intent  

### 1.2 Context is required  
Meaning depends on:

- relationship  
- topic sensitivity  
- history  
- cultural and gender norms  
- conversational frame  
- implicit expectations  

### 1.3 Sender ≠ receiver  
The sender's intention often differs from how the receiver interprets it.

### 1.4 Physiology and environment matter  
Text is shaped by:

- fatigue, illness, hunger  
- sensory load  
- environmental noise  
- comfort vs discomfort  
- time of day  

These factors modify emotional interpretation.

### 1.5 Interpretation is dynamic  
Emojis are not static labels  
—they participate in a dynamic reasoning process.

### 1.6 Human-aligned reasoning  
BIP models how humans actually infer tone and emotional meaning.

---

# 2. Layers of the Protocol

BIP operates across **four main layers** (plus intentionality in v1.1).

---

## 2.1 Signal Layer  
**Input:** text, emojis, punctuation  
Extract:

- emojis  
- ellipsis `…`  
- emphasis (ALL CAPS, repeating letters)  
- repetition (😂😂😂)  
- softeners and intensifiers  

**Output:** structured nonverbal markers.

---

## 2.2 Context Layer  
**Input:** signals + conversation frame  
Includes:

- social relationship  
- recent events  
- topic type  
- shared history  
- cultural/gender patterns  

**Output:** contextual interpretation frame.

---

## 2.3 State Layer (Receiver)  
Infers:

- emotional baseline (calm, stressed, lonely, tired)  
- physiological modifiers (fatigue, hunger, discomfort)  
- environmental context (noise, privacy, pressure)  

**Output:** receiver sensitivity profile.

---

## 2.4 Reaction Layer  
Generates:

- 1–3 tone labels  
- predicted emotional impact  
- mismatch between intention and reaction  
- `context_note` with concise reasoning  

**Output:** final BIP annotation.

---

# 3. Core Interpretation Equation

```
Reaction ≈ Intention × Relationship × Context × State × Physiology × Environment
```

A small change in any factor can flip meaning:

- humour → humiliation  
- teasing → hostility  
- affection → sadness  
- softening → passive-aggressiveness  

---

# 4. File Roles in the Repository

| File | Purpose |
|------|---------|
| `guidelines.md` | Annotation workflow |
| `emoji_semantics.md` | Social meaning of emojis |
| `reaction_logic.md` | How context modifies interpretation |
| `data/samples.jsonl` | Example dataset |
| `schema.json` | JSON schema |
| `intentionality_examples.md` | Intent-focused examples |

---

# 5. Intended Use

BECIA is designed to support:

- contextual emotion modelling  
- tone classification  
- nonverbal cue interpretation  
- AI alignment and safety research  
- dataset creation and annotation consistency  
- teaching materials in AI communication  

It is intentionally readable and modular.

---

# 6. Intentionality Layer (v1.1)

**Intentionality** describes *why* a sender uses a certain tone or emoji.

Common intentions include:

- softening a negative message  
- reassurance  
- distancing  
- teasing for closeness  
- masking vulnerability  
- signalling trust  
- controlling social distance  

This layer interacts with:

```
Intention × Relationship × Context × State × Expected Reaction
```

Intentionality is essential for modelling true human emotional reasoning.

---

# 7. Summary

BECIA defines a **multi-layered protocol** for interpreting:

- emotional signals  
- social meaning  
- relational nuance  
- physiological and environmental modifiers  
- sender intention  
- receiver reaction  

It moves beyond sentiment analysis into **human-aligned contextual understanding**.
