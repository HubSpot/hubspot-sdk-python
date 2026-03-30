# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..hub_db_table_row_batch_clone_request_param import HubDBTableRowBatchCloneRequestParam

__all__ = ["RowCloneBatchParams"]


class RowCloneBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[HubDBTableRowBatchCloneRequestParam]]
