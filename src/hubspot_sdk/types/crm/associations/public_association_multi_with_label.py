# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...marketing.emails_paging import EmailsPaging
from ...shared.public_object_id import PublicObjectID
from ..multi_associated_object_with_label import MultiAssociatedObjectWithLabel

__all__ = ["PublicAssociationMultiWithLabel"]


class PublicAssociationMultiWithLabel(BaseModel):
    from_: PublicObjectID = FieldInfo(alias="from")

    to: List[MultiAssociatedObjectWithLabel]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
