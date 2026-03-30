# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .developer_qualified_symbol import DeveloperQualifiedSymbol

__all__ = ["AppEventResolutionResponse"]


class AppEventResolutionResponse(BaseModel):
    developer_qualified_symbol: DeveloperQualifiedSymbol = FieldInfo(alias="developerQualifiedSymbol")

    fully_qualified_name: str = FieldInfo(alias="fullyQualifiedName")
