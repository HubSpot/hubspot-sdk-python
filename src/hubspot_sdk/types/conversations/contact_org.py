# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContactOrg"]


class ContactOrg(BaseModel):
    company: Optional[str] = None

    department: Optional[str] = None

    title: Optional[str] = None
