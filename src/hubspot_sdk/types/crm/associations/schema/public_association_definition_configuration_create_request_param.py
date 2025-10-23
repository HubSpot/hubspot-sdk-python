# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PublicAssociationDefinitionConfigurationCreateRequestParam"]


class PublicAssociationDefinitionConfigurationCreateRequestParam(TypedDict, total=False):
    category: Required[Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"]]

    max_to_object_ids: Required[Annotated[int, PropertyInfo(alias="maxToObjectIds")]]

    type_id: Required[Annotated[int, PropertyInfo(alias="typeId")]]
