# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FunctionCreateOrReplaceByFunctionTypeParams"]


class FunctionCreateOrReplaceByFunctionTypeParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    definition_id: Required[Annotated[str, PropertyInfo(alias="definitionId")]]

    body: Required[str]
