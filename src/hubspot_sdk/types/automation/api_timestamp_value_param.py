# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APITimestampValueParam"]


class APITimestampValueParam(TypedDict, total=False):
    timestamp_type: Required[Annotated[Literal["EXECUTION_TIME"], PropertyInfo(alias="timestampType")]]

    type: Required[Literal["TIMESTAMP"]]
