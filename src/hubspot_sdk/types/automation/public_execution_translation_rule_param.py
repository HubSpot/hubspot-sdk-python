# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicExecutionTranslationRuleParam"]


class PublicExecutionTranslationRuleParam(TypedDict, total=False):
    conditions: Required[Dict[str, object]]
    """Defines the conditions that must be met for the execution rule to apply."""

    label_name: Required[Annotated[str, PropertyInfo(alias="labelName")]]
    """Specifies the name of the label associated with the execution rule."""
