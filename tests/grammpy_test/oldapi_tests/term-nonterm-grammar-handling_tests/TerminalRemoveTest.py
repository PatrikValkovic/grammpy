#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy.old_api import Grammar


class TempClass:
    pass


class TerminalRemoveTest(TestCase):
    def test_removeOne(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        gr.remove_term(0)
        self.assertEqual(gr.terms_count(), 2)
        self.assertTrue(gr.have_term('asdf'))
        self.assertTrue(gr.have_term(TempClass))
        self.assertFalse(gr.have_term(0))

    def test_removeClass(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        gr.remove_term(TempClass)
        self.assertEqual(gr.terms_count(), 2)
        self.assertTrue(gr.have_term('asdf'))
        self.assertTrue(gr.have_term(0))
        self.assertFalse(gr.have_term(TempClass))

    def test_removeTwo(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        gr.remove_term(0)
        gr.remove_term('asdf')
        self.assertEqual(gr.terms_count(), 1)
        self.assertTrue(gr.have_term(TempClass))
        self.assertFalse(gr.have_term('asdf'))
        self.assertFalse(gr.have_term(0))

    def test_removeTwoInArray(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        gr.remove_term([0, 'asdf'])
        self.assertEqual(gr.terms_count(), 1)
        self.assertTrue(gr.have_term(TempClass))
        self.assertFalse(gr.have_term('asdf'))
        self.assertFalse(gr.have_term(0))

    def test_removeTwoInTuple(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        gr.remove_term((0, 'asdf'))
        self.assertEqual(gr.terms_count(), 1)
        self.assertTrue(gr.have_term(TempClass))
        self.assertFalse(gr.have_term('asdf'))
        self.assertFalse(gr.have_term(0))

    def test_removeAllWithoutParam(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        gr.remove_term()
        self.assertEqual(gr.terms_count(), 0)
        self.assertFalse(gr.have_term(TempClass))
        self.assertFalse(gr.have_term('asdf'))
        self.assertFalse(gr.have_term(0))

    def test_removeEmptyGrammar(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        gr.remove_term()
        self.assertEqual(gr.terms_count(), 0)


if __name__ == '__main__':
    main()