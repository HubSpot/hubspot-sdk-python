# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicSingleSendEmailParam"]

_PublicSingleSendEmailParamReservedKeywords = TypedDict(
    "_PublicSingleSendEmailParamReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class PublicSingleSendEmailParam(_PublicSingleSendEmailParamReservedKeywords, total=False):
    """A JSON object containing anything you want to override."""

    to: Required[str]
    """The recipient of the email."""

    bcc: SequenceNotStr[str]
    """List of email addresses to send as Bcc."""

    cc: SequenceNotStr[str]
    """List of email addresses to send as Cc."""

    reply_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="replyTo")]
    """List of Reply-To header values for the email."""

    send_id: Annotated[str, PropertyInfo(alias="sendId")]
    """ID for a particular send. No more than one email will be sent per sendId."""
