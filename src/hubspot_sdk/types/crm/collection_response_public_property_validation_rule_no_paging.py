# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_property_validation_rule import PublicPropertyValidationRule

__all__ = ["CollectionResponsePublicPropertyValidationRuleNoPaging"]


class CollectionResponsePublicPropertyValidationRuleNoPaging(BaseModel):
    results: List[PublicPropertyValidationRule]
