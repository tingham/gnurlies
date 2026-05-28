# gnurlies — Python-Markdown extension

A [Python-Markdown](https://python-markdown.github.io/) extension that parses **questache** and **attaché** syntax — inline calls-to-action for human–AI document collaboration.

For background on the convention, see the [gnurlies whitepaper](https://github.com/tingham/gnurlies).

## Install

```sh
pip install gnurlies
```

## Usage

```python
import markdown
from gnurlies import GnurliesExtension

md = markdown.Markdown(extensions=[GnurliesExtension()])
result = md.convert('The {? glue, bridge, handshake ?} between layers.')
```

Or by name:

```python
md = markdown.Markdown(extensions=['gnurlies'])
```

The extension adds two inline element types to the parse tree:

| Element | Attributes | Meaning |
|---|---|---|
| `<questache>` | `hints` — comma-separated hint string | Ask for names or verbiage |
| `<attache>` | `action`, `hints` | Request a concrete insertion |

### Questache

```markdown
The {? glue, bridge, handshake ?} between the canvas layer and the stroke model
is resolved at render time.
```

Produces `<questache hints="glue,bridge,handshake">...</questache>` in the element tree.

### Attaché

```markdown
See [here]({! insert: image of Garfield being lazy !}) for a vivid illustration.
```

Produces `<attache action="insert" hints="image of Garfield being lazy">...</attache>`.

### Escaping

Prefix with a backslash to emit literal text:

```markdown
\{? this will not be parsed ?}
\{! neither will this !}
```

Gnurlies inside fenced code blocks are never parsed.

### Block suppression

```markdown
<!-- gnurlies-off -->
{? ignored ?} and {! also ignored !}
<!-- gnurlies-on -->
```

## Post-processing

The extension emits raw XML elements. To act on them — rendering suggestions, fulfilling attachés, stripping markers — register a [Treeprocessor](https://python-markdown.github.io/extensions/api/#treeprocessors) that walks the element tree and handles `questache` and `attache` tags.

## Requirements

- Python 3.9+
- Markdown >= 3.0

## License

MIT
