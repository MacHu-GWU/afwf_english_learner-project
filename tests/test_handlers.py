# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from workflow import Workflow3
from english_learner.handlers import handler


class Test(unittest.TestCase):
    def test(self):
        wf = Workflow3()
        handler(wf, args=["garunte",])

        # settings[Keys._debug] = "debug info"


if __name__ == '__main__':
    unittest.main()
