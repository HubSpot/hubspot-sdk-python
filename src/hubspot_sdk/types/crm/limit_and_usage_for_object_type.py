# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LimitAndUsageForObjectType"]


class LimitAndUsageForObjectType(BaseModel):
    limit: int

    object_type_id: str = FieldInfo(alias="objectTypeId")

    percentage: float

    plural_label: str = FieldInfo(alias="pluralLabel")

    singular_label: str = FieldInfo(alias="singularLabel")

    usage: int
