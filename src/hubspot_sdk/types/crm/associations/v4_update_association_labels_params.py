# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .association_spec_1_param import AssociationSpec1Param

__all__ = ["V4UpdateAssociationLabelsParams"]


class V4UpdateAssociationLabelsParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    to_object_type: Required[Annotated[str, PropertyInfo(alias="toObjectType")]]

    body: Required[Iterable[AssociationSpec1Param]]
