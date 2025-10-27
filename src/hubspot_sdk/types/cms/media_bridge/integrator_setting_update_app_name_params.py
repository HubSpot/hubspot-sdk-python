# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegratorSettingUpdateAppNameParams"]


class IntegratorSettingUpdateAppNameParams(TypedDict, total=False):
    updated_at: Required[Annotated[int, PropertyInfo(alias="updatedAt")]]

    name: str
