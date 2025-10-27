# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ObjectTypeDefinitionLabels"]


class ObjectTypeDefinitionLabels(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None
