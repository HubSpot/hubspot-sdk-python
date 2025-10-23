# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .contact_association import ContactAssociation
from .marketing_event_association import MarketingEventAssociation

__all__ = ["ParticipationAssociations"]


class ParticipationAssociations(BaseModel):
    contact: ContactAssociation

    marketing_event: MarketingEventAssociation = FieldInfo(alias="marketingEvent")
