# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

__all__ = ["APIFlowPutRequestParam"]

APIFlowPutRequestParam: TypeAlias = Union["APIContactFlowPutRequestParam", "APIPlatformFlowPutRequestParam"]

from .api_contact_flow_put_request_param import APIContactFlowPutRequestParam
from .api_platform_flow_put_request_param import APIPlatformFlowPutRequestParam
