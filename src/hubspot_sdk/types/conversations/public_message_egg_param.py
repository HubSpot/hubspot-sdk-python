# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .public_comment_egg_param import PublicCommentEggParam
from .public_conversations_message_egg_param import PublicConversationsMessageEggParam

__all__ = ["PublicMessageEggParam"]

PublicMessageEggParam: TypeAlias = Union[PublicConversationsMessageEggParam, PublicCommentEggParam]
