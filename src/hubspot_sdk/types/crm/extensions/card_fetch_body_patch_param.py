# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .card_object_type_body_param import CardObjectTypeBodyParam

__all__ = ["CardFetchBodyPatchParam"]


class CardFetchBodyPatchParam(TypedDict, total=False):
    object_types: Required[Annotated[Iterable[CardObjectTypeBodyParam], PropertyInfo(alias="objectTypes")]]
    """An array of CRM object types where this card should be displayed.

    HubSpot will call your target URL whenever a user visits a record page of the
    types defined here.
    """

    card_type: Annotated[Literal["EXTERNAL", "SERVERLESS"], PropertyInfo(alias="cardType")]

    serverless_function: Annotated[str, PropertyInfo(alias="serverlessFunction")]

    target_url: Annotated[str, PropertyInfo(alias="targetUrl")]
    """URL to a service endpoint that will respond with details for this card.

    HubSpot will call this endpoint each time a user visits a CRM record page where
    this card should be displayed.
    """
