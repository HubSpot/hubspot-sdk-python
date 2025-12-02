# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.association_spec import AssociationSpec

__all__ = ["RollupExpression"]


class RollupExpression(BaseModel):
    association_types: List[AssociationSpec] = FieldInfo(alias="associationTypes")

    rollup_operator: str = FieldInfo(alias="rollupOperator")

    source_object_type_id: str = FieldInfo(alias="sourceObjectTypeId")

    source_property_name: str = FieldInfo(alias="sourcePropertyName")

    conditional_expression: Optional["Expression"] = FieldInfo(alias="conditionalExpression", default=None)

    conditional_formula: Optional[str] = FieldInfo(alias="conditionalFormula", default=None)

    empty_rollup_value: Optional[str] = FieldInfo(alias="emptyRollupValue", default=None)

    source_compare_by_property_name: Optional[str] = FieldInfo(alias="sourceCompareByPropertyName", default=None)


from .expression import Expression
