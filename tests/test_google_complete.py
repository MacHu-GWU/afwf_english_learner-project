# -*- coding: utf-8 -*-

import unittest
from english_learner.google_complete import GoogleComplete


class TestGoogleComplete(unittest.TestCase):
    gc = GoogleComplete()

    def test_get(self):
        self.assertEqual(self.gc.get("guarantee")[0], "guarantee")
        self.assertEqual(self.gc.get("garunte")[0], "guarantee")


if __name__ == '__main__':
    unittest.main()
