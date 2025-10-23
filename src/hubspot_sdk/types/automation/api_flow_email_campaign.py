# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIFlowEmailCampaign"]


class APIFlowEmailCampaign(BaseModel):
    email_campaign_id: str = FieldInfo(alias="emailCampaignId")

    email_content_id: str = FieldInfo(alias="emailContentId")

    flow_id: str = FieldInfo(alias="flowId")
