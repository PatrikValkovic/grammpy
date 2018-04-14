#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.07.2017 20:16
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Terminal


class TempClass:
    pass


class TerminalCreationTest(TestCase):
    def test_noneClass(self):
        ter1 = Terminal(0, None)
        ter2 = Terminal(0, TempClass)
        self.assertNotEqual(ter1, ter2)

    def test_noneInstance(self):
        ter1 = Terminal(0, None)
        ter2 = Terminal(0, TempClass())
        self.assertNotEqual(ter1, ter2)

    def test_noneString(self):
        ter1 = Terminal(0, None)
        ter2 = Terminal(0, 'str')
        self.assertNotEqual(ter1, ter2)

    def test_noneNumber(self):
        ter1 = Terminal(0, None)
        ter2 = Terminal(0, 5)
        self.assertNotEqual(ter1, ter2)

    def test_classInstance(self):
        ter1 = Terminal(0, TempClass)
        ter2 = Terminal(0, TempClass())
        self.assertNotEqual(ter1, ter2)

    def test_classString(self):
        ter1 = Terminal(0, TempClass)
        ter2 = Terminal(0, 'str')
        self.assertNotEqual(ter1, ter2)

    def test_classNumber(self):
        ter1 = Terminal(0, TempClass)
        ter2 = Terminal(0, 5)
        self.assertNotEqual(ter1, ter2)

    def test_instanceString(self):
        ter1 = Terminal(0, TempClass())
        ter2 = Terminal(0, 'str')
        self.assertNotEqual(ter1, ter2)

    def test_instanceNumber(self):
        ter1 = Terminal(0, TempClass)
        ter2 = Terminal(0, 5)
        self.assertNotEqual(ter1, ter2)

    def test_stringNumber(self):
        ter1 = Terminal(0, 'str')
        ter2 = Terminal(0, 5)
        self.assertNotEqual(ter1, ter2)

    def test_defferentInstances(self):
        ter1 = Terminal(0, TempClass())
        ter2 = Terminal(0, TempClass())
        self.assertNotEqual(ter1, ter2)


if __name__ == '__main__':
    main()