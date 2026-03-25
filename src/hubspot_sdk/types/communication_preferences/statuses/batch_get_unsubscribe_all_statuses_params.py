# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchGetUnsubscribeAllStatusesParams"]


class BatchGetUnsubscribeAllStatusesParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel to check the unsubscribe-all status for.

    Currently, only 'EMAIL' is supported. This parameter is required.
    """

    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit for which the statuses are being retrieved.

    This is an optional parameter.
    """
