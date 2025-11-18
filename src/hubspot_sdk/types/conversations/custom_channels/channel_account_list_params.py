# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ChannelAccountListParams"]


class ChannelAccountListParams(TypedDict, total=False):
    after: str

    archived: bool

    default_page_length: Annotated[int, PropertyInfo(alias="defaultPageLength")]

    delivery_identifier_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="deliveryIdentifierType")]

    delivery_identifier_value: Annotated[SequenceNotStr[str], PropertyInfo(alias="deliveryIdentifierValue")]

    limit: int

    sort: SequenceNotStr[str]
