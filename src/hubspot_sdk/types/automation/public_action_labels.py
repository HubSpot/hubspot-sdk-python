# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicActionLabels"]


class PublicActionLabels(BaseModel):
    action_name: str = FieldInfo(alias="actionName")
    """The name of the action."""

    action_card_content: Optional[str] = FieldInfo(alias="actionCardContent", default=None)
    """Content displayed on the action card."""

    action_description: Optional[str] = FieldInfo(alias="actionDescription", default=None)
    """A description of what the action does."""

    app_display_name: Optional[str] = FieldInfo(alias="appDisplayName", default=None)
    """The display name of the application associated with the action."""

    execution_rules: Optional[Dict[str, str]] = FieldInfo(alias="executionRules", default=None)
    """Rules that govern the execution of the action."""

    input_field_descriptions: Optional[Dict[str, str]] = FieldInfo(alias="inputFieldDescriptions", default=None)
    """Descriptions for each input field."""

    input_field_labels: Optional[Dict[str, str]] = FieldInfo(alias="inputFieldLabels", default=None)
    """Labels for the input fields."""

    input_field_option_labels: Optional[Dict[str, Dict[str, str]]] = FieldInfo(
        alias="inputFieldOptionLabels", default=None
    )
    """Labels for the options available in input fields."""

    output_field_labels: Optional[Dict[str, str]] = FieldInfo(alias="outputFieldLabels", default=None)
    """Labels for the output fields."""
