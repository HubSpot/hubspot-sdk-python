# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .labels_between_object_pair import LabelsBetweenObjectPair

__all__ = ["CreatedResponseLabelsBetweenObjectPair"]


class CreatedResponseLabelsBetweenObjectPair(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")

    entity: LabelsBetweenObjectPair

    location: Optional[str] = None
