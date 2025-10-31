# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam

__all__ = ["APIAbTestBranchActionParam"]


class APIAbTestBranchActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    test_branches: Required[Annotated[Iterable[APIConnectionParam], PropertyInfo(alias="testBranches")]]

    type: Required[Literal["AB_TEST_BRANCH"]]
