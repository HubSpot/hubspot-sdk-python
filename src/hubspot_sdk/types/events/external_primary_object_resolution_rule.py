# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalPrimaryObjectResolutionRule"]


class ExternalPrimaryObjectResolutionRule(BaseModel):
    event_property_name: str = FieldInfo(alias="eventPropertyName")

    target_object_property_name: str = FieldInfo(alias="targetObjectPropertyName")
