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
    """The ID for this action."""

    input_fields: List[APIInputVariable] = FieldInfo(alias="inputFields")

    output_fields: List[APIEnumerationOutputField] = FieldInfo(alias="outputFields")
    """
    The list of output fields that this custom action makes available to the rest of
    the flow.
    """

    runtime: str
    """The runtime to use to execute the source code.

    Supported runtimes are: "NODE16X", "NODE20X", "PYTHON39"
    """

    secret_names: List[str] = FieldInfo(alias="secretNames")
    """
    The names of any "secrets" setup in this portal that will be used in this
    action.
    """

    source_code: str = FieldInfo(alias="sourceCode")
    """The source code to execute when this action executes."""

    type: Literal["CUSTOM_CODE"]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    connection: Optional[APIConnection] = None
