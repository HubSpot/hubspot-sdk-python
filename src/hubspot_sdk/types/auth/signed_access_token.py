# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SignedAccessToken"]


class SignedAccessToken(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    expires_at: int = FieldInfo(alias="expiresAt")

    hub_id: int = FieldInfo(alias="hubId")

    hublet: str

    installing_user_id: int = FieldInfo(alias="installingUserId")

    is_private_distribution: bool = FieldInfo(alias="isPrivateDistribution")

    is_service_account: bool = FieldInfo(alias="isServiceAccount")

    is_user_level: bool = FieldInfo(alias="isUserLevel")

    new_signature: str = FieldInfo(alias="newSignature")

    scopes: str

    scope_to_scope_group_pks: str = FieldInfo(alias="scopeToScopeGroupPks")

    signature: str

    trial_scopes: str = FieldInfo(alias="trialScopes")

    trial_scope_to_scope_group_pks: str = FieldInfo(alias="trialScopeToScopeGroupPks")

    user_id: int = FieldInfo(alias="userId")
