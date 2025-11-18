# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ....shared.paging import Paging
from .public_association_definition_user_configuration import PublicAssociationDefinitionUserConfiguration

__all__ = ["CollectionResponsePublicAssociationDefinitionUserConfiguration"]


class CollectionResponsePublicAssociationDefinitionUserConfiguration(BaseModel):
    results: List[PublicAssociationDefinitionUserConfiguration]

    paging: Optional[Paging] = None
