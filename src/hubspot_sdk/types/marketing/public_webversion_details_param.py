# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicWebversionDetailsParam"]


class PublicWebversionDetailsParam(TypedDict, total=False):
    domain: str

    enabled: bool

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    is_page_redirected: Annotated[bool, PropertyInfo(alias="isPageRedirected")]

    meta_description: Annotated[str, PropertyInfo(alias="metaDescription")]

    page_expiry_enabled: Annotated[bool, PropertyInfo(alias="pageExpiryEnabled")]

    redirect_to_page_id: Annotated[str, PropertyInfo(alias="redirectToPageId")]

    redirect_to_url: Annotated[str, PropertyInfo(alias="redirectToUrl")]

    slug: str

    title: str

    url: str
