# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CardActions"]


class CardActions(BaseModel):
    """Configuration for custom user actions on cards."""

    base_urls: List[str] = FieldInfo(alias="baseUrls")
    """A list of URL prefixes that will be accepted for card action URLs.

    If your data fetch response includes an action URL that doesn't begin with one
    of these values, it will result in an error and the card will not be displayed.
    """
