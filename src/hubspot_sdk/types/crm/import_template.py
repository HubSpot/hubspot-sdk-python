# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ImportTemplate"]


class ImportTemplate(BaseModel):
    template_id: int = FieldInfo(alias="templateId")

    template_type: Literal["admin_defined", "previous_import", "user_file"] = FieldInfo(alias="templateType")
