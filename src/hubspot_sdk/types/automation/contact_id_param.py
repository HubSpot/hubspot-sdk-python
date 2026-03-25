# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactIDParam"]


class ContactIDParam(TypedDict, total=False):
    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    email: str

    vid: int
