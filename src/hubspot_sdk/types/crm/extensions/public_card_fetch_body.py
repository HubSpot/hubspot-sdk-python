# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .card_object_type_body import CardObjectTypeBody

__all__ = ["PublicCardFetchBody"]


class PublicCardFetchBody(BaseModel):
    object_types: List[CardObjectTypeBody] = FieldInfo(alias="objectTypes")
    """An array of CRM object types where this card should be displayed.

    HubSpot will call your data fetch URL whenever a user visits a record page of
    the types defined here.
    """

    target_url: str = FieldInfo(alias="targetUrl")
    """URL to a service endpoint that will respond with card details.

    HubSpot will call this endpoint each time a user visits a CRM record page where
    this card should be displayed.
    """
