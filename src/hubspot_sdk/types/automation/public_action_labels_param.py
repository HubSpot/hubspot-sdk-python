# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicActionLabelsParam"]


class PublicActionLabelsParam(TypedDict, total=False):
    action_name: Required[Annotated[str, PropertyInfo(alias="actionName")]]

    action_card_content: Annotated[str, PropertyInfo(alias="actionCardContent")]

    action_description: Annotated[str, PropertyInfo(alias="actionDescription")]

    app_display_name: Annotated[str, PropertyInfo(alias="appDisplayName")]

    execution_rules: Annotated[Dict[str, str], PropertyInfo(alias="executionRules")]

    input_field_descriptions: Annotated[Dict[str, str], PropertyInfo(alias="inputFieldDescriptions")]

    input_field_labels: Annotated[Dict[str, str], PropertyInfo(alias="inputFieldLabels")]

    input_field_option_labels: Annotated[Dict[str, Dict[str, str]], PropertyInfo(alias="inputFieldOptionLabels")]

    output_field_labels: Annotated[Dict[str, str], PropertyInfo(alias="outputFieldLabels")]
