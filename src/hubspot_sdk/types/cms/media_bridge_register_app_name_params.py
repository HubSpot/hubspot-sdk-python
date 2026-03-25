# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MediaBridgeRegisterAppNameParams"]


class MediaBridgeRegisterAppNameParams(TypedDict, total=False):
    updated_at: Required[Annotated[int, PropertyInfo(alias="updatedAt")]]

    allow_import_on_disconnect: Annotated[bool, PropertyInfo(alias="allowImportOnDisconnect")]

    module_name: Annotated[str, PropertyInfo(alias="moduleName")]

    name: str
