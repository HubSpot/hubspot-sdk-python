# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .subscriber_email_response import SubscriberEmailResponse

__all__ = ["BatchResponseSubscriberEmailResponse"]


class BatchResponseSubscriberEmailResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """Timestamp that represents when the request finished processing"""

    results: List[SubscriberEmailResponse]

    started_at: datetime = FieldInfo(alias="startedAt")
    """Timestamp that represents when the request started processing"""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The status of the request processing"""

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """Result of the request"""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors that occurred during the processing"""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Timestamp that represents when the request was made"""
