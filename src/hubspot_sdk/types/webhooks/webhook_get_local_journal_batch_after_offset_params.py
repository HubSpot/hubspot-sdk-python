# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookGetLocalJournalBatchAfterOffsetParams"]


class WebhookGetLocalJournalBatchAfterOffsetParams(TypedDict, total=False):
    offset: Required[str]

    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
