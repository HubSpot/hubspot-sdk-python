# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JournalLocalGetLatestParams"]


class JournalLocalGetLatestParams(TypedDict, total=False):
    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """
    The unique identifier of the portal installation for which to retrieve the
    latest journal entries. This parameter is optional and should be an integer.
    """
