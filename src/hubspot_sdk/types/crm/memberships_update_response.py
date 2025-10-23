# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MembershipsUpdateResponse"]


class MembershipsUpdateResponse(BaseModel):
    record_ids_missing: List[str] = FieldInfo(alias="recordIdsMissing")
    """The IDs of the records that were `missing` (e.g.

    did not exist in the portal) and so were not `added` or `removed`.
    """

    record_ids_removed: List[str] = FieldInfo(alias="recordIdsRemoved")
    """The IDs of the records that were `removed` from the list."""

    records_ids_added: List[str] = FieldInfo(alias="recordsIdsAdded")
