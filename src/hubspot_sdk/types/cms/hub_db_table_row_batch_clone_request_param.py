# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HubDBTableRowBatchCloneRequestParam"]


class HubDBTableRowBatchCloneRequestParam(TypedDict, total=False):
    id: Required[str]
    """The ID of the row to be cloned."""

    name: str
    """The name for the cloned row."""
