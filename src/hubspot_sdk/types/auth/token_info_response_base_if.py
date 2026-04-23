# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .public_access_token_info_response import PublicAccessTokenInfoResponse
from .public_refresh_token_info_response import PublicRefreshTokenInfoResponse

__all__ = ["TokenInfoResponseBaseIf"]

TokenInfoResponseBaseIf: TypeAlias = Union[PublicAccessTokenInfoResponse, PublicRefreshTokenInfoResponse]
