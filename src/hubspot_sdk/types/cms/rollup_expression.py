# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.association_spec import AssociationSpec

__all__ = ["RollupExpression"]


class RollupExpression(BaseModel):
    association_types: List[AssociationSpec] = FieldInfo(alias="associationTypes")

    rollup_operator: Literal[
        "AVERAGE",
        "COUNT",
        "EARLIEST_VALUE",
        "LATEST_VALUE",
        "MAX",
        "MAX_BY",
        "MIN",
        "MIN_BY",
        "REFERENCED_ID_SET",
        "REFERENCED_STRING_SET",
        "REFERENCED_STRING_SET_INTERSECTION",
        "SUM",
        "SYNC_MAX_BY",
        "SYNC_MIN_BY",
        "SYNC_VALUE",
        "UNKNOWN_ROLLUP_OPERATOR",
    ] = FieldInfo(alias="rollupOperator")

    source_object_type_id: str = FieldInfo(alias="sourceObjectTypeId")

    source_property_name: str = FieldInfo(alias="sourcePropertyName")

    conditional_expression: Optional[object] = FieldInfo(alias="conditionalExpression", default=None)

    conditional_formula: Optional[str] = FieldInfo(alias="conditionalFormula", default=None)

    empty_rollup_value: Optional[str] = FieldInfo(alias="emptyRollupValue", default=None)

    source_compare_by_property_name: Optional[str] = FieldInfo(alias="sourceCompareByPropertyName", default=None)
