# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicClient"]


class PublicClient(BaseModel):
    client_type: Literal["HUBSPOT", "SYSTEM", "INTEGRATION", "UNKNOWN"] = FieldInfo(alias="clientType")

    integration_app_id: Optional[int] = FieldInfo(alias="integrationAppId", default=None)
