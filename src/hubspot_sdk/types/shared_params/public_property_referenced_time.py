# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicPropertyReferencedTime"]


class PublicPropertyReferencedTime(TypedDict, total=False):
    property: Required[str]

    reference_type: Required[Annotated[str, PropertyInfo(alias="referenceType")]]

    time_type: Required[Annotated[Literal["PROPERTY_REFERENCED"], PropertyInfo(alias="timeType")]]

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    timezone_source: Annotated[str, PropertyInfo(alias="timezoneSource")]
