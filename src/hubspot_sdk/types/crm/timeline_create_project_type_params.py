# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimelineCreateProjectTypeParams"]


class TimelineCreateProjectTypeParams(TypedDict, total=False):
    developer_symbol: Required[Annotated[str, PropertyInfo(alias="developerSymbol")]]

    project_name: Required[Annotated[str, PropertyInfo(alias="projectName")]]
