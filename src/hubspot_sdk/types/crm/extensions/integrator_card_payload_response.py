# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .top_level_actions import TopLevelActions
from .integrator_object_result import IntegratorObjectResult

__all__ = ["IntegratorCardPayloadResponse"]


class IntegratorCardPayloadResponse(BaseModel):
    response_version: Literal["v1", "v3"] = FieldInfo(alias="responseVersion")
    """The number version of the response."""

    sections: List[IntegratorObjectResult]
    """A list of up to five valid card sub categories."""

    total_count: int = FieldInfo(alias="totalCount")
    """The total number of cards that are sent in this response."""

    all_items_link_url: Optional[str] = FieldInfo(alias="allItemsLinkUrl", default=None)
    """
    URL to a page the integrator has built that displays all details for the object
    cards. This URL will be displayed to users on the title of the card.
    """

    card_label: Optional[str] = FieldInfo(alias="cardLabel", default=None)
    """The label to be used for the `allItemsLinkUrl` link (e.g.

    'See more tickets') and the title of the card.
    """

    top_level_actions: Optional[TopLevelActions] = FieldInfo(alias="topLevelActions", default=None)
