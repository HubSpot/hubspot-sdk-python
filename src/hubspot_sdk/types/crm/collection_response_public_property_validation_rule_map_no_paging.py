# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_property_validation_rule_map import PublicPropertyValidationRuleMap

__all__ = ["CollectionResponsePublicPropertyValidationRuleMapNoPaging"]


class CollectionResponsePublicPropertyValidationRuleMapNoPaging(BaseModel):
    results: List[PublicPropertyValidationRuleMap]
