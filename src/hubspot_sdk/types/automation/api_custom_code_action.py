# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection
from .api_input_variable import APIInputVariable
from .api_enumeration_output_field import APIEnumerationOutputField

__all__ = ["APICustomCodeAction"]


class APICustomCodeAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")

    input_fields: List[APIInputVariable] = FieldInfo(alias="inputFields")

    output_fields: List[APIEnumerationOutputField] = FieldInfo(alias="outputFields")

    runtime: str

    secret_names: List[str] = FieldInfo(alias="secretNames")

    source_code: str = FieldInfo(alias="sourceCode")

    type: Literal["CUSTOM_CODE"]

    connection: Optional[APIConnection] = None
