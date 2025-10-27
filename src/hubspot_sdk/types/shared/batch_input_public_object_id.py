# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_object_id import PublicObjectID

__all__ = ["BatchInputPublicObjectID"]


class BatchInputPublicObjectID(BaseModel):
    inputs: List[PublicObjectID]
