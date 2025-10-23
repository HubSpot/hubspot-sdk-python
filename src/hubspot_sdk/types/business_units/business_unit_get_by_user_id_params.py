# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["BusinessUnitGetByUserIDParams"]


class BusinessUnitGetByUserIDParams(TypedDict, total=False):
    name: SequenceNotStr[str]
    """The names of Business Units to retrieve.

    If empty or not provided, then all associated Business Units will be returned.
    """

    properties: SequenceNotStr[str]
    """The names of properties to optionally include in the response body.

    The only valid value is `logoMetadata`.
    """
