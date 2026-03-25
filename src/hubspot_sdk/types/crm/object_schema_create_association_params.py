# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectSchemaCreateAssociationParams"]


class ObjectSchemaCreateAssociationParams(TypedDict, total=False):
    from_object_type_id: Required[Annotated[str, PropertyInfo(alias="fromObjectTypeId")]]

    to_object_type_id: Required[Annotated[str, PropertyInfo(alias="toObjectTypeId")]]

    name: str
