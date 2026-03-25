# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared_params.public_object_id import PublicObjectID

__all__ = ["PublicDefaultAssociationMultiPostParam"]

_PublicDefaultAssociationMultiPostParamReservedKeywords = TypedDict(
    "_PublicDefaultAssociationMultiPostParamReservedKeywords",
    {
        "from": PublicObjectID,
    },
    total=False,
)


class PublicDefaultAssociationMultiPostParam(_PublicDefaultAssociationMultiPostParamReservedKeywords, total=False):
    to: Required[PublicObjectID]
    """Contains the Id of a Public Object"""
