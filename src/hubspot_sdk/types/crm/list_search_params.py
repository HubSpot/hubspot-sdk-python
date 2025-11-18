# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ListSearchParams"]


class ListSearchParams(TypedDict, total=False):
    additional_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="additionalProperties")]]
    """The property names of any additional list properties to include in the response.

    Properties that do not exist or that are empty for a particular list are not
    included in the response.

    By default, all requests will fetch the following properties for each list:
    `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`,
    `hs_folder_name`, and `hs_list_reference_count`.
    """

    offset: Required[int]
    """Value used to paginate through lists.

    The `offset` provided in the response can be used in the next request to fetch
    the next page of results. Defaults to `0` if no offset is provided.
    """

    count: int
    """The number of lists to include in the response.

    Defaults to `20` if no value is provided. The max `count` is `500`.
    """

    list_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="listIds")]
    """The `listIds` that will be used to filter results by `listId`.

    If values are provided, then the response will only include results that have a
    `listId` in this array.

    If no value is provided, or if an empty list is provided, then the results will
    not be filtered by `listId`.
    """

    processing_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="processingTypes")]
    """The `processingTypes` that will be used to filter results by `processingType`.

    If values are provided, then the response will only include results that have a
    `processingType` in this array.

    If no value is provided, or if an empty list is provided, then results will not
    be filtered by `processingType`.

    Valid `processingTypes` are: `MANUAL`, `SNAPSHOT`, or `DYNAMIC`.
    """

    query: str
    """The `query` that will be used to search for lists by list name.

    If no `query` is provided, then the results will include all lists.
    """

    sort: str
