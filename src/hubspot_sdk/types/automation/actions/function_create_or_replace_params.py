# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FunctionCreateOrReplaceParams"]


class FunctionCreateOrReplaceParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    definition_id: Required[Annotated[str, PropertyInfo(alias="definitionId")]]

    function_type: Required[
        Annotated[
            Literal["PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"],
            PropertyInfo(alias="functionType"),
        ]
    ]

    body: Required[str]
