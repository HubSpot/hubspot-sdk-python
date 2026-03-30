# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["BatchGetParams"]


class BatchGetParams(TypedDict, total=False):
    include_association_definitions: Required[Annotated[bool, PropertyInfo(alias="includeAssociationDefinitions")]]
    """Indicates whether to include association definitions in the response."""

    include_audit_metadata: Required[Annotated[bool, PropertyInfo(alias="includeAuditMetadata")]]
    """Indicates whether to include audit metadata in the response."""

    include_property_definitions: Required[Annotated[bool, PropertyInfo(alias="includePropertyDefinitions")]]
    """Indicates whether to include property definitions in the response."""

    inputs: Required[SequenceNotStr[str]]
