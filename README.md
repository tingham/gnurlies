# Questache: An Inline Naming Convention for Human–AI Document Collaboration

**Version:** 0.1  
**Date:** 2026-05-28  
**Status:** Draft

---

## Abstract

Questache is a lightweight inline syntax for embedding calls-to-action inside markdown documents. It signals to an AI collaborator that the author needs help generating names, labels, or verbiage for a nearby concept — without leaving the document to ask in a separate chat interface. The result is a tighter authoring loop where the document itself is the conversation.

---

## Motivation

When writing documentation, specifications, or prose alongside an AI assistant, the workflow commonly breaks down at naming. The author has a concept in mind but no settled term for it. They interrupt the document, switch to a chat interface, describe the concept, receive suggestions, return to the document, and insert the chosen name — losing context and flow in the process.

Questache eliminates the interruption. The author drops a hint directly into the prose, and the AI responds in place.

---

## Syntax

```
{? hint, hint, hint ?}
```

A questache is a pair of curly braces enclosing one or more comma-separated hints, bookended by question marks:

| Token | Role |
|---|---|
| `{?` | Opening marker — signals a questache |
| hints | Comma-separated words that guide the suggestion: fragments, vibes, roots, or constraints |
| `?}` | Closing marker |

The hints are **not** a definition. They are directional — a compass, not a map. The AI evaluates the surrounding context (the sentence, section, or document) and uses the hints to constrain or flavor its suggestions.

### Examples

```markdown
The {? glue, bridge, handshake ?} between the canvas layer and the stroke model
is resolved at render time.
```

```markdown
## {? boot, wake, ignite, cold-start ?}

This section describes the sequence of events from process launch to first frame.
```

```markdown
We call this pattern a {? curlop, curlfel, curlit, mustion, questard, questache ?}.
```

(The last example is self-referential: it is the questache that named the questache.)

---

## AI Response Behavior

When an AI assistant encounters a questache in a markdown document, it should:

1. **Respond inline** — place suggestions on a new line immediately following the line containing the questache.
2. **Use a consistent identity prefix** — e.g. `**Claude Code**:` — so the author can distinguish AI contributions from their own prose.
3. **Offer multiple candidates** — ranked or grouped, with brief rationale if the hints are ambiguous.
4. **Not interrupt chat** — the questache is a document-native signal; the response belongs in the document, not in a sidebar.

### Example Response

```markdown
The {? glue, bridge, handshake ?} between the canvas layer and the stroke model
is resolved at render time.
**Claude Code**: *binding*, *junction*, *mediator*, *seam* — "seam" carries the most spatial resonance given "canvas layer."
```

---

## Design Principles

**Hints, not specs.** The content inside `{? ?}` is deliberately loose. Precise definitions belong in prose; the questache is for the moment *before* you have the words.

**Document-first.** The questache keeps the document as the focal point of collaboration. The AI is a contributor in the margin, not an ![interlocutor](https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyOTl0aXJ4N29heDVtazk4N2g1N3VqYTNtc3dqaGFrZWxvOTFuc3doaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/GbzIMCw41eUBa/giphy.gif "I am Locutus of Borg") in a separate window.

The companion to the questache is the **attaché** — `{! action: hints !}` — an imperative directive that asks the AI to produce or insert something concrete at that location in the document. Where a questache asks *what to call* something, an attaché asks *for* something.

**Lightweight.** The syntax is minimal enough to type without friction and visually distinctive enough to scan for — the `?` bookends read as a literal question mark on each side of the concept.

**Author-controlled.** The AI responds; the author decides. Questache suggestions are proposals, not insertions.

---

## Escaping Gnurlies

Questaches and attachés are collectively called **gnurlies**. When you need to write gnurlie syntax without triggering it — in examples, documentation about the convention itself, or any context where the syntax should be treated as literal text — use an escape.

### Inline escape

Prefix the opening marker with a backslash:

```
\{? this will not be acted on ?}
\{! insert: neither will this !}
```

The AI reads the backslash as "literal text follows" and leaves the gnurlie in place, stripping the backslash from the rendered output as markdown normally would.

### Code fences

Gnurlies inside fenced code blocks are never active. The fence is its own escape context — no backslash needed.

````markdown
```
{? this is an example, not a call to action ?}
```
````

### Block suppression

For larger regions containing multiple gnurlies, wrap the block in an HTML comment toggle:

```markdown
<!-- gnurlies-off -->
Everything in here — {? including this ?} and {! this !} — is ignored.
<!-- gnurlies-on -->
```

