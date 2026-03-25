# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.paging import Paging
from ..shared.public_object_id import PublicObjectID
from .multi_associated_object_with_label import MultiAssociatedObjectWithLabel

__all__ = ["PublicAssociationMultiWithLabel"]


class PublicAssociationMultiWithLabel(BaseModel):
    from_: PublicObjectID = FieldInfo(alias="from")
    """Contains the Id of a Public Object"""

    to: List[MultiAssociatedObjectWithLabel]

    paging: Optional[Paging] = None
