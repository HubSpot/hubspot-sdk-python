# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MeetingSettingsResponse"]


class MeetingSettingsResponse(BaseModel):
    criteria: Literal["ALL", "NONE"]

    selling_strategy: Literal["ACCOUNT_BASED", "LEAD_BASED"] = FieldInfo(alias="sellingStrategy")