This is useful when quoting gnurlie-heavy documents inside another gnurlie-aware document.

---

## The Attaché

The attaché is the imperative sibling of the questache. Where a questache asks *what to call* something, an attaché asks the AI to *produce* something and place it at that exact location.

```
{! action: hint, hint !}
```

The action field names what is being requested; the hints constrain it.

```markdown
The AI is a contributor in the margin, not an [interlocutor]({! insert: public link to borg.gif !}) in a separate window.
```

```markdown
See [here]({! insert: image of Garfield being lazy !}) for a vivid illustration.
```

An attaché is fulfilled differently from a questache. The AI does not offer candidates — it produces the thing and **replaces the entire `{! !}` token** with the result. The invocation string disappears; the content takes its place.

When an attaché appears as the `href` of a markdown link, the surrounding link text migrates to the `alt` or `title` attribute of the inserted element:

```markdown
Before: [interlocutor]({! insert: public link to borg.gif !})
After:  ![interlocutor](https://example.com/borg.gif "Locutus of Borg")
```

The author's label becomes accessibility text almost for free — a useful property when the insertion is an image or external resource.

The name follows naturally from the same root as questache. A diplomatic *attaché* carries things to important meetings and delivers them. `{! !}` carries things into the document.

| Syntax | Name | Role |
|---|---|---|
| `{? hints ?}` | questache | Ask for names or verbiage |
| `{! action: hints !}` | attaché | Request a concrete insertion |

---

## The Name

The syntax itself was named using a questache:

```
{? curlop, curlfel, curlit, mustion, questard, questache ?}
```

*Questache* — from *question* and *mustache* — won because the `{` `}` curly braces visually evoke a mustache, and the `?` marks frame a question. It is memorable, pronounceable, and self-describing.

---

## Status and Scope

Questache is a convention, not a specification. It requires no parser, no tooling, and no plugin — only an AI collaborator that knows to look for it. Any document format that supports freeform text can host a questache.

It is, however, highly ["markdown-able"](https://github.com/tingham/gnurlies)

This whitepaper describes version 0.1. Extensions (typed questaches, nested hints, multi-line questaches) are left for future revision.

---

## System Prompt Templates

Drop either block into your AI assistant's system prompt, custom instructions, or rules file (Claude Code `CLAUDE.md`, Cursor `.cursorrules`, VS Code Copilot instructions, or equivalent).

### A — Compressed

For tight system prompt budgets. Covers the essentials with minimal tokens.

```
## Gnurlies

{? hints ?} in a markdown file is a **questache** — suggest names or verbiage for the nearby concept inline, on the next line, prefixed with your identity (e.g. **Claude Code**:). Offer multiple candidates with brief rationale.

{! action: hints !} is an **attaché** — produce the requested thing and insert it inline at that location. Mark what you did with your identity prefix.

Escaped gnurlies (\{? \{!) and gnurlies inside code fences are never active — treat as literal text.
```

### B — Precision

For assistants where explicit rules reduce ambiguity. Covers edge cases and AI response behavior in full.

```
## Gnurlies — Inline Collaboration Syntax

Gnurlies are inline calls-to-action embedded in markdown documents. There are two forms:

**Questache** `{? hint, hint, ... ?}`
- Signals that the author needs names, labels, or verbiage for the nearby concept.
- Respond inline: place suggestions on a new line immediately following the line containing the questache.
- Use your identity prefix (e.g. **Claude Code**:) so the author can distinguish your contributions.
- Offer multiple candidates. Add brief rationale when the hints are ambiguous.
- Do not respond in chat — the response belongs in the document.

**Attaché** `{! action: hint, hint !}`
- Signals that the author wants you to produce something and insert it at that location.
- The action field names what is requested; hints constrain it.
- Replace the entire `{! action: hints !}` token with the produced content — the invocation string disappears.
- When the attaché is the `href` of a markdown link `[text]({! ... !})`, migrate the link text to the `alt` or `title` attribute of the inserted element.
- Do not offer candidates — act, then let the author review.

**Escaping**
- `\{?` and `\{!` — backslash-escaped gnurlies are literal text. Do not act on them.
- Gnurlies inside fenced code blocks are never active.
- Content between `<!-- gnurlies-off -->` and `<!-- gnurlies-on -->` is suppressed entirely.

**General**
- The author decides what to keep. Your responses are proposals, not final insertions.
- If a document contains unresolved gnurlies, treat each one as a pending task.
```

---

*Originated by Thomas Ingham, May 2026.*
