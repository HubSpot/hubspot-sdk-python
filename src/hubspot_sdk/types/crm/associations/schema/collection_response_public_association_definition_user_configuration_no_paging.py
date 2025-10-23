# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .public_association_definition_user_configuration import PublicAssociationDefinitionUserConfiguration

__all__ = ["CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging"]


class CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging(BaseModel):
    results: List[PublicAssociationDefinitionUserConfiguration]
