# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection

__all__ = ["APIListBranchAction"]


class APIListBranchAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")

    list_branches: List["APIListBranch"] = FieldInfo(alias="listBranches")

    type: Literal["LIST_BRANCH"]

    default_branch: Optional[APIConnection] = FieldInfo(alias="defaultBranch", default=None)

    default_branch_name: Optional[str] = FieldInfo(alias="defaultBranchName", default=None)


from .api_list_branch import APIListBranch
