# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TableUnpublishParams"]


class TableUnpublishParams(TypedDict, total=False):
    include_foreign_ids: Annotated[bool, PropertyInfo(alias="includeForeignIds")]
