# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ImportRowCore"]


class ImportRowCore(BaseModel):
    contains_encrypted_properties: bool = FieldInfo(alias="containsEncryptedProperties")

    file_id: int = FieldInfo(alias="fileId")

    line_number: int = FieldInfo(alias="lineNumber")

    row_data: List[str] = FieldInfo(alias="rowData")

    page_name: Optional[str] = FieldInfo(alias="pageName", default=None)
