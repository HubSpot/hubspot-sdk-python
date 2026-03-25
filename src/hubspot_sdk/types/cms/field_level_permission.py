# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FieldLevelPermission"]


class FieldLevelPermission(BaseModel):
    access_level: str = FieldInfo(alias="accessLevel")
