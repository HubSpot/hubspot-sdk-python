# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BatchGetLandingPagesParams"]


class BatchGetLandingPagesParams(TypedDict, total=False):
    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    archived: bool
    """Whether to return only results that have been archived."""
