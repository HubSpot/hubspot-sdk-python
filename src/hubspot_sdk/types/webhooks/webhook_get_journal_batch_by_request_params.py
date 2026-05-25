# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookGetJournalBatchByRequestParams"]


class WebhookGetJournalBatchByRequestParams(TypedDict, total=False):
    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """
    An integer representing the ID of the portal installation for which the webhooks
    journal data should be retrieved.
    """
