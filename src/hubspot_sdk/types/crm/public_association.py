# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.public_object_id import PublicObjectID

__all__ = ["PublicAssociation"]


class PublicAssociation(BaseModel):
    from_: PublicObjectID = FieldInfo(alias="from")

    to: PublicObjectID

    type: str
    """The type of association between the 'from' and 'to' objects."""
