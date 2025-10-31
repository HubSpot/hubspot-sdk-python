# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam

__all__ = ["APIStaticBranchParam"]


class APIStaticBranchParam(TypedDict, total=False):
    branch_value: Required[Annotated[str, PropertyInfo(alias="branchValue")]]

    connection: APIConnectionParam
