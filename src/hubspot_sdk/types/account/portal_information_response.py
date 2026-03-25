# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortalInformationResponse"]


class PortalInformationResponse(BaseModel):
    account_type: Literal["APP_DEVELOPER", "DEVELOPER_TEST", "SANDBOX", "STANDARD"] = FieldInfo(alias="accountType")
    """
    The type of account, such as APP_DEVELOPER, DEVELOPER_TEST, SANDBOX, or
    STANDARD.
    """

    additional_currencies: List[str] = FieldInfo(alias="additionalCurrencies")

    company_currency: str = FieldInfo(alias="companyCurrency")
    """The primary currency used by the company."""

    data_hosting_location: str = FieldInfo(alias="dataHostingLocation")
    """The location where the account's data is hosted."""

    portal_id: int = FieldInfo(alias="portalId")
    """The unique identifier for the HubSpot account."""

    time_zone: str = FieldInfo(alias="timeZone")
    """The time zone in which the account operates."""

    ui_domain: str = FieldInfo(alias="uiDomain")
    """The domain used for accessing the HubSpot user interface."""

    utc_offset: str = FieldInfo(alias="utcOffset")
    """The time zone offset from UTC in hours and minutes."""

    utc_offset_milliseconds: int = FieldInfo(alias="utcOffsetMilliseconds")
    """The time zone offset from UTC in milliseconds."""
