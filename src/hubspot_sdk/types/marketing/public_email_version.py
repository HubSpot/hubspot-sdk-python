# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_email import PublicEmail
from ..shared.version_user import VersionUser

__all__ = ["PublicEmailVersion"]


class PublicEmailVersion(BaseModel):
    id: str

    object: PublicEmail

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser
