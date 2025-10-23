# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .contact_org import ContactOrg
from .contact_url import ContactURL
from .contact_name import ContactName
from .contact_email import ContactEmail
from .contact_phone import ContactPhone
from .contact_address import ContactAddress

__all__ = ["ContactProfile"]


class ContactProfile(BaseModel):
    addresses: List[ContactAddress]

    emails: List[ContactEmail]

    phones: List[ContactPhone]

    urls: List[ContactURL]

    name: Optional[ContactName] = None

    org: Optional[ContactOrg] = None
