import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import MarkdownIt from 'markdown-it';
import questachePlugin from '../index';

describe('gnurlies plugin', () => {
  const md = MarkdownIt().use(questachePlugin);

  it('tokenizes a questache', () => {
    const tokens = md.parse('The {? glue, bridge, handshake ?} between layers.', {});
    const tok = tokens.find(t => t.type === 'questache');
    assert.ok(tok, 'expected a questache token');
    assert.deepEqual(tok!.meta.hints, ['glue', 'bridge', 'handshake']);
  });

  it('tokenizes an attaché', () => {
    const tokens = md.parse('See [here]({! insert: image of Garfield being lazy !}).', {});
    const tok = tokens.find(t => t.type === 'attache');
    assert.ok(tok, 'expected an attaché token');
    assert.equal(tok!.meta.action, 'insert');
    assert.deepEqual(tok!.meta.hints, ['image of Garfield being lazy']);
  });

  it('ignores escaped gnurlies', () => {
    const tokens = md.parse('Literal: \\{? not active ?} and \\{! insert: nope !}.', {});
    assert.equal(tokens.find(t => t.type === 'questache'), undefined);
    assert.equal(tokens.find(t => t.type === 'attache'), undefined);
  });
});