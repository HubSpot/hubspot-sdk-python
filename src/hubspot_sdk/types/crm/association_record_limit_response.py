# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .at_limit_record_sample import AtLimitRecordSample
from .near_limit_record_sample import NearLimitRecordSample

__all__ = ["AssociationRecordLimitResponse"]


class AssociationRecordLimitResponse(BaseModel):
    at_limit_from_record_samples: List[AtLimitRecordSample] = FieldInfo(alias="atLimitFromRecordSamples")

    limit: int
    """The maximum number of associations allowed for records."""

    near_limit_from_record_samples: List[NearLimitRecordSample] = FieldInfo(alias="nearLimitFromRecordSamples")

    total_records_at_limit: int = FieldInfo(alias="totalRecordsAtLimit")
    """The total number of records that have reached their association limit."""

    total_records_near_limit: int = FieldInfo(alias="totalRecordsNearLimit")
    """The total number of records that are approaching their association limit."""
