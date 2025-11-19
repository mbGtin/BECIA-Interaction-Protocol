# Contributing Guidelines — BECIA Interaction Protocol (BIP)
### Behavioral Emotion & Context Inference Architecture  
### Version: v1.1 (Intentionality Update)

Thank you for your interest in contributing to BECIA.  
This document outlines the rules, style guide and submission process  
for extending the protocol and dataset.

The goal is to maintain **consistency, interpretability and academic quality**  
across all contributions.

---

# 1. General Principles

Contributions should:

- follow the **BECIA interpretation framework**  
- reflect human conversational dynamics  
- avoid flat sentiment labels  
- respect the tone–intention–reaction separation  
- include concise, expert-level reasoning  

All annotations must be **faithful, consistent and context-aware**.

---

# 2. Adding New Samples (JSONL)

All dataset entries must comply with the official schema:

```json
{
  "id": "string",
  "text": "string",
  "language": "EN",
  "emojis": ["…", "😅"],
  "tone": ["label1", "label2"],
  "intention": "string or null",
  "context_note": "string"
}
```

### 2.1 Required fields
- `id`  
- `text`  
- `language`  
- `tone`  
- `context_note`

### 2.2 Optional field
- `intention` (recommended when identifiable)

### 2.3 Emoji extraction
Emojis and markers must be listed exactly as they appear, e.g.:

```
["…", "😂"]
["😏"]
["🩷"]
```

Ellipsis (`…`) counts as a **nonverbal signal**.

---

# 3. Tone Labels (1–3 allowed)

Tone labels must be selected from the controlled vocabulary used in BECIA, such as:

- humour  
- micro-humour  
- sarcasm  
- teasing  
- elegant mockery  
- warmth  
- deep affection  
- symbolic positivity  
- hesitation  
- mild frustration  
- dramatic humour  

Do **not** invent new labels without prior discussion.

Contributors may propose new tone categories via pull request  
with a written justification.

---

# 4. Intention Labels (optional but recommended)

Intention describes the **communicative motive**, such as:

- reassurance  
- softening  
- distancing  
- masking vulnerability  
- maintaining closeness  
- signalling trust  

If intention cannot be inferred confidently, leave it `null`.

---

# 5. Context Note (mandatory)

The context note must be:

- short  
- precise  
- expert-level  
- focused on interpretive logic  

Example:

```
"Ellipsis signals hesitation; smirk reframes the doubt as playful mockery."
```

Avoid subjective or emotional descriptions.  
Explain **mechanics**, not personal opinions.

---

# 6. Interpretation Rules

All annotations must follow the 4-layer protocol:

1. **Signal Layer** — emojis, markers, prosody  
2. **Context Layer** — relationship, topic, sensitivity  
3. **State Layer** — inferred baseline of the receiver  
4. **Reaction Layer** — tones, intention, context reasoning

Do not skip layers.

Annotations must remain internally consistent  
with `emoji_semantics.md` and `reaction_logic.md`.

---

# 7. Adding Documentation

All documentation must:

- use neutral, academic tone  
- be consistent with terminology  
- follow existing structure  
- avoid duplication across documents  

Sections requiring major conceptual changes  
should be proposed through an Issue before submission.

---

# 8. Pull Request Requirements

Each PR must include:

- description of the change  
- rationale (why the addition is aligned with BECIA)  
- confirmation that schema and guidelines were followed  
- example entry if adding data  

PRs that do not meet schema or style requirements  
will not be merged.

---

# 9. What Not to Submit

Please do not submit:

- flat sentiment labels (“joy”, “sadness”, etc.)  
- annotations without context notes  
- invented or ad hoc tone categories  
- entries lacking emojis or nonverbal markers  
- long personal narratives instead of message-style samples  
- messages in languages other than English (for v1.1)  
- interpretations based on speculation about personal history  

BECIA focuses strictly on **interaction-level reasoning**.

---

# 10. Code of Conduct

All contributors must:

- treat the protocol as a scientific framework  
- respect others’ expertise  
- ensure clarity and reproducibility  
- avoid emotionally charged language  
- remain open to revision and correction  

The aim is collaborative, academically credible improvement.

---

# 11. Summary

BECIA is a research-oriented protocol.  
Contributions must maintain:

- clarity  
- consistency  
- precision  
- contextual awareness  
- alignment with the multi-layer interpretation model  

Thank you for helping build a rigorous, human-aligned communication dataset.

---

# End of Document
