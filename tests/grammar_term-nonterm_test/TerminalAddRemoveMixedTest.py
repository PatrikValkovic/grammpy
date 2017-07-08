#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase
from grammpy import Grammar
from grammpy.Terminal import Terminal


class TempClass:
    pass


class TerminalAddRemoveMixedTest(TestCase):
    def test_add_remove_add_one(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        self.assertFalse(gr.have_term(0))
        self.assertIsNone(gr.get_term(0))
        self.assertIsNone(gr.term(0))
        gr.add_term(0)
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).symbol(), 0)
        gr.remove_term(0)
        self.assertEqual(gr.terms_count(), 0)
        self.assertFalse(gr.have_term(0))
        self.assertIsNone(gr.get_term(0))
        self.assertIsNone(gr.term(0))

    def test_addTwoRemoveOneAndAddThird(self):
        gr = Grammar()
        gr.add_term(0)
        gr.add_term('asdf')
        self.assertEqual(gr.terms_count(), 2)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        self.assertIsNotNone(gr.get_term('asdf'))
        self.assertIsNotNone(gr.term('asdf'))
        self.assertTrue(isinstance(gr.term('asdf'), Terminal))
        self.assertEqual(gr.term('asdf').s, 'asdf')
        gr.remove_term('asdf')
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        gr.add_term(TempClass)
        self.assertEqual(gr.terms_count(), 2)
        self.assertTrue(gr.have_term(0))
        self.assertFalse(gr.have_term('asdf'))
        self.assertTrue(gr.have_term(TempClass))

    def test_addThreeRemoveTwoInArray(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        self.assertIsNotNone(gr.get_term('asdf'))
        self.assertIsNotNone(gr.term('asdf'))
        self.assertTrue(isinstance(gr.term('asdf'), Terminal))
        self.assertEqual(gr.term('asdf').s, 'asdf')
        self.assertIsNotNone(gr.get_term(TempClass))
        self.assertIsNotNone(gr.term(TempClass))
        self.assertTrue(isinstance(gr.term(TempClass), Terminal))
        self.assertEqual(gr.term(TempClass).s, TempClass)
        gr.remove_term([0, 'asdf'])
        self.assertEqual(gr.terms_count(), 1)
        self.assertTrue(gr.have_term(TempClass))
        self.assertFalse(gr.have_term(0))
        self.assertFalse(gr.have_term('asdf'))
        gr.add_term(0)
        self.assertEqual(gr.terms_count(), 2)
        self.assertTrue(gr.have_term(TempClass))
        self.assertTrue(gr.have_term(0))
        self.assertFalse(gr.have_term('asdf'))
