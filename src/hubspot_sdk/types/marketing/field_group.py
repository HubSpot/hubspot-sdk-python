# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FieldGroup", "Field"]

Field: TypeAlias = Union[
    "EmailField",
    "PhoneField",
    "MobilePhoneField",
    "SingleLineTextField",
    "MultiLineTextField",
    "NumberField",
    "SingleCheckboxField",
    "MultipleCheckboxesField",
    "DropdownField",
    "RadioField",
    "DatepickerField",
    "FileField",
    "PaymentLinkRadioField",
]


class FieldGroup(BaseModel):
    fields: List[Field]
    """The form fields included in the group"""

    group_type: Literal["default_group", "progressive", "queued"] = FieldInfo(alias="groupType")

    rich_text_type: Literal["image", "text"] = FieldInfo(alias="richTextType")
    """The type of rich text included. The default value is text."""

    rich_text: Optional[str] = FieldInfo(alias="richText", default=None)
    """A block of rich text or an image.

    Those can be used to add extra information for the customers filling in the
    form. If the field group includes fields, the rich text will be displayed before
    the fields.
    """


from .file_field import FileField
from .email_field import EmailField
from .phone_field import PhoneField
from .radio_field import RadioField
from .number_field import NumberField
from .dropdown_field import DropdownField
from .datepicker_field import DatepickerField
from .mobile_phone_field import MobilePhoneField
from .multi_line_text_field import MultiLineTextField
from .single_checkbox_field import SingleCheckboxField
from .single_line_text_field import SingleLineTextField
from .payment_link_radio_field import PaymentLinkRadioField
from .multiple_checkboxes_field import MultipleCheckboxesField
