# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicAssociationDefinitionConfigurationUpdateRequestParam"]


class PublicAssociationDefinitionConfigurationUpdateRequestParam(TypedDict, total=False):
    category: Required[Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED", "WORK"]]
    """
    Specifies the category of the association, which can be HUBSPOT_DEFINED,
    INTEGRATOR_DEFINED, or USER_DEFINED.
    """

    max_to_object_ids: Required[Annotated[int, PropertyInfo(alias="maxToObjectIds")]]
    """Defines the maximum number of target object IDs that can be associated."""

    type_id: Required[Annotated[int, PropertyInfo(alias="typeId")]]
    """A unique identifier for the association type."""
