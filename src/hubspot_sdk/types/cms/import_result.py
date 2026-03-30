# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.error import Error

__all__ = ["ImportResult"]


class ImportResult(BaseModel):
    duplicate_rows: int = FieldInfo(alias="duplicateRows")
    """Specifies number of duplicate rows"""

    errors: List[Error]
    """List of errors during import"""

    row_limit_exceeded: bool = FieldInfo(alias="rowLimitExceeded")
    """Specifies whether row limit exceeded during import"""

    rows_imported: int = FieldInfo(alias="rowsImported")
    """Specifies number of rows imported"""
