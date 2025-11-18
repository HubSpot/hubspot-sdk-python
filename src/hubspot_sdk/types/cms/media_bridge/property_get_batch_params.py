# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.property_name import PropertyName

__all__ = ["PropertyGetBatchParams"]


class PropertyGetBatchParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    archived: Required[bool]

    data_sensitivity: Required[
        Annotated[Literal["non_sensitive", "sensitive", "highly_sensitive"], PropertyInfo(alias="dataSensitivity")]
    ]

    inputs: Required[Iterable[PropertyName]]
