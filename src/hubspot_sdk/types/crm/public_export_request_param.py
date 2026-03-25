# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .public_export_list_request_param import PublicExportListRequestParam
from .public_export_view_request_param import PublicExportViewRequestParam

__all__ = ["PublicExportRequestParam"]

PublicExportRequestParam: TypeAlias = Union[PublicExportViewRequestParam, PublicExportListRequestParam]
