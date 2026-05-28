# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .access_token_response import AccessTokenResponse
from .client_credentials_token_response import ClientCredentialsTokenResponse

__all__ = ["TokenResponseIf"]

TokenResponseIf: TypeAlias = Annotated[
    Union[AccessTokenResponse, ClientCredentialsTokenResponse], PropertyInfo(discriminator="token_use")
]
