# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIContactPropertyAnchor"]


class APIContactPropertyAnchor(BaseModel):
    contact_property: str = FieldInfo(alias="contactProperty")
    """A date property on the contact to use as the anchor point of this workflow."""

    type: Literal["CONTACT_PROPERTY_ANCHOR"]
    """
    The type of event anchor this is, can be: "CONTACT_PROPERTY_ANCHOR" or
    "STATIC_DATE_ANCHOR"
    """
