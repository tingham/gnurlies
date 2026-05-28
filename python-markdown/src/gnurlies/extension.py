from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor


QUESTACHE_RE = r'(?<!\\)\{\?\s*([^?]+?)\s*\?\}'
ATTACHE_RE   = r'(?<!\\)\{!\s*([^:!]+?)\s*:\s*([^!]+?)\s*!\}'


def _split_csv(s: str) -> list[str]:
    return [p.strip() for p in s.split(',') if p.strip()]


class QuestacheProcessor(InlineProcessor):
    def handleMatch(self, m: re.Match, data: str):  # type: ignore[override]
        el = ET.Element('questache')
        hints = _split_csv(m.group(1))
        el.set('hints', ','.join(hints))
        el.text = m.group(0)
        return el, m.start(0), m.end(0)


class AttacheProcessor(InlineProcessor):
    def handleMatch(self, m: re.Match, data: str):  # type: ignore[override]
        el = ET.Element('attache')
        el.set('action', m.group(1).strip())
        hints = _split_csv(m.group(2))
        el.set('hints', ','.join(hints))
        el.text = m.group(0)
        return el, m.start(0), m.end(0)


class GnurliesOffPreprocessor(Preprocessor):
    """Strip content between <!-- gnurlies-off --> and <!-- gnurlies-on -->."""

    def run(self, lines: list[str]) -> list[str]:
        result: list[str] = []
        suppressed = False
        for line in lines:
            if '<!-- gnurlies-off -->' in line:
                suppressed = True
            elif '<!-- gnurlies-on -->' in line:
                suppressed = False
            elif not suppressed:
                result.append(line)
        return result


class GnurliesExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(GnurliesOffPreprocessor(md), 'gnurlies_off', 175)
        md.inlinePatterns.register(QuestacheProcessor(QUESTACHE_RE, md), 'questache', 180)
        md.inlinePatterns.register(AttacheProcessor(ATTACHE_RE, md), 'attache', 179)


def makeExtension(**kwargs):
    return GnurliesExtension(**kwargs)
