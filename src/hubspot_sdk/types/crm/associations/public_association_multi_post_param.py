# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .association_spec_1_param import AssociationSpec1Param
from ...shared_params.public_object_id import PublicObjectID

__all__ = ["PublicAssociationMultiPostParam"]

_PublicAssociationMultiPostParamReservedKeywords = TypedDict(
    "_PublicAssociationMultiPostParamReservedKeywords",
    {
        "from": PublicObjectID,
    },
    total=False,
)


class PublicAssociationMultiPostParam(_PublicAssociationMultiPostParamReservedKeywords, total=False):
    to: Required[PublicObjectID]

    types: Required[Iterable[AssociationSpec1Param]]
