# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ListAddAndRemoveMembershipsParams"]


class ListAddAndRemoveMembershipsParams(TypedDict, total=False):
    record_ids_to_add: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="recordIdsToAdd")]]

    record_ids_to_remove: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="recordIdsToRemove")]]
