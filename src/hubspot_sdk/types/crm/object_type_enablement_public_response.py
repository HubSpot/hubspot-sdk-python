# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ObjectTypeEnablementPublicResponse"]


class ObjectTypeEnablementPublicResponse(BaseModel):
    enablement: bool
    """Whether the object type is enabled or not"""
