# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .object_coordinates import ObjectCoordinates

__all__ = ["ContactCallerID"]


class ContactCallerID(BaseModel):
    caller_id_type: Literal["CONTACT"] = FieldInfo(alias="callerIdType")

    object_coordinates: ObjectCoordinates = FieldInfo(alias="objectCoordinates")

    email: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
