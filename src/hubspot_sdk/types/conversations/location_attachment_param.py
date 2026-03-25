# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LocationAttachmentParam"]


class LocationAttachmentParam(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]

    type: Required[Literal["LOCATION"]]

    address: str

    name: str

    url: str
