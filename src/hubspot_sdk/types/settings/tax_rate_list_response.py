# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["TaxRateListResponse", "Result"]


class Result(BaseModel):
    id: str

    active: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    label: str

    name: str

    percentage_rate: float = FieldInfo(alias="percentageRate")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class TaxRateListResponse(BaseModel):
    results: List[Result]

    paging: Optional[ForwardPaging] = None
