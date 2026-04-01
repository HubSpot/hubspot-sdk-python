# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ListListBySearchParams"]


class ListListBySearchParams(TypedDict, total=False):
    additional_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="additionalProperties")]]
    """The property names of any additional list properties to include in the response.

    Properties that do not exist or that are empty for a particular list are not
    included in the response.

    By default, all requests will fetch the following properties for each list:
    `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`,
    `hs_folder_name`, and `hs_list_reference_count`.
    """

    list_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="listIds")]]
    """ILS list ids to be included in search results.

    If not specified, all lists matching other criteria will be included
    """

    offset: Required[int]
    """Value used to paginate through lists.

    The `offset` provided in the response can be used in the next request to fetch
    the next page of results. Defaults to `0` if no offset is provided.
    """

    processing_types: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="processingTypes")]]
    """List processing types to be included in search results.

    If not specified, all lists with all processing types will be included.
    """

    count: int
    """The number of lists to include in the response.

    Defaults to `20` if no value is provided. The max `count` is `500`.
    """

    object_type_id: Annotated[str, PropertyInfo(alias="objectTypeId")]

    query: str
    """The `query` that will be used to search for lists by list name.

    If no `query` is provided, then the results will include all lists.
    """

    sort: str
    """Sort field and order"""
