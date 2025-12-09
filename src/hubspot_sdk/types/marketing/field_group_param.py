# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FieldGroupParam", "Field"]

Field: TypeAlias = Union[
    "EmailFieldParam",
    "PhoneFieldParam",
    "MobilePhoneFieldParam",
    "SingleLineTextFieldParam",
    "MultiLineTextFieldParam",
    "NumberFieldParam",
    "SingleCheckboxFieldParam",
    "MultipleCheckboxesFieldParam",
    "DropdownFieldParam",
    "RadioFieldParam",
    "DatepickerFieldParam",
    "FileFieldParam",
    "PaymentLinkRadioFieldParam",
]


class FieldGroupParam(TypedDict, total=False):
    """A collection of up to three form fields usually displayed in a row."""

    fields: Required[Iterable[Field]]
    """The form fields included in the group"""

    group_type: Required[Annotated[Literal["default_group", "progressive", "queued"], PropertyInfo(alias="groupType")]]

    rich_text_type: Required[Annotated[Literal["image", "text"], PropertyInfo(alias="richTextType")]]
    """The type of rich text included. The default value is text."""

    rich_text: Annotated[str, PropertyInfo(alias="richText")]
    """A block of rich text or an image.

    Those can be used to add extra information for the customers filling in the
    form. If the field group includes fields, the rich text will be displayed before
    the fields.
    """


from .file_field_param import FileFieldParam
from .email_field_param import EmailFieldParam
from .phone_field_param import PhoneFieldParam
from .radio_field_param import RadioFieldParam
from .number_field_param import NumberFieldParam
from .dropdown_field_param import DropdownFieldParam
from .datepicker_field_param import DatepickerFieldParam
from .mobile_phone_field_param import MobilePhoneFieldParam
from .multi_line_text_field_param import MultiLineTextFieldParam
from .single_checkbox_field_param import SingleCheckboxFieldParam
from .single_line_text_field_param import SingleLineTextFieldParam
from .payment_link_radio_field_param import PaymentLinkRadioFieldParam
from .multiple_checkboxes_field_param import MultipleCheckboxesFieldParam
