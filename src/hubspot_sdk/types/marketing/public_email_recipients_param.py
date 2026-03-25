# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["PublicEmailRecipientsParam"]


class PublicEmailRecipientsParam(TypedDict, total=False):
    exclude: SequenceNotStr[str]
    """Excluded IDs."""

    include: SequenceNotStr[str]
    """Included IDs."""
