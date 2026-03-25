# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .contact_org_param import ContactOrgParam
from .contact_url_param import ContactURLParam
from .contact_name_param import ContactNameParam
from .contact_email_param import ContactEmailParam
from .contact_phone_param import ContactPhoneParam
from .contact_address_param import ContactAddressParam

__all__ = ["ContactProfileParam"]


class ContactProfileParam(TypedDict, total=False):
    addresses: Required[Iterable[ContactAddressParam]]

    emails: Required[Iterable[ContactEmailParam]]

    phones: Required[Iterable[ContactPhoneParam]]

    urls: Required[Iterable[ContactURLParam]]

    name: ContactNameParam

    org: ContactOrgParam
