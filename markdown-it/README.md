# gnurlies — markdown-it plugin

A [markdown-it](https://github.com/markdown-it/markdown-it) plugin that parses **questache** and **attaché** syntax — inline calls-to-action for human–AI document collaboration.

For background on the convention, see the [gnurlies whitepaper](https://github.com/tingham/gnurlies).

## Install

```sh
npm install gnurlies
```

## Usage

```ts
import MarkdownIt from 'markdown-it';
import gnurlies from 'gnurlies';

const md = new MarkdownIt();
md.use(gnurlies);

const result = md.parse('The {? glue, bridge, handshake ?} between layers.');
```

The plugin adds two token types to the core pipeline:

| Token | Attributes | Meaning |
|---|---|---|
| `questache` | `hints` — comma-separated hint string | Ask for names or verbiage |
| `attache` | `action`, `hints` | Request a concrete insertion |

### Questache

```markdown
The {? glue, bridge, handshake ?} between the canvas layer and the stroke model
is resolved at render time.
```

Produces a `questache` token with `meta.hints = ['glue', 'bridge', 'handshake']`.

### Attaché

```markdown
See [here]({! insert: image of Garfield being lazy !}) for a vivid illustration.
```

Produces an `attache` token with `meta.action = 'insert'` and `meta.hints = ['image of Garfield being lazy']`.

### Escaping

Prefix with a backslash to emit literal text:

```markdown
\{? this will not produce a token ?}
\{! neither will this !}
```

Gnurlies inside fenced code blocks are never parsed.

### Block suppression

```markdown
<!-- gnurlies-off -->
{? ignored ?} and {! also ignored !}
<!-- gnurlies-on -->
```

## Token shape

```ts
token.type    // 'questache' | 'attache'
token.meta    // { hints: string[] } | { action: string, hints: string[] }
token.attrs   // [['hints', '...'], ...] | [['action', '...'], ['hints', '...']]
token.content // the original matched string
```

## License

MIT
