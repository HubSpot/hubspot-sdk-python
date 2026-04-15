# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookGetLatestLocalJournalEntryParams"]


class WebhookGetLatestLocalJournalEntryParams(TypedDict, total=False):
    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """
    An integer representing the ID of the portal to filter the webhook journal
    entries.
    """
