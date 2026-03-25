# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BehavioralEventTypeDefinitionLabels"]


class BehavioralEventTypeDefinitionLabels(BaseModel):
    singular: str

    plural: Optional[str] = None
