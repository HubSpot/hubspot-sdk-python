# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_subscription_translation import PublicSubscriptionTranslation

__all__ = ["SubscriptionDefinition"]


class SubscriptionDefinition(BaseModel):
    id: str
    """The unique identifier for the subscription."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the subscription was created."""

    description: str
    """A description of the subscription."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether the subscription is active."""

    is_default: bool = FieldInfo(alias="isDefault")
    """Indicates whether the subscription is the default option."""

    is_internal: bool = FieldInfo(alias="isInternal")
    """Indicates whether the subscription is internal."""

    name: str
    """The name of the subscription."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the subscription was last updated."""

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)
    """The ID of the business unit associated with the subscription."""

    communication_method: Optional[str] = FieldInfo(alias="communicationMethod", default=None)
    """The method of communication for the subscription."""

    purpose: Optional[str] = None
    """The purpose of the subscription."""

    subscription_translations: Optional[List[PublicSubscriptionTranslation]] = FieldInfo(
        alias="subscriptionTranslations", default=None
    )
    """A list of translations associated with the subscription."""
