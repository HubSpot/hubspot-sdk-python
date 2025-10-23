# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["WorkflowListEmailCampaignsParams"]


class WorkflowListEmailCampaignsParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    before: str

    flow_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="flowId")]
    """The ID of the workflow."""

    limit: int
    """The maximum number of results to display per page."""
