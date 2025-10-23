# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

__all__ = ["APIFlowCreateRequestParam"]

APIFlowCreateRequestParam: TypeAlias = Union["APIContactFlowCreateRequestParam", "APIPlatformFlowCreateRequestParam"]

from .api_contact_flow_create_request_param import APIContactFlowCreateRequestParam
from .api_platform_flow_create_request_param import APIPlatformFlowCreateRequestParam
