# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JoinTimeAndRecordID"]


class JoinTimeAndRecordID(BaseModel):
    membership_timestamp: datetime = FieldInfo(alias="membershipTimestamp")

    record_id: str = FieldInfo(alias="recordId")
