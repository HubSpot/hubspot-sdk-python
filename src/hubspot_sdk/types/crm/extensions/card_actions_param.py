# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CardActionsParam"]


class CardActionsParam(TypedDict, total=False):
    base_urls: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="baseUrls")]]
    """A list of URL prefixes that will be accepted for card action URLs.

    If your data fetch response includes an action URL that doesn't begin with one
    of these values, it will result in an error and the card will not be displayed.
    """
