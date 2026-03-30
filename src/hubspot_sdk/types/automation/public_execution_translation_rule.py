# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicExecutionTranslationRule"]


class PublicExecutionTranslationRule(BaseModel):
    conditions: Dict[str, object]
    """Defines the conditions that must be met for the execution rule to apply."""

    label_name: str = FieldInfo(alias="labelName")
    """Specifies the name of the label associated with the execution rule."""
