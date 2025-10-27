# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegratorSettingCreateObjectDefinitionParams"]


class IntegratorSettingCreateObjectDefinitionParams(TypedDict, total=False):
    media_types: Required[
        Annotated[List[Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"]], PropertyInfo(alias="mediaTypes")]
    ]
