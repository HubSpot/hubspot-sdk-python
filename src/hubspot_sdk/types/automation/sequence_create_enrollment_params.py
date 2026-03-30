# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SequenceCreateEnrollmentParams"]


class SequenceCreateEnrollmentParams(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]

    contact_id: Required[Annotated[str, PropertyInfo(alias="contactId")]]
    """The unique identifier of the contact to be enrolled in the sequence."""

    sender_email: Required[Annotated[str, PropertyInfo(alias="senderEmail")]]
    """The email address of the sender enrolling the contact in the sequence."""

    sequence_id: Required[Annotated[str, PropertyInfo(alias="sequenceId")]]
    """The unique identifier of the sequence in which the contact will be enrolled."""

    sender_alias_address: Annotated[str, PropertyInfo(alias="senderAliasAddress")]
    """The alias email address used by the sender when enrolling the contact."""
