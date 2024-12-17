#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.12.2024 11:51
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING
from .create_follow_table import create_follow_table

if TYPE_CHECKING:  # pragma: no cover
    from .create_follow_table import FollowTableType, FollowTableTypeValue