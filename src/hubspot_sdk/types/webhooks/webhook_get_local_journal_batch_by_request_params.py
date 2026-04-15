# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WebhookGetLocalJournalBatchByRequestParams"]


class WebhookGetLocalJournalBatchByRequestParams(TypedDict, total=False):
    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    install_portal_id: Annotated[int, PropertyInfo(alias="installPortalId")]
    """The ID of the portal where the webhook is installed.

    This parameter is optional and is used to specify the portal context for the
    operation.
    """
