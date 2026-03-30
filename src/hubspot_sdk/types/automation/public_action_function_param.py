# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicActionFunctionParam"]


class PublicActionFunctionParam(TypedDict, total=False):
    function_source: Required[Annotated[str, PropertyInfo(alias="functionSource")]]
    """The source code or script that defines the function's behavior."""

    function_type: Required[
        Annotated[
            Literal["POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"],
            PropertyInfo(alias="functionType"),
        ]
    ]
    """
    The type of function, with accepted values: POST_ACTION_EXECUTION,
    POST_FETCH_OPTIONS, PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS.
    """

    id: str
    """The unique identifier for the action function."""
