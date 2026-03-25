# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AngleParam"]


class AngleParam(TypedDict, total=False):
    units: Required[Literal["deg", "grad", "rad", "turn"]]
    """The unit of measurement for the angle."""

    value: Required[float]
    """The numerical representation of the angle."""
