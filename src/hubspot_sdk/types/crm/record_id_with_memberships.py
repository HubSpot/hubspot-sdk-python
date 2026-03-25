# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .record_list_membership import RecordListMembership

__all__ = ["RecordIDWithMemberships"]


class RecordIDWithMemberships(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    record_id: str = FieldInfo(alias="recordId")

    record_list_memberships: List[RecordListMembership] = FieldInfo(alias="recordListMemberships")
