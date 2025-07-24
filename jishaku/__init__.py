# -*- coding: utf-8 -*-

"""
jishaku
~~~~~~~

A nextcord extension including useful tools for bot development and debugging.

:copyright: (c) 2024 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.

"""

# pylint: disable=wildcard-import
from jishaku.cog import *  # noqa: F401
from jishaku.features.baseclass import Feature  # noqa: F401
from jishaku.flags import Flags  # noqa: F401
from jishaku.meta import *  # noqa: F401

__all__ = (
    'Jishaku',
    'Feature',
    'Flags',
    'setup'
)
