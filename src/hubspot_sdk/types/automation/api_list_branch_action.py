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
    """The ID for this action."""

    list_branches: List["APIListBranch"] = FieldInfo(alias="listBranches")

    type: Literal["LIST_BRANCH"]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    default_branch: Optional[APIConnection] = FieldInfo(alias="defaultBranch", default=None)

    default_branch_name: Optional[str] = FieldInfo(alias="defaultBranchName", default=None)
    """
    The name of the default branch, the branch that gets executed if the object does
    not match any of the `listBranch` criteria.
    """


from .api_list_branch import APIListBranch
