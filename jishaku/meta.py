# -*- coding: utf-8 -*-

"""
jishaku.meta
~~~~~~~~~~~~

Meta information about jishaku.

:copyright: (c) 2021 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.

"""

import typing

__all__ = (
    '__author__',
    '__copyright__',
    '__docformat__',
    '__license__',
    '__title__',
    '__version__',
    'version_info'
)


class VersionInfo(typing.NamedTuple):
    """Version info named tuple for Jishaku"""
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


version_info = VersionInfo(major=3, minor=0, micro=0, releaselevel='alpha', serial=0)

__author__ = 'CrystalAlpha358'
__copyright__ = 'Copyright (c) 2025 CrystalAlpha358'
__docformat__ = 'restructuredtext en'
__license__ = 'MIT'
__title__ = 'next-jishaku'
__version__ = '.'.join(map(str, (version_info.major, version_info.minor, version_info.micro)))
