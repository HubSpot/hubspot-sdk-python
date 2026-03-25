# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CardAuditResponse"]


class CardAuditResponse(BaseModel):
    action_type: Literal["CREATE", "DELETE", "UPDATE"] = FieldInfo(alias="actionType")
    """The type of action performed, with possible values: CREATE, DELETE, UPDATE."""

    application_id: int = FieldInfo(alias="applicationId")
    """The ID of the application associated with the card."""

    auth_source: Literal["APP", "EXTERNAL", "INTERNAL"] = FieldInfo(alias="authSource")
    """
    The source of authentication for the action, with possible values: APP,
    EXTERNAL, INTERNAL.
    """

    changed_at: int = FieldInfo(alias="changedAt")
    """The timestamp indicating when the change occurred."""

    initiating_user_id: int = FieldInfo(alias="initiatingUserId")
    """The ID of the user who initiated the action."""

    object_type_id: int = FieldInfo(alias="objectTypeId")
    """The ID of the card."""
