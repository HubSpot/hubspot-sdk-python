# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LabelsBetweenObjectPair"]


class LabelsBetweenObjectPair(BaseModel):
    """The relationship descriptors applicable between two object types."""

    from_object_id: str = FieldInfo(alias="fromObjectId")
    """The ID of the source object in the association."""

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")
    """The type ID of the source object in the association."""

    labels: List[str]
    """An array of labels associated with the relationship between the objects."""

    to_object_id: str = FieldInfo(alias="toObjectId")
    """The ID of the target object in the association."""

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
    """The type ID of the target object in the association."""
