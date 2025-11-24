# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_sort_param import APISortParam

__all__ = ["APIAssociationDataSourceParam"]


class APIAssociationDataSourceParam(TypedDict, total=False):
    association_category: Required[
        Annotated[
            Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED"], PropertyInfo(alias="associationCategory")
        ]
    ]

    association_type_id: Required[Annotated[int, PropertyInfo(alias="associationTypeId")]]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    type: Required[Literal["ASSOCIATION"]]

    sort_by: Annotated[APISortParam, PropertyInfo(alias="sortBy")]
