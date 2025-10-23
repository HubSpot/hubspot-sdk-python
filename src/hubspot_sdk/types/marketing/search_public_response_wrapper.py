# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SearchPublicResponseWrapper"]


class SearchPublicResponseWrapper(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    external_account_id: str = FieldInfo(alias="externalAccountId")

    external_event_id: str = FieldInfo(alias="externalEventId")

    object_id: str = FieldInfo(alias="objectId")
