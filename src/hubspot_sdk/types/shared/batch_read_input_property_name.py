# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .property_name import PropertyName

__all__ = ["BatchReadInputPropertyName"]


class BatchReadInputPropertyName(BaseModel):
    archived: bool

    data_sensitivity: Literal["highly_sensitive", "non_sensitive", "sensitive"] = FieldInfo(alias="dataSensitivity")

    inputs: List[PropertyName]
