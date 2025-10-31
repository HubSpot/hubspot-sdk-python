# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIContactPropertyAnchorParam"]


class APIContactPropertyAnchorParam(TypedDict, total=False):
    contact_property: Required[Annotated[str, PropertyInfo(alias="contactProperty")]]

    type: Required[Literal["CONTACT_PROPERTY_ANCHOR"]]
