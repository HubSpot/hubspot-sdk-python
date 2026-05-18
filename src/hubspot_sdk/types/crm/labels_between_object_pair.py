# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LabelsBetweenObjectPair"]


class LabelsBetweenObjectPair(BaseModel):
    """The relationship descriptors applicable between two object types."""

    from_object_id: str = FieldInfo(alias="fromObjectId")
    """Source unique ID of the object."""

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")
    """Source object type."""

    labels: List[str]

    to_object_id: str = FieldInfo(alias="toObjectId")
    """Target unique ID of the object."""

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
    """Target object type."""
