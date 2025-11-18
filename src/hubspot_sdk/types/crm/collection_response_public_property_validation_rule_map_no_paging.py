# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_property_validation_rule_map import PublicPropertyValidationRuleMap

__all__ = ["CollectionResponsePublicPropertyValidationRuleMapNoPaging"]


class CollectionResponsePublicPropertyValidationRuleMapNoPaging(BaseModel):
    results: List[PublicPropertyValidationRuleMap]
    """Collection of properties with their validation rules.

    Each item maps a property name to its configured validation rules for the
    specified object type.
    """
