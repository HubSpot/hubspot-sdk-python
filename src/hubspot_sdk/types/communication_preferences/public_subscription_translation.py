# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSubscriptionTranslation"]


class PublicSubscriptionTranslation(BaseModel):
    created_at: int = FieldInfo(alias="createdAt")
    """The timestamp indicating when the subscription translation was created."""

    description: str
    """A text description of the subscription translation."""

    language_code: str = FieldInfo(alias="languageCode")
    """The code representing the language of the subscription translation."""

    name: str
    """The name of the subscription translation."""

    subscription_id: int = FieldInfo(alias="subscriptionId")
    """The unique identifier for the subscription associated with the translation."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """The timestamp indicating when the subscription translation was last updated."""
