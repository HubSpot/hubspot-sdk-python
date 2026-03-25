# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicWebinarFilterParam"]


class PublicWebinarFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["WEBINAR"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter, (WEBINAR)."""

    operator: Required[str]
    """
    Specifies the operation to be performed by the filter (HAS_WEBINAR_REGISTRATION,
    NOT_HAS_WEBINAR_REGISTRATION, HAS_WEBINAR_ATTENDANCE,
    NOT_HAS_WEBINAR_ATTENDANCE).
    """

    webinar_id: Annotated[str, PropertyInfo(alias="webinarId")]
    """The ID of the webinar associated with the filter."""
