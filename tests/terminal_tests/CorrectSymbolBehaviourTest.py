#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy.Terminal import Terminal


class TempClass:
    pass


class CorrectSymbolBehaviourTest(TestCase):
    def test_createWithSymbol(self):
        ter = Terminal('a', None)
        self.assertEqual('a', ter.symbol(), 'Terminal should return same symbol')
        self.assertEqual('a', ter.s, 'Terminal should return same symbol')
        self.assertEqual(ter.symbol(), ter.s, 'Symbol and s property should have same value')

    def test_createWithNumber(self):
        ter = Terminal(5, None)
        self.assertEqual(5, ter.symbol(), 'Terminal should return same number')
        self.assertEqual(5, ter.s, 'Terminal should return same number')
        self.assertEqual(ter.symbol(), ter.s, 'Symbol and s property should have same value')

    def test_createWithClass(self):
        ter = Terminal(TempClass, None)
        self.assertEqual(TempClass, ter.symbol(), 'Terminal should return same class')
        self.assertEqual(TempClass, ter.s, 'Terminal should return same class')
        self.assertEqual(ter.symbol(), ter.s, 'Symbol and s property should have same value')

    def test_createWithInstance(self):
        inst = TempClass()
        ter = Terminal(inst, None)
        self.assertEqual(inst, ter.symbol(), 'Terminal should return same instance')
        self.assertEqual(inst, ter.s, 'Terminal should return same instance')
        self.assertEqual(ter.symbol(), ter.s, 'Symbol and s property should have same value')


if __name__ == '__main__':
    main()