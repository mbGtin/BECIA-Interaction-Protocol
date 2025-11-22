# BECIA Annotation Guidelines (BIP Workflow)

Version: v1.1 — Intentionality Update  
Scope: How to annotate messages using the BECIA Interaction Protocol (BIP).

These guidelines describe the **step-by-step workflow** for turning a raw message into a structured BECIA entry (e.g. in `data/samples.jsonl`).

---

## 1. Core Principles

1. **Text ≠ Emotion**  
   Never assume that literal text fully expresses the emotional state.  
   Emojis, punctuation, timing and relationship can completely invert the surface meaning.

2. **Emoji are nonverbal markers**  
   Emoji are not decoration. They function like facial expressions, tone of voice, body language.

3. **Context is layered**  
   Interpretation depends on:  
   - who is talking to whom (relationship),  
   - what is happening (context),  
   - in what state the sender is (state, physiology),  
   - in what environment (privacy, time pressure, noise).

4. **Intention matters**  
   The same emoji/tone can serve different motives: soften, attack, deflect, seek reassurance, mask vulnerability.

5. **Mismatch is a first-class signal**  
   When tone/emoji and topic diverge (e.g. trauma + 😂), this is not noise but a key variant of behaviour.

---

## 2. BECIA Six-Factor Frame

When annotating, you are implicitly or explicitly reasoning over six axes:

1. **Intention** – what the sender is trying to achieve socially.  
2. **Relationship** – how close / formal / asymmetric the dyad is.  
3. **Context** – the conversational frame (small talk, conflict, crisis, work, etc.).  
4. **State** – sender’s baseline emotional/mental state.  
5. **Physiology** – known physical factors (fatigue, pain, substance use, sensory overload).  
6. **Environment** – place, time, pressure, privacy, distractions.

You do **not** need to fill all six fields in every entry,  
but you should be **aware** that these influences exist and inform your choices.

---

## 3. High-Level Workflow

For each message you annotate:

1. Identify the raw **signal** (text + emoji).  
2. Identify the **relationship** between participants.  
3. Identify the **local context** of this message.  
4. Infer the sender’s **baseline state** (if knowable).  
5. Assign **1–3 tones** that best capture how it comes across.  
6. Assign an **intention** (what the sender wants to achieve).  
7. Evaluate **mismatch** (text vs tone vs emoji).  
8. Write a **context_note** that makes the reading reproducible.  
9. Validate against `emoji_semantics.md` and `reaction-logic.md`.

---

## 4. Step-by-Step BIP Workflow

### Step 1 — Capture the raw message

Record:

- `text` — the exact message text, as sent.  
- `emojis` — a list of emoji in **order of appearance**.  
- `language` — ISO-like language tag, e.g. `"EN"`, `"PL"`.

If the message is *only* emoji, `text` can be empty string, but `emojis` must be filled.

> Example  
> Text: `"No super 😂"`  
> Emojis: `["😂"]`  
> Language: `"PL"`

---

### Step 2 — Identify relationship_type

Define **who** is talking to whom:

Examples of allowed values (you can extend locally):

- `close_friend`  
- `acquaintance`  
- `colleague`  
- `boss`  
- `subordinate`  
- `partner`  
- `ex_partner`  
- `family`  
- `stranger`  
- `ai_assistant`  

Pick the one that best fits the **current** relationship in this conversation, not in some abstract history.

---

### Step 3 — Identify context_type

In what **scene** is this message happening?

Suggested controlled vocabulary (extendable):

- `small_talk`  
- `logistics` (arranging, planning)  
- `banter` (light teasing, jokes)  
- `support` (emotional support, listening)  
- `conflict` (argument, tension)  
- `post_conflict_cooling`  
- `crisis` (acute distress, breakdown)  
- `work_task` (professional, task-oriented)  
- `meta_conversation` (discussing the relationship / conversation itself)

Choose the context that fits the **local window** around the message.

---

### Step 4 — Infer baseline sender_state

Annotate how the sender seems to be *coming into* this message.

Examples:

- `calm`  
- `playful`  
- `tired`  
- `irritated`  
- `overloaded` (too many inputs / tasks / emotions)  
- `shut_down` (minimal affect, emotionally withdrawn)  
- `euphoric`  
- `anxious`  
- `numb` (low feeling, flat tone)  

Only fill this when there is enough context.  
If uncertain, use `unknown` or leave the field absent.

---

### Step 5 — Assign 1–3 tones

`tones` describes **how the message lands** — perceived emotional colouring, not just sentiment.

You can use combinations like:

- `warm`, `reassuring`  
- `dry`, `matter_of_fact`  
- `ironic`, `teasing`  
- `bitter`, `resentful`  
- `playful`, `chaotic`  
- `passive_aggressive`  
- `mocking`, `hostile`  
- `self_deprecating`  
- `detached`, `cold`

Pick **1–3** tones that jointly describe the feel.  
Avoid long lists; be precise instead of exhaustive.

---

### Step 6 — Add intention

`intention` describes **why** the sender uses this wording/emoji pattern.

Common intentions (you can reuse and extend those in `intentionality-examples.md`):

- `soften_negative_message`  
- `reassure_through_humour`  
- `maintain_closeness_through_teasing`  
- `mask_vulnerability`  
- `deflect_topic`  
- `test_boundaries`  
- `deescalate_conflict`  
- `provoke_reaction`  
- `signal_distance_without_rejection`  
- `invite_emotional_disclosure`

If intention is ambiguous, note the **most plausible** one given relationship + context, and clarify in `context_note`.

---

### Step 7 — Evaluate mismatch_status

`mismatch_status` expresses whether **text, tone and emoji** align.

Suggested values:

- `match` — emotional meaning and literal content are aligned.  
- `soft_mismatch` — slight dissonance (e.g. joke used to soften real
