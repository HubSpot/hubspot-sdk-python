# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicPrivacyAnalyticsFilter"]


class PublicPrivacyAnalyticsFilter(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["PRIVACY"], PropertyInfo(alias="filterType")]]

    operator: Required[str]

    privacy_name: Required[Annotated[str, PropertyInfo(alias="privacyName")]]
