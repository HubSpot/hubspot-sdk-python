# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LabelUpdateLabelParams"]


class LabelUpdateLabelParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    association_type_id: Required[Annotated[int, PropertyInfo(alias="associationTypeId")]]
    """The unique identifier for the association type."""

    label: Required[str]
    """
    A descriptor that provides context about the relationship between associated
    records.
    """

    inverse_label: Annotated[str, PropertyInfo(alias="inverseLabel")]
    """An optional descriptor for the inverse relationship between associated records."""
