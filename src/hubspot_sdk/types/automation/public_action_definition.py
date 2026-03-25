# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_action_labels import PublicActionLabels
from .public_input_field_definition import PublicInputFieldDefinition
from .public_object_request_options import PublicObjectRequestOptions
from .public_single_field_dependency import PublicSingleFieldDependency
from .public_action_function_identifier import PublicActionFunctionIdentifier
from .public_execution_translation_rule import PublicExecutionTranslationRule
from .public_conditional_single_field_dependency import PublicConditionalSingleFieldDependency

__all__ = ["PublicActionDefinition", "InputFieldDependency"]

InputFieldDependency: TypeAlias = Union[PublicSingleFieldDependency, PublicConditionalSingleFieldDependency]


class PublicActionDefinition(BaseModel):
    id: str

    action_url: str = FieldInfo(alias="actionUrl")

    functions: List[PublicActionFunctionIdentifier]

    input_fields: List[PublicInputFieldDefinition] = FieldInfo(alias="inputFields")

    labels: Dict[str, PublicActionLabels]

    object_types: List[str] = FieldInfo(alias="objectTypes")

    published: bool

    revision_id: str = FieldInfo(alias="revisionId")

    archived_at: Optional[int] = FieldInfo(alias="archivedAt", default=None)

    execution_rules: Optional[List[PublicExecutionTranslationRule]] = FieldInfo(alias="executionRules", default=None)

    input_field_dependencies: Optional[List[InputFieldDependency]] = FieldInfo(
        alias="inputFieldDependencies", default=None
    )

    object_request_options: Optional[PublicObjectRequestOptions] = FieldInfo(alias="objectRequestOptions", default=None)

    output_fields: Optional[List["OutputFieldDefinition"]] = FieldInfo(alias="outputFields", default=None)


from .output_field_definition import OutputFieldDefinition
