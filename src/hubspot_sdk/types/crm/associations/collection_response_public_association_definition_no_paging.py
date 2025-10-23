# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .public_association_definition import PublicAssociationDefinition

__all__ = ["CollectionResponsePublicAssociationDefinitionNoPaging"]


class CollectionResponsePublicAssociationDefinitionNoPaging(BaseModel):
    results: List[PublicAssociationDefinition]
