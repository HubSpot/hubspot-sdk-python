# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortalObjectTypeEnablementPublicResponse"]


class PortalObjectTypeEnablementPublicResponse(BaseModel):
    enablement_by_object_type_id: Dict[str, bool] = FieldInfo(alias="enablementByObjectTypeId")
