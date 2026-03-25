# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...shared_params.property_name import PropertyName

__all__ = ["BatchDeleteParams"]


class BatchDeleteParams(TypedDict, total=False):
    inputs: Required[Iterable[PropertyName]]
