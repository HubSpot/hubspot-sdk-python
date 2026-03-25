# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .contact_profile_param import ContactProfileParam

__all__ = ["ContactAttachmentParam"]


class ContactAttachmentParam(TypedDict, total=False):
    contact_profile: Required[Annotated[ContactProfileParam, PropertyInfo(alias="contactProfile")]]

    type: Required[Literal["CONTACT"]]
