# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWhatsAppTemplateMetadata"]


class PublicWhatsAppTemplateMetadata(BaseModel):
    crm_object_ids: Dict[str, int] = FieldInfo(alias="crmObjectIds")

    mapped_template_id: str = FieldInfo(alias="mappedTemplateId")

    parameters: Dict[str, str]

    type: Literal["WHATSAPP_TEMPLATE_METADATA"]
