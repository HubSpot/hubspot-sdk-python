# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..marketing_event_email_subscriber_param import MarketingEventEmailSubscriberParam

__all__ = ["AttendanceCreateByEventIDAndEmailParams"]


class AttendanceCreateByEventIDAndEmailParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    inputs: Required[Iterable[MarketingEventEmailSubscriberParam]]
    """List of marketing event details to create or update"""
