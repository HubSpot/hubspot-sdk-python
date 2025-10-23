# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LandingPageEndAbTestParams"]


class LandingPageEndAbTestParams(TypedDict, total=False):
    ab_test_id: Required[Annotated[str, PropertyInfo(alias="abTestId")]]
    """ID of the test to end."""

    winner_id: Required[Annotated[str, PropertyInfo(alias="winnerId")]]
    """ID of the object to designate as the test winner."""
