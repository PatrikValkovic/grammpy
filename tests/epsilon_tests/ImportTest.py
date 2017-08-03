#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import EPS
from grammpy import EPSILON


class ImportTest(TestCase):
    def test_idSame(self):
        self.assertEqual(id(EPS), id(EPSILON))

    def test_equal(self):
        self.assertEqual(EPS, EPSILON)

    def test_equalToSelf(self):
        self.assertEqual(EPS, EPS)

    def test_notEqualToNumber(self):
        self.assertNotEqual(EPS, 5)

    def test_notEqualToString(self):
        self.assertNotEqual(EPS, "asdf")

    def test_notEqualToObject(self):
        self.assertNotEqual(EPS, object())


if __name__ == '__main__':
    main()
