# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam

__all__ = ["APIListBranchActionParam"]


class APIListBranchActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    list_branches: Required[Annotated[Iterable["APIListBranchParam"], PropertyInfo(alias="listBranches")]]

    type: Required[Literal["LIST_BRANCH"]]

    default_branch: Annotated[APIConnectionParam, PropertyInfo(alias="defaultBranch")]

    default_branch_name: Annotated[str, PropertyInfo(alias="defaultBranchName")]


from .api_list_branch_param import APIListBranchParam
