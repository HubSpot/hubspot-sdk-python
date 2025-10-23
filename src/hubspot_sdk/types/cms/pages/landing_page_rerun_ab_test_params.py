# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LandingPageRerunAbTestParams"]


class LandingPageRerunAbTestParams(TypedDict, total=False):
    ab_test_id: Required[Annotated[str, PropertyInfo(alias="abTestId")]]
    """ID of the test to rerun."""

    variation_id: Required[Annotated[str, PropertyInfo(alias="variationId")]]
    """ID of the object to reactivate as a test variation."""
