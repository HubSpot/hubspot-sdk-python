# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AtLimitRecordSample"]


class AtLimitRecordSample(BaseModel):
    label: str
    """The label associated with a record that is at its limit."""

    object_id: int = FieldInfo(alias="objectId")
    """The objectId of the object that is at its limit."""
