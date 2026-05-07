# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CardMigrateViewsResponse"]


class CardMigrateViewsResponse(BaseModel):
    message: str
    """A human readable message describing the progress of the migration."""

    ended_at: Optional[int] = FieldInfo(alias="endedAt", default=None)
    """The timestamp for when the migration ended."""

    remaining_portal_count: Optional[int] = FieldInfo(alias="remainingPortalCount", default=None)
    """
    The number of portals that remain to be swapped from the Legacy CRM Card to the
    App Card
    """

    started_at: Optional[int] = FieldInfo(alias="startedAt", default=None)
    """The timestamp for when the migration started."""

    total_portal_count: Optional[int] = FieldInfo(alias="totalPortalCount", default=None)
    """The total number of portals that have access to the Legacy CRM Card"""
