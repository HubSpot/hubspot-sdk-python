# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicActionLabelsParam"]


class PublicActionLabelsParam(TypedDict, total=False):
    action_name: Required[Annotated[str, PropertyInfo(alias="actionName")]]
    """The name of the action."""

    action_card_content: Annotated[str, PropertyInfo(alias="actionCardContent")]
    """Content displayed on the action card."""

    action_description: Annotated[str, PropertyInfo(alias="actionDescription")]
    """A description of what the action does."""

    app_display_name: Annotated[str, PropertyInfo(alias="appDisplayName")]
    """The display name of the application associated with the action."""

    execution_rules: Annotated[Dict[str, str], PropertyInfo(alias="executionRules")]
    """Rules that govern the execution of the action."""

    input_field_descriptions: Annotated[Dict[str, str], PropertyInfo(alias="inputFieldDescriptions")]
    """Descriptions for each input field."""

    input_field_labels: Annotated[Dict[str, str], PropertyInfo(alias="inputFieldLabels")]
    """Labels for the input fields."""

    input_field_option_labels: Annotated[Dict[str, Dict[str, str]], PropertyInfo(alias="inputFieldOptionLabels")]
    """Labels for the options available in input fields."""

    output_field_labels: Annotated[Dict[str, str], PropertyInfo(alias="outputFieldLabels")]
    """Labels for the output fields."""
