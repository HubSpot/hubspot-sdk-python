# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalCommunicationConsentCheckbox"]


class ExternalCommunicationConsentCheckbox(BaseModel):
    communication_type_id: str = FieldInfo(alias="communicationTypeId")
    """The ID of the communication consent form being recorded."""

    label: str
    """The text label describing the consent being given."""

    required: bool
    """Whether the consent checkbox is required."""
