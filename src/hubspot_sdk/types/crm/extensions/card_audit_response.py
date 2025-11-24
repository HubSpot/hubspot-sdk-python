# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CardAuditResponse"]


class CardAuditResponse(BaseModel):
    action_type: Literal["CREATE", "DELETE", "UPDATE"] = FieldInfo(alias="actionType")

    application_id: int = FieldInfo(alias="applicationId")

    auth_source: Literal["APP", "EXTERNAL", "INTERNAL"] = FieldInfo(alias="authSource")

    changed_at: int = FieldInfo(alias="changedAt")

    initiating_user_id: int = FieldInfo(alias="initiatingUserId")

    object_type_id: int = FieldInfo(alias="objectTypeId")
