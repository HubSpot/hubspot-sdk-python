# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["DefinitionCreateParams"]


class DefinitionCreateParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    label: Required[str]

    name: Required[str]

    inverse_label: Annotated[str, PropertyInfo(alias="inverseLabel")]
