# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...shared_params.public_object_id import PublicObjectID

__all__ = ["PublicAssociationMultiArchiveParam"]

_PublicAssociationMultiArchiveParamReservedKeywords = TypedDict(
    "_PublicAssociationMultiArchiveParamReservedKeywords",
    {
        "from": PublicObjectID,
    },
    total=False,
)


class PublicAssociationMultiArchiveParam(_PublicAssociationMultiArchiveParamReservedKeywords, total=False):
    to: Required[Iterable[PublicObjectID]]
