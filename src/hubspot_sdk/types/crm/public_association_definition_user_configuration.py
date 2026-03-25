# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAssociationDefinitionUserConfiguration"]


class PublicAssociationDefinitionUserConfiguration(BaseModel):
    category: Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED", "WORK"]
    """
    The category of the association, which can be HUBSPOT_DEFINED,
    INTEGRATOR_DEFINED, or USER_DEFINED.
    """

    type_id: int = FieldInfo(alias="typeId")
    """A unique integer identifier for the association type within its category."""

    label: Optional[str] = None
    """
    A descriptor providing context about the relationship between associated
    records.
    """

    user_enforced_max_to_object_ids: Optional[int] = FieldInfo(alias="userEnforcedMaxToObjectIds", default=None)
    """
    The maximum number of target object IDs that a user can enforce in an
    association.
    """
