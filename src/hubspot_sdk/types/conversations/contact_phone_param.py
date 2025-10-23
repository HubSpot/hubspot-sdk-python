# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContactPhoneParam"]


class ContactPhoneParam(TypedDict, total=False):
    phone: Required[str]

    type: Literal["CELL", "MAIN", "HOME", "WORK"]
