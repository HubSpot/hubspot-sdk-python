# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContactURLParam"]


class ContactURLParam(TypedDict, total=False):
    url: Required[str]

    type: Literal["HOME", "WORK"]
