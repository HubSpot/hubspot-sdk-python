# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.version_user import VersionUser

__all__ = ["PageVersion"]


class PageVersion(BaseModel):
    id: str

    object: "PageData"

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser


from .page_data import PageData
