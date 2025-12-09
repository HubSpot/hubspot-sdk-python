# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NumberFieldValidation"]


class NumberFieldValidation(BaseModel):
    """Describes how a numeric value should be validated."""

    max_allowed_digits: int = FieldInfo(alias="maxAllowedDigits")

    min_allowed_digits: int = FieldInfo(alias="minAllowedDigits")
