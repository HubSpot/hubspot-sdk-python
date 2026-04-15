# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookGetEarliestJournalBatchParams"]


class WebhookGetEarliestJournalBatchParams(TypedDict, total=False):
    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """The ID of the portal installation for which to fetch the journal entries.

    This is an optional parameter.
    """
