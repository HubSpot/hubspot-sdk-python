# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PublicObjectIDParam"]


class PublicObjectIDParam(TypedDict, total=False):
    """Contains the Id of a Public Object"""

    id: Required[str]
    """The unique ID of the object."""
