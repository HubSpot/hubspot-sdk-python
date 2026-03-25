# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .object_coordinates import ObjectCoordinates

__all__ = ["CompanyCallerID"]


class CompanyCallerID(BaseModel):
    caller_id_type: Literal["COMPANY"] = FieldInfo(alias="callerIdType")

    object_coordinates: ObjectCoordinates = FieldInfo(alias="objectCoordinates")

    name: Optional[str] = None
