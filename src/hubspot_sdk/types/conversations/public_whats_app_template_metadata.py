# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWhatsAppTemplateMetadata"]


class PublicWhatsAppTemplateMetadata(BaseModel):
    crm_object_ids: Dict[str, int] = FieldInfo(alias="crmObjectIds")

    parameters: Dict[str, str]

    type: Literal["WHATSAPP_TEMPLATE_METADATA"]

    content_id: Optional[int] = FieldInfo(alias="contentId", default=None)

    mapped_template_id: Optional[int] = FieldInfo(alias="mappedTemplateId", default=None)

    root_mic_id: Optional[int] = FieldInfo(alias="rootMicId", default=None)
