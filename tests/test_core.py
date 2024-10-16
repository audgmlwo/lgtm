
import unittest


# python -m unittest tests.test_core.LgtmTest -v

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))
