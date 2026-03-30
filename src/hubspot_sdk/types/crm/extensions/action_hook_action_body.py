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
    """
    The HTTP method to be used when making the call, which can be set to GET, POST,
    PUT, DELETE, or PATCH. If using GET or DELETE
    """

    property_names_included: List[str] = FieldInfo(alias="propertyNamesIncluded")
    """A list of property names that will be included on the action.

    See the documentation for more information
    """

    type: Literal["ACTION_HOOK"]
    """The type of status."""

    url: str
    """The URL endpoint that will be called when the action is triggered."""

    confirmation: Optional[ActionConfirmationBody] = None

    label: Optional[str] = None
    """The label for this property as you'd like it displayed to users."""
