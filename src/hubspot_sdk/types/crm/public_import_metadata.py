# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_object_list_record import PublicObjectListRecord

__all__ = ["PublicImportMetadata"]


class PublicImportMetadata(BaseModel):
    counters: Dict[str, int]
    """Summarized outcomes of each row a developer attempted to import into HubSpot."""

    file_ids: List[str] = FieldInfo(alias="fileIds")
    """The IDs of files uploaded in the File Manager API."""

    object_lists: List[PublicObjectListRecord] = FieldInfo(alias="objectLists")
    """The lists containing the imported objects."""
