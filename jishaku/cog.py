# -*- coding: utf-8 -*-

"""
jishaku.cog
~~~~~~~~~~~~

The Jishaku debugging and diagnostics cog implementation.

:copyright: (c) 2021 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.

"""

import inspect
import typing

from nextcord.ext import commands

from jishaku.features.baseclass import Feature
from jishaku.features.filesystem import FilesystemFeature
from jishaku.features.guild import GuildFeature
from jishaku.features.invocation import InvocationFeature
from jishaku.features.management import ManagementFeature
from jishaku.features.python import PythonFeature
from jishaku.features.root_command import RootCommand
from jishaku.features.shell import ShellFeature
from jishaku.features.sql import SQLFeature
from jishaku.features.voice import VoiceFeature

__all__ = (
    "Jishaku",
    "STANDARD_FEATURES",
    "OPTIONAL_FEATURES",
    "setup",
)

STANDARD_FEATURES = (VoiceFeature, GuildFeature, FilesystemFeature, InvocationFeature, ShellFeature, SQLFeature, PythonFeature, ManagementFeature, RootCommand)

OPTIONAL_FEATURES: typing.List[typing.Type[Feature]] = []


class Jishaku(*OPTIONAL_FEATURES, *STANDARD_FEATURES):  # type: ignore  # pylint: disable=too-few-public-methods
    """
    The frontend subclass that mixes in to form the final Jishaku cog.
    """


async def async_setup(bot: commands.Bot):
    """
    The async setup function defining the jishaku.cog and jishaku extensions.
    """

    bot.add_cog(Jishaku(bot=bot))  # type: ignore


def setup(bot: commands.Bot):  # pylint: disable=inconsistent-return-statements
    """
    The setup function defining the jishaku.cog and jishaku extensions.
    """

    if inspect.iscoroutinefunction(bot.add_cog):
        return async_setup(bot)

    bot.add_cog(Jishaku(bot=bot))  # type: ignore
