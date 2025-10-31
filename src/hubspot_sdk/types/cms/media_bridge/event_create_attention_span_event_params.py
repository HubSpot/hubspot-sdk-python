# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..attention_span_calculated_values_param import AttentionSpanCalculatedValuesParam

__all__ = ["EventCreateAttentionSpanEventParams"]


class EventCreateAttentionSpanEventParams(TypedDict, total=False):
    media_type: Required[
        Annotated[Literal["VIDEO", "AUDIO", "DOCUMENT", "OTHER", "IMAGE"], PropertyInfo(alias="mediaType")]
    ]

    occurred_timestamp: Required[Annotated[int, PropertyInfo(alias="occurredTimestamp")]]

    raw_data_map: Required[Annotated[Dict[str, int], PropertyInfo(alias="rawDataMap")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    _hsenc: str

    contact_id: Annotated[int, PropertyInfo(alias="contactId")]

    contact_utk: Annotated[str, PropertyInfo(alias="contactUtk")]

    derived_values: Annotated[AttentionSpanCalculatedValuesParam, PropertyInfo(alias="derivedValues")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    media_bridge_id: Annotated[int, PropertyInfo(alias="mediaBridgeId")]

    media_name: Annotated[str, PropertyInfo(alias="mediaName")]

    media_url: Annotated[str, PropertyInfo(alias="mediaUrl")]

    page_id: Annotated[int, PropertyInfo(alias="pageId")]

    page_name: Annotated[str, PropertyInfo(alias="pageName")]

    page_url: Annotated[str, PropertyInfo(alias="pageUrl")]

    raw_data_string: Annotated[str, PropertyInfo(alias="rawDataString")]
