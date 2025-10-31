# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAuditLog"]


class PublicAuditLog(BaseModel):
    event: Literal["CREATED", "UPDATED", "PUBLISHED", "DELETED", "UNPUBLISHED", "RESTORE"]
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
        "LANDING_PAGE",
        "WEBSITE_PAGE",
        "TEMPLATE",
        "MODULE",
        "GLOBAL_MODULE",
        "SERVERLESS_FUNCTION",
        "DOMAIN",
        "URL_MAPPING",
        "EMAIL",
        "CONTENT_SETTINGS",
        "HUBDB_TABLE",
        "KNOWLEDGE_BASE_ARTICLE",
        "KNOWLEDGE_BASE",
        "THEME",
        "CSS",
        "JS",
        "CTA",
        "FILE",
    ] = FieldInfo(alias="objectType")
    """The type of the object (BLOG, LANDING_PAGE, DOMAIN, HUBDB_TABLE etc.)"""

    timestamp: datetime
    """The timestamp at which the event occurred."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user who caused the event."""

    meta: Optional[object] = None
