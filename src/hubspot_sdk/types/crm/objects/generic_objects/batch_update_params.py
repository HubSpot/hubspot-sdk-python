# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...simple_public_object_batch_input_param import SimplePublicObjectBatchInputParam

__all__ = ["BatchUpdateParams"]


class BatchUpdateParams(TypedDict, total=False):
    inputs: Required[Iterable[SimplePublicObjectBatchInputParam]]
