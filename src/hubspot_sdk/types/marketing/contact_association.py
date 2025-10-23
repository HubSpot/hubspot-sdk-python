# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContactAssociation"]


class ContactAssociation(BaseModel):
    contact_id: str = FieldInfo(alias="contactId")

    email: str

    firstname: Optional[str] = None

    lastname: Optional[str] = None
