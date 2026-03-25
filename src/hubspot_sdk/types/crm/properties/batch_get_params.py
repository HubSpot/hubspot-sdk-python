# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.property_name import PropertyName

__all__ = ["BatchGetParams"]


class BatchGetParams(TypedDict, total=False):
    archived: Required[bool]

    data_sensitivity: Required[
        Annotated[Literal["highly_sensitive", "non_sensitive", "sensitive"], PropertyInfo(alias="dataSensitivity")]
    ]

    inputs: Required[Iterable[PropertyName]]

    locale: str
