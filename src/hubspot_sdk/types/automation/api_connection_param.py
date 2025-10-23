# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIConnectionParam"]


class APIConnectionParam(TypedDict, total=False):
    edge_type: Required[Annotated[str, PropertyInfo(alias="edgeType")]]

    next_action_id: Required[Annotated[str, PropertyInfo(alias="nextActionId")]]
