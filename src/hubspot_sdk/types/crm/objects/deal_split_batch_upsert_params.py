# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DealSplitBatchUpsertParams", "Input", "InputSplit"]


class DealSplitBatchUpsertParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]


class InputSplit(TypedDict, total=False):
    owner_id: Required[Annotated[int, PropertyInfo(alias="ownerId")]]

    percentage: Required[float]


class Input(TypedDict, total=False):
    id: Required[int]

    splits: Required[Iterable[InputSplit]]
