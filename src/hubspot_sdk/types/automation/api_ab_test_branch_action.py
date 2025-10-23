# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection

__all__ = ["APIAbTestBranchAction"]


class APIAbTestBranchAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """The ID for this action."""

    test_branches: List[APIConnection] = FieldInfo(alias="testBranches")

    type: Literal["AB_TEST_BRANCH"]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """
