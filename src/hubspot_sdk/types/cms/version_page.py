# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.version_user import VersionUser

__all__ = ["VersionPage"]


class VersionPage(BaseModel):
    """Model definition for a landing page or site page version.

    Contains metadata describing the version of the page. It can be used to view edit history of a page.
    """

    id: str
    """ID of this page version."""

    object: "Page"
    """Model definition for a landing page or site page."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser
    """Model definition for a version user.

    Contains addition information about the user who created a version.
    """


from .page import Page
