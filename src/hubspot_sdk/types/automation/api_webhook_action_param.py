# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam
from .api_input_variable_param import APIInputVariableParam
from .api_auth_key_webhook_auth_settings_param import APIAuthKeyWebhookAuthSettingsParam
from .api_signature_webhook_auth_settings_param import APISignatureWebhookAuthSettingsParam

__all__ = ["APIWebhookActionParam", "AuthSettings"]

AuthSettings: TypeAlias = Union[APIAuthKeyWebhookAuthSettingsParam, APISignatureWebhookAuthSettingsParam]


class APIWebhookActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    method: Required[Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]

    query_params: Required[Annotated[Iterable[APIInputVariableParam], PropertyInfo(alias="queryParams")]]

    type: Required[Literal["WEBHOOK"]]

    webhook_url: Required[Annotated[str, PropertyInfo(alias="webhookUrl")]]

    auth_settings: Annotated[AuthSettings, PropertyInfo(alias="authSettings")]

    connection: APIConnectionParam
