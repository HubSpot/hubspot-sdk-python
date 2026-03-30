# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CopilotRequestContextParam"]


class CopilotRequestContextParam(TypedDict, total=False):
    source: Required[Literal["COPILOT"]]
    """Indicates the source of the request, with the default value being 'COPILOT'."""

    trajectory_id: Annotated[str, PropertyInfo(alias="trajectoryId")]
    """The unique identifier for the trajectory."""
