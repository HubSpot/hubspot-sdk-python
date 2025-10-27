# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .endpoints import Endpoints

__all__ = ["IntegratorOEmbedDomainModel"]


class IntegratorOEmbedDomainModel(BaseModel):
    id: int

    app_id: int = FieldInfo(alias="appId")

    created_at: int = FieldInfo(alias="createdAt")

    deleted_at: int = FieldInfo(alias="deletedAt")

    endpoints: Endpoints

    portal_id: int = FieldInfo(alias="portalId")

    updated_at: int = FieldInfo(alias="updatedAt")
