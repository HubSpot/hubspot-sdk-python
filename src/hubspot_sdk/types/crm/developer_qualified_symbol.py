# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeveloperQualifiedSymbol"]


class DeveloperQualifiedSymbol(BaseModel):
    developer_symbol: str = FieldInfo(alias="developerSymbol")

    project_name: str = FieldInfo(alias="projectName")
