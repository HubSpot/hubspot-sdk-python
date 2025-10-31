# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIContactPropertyAnchor"]


class APIContactPropertyAnchor(BaseModel):
    contact_property: str = FieldInfo(alias="contactProperty")

    type: Literal["CONTACT_PROPERTY_ANCHOR"]
