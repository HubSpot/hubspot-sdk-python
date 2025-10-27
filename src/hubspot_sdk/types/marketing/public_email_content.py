# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_email_style_settings import PublicEmailStyleSettings

__all__ = ["PublicEmailContent"]


class PublicEmailContent(BaseModel):
    flex_areas: Optional[Dict[str, object]] = FieldInfo(alias="flexAreas", default=None)

    plain_text_version: Optional[str] = FieldInfo(alias="plainTextVersion", default=None)

    smart_fields: Optional[Dict[str, object]] = FieldInfo(alias="smartFields", default=None)

    style_settings: Optional[PublicEmailStyleSettings] = FieldInfo(alias="styleSettings", default=None)

    template_path: Optional[str] = FieldInfo(alias="templatePath", default=None)

    theme_settings_values: Optional[Dict[str, object]] = FieldInfo(alias="themeSettingsValues", default=None)

    widget_containers: Optional[Dict[str, object]] = FieldInfo(alias="widgetContainers", default=None)

    widgets: Optional[Dict[str, object]] = None
