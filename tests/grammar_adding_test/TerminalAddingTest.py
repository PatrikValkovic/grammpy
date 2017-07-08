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


class TerminalAddingTest(TestCase):
    def test_correctAddOne(self):
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

    def test_correctAddTwo(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        self.assertIsNone(gr.get_term(0))
        self.assertIsNone(gr.term(0))
        self.assertIsNone(gr.get_term('asdf'))
        self.assertIsNone(gr.term('asdf'))
        gr.add_term(0)
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).symbol(), 0)
        self.assertIsNone(gr.get_term('asdf'))
        self.assertIsNone(gr.term('asdf'))
        gr.add_term('asdf')
        self.assertEqual(gr.terms_count(), 2)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).symbol(), 0)
        self.assertIsNotNone(gr.get_term('asdf'))
        self.assertIsNotNone(gr.term('asdf'))
        self.assertTrue(isinstance(gr.term('asdf'), Terminal))
        self.assertEqual(gr.term('asdf').symbol(), 'asdf')
