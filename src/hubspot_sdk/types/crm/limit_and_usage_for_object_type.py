# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LimitAndUsageForObjectType"]


class LimitAndUsageForObjectType(BaseModel):
    limit: int
    """The maximum allowed count for the object type."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The unique identifier for the object type."""

    percentage: float
    """The percentage of the limit that has been used."""

    plural_label: str = FieldInfo(alias="pluralLabel")
    """The plural label for the object type."""

    singular_label: str = FieldInfo(alias="singularLabel")
    """The singular label for the object type."""

    usage: int
    """The current usage count for the object type."""
