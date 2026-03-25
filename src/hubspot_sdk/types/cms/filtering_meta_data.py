# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FilteringMetaData"]


class FilteringMetaData(BaseModel):
    include_helpdesk_routable_teams_only: bool = FieldInfo(alias="includeHelpdeskRoutableTeamsOnly")

    include_unconfirmed_users: bool = FieldInfo(alias="includeUnconfirmedUsers")

    list_processing_types: List[str] = FieldInfo(alias="listProcessingTypes")

    pipeline_ids: List[str] = FieldInfo(alias="pipelineIds")
