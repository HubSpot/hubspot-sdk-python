# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWebinarFilter"]


class PublicWebinarFilter(BaseModel):
    filter_type: Literal["WEBINAR"] = FieldInfo(alias="filterType")
    """Indicates the type of filter, (WEBINAR)."""

    operator: str
    """
    Specifies the operation to be performed by the filter (HAS_WEBINAR_REGISTRATION,
    NOT_HAS_WEBINAR_REGISTRATION, HAS_WEBINAR_ATTENDANCE,
    NOT_HAS_WEBINAR_ATTENDANCE).
    """

    webinar_id: Optional[str] = FieldInfo(alias="webinarId", default=None)
    """The ID of the webinar associated with the filter."""
