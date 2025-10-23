# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIFlowBatchFetchFlowIDCoordinateParam"]


class APIFlowBatchFetchFlowIDCoordinateParam(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]

    type: Required[Literal["FLOW_ID"]]
