# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventDeleteByExternalEventIDParams"]


class EventDeleteByExternalEventIDParams(TypedDict, total=False):
    external_account_id: Required[Annotated[str, PropertyInfo(alias="externalAccountId")]]
