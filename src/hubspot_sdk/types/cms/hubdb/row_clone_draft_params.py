# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RowCloneDraftParams"]


class RowCloneDraftParams(TypedDict, total=False):
    table_id_or_name: Required[Annotated[str, PropertyInfo(alias="tableIdOrName")]]

    name: str
