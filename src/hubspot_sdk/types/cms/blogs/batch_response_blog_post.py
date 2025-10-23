# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BatchResponseBlogPost"]


class BatchResponseBlogPost(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """Time of batch operation completion."""

    results: List["BlogPost"]
    """Results of batch operation."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """Time of batch operation start."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """Status of batch operation."""

    links: Optional[Dict[str, str]] = None
    """Links associated with batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Time of batch operation request."""


from .blog_post import BlogPost
