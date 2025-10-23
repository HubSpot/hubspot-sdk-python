# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .public_deal_split_input_param import PublicDealSplitInputParam

__all__ = ["PublicDealSplitsCreateRequestParam"]


class PublicDealSplitsCreateRequestParam(TypedDict, total=False):
    id: Required[int]

    splits: Required[Iterable[PublicDealSplitInputParam]]
