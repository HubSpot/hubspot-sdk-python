# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookGetLocalJournalBatchFromOffsetParams"]


class WebhookGetLocalJournalBatchFromOffsetParams(TypedDict, total=False):
    offset: Required[str]

    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """The ID of the portal where the webhooks are installed.

    This is an integer value.
    """
