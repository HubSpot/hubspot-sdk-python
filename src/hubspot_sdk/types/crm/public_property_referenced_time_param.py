# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicPropertyReferencedTimeParam"]


class PublicPropertyReferencedTimeParam(TypedDict, total=False):
    property: Required[str]
    """Specifies the name of the property that the time reference is applied to."""

    reference_type: Required[Annotated[str, PropertyInfo(alias="referenceType")]]
    """
    Specifies the type of reference for the property (VALUE, UPDATED_AT,
    ANNIVERSARY, VALUE_WITH_ZONE_SAME_LOCAL_CONVERSION,
    ANNIVERSARY_WITH_ZONE_SAME_LOCAL_CONVERSION).
    """

    time_type: Required[Annotated[Literal["PROPERTY_REFERENCED"], PropertyInfo(alias="timeType")]]
    """Defines the type of time (PROPERTY_REFERENCED)."""

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]
    """Indicates the identifier for the time zone associated with the property."""

    timezone_source: Annotated[str, PropertyInfo(alias="timezoneSource")]
    """
    Specifies the source of the time zone information for the property (CUSTOM,
    USER, PORTAL).
    """
