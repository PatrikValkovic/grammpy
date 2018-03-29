#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:45
:Licence GNUv3
Part of lambda-cli

"""

from grammpy import Grammar
from .terminals import all_terms


lambda_grammar = Grammar(terminals=all_terms)