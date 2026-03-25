# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CrmPropertyWrapper"]


class CrmPropertyWrapper(BaseModel):
    name: str
    """The name of the property in the CRM"""

    value: str
    """The value of the property in the CRM"""
