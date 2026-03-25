# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .contact_id_param import ContactIDParam

__all__ = ["ComplianceIDsParam"]


class ComplianceIDsParam(TypedDict, total=False):
    contact_ids: Required[Annotated[Iterable[ContactIDParam], PropertyInfo(alias="contactIds")]]

    portal_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="portalIds")]]

    user_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="userIds")]]

    no_contact_id_reason: Annotated[str, PropertyInfo(alias="noContactIdReason")]

    no_portal_id_reason: Annotated[str, PropertyInfo(alias="noPortalIdReason")]

    no_user_id_reason: Annotated[str, PropertyInfo(alias="noUserIdReason")]
