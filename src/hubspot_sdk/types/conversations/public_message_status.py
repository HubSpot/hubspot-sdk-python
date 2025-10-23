# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_message_failure_details import PublicMessageFailureDetails

__all__ = ["PublicMessageStatus"]


class PublicMessageStatus(BaseModel):
    status_type: Literal["SENT", "FAILED", "RECEIVED", "READ"] = FieldInfo(alias="statusType")

    failure_details: Optional[PublicMessageFailureDetails] = FieldInfo(alias="failureDetails", default=None)
