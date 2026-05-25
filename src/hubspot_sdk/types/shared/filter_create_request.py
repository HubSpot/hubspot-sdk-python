# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .filter import Filter
from ..._models import BaseModel

__all__ = ["FilterCreateRequest"]


class FilterCreateRequest(BaseModel):
    filter: Filter
    """
    Defines a single condition for searching CRM objects, specifying the property to
    filter on, the operator to use (such as equals, greater than, or contains), and
    the value(s) to compare against.
    """

    subscription_id: int = FieldInfo(alias="subscriptionId")
    """The unique identifier of the subscription to which the filter will be applied.

    It is an integer formatted as int64.
    """
