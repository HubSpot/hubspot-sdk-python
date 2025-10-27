# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventCompleteByExternalEventIDParams"]


class EventCompleteByExternalEventIDParams(TypedDict, total=False):
    external_account_id: Required[Annotated[str, PropertyInfo(alias="externalAccountId")]]
    """
    The accountId that is associated with this marketing event in the external event
    application.
    """

    end_date_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endDateTime", format="iso8601")]]

    start_date_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startDateTime", format="iso8601")]]
