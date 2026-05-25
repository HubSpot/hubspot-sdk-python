# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .crm_filter_param import CrmFilterParam

__all__ = ["FilterGroupParam"]


class FilterGroupParam(TypedDict, total=False):
    filters: Required[Iterable[CrmFilterParam]]
