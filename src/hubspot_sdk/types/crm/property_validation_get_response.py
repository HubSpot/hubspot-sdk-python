# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyValidationGetResponse", "Result"]


class Result(BaseModel):
    rule_arguments: List[str] = FieldInfo(alias="ruleArguments")

    rule_type: str = FieldInfo(alias="ruleType")


class PropertyValidationGetResponse(BaseModel):
    results: List[Result]
