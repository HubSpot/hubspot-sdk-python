# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NearLimitRecordSample"]


class NearLimitRecordSample(BaseModel):
    label: str
    """The primary identifier of the record."""

    object_id: int = FieldInfo(alias="objectId")
    """The unique identifier for the object."""

    percentage: float
    """The percentage of the limit that has been used."""

    usage: int
    """The number of records currently in use."""
