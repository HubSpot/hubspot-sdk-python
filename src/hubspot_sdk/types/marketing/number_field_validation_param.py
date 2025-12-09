# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NumberFieldValidationParam"]


class NumberFieldValidationParam(TypedDict, total=False):
    """Describes how a numeric value should be validated."""

    max_allowed_digits: Required[Annotated[int, PropertyInfo(alias="maxAllowedDigits")]]

    min_allowed_digits: Required[Annotated[int, PropertyInfo(alias="minAllowedDigits")]]
