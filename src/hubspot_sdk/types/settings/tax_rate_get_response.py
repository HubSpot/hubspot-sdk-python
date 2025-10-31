# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TaxRateGetResponse"]


class TaxRateGetResponse(BaseModel):
    id: str

    active: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    label: str

    name: str

    percentage_rate: float = FieldInfo(alias="percentageRate")

    updated_at: datetime = FieldInfo(alias="updatedAt")
