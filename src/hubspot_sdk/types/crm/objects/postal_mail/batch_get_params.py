# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo
from ...simple_public_object_id_param import SimplePublicObjectIDParam

__all__ = ["BatchGetParams"]


class BatchGetParams(TypedDict, total=False):
    inputs: Required[Iterable[SimplePublicObjectIDParam]]

    properties: Required[SequenceNotStr[str]]
    """Key-value pairs for setting properties for the new object."""

    properties_with_history: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="propertiesWithHistory")]]
    """Key-value pairs for setting properties for the new object and their histories."""

    archived: bool

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
