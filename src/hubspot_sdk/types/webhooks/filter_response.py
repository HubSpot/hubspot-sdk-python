# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .filter import Filter
from ..._models import BaseModel

__all__ = ["FilterResponse"]


class FilterResponse(BaseModel):
    id: int
    """The unique identifier for the filter. It is an integer in int64 format."""

    created_at: int = FieldInfo(alias="createdAt")
    """
    A timestamp indicating when the filter was created, represented as an integer in
    int64 format.
    """

    filter: Filter
    """
    Defines a single condition for searching CRM objects, specifying the property to
    filter on, the operator to use (such as equals, greater than, or contains), and
    the value(s) to compare against.
    """
