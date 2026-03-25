# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchUnsubscribeAllParams"]


class BatchUnsubscribeAllParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """A required string specifying the communication channel.

    Currently, only 'EMAIL' is supported.
    """

    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit to which the operation applies.

    It is an optional parameter.
    """

    verbose: bool
    """A boolean indicating whether to include detailed information in the response.

    Defaults to false.
    """
