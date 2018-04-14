#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.07.2017 20:09
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main

from grammpy.representation.HashContainer import HashContainer


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
        self.assertEqual(h.add(1), [1])
        self.assertEqual(h.count(), 1)
        self.assertFalse(h.have(0))
        self.assertTrue(h.have(1))
        self.assertFalse(h.have(2))
        self.assertIsNone(h.get(0))
        self.assertEqual(h.get(1), 1)
        self.assertIsNone(h.get(2))

    def test_addMultipleSame(self):
        h = HashContainer()
        self.assertEqual(h.add(1), [1])
        self.assertEqual(h.add(1), [])
        self.assertEqual(h.add([1, 2, 3]), [2, 3])

    def test_removeMultipleSame(self):
        h = HashContainer([0, 1, 2, 3, 4])
        self.assertEqual(h.remove(0), [0])
        self.assertEqual(h.remove([1, 2]), [1, 2])
        self.assertEqual(h.remove([3, 2, 3, 4]), [3, 4])


if __name__ == '__main__':
    main()
