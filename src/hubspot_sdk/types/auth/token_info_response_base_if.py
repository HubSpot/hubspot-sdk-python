# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .public_access_token_info_response import PublicAccessTokenInfoResponse
from .public_refresh_token_info_response import PublicRefreshTokenInfoResponse

__all__ = ["TokenInfoResponseBaseIf"]

TokenInfoResponseBaseIf: TypeAlias = Annotated[
    Union[PublicAccessTokenInfoResponse, PublicRefreshTokenInfoResponse], PropertyInfo(discriminator="token_use")
]
