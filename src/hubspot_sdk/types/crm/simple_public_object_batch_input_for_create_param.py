# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_associations_for_object_param import PublicAssociationsForObjectParam

__all__ = ["SimplePublicObjectBatchInputForCreateParam"]


class SimplePublicObjectBatchInputForCreateParam(TypedDict, total=False):
    """
    An input object that contains a collection of objects to be created together in a batch.
    """

    associations: Required[Iterable[PublicAssociationsForObjectParam]]

    properties: Required[Dict[str, str]]
    """Key value pairs representing the properties of the object."""

    object_write_trace_id: Annotated[str, PropertyInfo(alias="objectWriteTraceId")]
    """An identifier used for tracing the creation or update request of the object."""
