# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectTypeNearOrAtAssociationLimit"]


class ObjectTypeNearOrAtAssociationLimit(BaseModel):
    has_records_at_limit: bool = FieldInfo(alias="hasRecordsAtLimit")

    has_records_near_limit: bool = FieldInfo(alias="hasRecordsNearLimit")

    object_type_id: str = FieldInfo(alias="objectTypeId")

    plural_label: str = FieldInfo(alias="pluralLabel")

    singular_label: str = FieldInfo(alias="singularLabel")
