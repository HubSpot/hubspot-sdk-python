# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchReadParams"]


class BatchReadParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel to filter the subscription statuses. Must be 'EMAIL'."""

    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """An optional integer representing the business unit ID.

    This parameter helps to filter the results based on the specific business unit.
    """
