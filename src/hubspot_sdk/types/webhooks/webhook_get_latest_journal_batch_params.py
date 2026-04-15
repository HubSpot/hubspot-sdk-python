# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookGetLatestJournalBatchParams"]


class WebhookGetLatestJournalBatchParams(TypedDict, total=False):
    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """The ID of the portal installation.

    This parameter is optional and can be used to filter results by a specific
    portal.
    """
