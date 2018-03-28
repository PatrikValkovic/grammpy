#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:45
:Licence GNUv3
Part of lambda-cli

"""

from grammpy import *
from .terminals import *


lambda_grammar = Grammar(terminals=[LambdaKeyword, Dot, Number, Variable] + rest_terms)