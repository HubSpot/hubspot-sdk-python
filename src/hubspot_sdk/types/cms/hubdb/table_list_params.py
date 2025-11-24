# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TableListParams"]


class TableListParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    archived: bool
    """Specifies whether to return archived tables. Defaults to `false`."""

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
    """Specifies the content type for the response."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Only return tables created after the specified time."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Only return tables created at exactly the specified time."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Only return tables created before the specified time."""

    is_get_localized_schema: Annotated[bool, PropertyInfo(alias="isGetLocalizedSchema")]
    """Indicates whether to retrieve the localized schema for the tables."""

    limit: int
    """The maximum number of results to return. Default is 1000."""

    sort: SequenceNotStr[str]
    """Specifies which fields to use for sorting results.

    Valid fields are `name`, `createdAt`, `updatedAt`, `createdBy`, `updatedBy`.
    `createdAt` will be used by default.
    """

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Only return tables last updated after the specified time."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Only return tables last updated at exactly the specified time."""

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Only return tables last updated before the specified time."""
