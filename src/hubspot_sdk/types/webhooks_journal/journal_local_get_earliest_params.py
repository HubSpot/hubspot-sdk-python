# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JournalLocalGetEarliestParams"]


class JournalLocalGetEarliestParams(TypedDict, total=False):
    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """The ID of the portal for which to retrieve the earliest webhook journal entries.

    This parameter is optional and should be an integer.
    """
