# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchUnsubscribeAllParams"]


class BatchUnsubscribeAllParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel from which subscribers will be unsubscribed.

    This parameter is required and currently supports only 'EMAIL'.
    """

    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """
    An optional integer representing the business unit ID for which the operation is
    being performed.
    """

    verbose: bool
    """A boolean indicating whether to include detailed information in the response.

    Defaults to false.
    """
