# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tag_param import TagParam

__all__ = ["TagCreateBatchParams"]


class TagCreateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[TagParam]]
    """Blog tags to input."""
