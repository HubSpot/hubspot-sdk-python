# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .timeline_event_template import TimelineEventTemplate

__all__ = ["CollectionResponseTimelineEventTemplateNoPaging"]


class CollectionResponseTimelineEventTemplateNoPaging(BaseModel):
    results: List[TimelineEventTemplate]
