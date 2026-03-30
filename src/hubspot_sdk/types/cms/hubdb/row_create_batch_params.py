# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..hub_db_table_row_v3_request_param import HubDBTableRowV3RequestParam

__all__ = ["RowCreateBatchParams"]


class RowCreateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[HubDBTableRowV3RequestParam]]
