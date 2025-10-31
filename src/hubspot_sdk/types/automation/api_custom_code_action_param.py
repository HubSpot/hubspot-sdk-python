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

    input_fields: Required[Annotated[Iterable[APIInputVariableParam], PropertyInfo(alias="inputFields")]]

    output_fields: Required[Annotated[Iterable[APIEnumerationOutputFieldParam], PropertyInfo(alias="outputFields")]]

    runtime: Required[str]

    secret_names: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="secretNames")]]

    source_code: Required[Annotated[str, PropertyInfo(alias="sourceCode")]]

    type: Required[Literal["CUSTOM_CODE"]]

    connection: APIConnectionParam
