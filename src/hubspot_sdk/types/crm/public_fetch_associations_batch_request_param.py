# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PublicFetchAssociationsBatchRequestParam"]


class PublicFetchAssociationsBatchRequestParam(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the object whose associations are being fetched."""

    after: str
    """
    A paging cursor token used to retrieve the next set of results in a paginated
    response.
    """
