# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AppInfo"]


class AppInfo(BaseModel):
    id: str
    """The ID of the application"""

    name: str
    """The name of the application"""
