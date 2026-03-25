# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectSchemaListParams"]


class ObjectSchemaListParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    include_association_definitions: Annotated[bool, PropertyInfo(alias="includeAssociationDefinitions")]

    include_audit_metadata: Annotated[bool, PropertyInfo(alias="includeAuditMetadata")]

    include_property_definitions: Annotated[bool, PropertyInfo(alias="includePropertyDefinitions")]
