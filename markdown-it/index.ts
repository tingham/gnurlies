// gnurlies/index.ts
//
// Markdown-it plugin that recognizes "gnurlies":
//   questache:  {? hint, hint ?}
//   attaché:    {! action: hint, hint !}
//
// Backslash-escaped openers (\{?  \{!) are treated as literal text.

// (?<!\\) — skip escaped openers like \{? or \{!
const QUESTACHE_RE = /(?<!\\)\{\?\s*([^?]+?)\s*\?\}/g;
const ATTACHE_RE   = /(?<!\\)\{!\s*([^:!]+?)\s*:\s*([^!]+?)\s*!\}/g;

function splitCsv(s: string): string[] {
  return s.split(',').map(p => p.trim()).filter(Boolean);
}

function questachePlugin(md: any): void {
  md.core.ruler.before('normalize', 'questache', (state: any) => {
    let match: RegExpExecArray | null;
    QUESTACHE_RE.lastIndex = 0;
    while ((match = QUESTACHE_RE.exec(state.src))) {
      const token = new state.Token('questache', 'span', 0);
      token.attrs = [['hints', match[1]]];
      token.content = match[0];
      token.meta = { hints: splitCsv(match[1]) };
      state.tokens.push(token);
    }
  });

  md.core.ruler.before('normalize', 'attache', (state: any) => {
    let match: RegExpExecArray | null;
    ATTACHE_RE.lastIndex = 0;
    while ((match = ATTACHE_RE.exec(state.src))) {
      const token = new state.Token('attache', 'span', 0);
      token.attrs = [
        ['action', match[1]],
        ['hints', match[2]],
      ];
      token.content = match[0];
      token.meta = { action: match[1], hints: splitCsv(match[2]) };
      state.tokens.push(token);
    }
  });
}

export default questachePlugin;
