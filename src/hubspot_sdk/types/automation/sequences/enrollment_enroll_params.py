# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnrollmentEnrollParams"]


class EnrollmentEnrollParams(TypedDict, total=False):
    contact_id: Required[Annotated[str, PropertyInfo(alias="contactId")]]

    sender_email: Required[Annotated[str, PropertyInfo(alias="senderEmail")]]

    sequence_id: Required[Annotated[str, PropertyInfo(alias="sequenceId")]]

    sender_alias_address: Annotated[str, PropertyInfo(alias="senderAliasAddress")]
