# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NearLimitRecordSample"]


class NearLimitRecordSample(BaseModel):
    label: str

    object_id: int = FieldInfo(alias="objectId")

    percentage: float

    usage: int
