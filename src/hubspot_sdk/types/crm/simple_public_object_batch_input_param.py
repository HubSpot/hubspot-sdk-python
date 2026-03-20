# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SimplePublicObjectBatchInputParam"]


class SimplePublicObjectBatchInputParam(TypedDict, total=False):
    """
    Contains an array of CRM object records to be processed in a batch operation, each defined by their ID and properties.
    """

    id: Required[str]
    """The ID of the contact to update.

    This can be the object ID, or the unique property value of the `idProperty`
    property.
    """

    properties: Required[Dict[str, str]]
    """Key-value pairs representing the properties of the object."""

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
    """The name of a unique property, when identifying records by property."""

    object_write_trace_id: Annotated[str, PropertyInfo(alias="objectWriteTraceId")]
    """A unique identifier for tracing the request."""
