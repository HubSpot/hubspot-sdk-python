# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.public_object_id import PublicObjectID
from .associations.association_spec_1_param import AssociationSpec1Param

__all__ = ["PublicAssociationsForObjectParam"]


class PublicAssociationsForObjectParam(TypedDict, total=False):
    to: Required[PublicObjectID]

    types: Required[Iterable[AssociationSpec1Param]]
