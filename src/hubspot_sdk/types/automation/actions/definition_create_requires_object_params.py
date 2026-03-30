# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DefinitionCreateRequiresObjectParams"]


class DefinitionCreateRequiresObjectParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    requires_object: Required[Annotated[bool, PropertyInfo(alias="requiresObject")]]
    """Indicates whether a custom action definition requires an associated object."""
