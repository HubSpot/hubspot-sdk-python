# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookGetJournalBatchFromOffsetParams"]


class WebhookGetJournalBatchFromOffsetParams(TypedDict, total=False):
    offset: Required[str]

    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """The ID of the portal installation to filter the webhook journal entries.

    This parameter is optional and is used to specify which portal's data to
    retrieve.
    """
