# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict, TypeAliasType

from ..._utils import PropertyInfo
from ..._compat import PYDANTIC_V1
from .dependent_field_filter_param import DependentFieldFilterParam

__all__ = ["DependentFieldParam", "DependentField"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DependentField = TypeAliasType(
        "DependentField",
        Union[
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
        ],
    )
else:
    DependentField: TypeAlias = Union[
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


class DependentFieldParam(TypedDict, total=False):
    """
    A form field that will be displayed based on what the customer entered in another field.
    """

    dependent_condition: Required[Annotated[DependentFieldFilterParam, PropertyInfo(alias="dependentCondition")]]
    """A condition based on customer input"""

    dependent_field: Required[Annotated[DependentField, PropertyInfo(alias="dependentField")]]
    """A form field used for collecting an email address."""


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
