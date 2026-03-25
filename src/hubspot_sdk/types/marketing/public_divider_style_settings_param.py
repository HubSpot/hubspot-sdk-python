# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDividerStyleSettingsParam"]


class PublicDividerStyleSettingsParam(TypedDict, total=False):
    color: object

    height: int

    line_type: Annotated[str, PropertyInfo(alias="lineType")]
