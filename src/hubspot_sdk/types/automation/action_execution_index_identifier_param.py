# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionExecutionIndexIdentifierParam"]


class ActionExecutionIndexIdentifierParam(TypedDict, total=False):
    action_execution_index: Required[Annotated[int, PropertyInfo(alias="actionExecutionIndex")]]
    """The index number representing the execution order of the action."""

    enrollment_id: Required[Annotated[int, PropertyInfo(alias="enrollmentId")]]
    """The ID associated with the enrollment process."""
