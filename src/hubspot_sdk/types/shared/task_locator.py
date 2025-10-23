# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["TaskLocator"]


class TaskLocator(BaseModel):
    id: str

    links: Optional[Dict[str, str]] = None
