# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .compliance_ids_param import ComplianceIDsParam

__all__ = ["ChirpAIContextObjectParam"]


class ChirpAIContextObjectParam(TypedDict, total=False):
    application_group: Required[Annotated[str, PropertyInfo(alias="applicationGroup")]]
    """The group to which the application belongs."""

    application_id: Required[Annotated[str, PropertyInfo(alias="applicationId")]]
    """The identifier for the application associated with the context."""

    metadata: Required[Dict[str, str]]
    """Additional metadata related to the context, represented as key-value pairs."""

    otel_context_holder: Required[Annotated[Dict[str, str], PropertyInfo(alias="otelContextHolder")]]
    """Holds OpenTelemetry context information as key-value pairs."""

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
    """The identifier for the feature associated with the context."""

    inference_id: Annotated[str, PropertyInfo(alias="inferenceId")]
    """The identifier for the inference associated with the context."""

    trajectory_id: Annotated[str, PropertyInfo(alias="trajectoryId")]
    """The identifier for the trajectory, formatted as a UUID."""
