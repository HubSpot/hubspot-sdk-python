# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchReadParams"]


class BatchReadParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel to filter by.

    This parameter is required and currently only supports 'EMAIL'.
    """

    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """An optional identifier for the business unit. This is an integer value."""
