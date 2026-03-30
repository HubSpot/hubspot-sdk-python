# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicActionRevision"]


class PublicActionRevision(BaseModel):
    id: str
    """The unique identifier for the action revision."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the action revision was created."""

    definition: "PublicActionDefinition"

    revision_id: str = FieldInfo(alias="revisionId")
    """The unique identifier for the specific revision of the action."""


from .public_action_definition import PublicActionDefinition
