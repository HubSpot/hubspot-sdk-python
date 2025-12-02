# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .object_schema import ObjectSchema

__all__ = ["SchemaListResponse"]


class SchemaListResponse(BaseModel):
    results: List[ObjectSchema]
