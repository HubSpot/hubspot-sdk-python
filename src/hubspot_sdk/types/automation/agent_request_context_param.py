# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .chirp_ai_context_object_param import ChirpAIContextObjectParam

__all__ = ["AgentRequestContextParam"]


class AgentRequestContextParam(TypedDict, total=False):
    agent_id: Required[Annotated[int, PropertyInfo(alias="agentId")]]
    """The unique identifier for the agent making the request."""

    chirp_ai_context_object: Required[Annotated[ChirpAIContextObjectParam, PropertyInfo(alias="chirpAiContextObject")]]

    source: Required[Literal["AGENTS"]]
    """Indicates the source of the request, with the default value being 'AGENTS'."""

    trajectory_id: Annotated[str, PropertyInfo(alias="trajectoryId")]
    """The unique identifier for the trajectory associated with the agent request."""
