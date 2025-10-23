# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIFlowListing"]


class APIFlowListing(BaseModel):
    id: str
    """The unique ID for this flow. This is auto-generated when creating the flow."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp this flow was created."""

    flow_type: str = FieldInfo(alias="flowType")
    """Deprecated. Will be removed."""

    is_enabled: bool = FieldInfo(alias="isEnabled")
    """
    This controls whether or not the flow is "enabled" if it's actively listening
    for enrollment triggers and executing actions. If this is `false` the flow is
    not accepting any enrollments or executing any actions.
    """

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The CRM object type for objects that can be enrolled into this flow."""

    revision_id: str = FieldInfo(alias="revisionId")
    """Deprecated. Will be removed."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp this flow was last updated."""

    name: Optional[str] = None
    """The user-provided name for this flow.

    Names get auto-created for workflows that are created without a name.
    """

    uuid: Optional[str] = None
    """An optional unique key for this flow. This is only unique per-portal."""
