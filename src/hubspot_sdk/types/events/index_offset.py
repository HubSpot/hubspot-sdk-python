# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IndexOffset"]


class IndexOffset(BaseModel):
    days: Optional[int] = None

    hours: Optional[int] = None

    milliseconds: Optional[int] = None

    minutes: Optional[int] = None

    months: Optional[int] = None

    quarters: Optional[int] = None

    seconds: Optional[int] = None

    weeks: Optional[int] = None

    years: Optional[int] = None
