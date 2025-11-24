# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CompanyCurrency"]


class CompanyCurrency(BaseModel):
    id: str
    """The currency code for the company currency"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date the company currency was created."""
