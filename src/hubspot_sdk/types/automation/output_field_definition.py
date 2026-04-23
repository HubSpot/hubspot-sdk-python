# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .field_type_definition import FieldTypeDefinition

__all__ = ["OutputFieldDefinition"]


class OutputFieldDefinition(BaseModel):
    type_definition: FieldTypeDefinition = FieldInfo(alias="typeDefinition")
