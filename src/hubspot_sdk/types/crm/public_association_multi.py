# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .associated_id import AssociatedID
from ..marketing.emails_paging import EmailsPaging
from ..shared.public_object_id import PublicObjectID

__all__ = ["PublicAssociationMulti"]


class PublicAssociationMulti(BaseModel):
    from_: PublicObjectID = FieldInfo(alias="from")

    to: List[AssociatedID]
    """
    The IDs of objects that are associated with the object identified by the ID in
    'from'.
    """

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
