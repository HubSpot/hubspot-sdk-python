# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortalInformationResponse"]


class PortalInformationResponse(BaseModel):
    account_type: Literal["STANDARD", "DEVELOPER_TEST", "SANDBOX", "APP_DEVELOPER"] = FieldInfo(alias="accountType")

    additional_currencies: List[str] = FieldInfo(alias="additionalCurrencies")

    company_currency: str = FieldInfo(alias="companyCurrency")

    data_hosting_location: str = FieldInfo(alias="dataHostingLocation")

    portal_id: int = FieldInfo(alias="portalId")

    time_zone: str = FieldInfo(alias="timeZone")

    ui_domain: str = FieldInfo(alias="uiDomain")

    utc_offset: str = FieldInfo(alias="utcOffset")

    utc_offset_milliseconds: int = FieldInfo(alias="utcOffsetMilliseconds")
