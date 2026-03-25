# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicExecutionTranslationRule"]


class PublicExecutionTranslationRule(BaseModel):
    conditions: Dict[str, object]

    label_name: str = FieldInfo(alias="labelName")
