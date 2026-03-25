# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["IPRangeListSimpleParams"]


class IPRangeListSimpleParams(TypedDict, total=False):
    direction: List[Literal["INGRESS", "EGRESS"]]
    """An array of directions to filter the IP ranges by.

    Valid values are `INGRESS` and `EGRESS`.
    """

    service: List[Literal["EMAIL", "API", "DNS", "WEB_SCRAPING"]]
    """An array specifying the service types to filter by.

    Valid values include `EMAIL`, `API`, `DNS`, `WEB_SCRAPING`, and `TEST_SERVICE`.
    """
