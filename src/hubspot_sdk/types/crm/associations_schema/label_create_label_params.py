# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LabelCreateLabelParams"]


class LabelCreateLabelParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    label: Required[str]
    """
    A descriptor that provides context about the relationship between two associated
    CRM objects.
    """

    name: Required[str]
    """The unique identifier for the association definition."""

    inverse_label: Annotated[str, PropertyInfo(alias="inverseLabel")]
    """
    An optional descriptor that clarifies the reverse relationship in the
    association.
    """
