# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndexedField"]


class IndexedField(BaseModel):
    metadata_field: bool = FieldInfo(alias="metadataField")
    """Indicates whether the field is a metadata field."""

    name: str
    """The name of the indexed field."""

    value: object
    """The primary value of the indexed field."""

    values: List[object]
