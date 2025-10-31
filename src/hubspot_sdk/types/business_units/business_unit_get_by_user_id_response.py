# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..marketing.public_business_unit import PublicBusinessUnit

__all__ = ["BusinessUnitGetByUserIDResponse"]


class BusinessUnitGetByUserIDResponse(BaseModel):
    results: List[PublicBusinessUnit]
    """The collection of Business Units"""
