# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .chirp_ai_context_object_param import ChirpAIContextObjectParam

__all__ = ["StandaloneRequestContextParam"]


class StandaloneRequestContextParam(TypedDict, total=False):
    chirp_ai_context_object: Required[Annotated[ChirpAIContextObjectParam, PropertyInfo(alias="chirpAiContextObject")]]

    source: Required[Literal["STANDALONE"]]

    trajectory_id: Annotated[str, PropertyInfo(alias="trajectoryId")]
