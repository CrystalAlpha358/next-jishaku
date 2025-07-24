# -*- coding: utf-8 -*-

"""
jishaku subclassing test 2
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a valid extension file for nextcord intended to
discover weird behaviors related to subclassing.

This variant overrides behavior directly.

:copyright: (c) 2021 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.

"""

from nextcord.ext import commands

import jishaku
from jishaku.types import ContextT


class Magnet2(*jishaku.OPTIONAL_FEATURES, *jishaku.STANDARD_FEATURES):  # pylint: disable=too-few-public-methods
    """
    The extended Jishaku cog
    """

    @jishaku.Feature.Command(name="jishaku", aliases=["jsk"], invoke_without_command=True, ignore_extra=False)
    async def jsk(self, ctx: ContextT):
        """
        override test
        """
        return await ctx.send("The behavior of this command has been overridden directly.")


def setup(bot: commands.Bot):
    """
    The setup function for the extended cog
    """

    bot.add_cog(Magnet2(bot=bot))  # type: ignore
