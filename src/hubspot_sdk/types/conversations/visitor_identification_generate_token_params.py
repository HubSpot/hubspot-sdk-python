# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VisitorIdentificationGenerateTokenParams"]


class VisitorIdentificationGenerateTokenParams(TypedDict, total=False):
    email: Required[str]
    """The email of the visitor that you wish to identify"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The first name of the visitor that you wish to identify.

    This value will only be set in HubSpot for new contacts and existing contacts
    where first name is unknown. Optional.
    """

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The last name of the visitor that you wish to identify.

    This value will only be set in HubSpot for new contacts and existing contacts
    where last name is unknown. Optional.
    """
