# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicExecutionTranslationRuleParam"]


class PublicExecutionTranslationRuleParam(TypedDict, total=False):
    conditions: Required[Dict[str, object]]

    label_name: Required[Annotated[str, PropertyInfo(alias="labelName")]]
