# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .filtering_meta_data import FilteringMetaData

__all__ = ["ExternalOptionsMetaData"]


class ExternalOptionsMetaData(BaseModel):
    filter: Optional[FilteringMetaData] = None

    related_object_type_id: Optional[str] = FieldInfo(alias="relatedObjectTypeId", default=None)
