# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContactAssociation"]


class ContactAssociation(BaseModel):
    contact_id: str = FieldInfo(alias="contactId")
    """The internal ID of the contact in HubSpot"""

    email: str
    """The email of the contact in HubSpot"""

    firstname: Optional[str] = None
    """The first name of the contact in HubSpot"""

    lastname: Optional[str] = None
    """The last name of the contact in HubSpot"""
