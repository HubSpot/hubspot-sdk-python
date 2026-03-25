# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .callback_completion_batch_request_param import CallbackCompletionBatchRequestParam

__all__ = ["ActionCompleteBatchParams"]


class ActionCompleteBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[CallbackCompletionBatchRequestParam]]
