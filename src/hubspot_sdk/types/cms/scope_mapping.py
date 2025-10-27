# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScopeMapping"]


class ScopeMapping(BaseModel):
    access_level: str = FieldInfo(alias="accessLevel")

    request_action: str = FieldInfo(alias="requestAction")

    scope_name: str = FieldInfo(alias="scopeName")
