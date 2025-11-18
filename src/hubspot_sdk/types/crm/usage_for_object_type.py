# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageForObjectType"]


class UsageForObjectType(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The unique identifier for the object type."""

    plural_label: str = FieldInfo(alias="pluralLabel")
    """The plural form of the label for the object type."""

    singular_label: str = FieldInfo(alias="singularLabel")
    """The singular form of the label for the object type."""

    usage: int
    """The number of records used for the object type."""
