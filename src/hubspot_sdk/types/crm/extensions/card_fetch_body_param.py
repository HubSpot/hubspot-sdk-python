# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .card_object_type_body_param import CardObjectTypeBodyParam

__all__ = ["CardFetchBodyParam"]


class CardFetchBodyParam(TypedDict, total=False):
    card_type: Required[Annotated[Literal["EXTERNAL", "SERVERLESS"], PropertyInfo(alias="cardType")]]
    """A deprecated field to determine the type of card returned."""

    object_types: Required[Annotated[Iterable[CardObjectTypeBodyParam], PropertyInfo(alias="objectTypes")]]
    """An array of CRM object types where this card should be displayed.

    HubSpot will call your data fetch URL whenever a user visits a record page of
    the types defined here.
    """

    target_url: Required[Annotated[str, PropertyInfo(alias="targetUrl")]]
    """URL to a service endpoints that will respond with card details.

    HubSpot will call this endpoint each time a user visits a CRM record page where
    this card should be displayed.
    """

    serverless_function: Annotated[str, PropertyInfo(alias="serverlessFunction")]
    """A deprecated field to specify serverless functionality with the card"""
