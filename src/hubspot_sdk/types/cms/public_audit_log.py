# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAuditLog"]


class PublicAuditLog(BaseModel):
    event: Literal["CREATED", "DELETED", "PUBLISHED", "RESTORE", "UNPUBLISHED", "UPDATED"]
    """
    The type of event that took place (CREATED, UPDATED, PUBLISHED, DELETED,
    UNPUBLISHED).
    """

    full_name: str = FieldInfo(alias="fullName")
    """The name of the user who caused the event."""

    object_id: str = FieldInfo(alias="objectId")
    """The ID of the object."""

    object_name: str = FieldInfo(alias="objectName")
    """The internal name of the object in HubSpot."""

    object_type: Literal[
        "BLOG",
        "BLOG_POST",
        "CONTENT_SETTINGS",
        "CSS",
        "CTA",
        "DOMAIN",
        "EMAIL",
        "FILE",
        "GLOBAL_MODULE",
        "HUBDB_TABLE",
        "JS",
        "KNOWLEDGE_BASE",
        "KNOWLEDGE_BASE_ARTICLE",
        "LANDING_PAGE",
        "MODULE",
        "SERVERLESS_FUNCTION",
        "TEMPLATE",
        "THEME",
        "URL_MAPPING",
        "WEBSITE_PAGE",
    ] = FieldInfo(alias="objectType")
    """The type of the object (BLOG, LANDING_PAGE, DOMAIN, HUBDB_TABLE etc.)"""

    timestamp: datetime
    """The timestamp at which the event occurred."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user who caused the event."""

    meta: Optional[object] = None
    """Supplementary metadata associated with the audit log entry.

    It provides additional context about the audited event (ex: rows deleted/updated
    for a HubDB event, the specific fields that were changed for a Content Settings
    event).
    """
