# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ImportRowCore"]


class ImportRowCore(BaseModel):
    additional_row_data: List[str] = FieldInfo(alias="additionalRowData")

    contains_encrypted_properties: bool = FieldInfo(alias="containsEncryptedProperties")
    """Indicates whether this row contains values that were encrypted."""

    file_id: int = FieldInfo(alias="fileId")
    """The unique identifier of the uploaded file containing this row."""

    line_number: int = FieldInfo(alias="lineNumber")
    """The 1-indexed line number of this row in the source file.

    Line number 0 is reserved for file-wide errors that don't correspond to a
    specific row.
    """

    row_data: List[str] = FieldInfo(alias="rowData")

    page_name: Optional[str] = FieldInfo(alias="pageName", default=None)
    """The name of the spreadsheet sheet/page containing this row."""
