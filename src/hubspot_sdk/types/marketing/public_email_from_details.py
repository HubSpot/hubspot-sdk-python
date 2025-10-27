# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicEmailFromDetails"]


class PublicEmailFromDetails(BaseModel):
    custom_reply_to: Optional[str] = FieldInfo(alias="customReplyTo", default=None)
    """The reply to recipients will see."""

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)
    """The name recipients will see."""

    reply_to: Optional[str] = FieldInfo(alias="replyTo", default=None)
    """
    The from address and reply to email address (if no customReplyTo defined)
    recipients will see.
    """
