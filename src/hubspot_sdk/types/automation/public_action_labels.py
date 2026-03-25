# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicActionLabels"]


class PublicActionLabels(BaseModel):
    action_name: str = FieldInfo(alias="actionName")

    action_card_content: Optional[str] = FieldInfo(alias="actionCardContent", default=None)

    action_description: Optional[str] = FieldInfo(alias="actionDescription", default=None)

    app_display_name: Optional[str] = FieldInfo(alias="appDisplayName", default=None)

    execution_rules: Optional[Dict[str, str]] = FieldInfo(alias="executionRules", default=None)

    input_field_descriptions: Optional[Dict[str, str]] = FieldInfo(alias="inputFieldDescriptions", default=None)

    input_field_labels: Optional[Dict[str, str]] = FieldInfo(alias="inputFieldLabels", default=None)

    input_field_option_labels: Optional[Dict[str, Dict[str, str]]] = FieldInfo(
        alias="inputFieldOptionLabels", default=None
    )

    output_field_labels: Optional[Dict[str, str]] = FieldInfo(alias="outputFieldLabels", default=None)
