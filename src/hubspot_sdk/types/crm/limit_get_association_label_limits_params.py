# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LimitGetAssociationLabelLimitsParams"]


class LimitGetAssociationLabelLimitsParams(TypedDict, total=False):
    from_object_type_id: Annotated[str, PropertyInfo(alias="fromObjectTypeId")]

    to_object_type_id: Annotated[str, PropertyInfo(alias="toObjectTypeId")]
