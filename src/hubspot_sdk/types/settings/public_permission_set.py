# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPermissionSet"]


class PublicPermissionSet(BaseModel):
    """A role that can be assigned to a user"""

    id: str
    """The role's unique ID"""

    name: str
    """The role's name"""

    requires_billing_write: bool = FieldInfo(alias="requiresBillingWrite")
    """
    Whether this role has a paid seat and requires the billing-write scope to
    assign/unassign to users
    """
