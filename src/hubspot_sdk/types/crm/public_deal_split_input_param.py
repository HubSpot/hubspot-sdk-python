# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDealSplitInputParam"]


class PublicDealSplitInputParam(TypedDict, total=False):
    owner_id: Required[Annotated[int, PropertyInfo(alias="ownerId")]]
    """The unique identifier of the owner receiving the deal split."""

    percentage: Required[float]
    """The portion of the deal assigned to the owner, expressed as a percentage.

    The total percentage for all splits in a deal must sum up to 1.0 (100%) and can
    have up to 8 decimal places.
    """
