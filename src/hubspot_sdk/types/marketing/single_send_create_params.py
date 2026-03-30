# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_single_send_email_param import PublicSingleSendEmailParam

__all__ = ["SingleSendCreateParams"]


class SingleSendCreateParams(TypedDict, total=False):
    contact_properties: Required[Annotated[Dict[str, str], PropertyInfo(alias="contactProperties")]]
    """The contactProperties field is a map of contact property values.

    Each contact property value contains a name and value property. Each property
    will get set on the contact record and will be visible in the template under
    {{ contact.NAME }}. Use these properties when you want to set a contact property
    while you’re sending the email. For example, when sending a receipt you may want
    to set a last_paid_date property, as the sending of the receipt will have
    information about the last payment.
    """

    custom_properties: Required[Annotated[Dict[str, object], PropertyInfo(alias="customProperties")]]
    """The customProperties field is a map of property values.

    Each property value contains a name and value property. Each property will be
    visible in the template under {{ custom.NAME }}. Note: Custom properties do not
    currently support arrays. To provide a listing in an email, one workaround is to
    build an HTML list (either with tables or ul) and specify it as a custom
    property.
    """

    email_id: Required[Annotated[int, PropertyInfo(alias="emailId")]]
    """The content ID for the email, which can be found in email tool UI."""

    message: Required[PublicSingleSendEmailParam]
