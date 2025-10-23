# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection
from .api_input_variable import APIInputVariable
from .api_auth_key_webhook_auth_settings import APIAuthKeyWebhookAuthSettings
from .api_signature_webhook_auth_settings import APISignatureWebhookAuthSettings

__all__ = ["APIWebhookAction", "AuthSettings"]

AuthSettings: TypeAlias = Union[APIAuthKeyWebhookAuthSettings, APISignatureWebhookAuthSettings]


class APIWebhookAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """The ID for this action."""

    method: Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]
    """The HTTP method to use when calling the webhook URL"""

    query_params: List[APIInputVariable] = FieldInfo(alias="queryParams")

    type: Literal["WEBHOOK"]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    webhook_url: str = FieldInfo(alias="webhookUrl")
    """The URL to call each time this action is executed."""

    auth_settings: Optional[AuthSettings] = FieldInfo(alias="authSettings", default=None)
    """The type of auth to use when calling the webhook endpoint."""

    connection: Optional[APIConnection] = None
