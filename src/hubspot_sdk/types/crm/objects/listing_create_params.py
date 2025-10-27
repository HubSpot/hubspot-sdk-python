# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..public_associations_for_object_param import PublicAssociationsForObjectParam

__all__ = ["ListingCreateParams"]


class ListingCreateParams(TypedDict, total=False):
    properties: Required[Dict[str, str]]
    """Key-value pairs for setting properties for the new object."""

    associations: Iterable[PublicAssociationsForObjectParam]
