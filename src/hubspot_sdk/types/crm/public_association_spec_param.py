# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicAssociationSpecParam"]


class PublicAssociationSpecParam(TypedDict, total=False):
    category: Required[str]
    """
    Specifies the category of the association, which can be HUBSPOT_DEFINED,
    INTEGRATOR_DEFINED, or USER_DEFINED.
    """

    type_id: Required[Annotated[int, PropertyInfo(alias="typeId")]]
    """
    A unique integer identifier for the specific association type within its
    category.
    """
