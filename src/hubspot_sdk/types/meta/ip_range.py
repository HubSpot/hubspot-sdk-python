# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IPRange"]


class IPRange(BaseModel):
    cidr: str
    """The CIDR notation representing the IP range."""

    description: str
    """A description of the IP range."""

    direction: Literal["EGRESS", "INGRESS"]
    """The direction of the IP traffic, which can be INGRESS or EGRESS."""

    service: Literal["API", "DNS", "EMAIL", "WEB_SCRAPING"]
    """
    The service associated with the IP range, such as EMAIL, API, DNS, or
    WEB_SCRAPING.
    """
