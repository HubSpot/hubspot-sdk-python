# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .size_param import SizeParam

__all__ = ["MarginParam"]


class MarginParam(TypedDict, total=False):
    bottom: Required[SizeParam]

    top: Required[SizeParam]
