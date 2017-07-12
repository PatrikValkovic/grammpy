#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy.HashContainer import HashContainer


class HashContainerSimpleTest(TestCase):
    def test_emptyCreation(self):
        h = HashContainer()
        self.assertEqual(h.count(), 0)

    def test_creationWithArray(self):
        h = HashContainer([0, 1])
        self.assertEqual(h.count(), 2)
        self.assertTrue(h.have(0))
        self.assertTrue(h.have(1))
        self.assertFalse(h.have(2))
        self.assertEqual(h.get(0), 0)
        self.assertEqual(h.get(1), 1)
        self.assertIsNone(h.get(2))

    def test_addOne(self):
        h = HashContainer()
        h.add(1)
        self.assertEqual(h.count(), 1)
        self.assertFalse(h.have(0))
        self.assertTrue(h.have(1))
        self.assertFalse(h.have(2))
        self.assertIsNone(h.get(0))
        self.assertEqual(h.get(1), 1)
        self.assertIsNone(h.get(2))


if __name__ == '__main__':
    main()
