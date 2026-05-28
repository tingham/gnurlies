import unittest
import xml.etree.ElementTree as ET
import markdown


class TestQuestache(unittest.TestCase):
    def setUp(self):
        self.md = markdown.Markdown(extensions=['gnurlies'])

    def _parse(self, src):
        self.md.reset()
        return self.md.convert(src)

    def test_questache_element(self):
        html = self._parse('The {? glue, bridge, handshake ?} between layers.')
        tree = ET.fromstring(f'<root>{html}</root>')
        el = tree.find('.//questache')
        self.assertIsNotNone(el, 'expected a <questache> element')
        self.assertEqual(el.get('hints'), 'glue,bridge,handshake')

    def test_attache_element(self):
        html = self._parse('See [{! insert: image of Garfield !}].')
        tree = ET.fromstring(f'<root>{html}</root>')
        el = tree.find('.//attache')
        self.assertIsNotNone(el, 'expected an <attache> element')
        self.assertEqual(el.get('action'), 'insert')
        self.assertEqual(el.get('hints'), 'image of Garfield')

    def test_escaped_questache_ignored(self):
        html = self._parse(r'Literal: \{? not active ?}')
        tree = ET.fromstring(f'<root>{html}</root>')
        self.assertIsNone(tree.find('.//questache'))

    def test_escaped_attache_ignored(self):
        html = self._parse(r'Literal: \{! insert: nope !}')
        tree = ET.fromstring(f'<root>{html}</root>')
        self.assertIsNone(tree.find('.//attache'))

    def test_block_suppression(self):
        src = '<!-- gnurlies-off -->\n{? ignored ?}\n<!-- gnurlies-on -->'
        html = self._parse(src)
        tree = ET.fromstring(f'<root>{html}</root>')
        self.assertIsNone(tree.find('.//questache'))


if __name__ == '__main__':
    unittest.main()
