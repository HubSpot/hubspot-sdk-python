# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SimplePublicObjectBatchInputUpsertParam"]


class SimplePublicObjectBatchInputUpsertParam(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the object."""

    properties: Required[Dict[str, str]]
    """Key value pairs representing the properties of the object."""

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
    """
    The name of a unique identifier property, which can be used for identifying
    objects instead of the object ID.
    """

    object_write_trace_id: Annotated[str, PropertyInfo(alias="objectWriteTraceId")]
    """An identifier for tracing the creation request."""
