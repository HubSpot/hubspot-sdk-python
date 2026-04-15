# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .property_create import PropertyCreate

__all__ = ["BatchInputPropertyCreate"]


class BatchInputPropertyCreate(BaseModel):
    inputs: List[PropertyCreate]
