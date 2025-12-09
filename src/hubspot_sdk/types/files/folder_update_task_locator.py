# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["FolderUpdateTaskLocator"]


class FolderUpdateTaskLocator(BaseModel):
    """Information on the task that has been started, and where to check it's status."""

    id: str
    """ID of the task"""

    links: Dict[str, str]
    """Links for where to check information related to the task.

    The `status` link gives the URL for where to check the status of the task.
    """
