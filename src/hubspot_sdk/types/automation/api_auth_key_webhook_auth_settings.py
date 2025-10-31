# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIAuthKeyWebhookAuthSettings"]


class APIAuthKeyWebhookAuthSettings(BaseModel):
    location: Literal["HEADER", "QUERY_PARAM"]

    name: str

    secret_name: str = FieldInfo(alias="secretName")

    type: Literal["AUTH_KEY"]
