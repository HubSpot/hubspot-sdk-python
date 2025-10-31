# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IntegratorSettingListOembedDomainsResponse", "Result", "ResultEndpoints"]


class ResultEndpoints(BaseModel):
    discovery: bool

    schemes: List[str]

    url: str


class Result(BaseModel):
    id: int

    app_id: int = FieldInfo(alias="appId")

    created_at: int = FieldInfo(alias="createdAt")

    deleted_at: int = FieldInfo(alias="deletedAt")

    endpoints: ResultEndpoints

    portal_id: int = FieldInfo(alias="portalId")

    updated_at: int = FieldInfo(alias="updatedAt")


class IntegratorSettingListOembedDomainsResponse(BaseModel):
    results: List[Result]

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
