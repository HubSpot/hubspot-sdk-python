# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .object_coordinates import ObjectCoordinates

__all__ = ["ContactCallerID"]


class ContactCallerID(BaseModel):
    caller_id_type: Literal["CONTACT"] = FieldInfo(alias="callerIdType")
    """Specifies the type of caller ID, with the default value being CONTACT."""

    object_coordinates: ObjectCoordinates = FieldInfo(alias="objectCoordinates")

    email: Optional[str] = None
    """The email address of the contact."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the contact."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the contact."""
