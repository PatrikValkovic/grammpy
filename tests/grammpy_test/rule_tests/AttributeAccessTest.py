#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:48
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase

from grammpy import Rule


class AttributeAccessTest(TestCase):
    def test_accessExistingAttribute(self):
        class R(Rule): rule=([1, 2], [3])
        self.assertEqual(R.rules, [([1, 2], [3])])
        self.assertEqual(R.rule, ([1, 2], [3]))
        self.assertEqual(R.left, [1, 2])
        self.assertEqual(R.right, [3])
        self.assertEqual(R.toSymbol, 3)

    def test_accessNonexistingAttribute(self):
        class R(Rule): rule=([1, 2], [3])
        with self.assertRaises(AttributeError) as e:
            R.asdf
        with self.assertRaises(AttributeError) as e:
            R.asdf()
        with self.assertRaises(AttributeError) as e:
            R.property

    def test_accessExistingAttributeOnInstance(self):
        class R(Rule): rule=([1, 2], [3])
        r = R()
        self.assertEqual(r.rules, [([1, 2], [3])])
        self.assertEqual(r.rule, ([1, 2], [3]))
        self.assertEqual(r.left, [1, 2])
        self.assertEqual(r.right, [3])
        self.assertEqual(r.toSymbol, 3)

    def test_accessNonexistingAttributeOnInstance(self):
        class R(Rule): rule=([1, 2], [3])
        r = R()
        with self.assertRaises(AttributeError) as e:
            r.asdf
        with self.assertRaises(AttributeError) as e:
            r.asdf()
        with self.assertRaises(AttributeError) as e:
            r.property


if __name__ == '__main__':
    main()
