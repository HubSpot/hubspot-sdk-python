# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PublicEmailRecipients"]


class PublicEmailRecipients(BaseModel):
    """Data structure representing lists of IDs that should be included and excluded."""

    exclude: Optional[List[str]] = None
    """Excluded IDs."""

    include: Optional[List[str]] = None
    """Included IDs."""
