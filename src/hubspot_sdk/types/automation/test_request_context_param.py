# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TestRequestContextParam"]


class TestRequestContextParam(TypedDict, total=False):
    source: Required[Literal["TEST"]]
    """
    Indicates the source of the test request, with the only accepted value being
    'TEST'.
    """
