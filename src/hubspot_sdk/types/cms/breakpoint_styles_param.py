# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .margin_param import MarginParam
from .padding_param import PaddingParam

__all__ = ["BreakpointStylesParam"]


class BreakpointStylesParam(TypedDict, total=False):
    hidden: Required[bool]

    margin: Required[MarginParam]

    padding: Required[PaddingParam]
