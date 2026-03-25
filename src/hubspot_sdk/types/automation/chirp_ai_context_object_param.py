# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .compliance_ids_param import ComplianceIDsParam

__all__ = ["ChirpAIContextObjectParam"]


class ChirpAIContextObjectParam(TypedDict, total=False):
    application_group: Required[Annotated[str, PropertyInfo(alias="applicationGroup")]]

    application_id: Required[Annotated[str, PropertyInfo(alias="applicationId")]]

    metadata: Required[Dict[str, str]]

    otel_context_holder: Required[Annotated[Dict[str, str], PropertyInfo(alias="otelContextHolder")]]

    unstructured_sources: Required[
        Annotated[
            List[
                Literal[
                    "NONE",
                    "USER_INPUT",
                    "LOGGED_EMAIL",
                    "VIDEO_CALL",
                    "AUDIO_CALL",
                    "CALL_TRANSCRIPT",
                    "MEETING_TRANSCRIPT",
                    "FORMS",
                    "FEEDBACK_SURVEY",
                    "PDF",
                    "QUOTE",
                    "INVOICE",
                    "OTHER_ATTACHMENT_DOC",
                    "WHATSAPP",
                    "SMS",
                    "CHAT",
                    "FACEBOOK_MESSENGER",
                    "CUSTOM_CHANNEL_OR_API",
                    "MANY",
                    "NOTE",
                    "DERIVED",
                ]
            ],
            PropertyInfo(alias="unstructuredSources"),
        ]
    ]

    compliance_ids: Annotated[ComplianceIDsParam, PropertyInfo(alias="complianceIds")]

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]

    inference_id: Annotated[str, PropertyInfo(alias="inferenceId")]

    trajectory_id: Annotated[str, PropertyInfo(alias="trajectoryId")]
