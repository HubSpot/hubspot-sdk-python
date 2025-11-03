# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.public_object_id import PublicObjectID
from .associations.association_spec_1 import AssociationSpec1

__all__ = ["PublicDefaultAssociation"]


class PublicDefaultAssociation(BaseModel):
    association_spec: AssociationSpec1 = FieldInfo(alias="associationSpec")
    """
    Defines the type, direction, and details of the relationship between two CRM
    objects.
    """

    from_: PublicObjectID = FieldInfo(alias="from")

    to: PublicObjectID
