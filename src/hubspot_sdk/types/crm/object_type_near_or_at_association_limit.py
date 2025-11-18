# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectTypeNearOrAtAssociationLimit"]


class ObjectTypeNearOrAtAssociationLimit(BaseModel):
    has_records_at_limit: bool = FieldInfo(alias="hasRecordsAtLimit")
    """Indicates whether there are records that have reached the association limit."""

    has_records_near_limit: bool = FieldInfo(alias="hasRecordsNearLimit")
    """Indicates whether there are records that are approaching the association limit."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The unique identifier for the object type."""

    plural_label: str = FieldInfo(alias="pluralLabel")
    """The plural form of the label for the object type."""

    singular_label: str = FieldInfo(alias="singularLabel")
    """The singular form of the label for the object type."""
