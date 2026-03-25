# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingMarkReadyParams"]


class CallingMarkReadyParams(TypedDict, total=False):
    engagement_id: Required[Annotated[int, PropertyInfo(alias="engagementId")]]
    """The unique identifier for the engagement associated with the call recording."""
