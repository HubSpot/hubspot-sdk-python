# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactAddressParam"]


class ContactAddressParam(TypedDict, total=False):
    city: str

    country: str

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]

    state: str

    street: str

    type: Literal["HOME", "WORK"]

    zip: str
