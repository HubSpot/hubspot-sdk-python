# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .smart_email_field_param import SmartEmailFieldParam
from .public_email_style_settings_param import PublicEmailStyleSettingsParam

__all__ = ["PublicEmailContentParam"]


class PublicEmailContentParam(TypedDict, total=False):
    flex_areas: Annotated[Dict[str, object], PropertyInfo(alias="flexAreas")]

    plain_text_version: Annotated[str, PropertyInfo(alias="plainTextVersion")]

    smart_fields: Annotated[Dict[str, SmartEmailFieldParam], PropertyInfo(alias="smartFields")]

    style_settings: Annotated[PublicEmailStyleSettingsParam, PropertyInfo(alias="styleSettings")]

    template_path: Annotated[str, PropertyInfo(alias="templatePath")]

    theme_settings_values: Annotated[Dict[str, object], PropertyInfo(alias="themeSettingsValues")]

    widget_containers: Annotated[Dict[str, object], PropertyInfo(alias="widgetContainers")]

    widgets: Dict[str, object]
