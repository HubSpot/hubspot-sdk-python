# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .property_filter import PropertyFilter

__all__ = ["ComboEventRule"]


class ComboEventRule(BaseModel):
    count: int

    event_type_id: str = FieldInfo(alias="eventTypeId")

    property_filters: List[PropertyFilter] = FieldInfo(alias="propertyFilters")

    lookback_window_days: Optional[int] = FieldInfo(alias="lookbackWindowDays", default=None)
