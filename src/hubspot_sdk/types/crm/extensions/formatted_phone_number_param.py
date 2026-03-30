# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FormattedPhoneNumberParam"]


class FormattedPhoneNumberParam(TypedDict, total=False):
    e164_number: Required[Annotated[str, PropertyInfo(alias="e164Number")]]
    """The phone number formatted in E.164 standard."""

    phone_number_type: Required[
        Annotated[
            Literal[
                "FIXED_LINE",
                "FIXED_LINE_OR_MOBILE",
                "MOBILE",
                "PAGER",
                "PERSONAL_NUMBER",
                "PREMIUM_RATE",
                "SHARED_COST",
                "TOLL_FREE",
                "UAN",
                "UNKNOWN",
                "VOICEMAIL",
                "VOIP",
            ],
            PropertyInfo(alias="phoneNumberType"),
        ]
    ]
    """
    The type of phone number, with accepted values including FIXED_LINE, MOBILE,
    VOIP, and others.
    """

    extension: str
    """The extension number associated with the phone number."""
