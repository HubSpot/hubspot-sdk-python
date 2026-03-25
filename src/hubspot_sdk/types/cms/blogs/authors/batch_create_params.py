# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..blog_author_param import BlogAuthorParam

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    inputs: Required[Iterable[BlogAuthorParam]]
    """Blog authors to input."""
