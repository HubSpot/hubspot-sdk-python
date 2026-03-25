# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssociationSpec"]


class AssociationSpec(TypedDict, total=False):
    """
    Defines the type, direction, and details of the relationship between two CRM objects.
    """

    association_category: Required[
        Annotated[
            Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED", "WORK"],
            PropertyInfo(alias="associationCategory"),
        ]
    ]
    """The category of the association, such as "HUBSPOT_DEFINED"."""

    association_type_id: Required[Annotated[int, PropertyInfo(alias="associationTypeId")]]
    """The ID representing the specific type of association."""
