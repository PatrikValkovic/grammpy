#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from typing import Any


class GrammpyException(Exception):
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)