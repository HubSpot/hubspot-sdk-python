# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .rgba_color_param import RgbaColorParam

__all__ = ["ColorStopParam"]


class ColorStopParam(TypedDict, total=False):
    color: Required[RgbaColorParam]
