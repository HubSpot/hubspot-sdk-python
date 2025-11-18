# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PublicAssociationDefinitionConfigurationUpdateResult"]


class PublicAssociationDefinitionConfigurationUpdateResult(BaseModel):
    category: Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"]

    type_id: int = FieldInfo(alias="typeId")

    user_enforced_max_to_object_ids: Optional[int] = FieldInfo(alias="userEnforcedMaxToObjectIds", default=None)
