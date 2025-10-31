# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APITimestampValue"]


class APITimestampValue(BaseModel):
    timestamp_type: Literal["EXECUTION_TIME"] = FieldInfo(alias="timestampType")

    type: Literal["TIMESTAMP"]
