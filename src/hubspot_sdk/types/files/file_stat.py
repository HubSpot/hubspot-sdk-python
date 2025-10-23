# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .file import File
from .folder import Folder
from ..._models import BaseModel

__all__ = ["FileStat"]


class FileStat(BaseModel):
    file: Optional[File] = None
    """File"""

    folder: Optional[Folder] = None
