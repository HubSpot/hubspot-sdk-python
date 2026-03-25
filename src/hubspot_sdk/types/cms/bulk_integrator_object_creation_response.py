# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BulkIntegratorObjectCreationResponse"]


class BulkIntegratorObjectCreationResponse(BaseModel):
    created_objects: Dict[str, "IntegratorObjectCreationResponse"] = FieldInfo(alias="createdObjects")


from .integrator_object_creation_response import IntegratorObjectCreationResponse
