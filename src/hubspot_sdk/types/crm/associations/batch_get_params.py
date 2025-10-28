# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.public_object_id import PublicObjectID

__all__ = ["BatchGetParams"]


class BatchGetParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    inputs: Required[Iterable[PublicObjectID]]
