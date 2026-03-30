# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicActionFunctionIdentifier"]


class PublicActionFunctionIdentifier(BaseModel):
    function_type: Literal[
        "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
    ] = FieldInfo(alias="functionType")
    """
    The type of function, with accepted values: POST_ACTION_EXECUTION,
    POST_FETCH_OPTIONS, PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS.
    """

    id: Optional[str] = None
    """The unique identifier for the function."""
