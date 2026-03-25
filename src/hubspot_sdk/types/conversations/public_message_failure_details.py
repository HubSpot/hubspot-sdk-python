# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicMessageFailureDetails"]


class PublicMessageFailureDetails(BaseModel):
    error_message_tokens: Dict[str, str] = FieldInfo(alias="errorMessageTokens")

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
