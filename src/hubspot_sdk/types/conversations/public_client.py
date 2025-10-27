# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicClient"]


class PublicClient(BaseModel):
    client_type: Optional[Literal["HUBSPOT", "SYSTEM", "INTEGRATION", "UNKNOWN"]] = FieldInfo(
        alias="clientType", default=None
    )
    """The type of the client."""

    integration_app_id: Optional[int] = FieldInfo(alias="integrationAppId", default=None)
    """The ID of the client if the client is an integration."""
