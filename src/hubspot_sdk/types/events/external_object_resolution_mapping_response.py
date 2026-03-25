# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_primary_object_resolution_rule import ExternalPrimaryObjectResolutionRule

__all__ = ["ExternalObjectResolutionMappingResponse"]


class ExternalObjectResolutionMappingResponse(BaseModel):
    primary_object_rule: ExternalPrimaryObjectResolutionRule = FieldInfo(alias="primaryObjectRule")
