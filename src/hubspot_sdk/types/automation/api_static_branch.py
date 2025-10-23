# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection

__all__ = ["APIStaticBranch"]


class APIStaticBranch(BaseModel):
    branch_value: str = FieldInfo(alias="branchValue")
    """If value to check for.

    If the value of the `inputValue` matches this `branchValue` than this
    `connection` will get traversed.
    """

    connection: Optional[APIConnection] = None
