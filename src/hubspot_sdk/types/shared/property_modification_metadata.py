# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyModificationMetadata"]


class PropertyModificationMetadata(BaseModel):
    archivable: bool

    read_only_definition: bool = FieldInfo(alias="readOnlyDefinition")

    read_only_value: bool = FieldInfo(alias="readOnlyValue")

    read_only_options: Optional[bool] = FieldInfo(alias="readOnlyOptions", default=None)
