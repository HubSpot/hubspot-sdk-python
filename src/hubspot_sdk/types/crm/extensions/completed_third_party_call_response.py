# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .company_caller_id import CompanyCallerID
from .contact_caller_id import ContactCallerID

__all__ = ["CompletedThirdPartyCallResponse", "CallerIDMatch"]

CallerIDMatch: TypeAlias = Union[ContactCallerID, CompanyCallerID]


class CompletedThirdPartyCallResponse(BaseModel):
    caller_id_matches: List[CallerIDMatch] = FieldInfo(alias="callerIdMatches")
