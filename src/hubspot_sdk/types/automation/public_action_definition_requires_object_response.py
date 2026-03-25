# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicActionDefinitionRequiresObjectResponse"]


class PublicActionDefinitionRequiresObjectResponse(BaseModel):
    requires_object: bool = FieldInfo(alias="requiresObject")
