# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["ListFolderFetchResponse"]


class ListFolderFetchResponse(BaseModel):
    folder: "PublicListFolder"


from .public_list_folder import PublicListFolder
