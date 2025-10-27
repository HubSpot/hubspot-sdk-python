# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicEmailSubscriptionDetails"]


class PublicEmailSubscriptionDetails(BaseModel):
    office_location_id: Optional[str] = FieldInfo(alias="officeLocationId", default=None)
    """ID of the selected office location."""

    preferences_group_id: Optional[str] = FieldInfo(alias="preferencesGroupId", default=None)

    subscription_id: Optional[str] = FieldInfo(alias="subscriptionId", default=None)
    """ID of the subscription."""

    subscription_name: Optional[str] = FieldInfo(alias="subscriptionName", default=None)
