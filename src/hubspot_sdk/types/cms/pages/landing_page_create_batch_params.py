# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["LandingPageCreateBatchParams"]


class LandingPageCreateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable["PageParam"]]
    """Pages to input."""


from ..page_param import PageParam
