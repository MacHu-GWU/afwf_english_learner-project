# -*- coding: utf-8 -*-

import unittest
from pprint import pprint
from english_learner.free_dictionary import fd


class TestGoogleComplete(unittest.TestCase):
    def test_get(self):
        pprint(fd.get("pick up")[0]["meanings"])
        pprint(fd.get("pick up")[0]["meanings"])


if __name__ == '__main__':
    unittest.main()
