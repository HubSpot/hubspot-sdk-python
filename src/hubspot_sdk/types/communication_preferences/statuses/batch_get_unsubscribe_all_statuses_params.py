# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchGetUnsubscribeAllStatusesParams"]


class BatchGetUnsubscribeAllStatusesParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel to filter the unsubscribe statuses.

    This parameter is required and currently supports 'EMAIL' as a valid value.
    """

    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit to filter the results.

    This is an optional parameter.
    """
