# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.public_object_id import PublicObjectID

__all__ = ["CurrencyBatchGetParams"]


class CurrencyBatchGetParams(TypedDict, total=False):
    inputs: Required[Iterable[PublicObjectID]]
