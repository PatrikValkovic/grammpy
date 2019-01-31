#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.07.2017 20:19
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main

from grammpy.old_api import Terminal


class TempClass:
    pass


class CorrectGrammarHandlingTest(TestCase):
    def test_sameNumber(self):
        ter1 = Terminal(0)
        ter2 = Terminal(0)
        self.assertEqual(ter1, ter2)

    def test_sameString(self):
        ter1 = Terminal(0)
        ter2 = Terminal(0)
        self.assertEqual(ter1, ter2)

    def test_sameClass(self):
        ter1 = Terminal(0)
        ter2 = Terminal(0)
        self.assertEqual(ter1, ter2)

    def test_sameInstance(self):
        ter1 = Terminal(0)
        ter2 = Terminal(0)
        self.assertEqual(ter1, ter2)


if __name__ == '__main__':
    main()