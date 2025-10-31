# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .combo_event_rule import ComboEventRule

__all__ = ["ComboEventRuleBranch"]


class ComboEventRuleBranch(BaseModel):
    composing_rules: List[ComboEventRule] = FieldInfo(alias="composingRules")

    operation_type: Literal["AND", "OR"] = FieldInfo(alias="operationType")

    rule_branches: List["ComboEventRuleBranch"] = FieldInfo(alias="ruleBranches")
