# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicListConversionDate"]


class PublicListConversionDate(BaseModel):
    conversion_type: Literal["CONVERSION_DATE"] = FieldInfo(alias="conversionType")
    """Specifies the type of conversion (CONVERSION_DATE)."""

    day: int
    """The day component of the conversion date."""

    month: int
    """The month component of the conversion date."""

    year: int
    """The year component of the conversion date."""
