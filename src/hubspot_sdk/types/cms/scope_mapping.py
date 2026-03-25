# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScopeMapping"]


class ScopeMapping(BaseModel):
    access_level: Literal["ALL", "OWNED", "TEAM_OWNED", "UNASSIGNED"] = FieldInfo(alias="accessLevel")

    request_action: Literal["COMMUNICATE", "DELETE", "EDIT", "EDIT_ASSOCIATION", "MERGE", "VIEW"] = FieldInfo(
        alias="requestAction"
    )

    scope_name: str = FieldInfo(alias="scopeName")
