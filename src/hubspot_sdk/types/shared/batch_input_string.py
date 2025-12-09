# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["BatchInputString"]


class BatchInputString(BaseModel):
    """Wrapper for providing an array of strings as inputs."""

    inputs: List[str]
    """Strings to input."""
