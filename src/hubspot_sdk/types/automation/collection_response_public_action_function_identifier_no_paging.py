# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_action_function_identifier import PublicActionFunctionIdentifier

__all__ = ["CollectionResponsePublicActionFunctionIdentifierNoPaging"]


class CollectionResponsePublicActionFunctionIdentifierNoPaging(BaseModel):
    results: List[PublicActionFunctionIdentifier]
