# -*- coding: utf-8 -*-

"""
jishaku.models tests
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2021 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.

"""

import pytest

from jishaku.models import copy_context_with
from tests import utils


@pytest.mark.asyncio
async def test_context_copy():
    with utils.mock_ctx() as ctx:
        await copy_context_with(ctx, author=1, channel=2, content=3)  # type: ignore

        ctx.bot.get_context.assert_called_once()
        alt_message = ctx.bot.get_context.call_args[0][0]

        alt_message._update.assert_called_once()  # pylint: disable=protected-access
        assert alt_message._update.call_args[0] == ({"content": 3},)  # pylint: disable=protected-access
