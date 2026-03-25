# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .public_action_labels_param import PublicActionLabelsParam
from .public_action_function_param import PublicActionFunctionParam
from .public_input_field_definition_param import PublicInputFieldDefinitionParam
from .public_object_request_options_param import PublicObjectRequestOptionsParam
from .public_single_field_dependency_param import PublicSingleFieldDependencyParam
from .public_execution_translation_rule_param import PublicExecutionTranslationRuleParam
from .public_conditional_single_field_dependency_param import PublicConditionalSingleFieldDependencyParam

__all__ = ["ActionCreateParams", "InputFieldDependency"]


class ActionCreateParams(TypedDict, total=False):
    action_url: Required[Annotated[str, PropertyInfo(alias="actionUrl")]]

    functions: Required[Iterable[PublicActionFunctionParam]]

    input_fields: Required[Annotated[Iterable[PublicInputFieldDefinitionParam], PropertyInfo(alias="inputFields")]]

    labels: Required[Dict[str, PublicActionLabelsParam]]

    object_types: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectTypes")]]

    published: Required[bool]

    archived_at: Annotated[int, PropertyInfo(alias="archivedAt")]

    execution_rules: Annotated[Iterable[PublicExecutionTranslationRuleParam], PropertyInfo(alias="executionRules")]

    input_field_dependencies: Annotated[Iterable[InputFieldDependency], PropertyInfo(alias="inputFieldDependencies")]

    object_request_options: Annotated[PublicObjectRequestOptionsParam, PropertyInfo(alias="objectRequestOptions")]

    output_fields: Annotated[Iterable["OutputFieldDefinitionParam"], PropertyInfo(alias="outputFields")]


InputFieldDependency: TypeAlias = Union[PublicSingleFieldDependencyParam, PublicConditionalSingleFieldDependencyParam]

from .output_field_definition_param import OutputFieldDefinitionParam
