# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .action_confirmation_body import ActionConfirmationBody

__all__ = ["ActionHookActionBody"]


class ActionHookActionBody(BaseModel):
    http_method: Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"] = FieldInfo(
        alias="httpMethod"
    )

    property_names_included: List[str] = FieldInfo(alias="propertyNamesIncluded")

    type: Literal["ACTION_HOOK"]

    url: str

    confirmation: Optional[ActionConfirmationBody] = None

    label: Optional[str] = None
