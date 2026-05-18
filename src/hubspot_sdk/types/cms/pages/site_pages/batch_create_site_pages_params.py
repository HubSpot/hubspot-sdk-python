# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BatchCreateSitePagesParams"]


class BatchCreateSitePagesParams(TypedDict, total=False):
    inputs: Required[Iterable["PagesPageParam"]]
    """Pages to input."""


from ...pages_page_param import PagesPageParam
