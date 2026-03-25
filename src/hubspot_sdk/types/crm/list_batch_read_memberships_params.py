# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .record_id_input_param import RecordIDInputParam

__all__ = ["ListBatchReadMembershipsParams"]


class ListBatchReadMembershipsParams(TypedDict, total=False):
    inputs: Required[Iterable[RecordIDInputParam]]
