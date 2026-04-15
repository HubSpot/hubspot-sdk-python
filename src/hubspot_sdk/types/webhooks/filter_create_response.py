# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FilterCreateResponse"]


class FilterCreateResponse(BaseModel):
    filter_id: int = FieldInfo(alias="filterId")
    """The unique identifier for the created filter.

    It is an integer formatted as int64.
    """
