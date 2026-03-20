# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .association_spec_param import AssociationSpecParam
from .public_object_id_param import PublicObjectIDParam

__all__ = ["PublicAssociationsForObjectParam"]


class PublicAssociationsForObjectParam(TypedDict, total=False):
    to: Required[PublicObjectIDParam]
    """Contains the Id of a Public Object"""

    types: Required[Iterable[AssociationSpecParam]]
