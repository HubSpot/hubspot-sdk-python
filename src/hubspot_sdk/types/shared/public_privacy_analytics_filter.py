# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPrivacyAnalyticsFilter"]


class PublicPrivacyAnalyticsFilter(BaseModel):
    filter_type: Literal["PRIVACY"] = FieldInfo(alias="filterType")

    operator: str

    privacy_name: str = FieldInfo(alias="privacyName")
