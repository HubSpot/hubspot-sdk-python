# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_status import PublicStatus

__all__ = ["PublicBulkOptOutFromAllResponse"]


class PublicBulkOptOutFromAllResponse(BaseModel):
    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")
    """The email address of the contact."""

    statuses: Optional[List[PublicStatus]] = None
    """An array of subscription status objects for the contact."""
