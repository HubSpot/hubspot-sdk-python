# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["TaskLocator"]


class TaskLocator(BaseModel):
    id: str
    """The unique identifier for the task."""

    links: Optional[Dict[str, str]] = None
    """
    A map of link names to associated URIs containing documentation about the error
    or recommended remediation steps
    """
