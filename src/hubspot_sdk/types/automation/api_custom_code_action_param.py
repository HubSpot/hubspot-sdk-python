# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam
from .api_input_variable_param import APIInputVariableParam
from .api_enumeration_output_field_param import APIEnumerationOutputFieldParam

__all__ = ["APICustomCodeActionParam"]


class APICustomCodeActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]
    """The ID for this action."""

    input_fields: Required[Annotated[Iterable[APIInputVariableParam], PropertyInfo(alias="inputFields")]]

    output_fields: Required[Annotated[Iterable[APIEnumerationOutputFieldParam], PropertyInfo(alias="outputFields")]]
    """
    The list of output fields that this custom action makes available to the rest of
    the flow.
    """

    runtime: Required[str]
    """The runtime to use to execute the source code.

    Supported runtimes are: "NODE16X", "NODE20X", "PYTHON39"
    """

    secret_names: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="secretNames")]]
    """
    The names of any "secrets" setup in this portal that will be used in this
    action.
    """

    source_code: Required[Annotated[str, PropertyInfo(alias="sourceCode")]]
    """The source code to execute when this action executes."""

    type: Required[Literal["CUSTOM_CODE"]]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    connection: APIConnectionParam
