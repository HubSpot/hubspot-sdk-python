# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .cms_audit_logging_export_filters_param import CmsAuditLoggingExportFiltersParam

__all__ = ["AuditLogExportParams"]


class AuditLogExportParams(TypedDict, total=False):
    email: Required[str]

    format: Required[Literal["CSV", "XLS", "XLSX"]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    recipient_user_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="recipientUserIds")]]

    should_mark_export_file_as_sensitive: Required[
        Annotated[bool, PropertyInfo(alias="shouldMarkExportFileAsSensitive")]
    ]

    type: Required[str]

    filters: CmsAuditLoggingExportFiltersParam

    partition: int

    user_id: Annotated[int, PropertyInfo(alias="userId")]

    user_time_zone: Annotated[str, PropertyInfo(alias="userTimeZone")]
