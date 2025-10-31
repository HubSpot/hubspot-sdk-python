# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    deleted: bool

    display_name: str = FieldInfo(alias="displayName")

    display_order: int = FieldInfo(alias="displayOrder")

    fulcrum_portal_id: int = FieldInfo(alias="fulcrumPortalId")

    fulcrum_timestamp: int = FieldInfo(alias="fulcrumTimestamp")

    hubspot_defined: bool = FieldInfo(alias="hubspotDefined")

    name: str

    portal_id: int = FieldInfo(alias="portalId")
