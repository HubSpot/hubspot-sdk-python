# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicEmailFromDetailsParam"]


class PublicEmailFromDetailsParam(TypedDict, total=False):
    custom_reply_to: Annotated[str, PropertyInfo(alias="customReplyTo")]
    """The reply to recipients will see."""

    from_name: Annotated[str, PropertyInfo(alias="fromName")]
    """The name recipients will see."""

    reply_to: Annotated[str, PropertyInfo(alias="replyTo")]
    """
    The from address and reply to email address (if no customReplyTo defined)
    recipients will see.
    """
