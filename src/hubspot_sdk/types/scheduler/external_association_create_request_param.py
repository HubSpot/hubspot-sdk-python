# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.association_spec import AssociationSpec
from ..shared_params.public_object_id import PublicObjectID

__all__ = ["ExternalAssociationCreateRequestParam"]


class ExternalAssociationCreateRequestParam(TypedDict, total=False):
    to: Required[PublicObjectID]

    types: Required[Iterable[AssociationSpec]]
