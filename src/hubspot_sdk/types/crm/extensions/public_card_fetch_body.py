# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .card_object_type_body import CardObjectTypeBody

__all__ = ["PublicCardFetchBody"]


class PublicCardFetchBody(BaseModel):
    object_types: List[CardObjectTypeBody] = FieldInfo(alias="objectTypes")

    target_url: str = FieldInfo(alias="targetUrl")
