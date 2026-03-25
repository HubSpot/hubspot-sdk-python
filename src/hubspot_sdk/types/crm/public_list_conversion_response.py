# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_list_conversion_date import PublicListConversionDate
from .public_list_conversion_inactivity import PublicListConversionInactivity

__all__ = ["PublicListConversionResponse", "RequestedConversionTime"]

RequestedConversionTime: TypeAlias = Union[PublicListConversionDate, PublicListConversionInactivity]


class PublicListConversionResponse(BaseModel):
    list_id: str = FieldInfo(alias="listId")
    """
    The unique identifier of the list for which the conversion details are provided.
    """

    converted_at: Optional[datetime] = FieldInfo(alias="convertedAt", default=None)
    """The date and time when the list was converted."""

    requested_conversion_time: Optional[RequestedConversionTime] = FieldInfo(
        alias="requestedConversionTime", default=None
    )
    """
    The scheduled time for the list conversion, which can be based on a specific
    date or inactivity period.
    """
