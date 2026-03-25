# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWebversionDetails"]


class PublicWebversionDetails(BaseModel):
    domain: Optional[str] = None

    enabled: Optional[bool] = None

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    is_page_redirected: Optional[bool] = FieldInfo(alias="isPageRedirected", default=None)

    meta_description: Optional[str] = FieldInfo(alias="metaDescription", default=None)

    page_expiry_enabled: Optional[bool] = FieldInfo(alias="pageExpiryEnabled", default=None)

    redirect_to_page_id: Optional[str] = FieldInfo(alias="redirectToPageId", default=None)

    redirect_to_url: Optional[str] = FieldInfo(alias="redirectToUrl", default=None)

    slug: Optional[str] = None

    title: Optional[str] = None

    url: Optional[str] = None
