# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IsPresent"]


class IsPresent(BaseModel):
    expression_to_evaluate: object = FieldInfo(alias="expressionToEvaluate")

    operator: Literal["IS_PRESENT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None
