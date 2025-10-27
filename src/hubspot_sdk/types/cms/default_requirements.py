# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DefaultRequirements"]


class DefaultRequirements(BaseModel):
    gates: List[str]

    operator: Literal["AND", "OR"]

    scope_names: List[str] = FieldInfo(alias="scopeNames")

    settings: List[str]
