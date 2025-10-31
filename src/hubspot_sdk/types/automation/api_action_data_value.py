# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIActionDataValue"]


class APIActionDataValue(BaseModel):
    action_id: str = FieldInfo(alias="actionId")

    data_key: str = FieldInfo(alias="dataKey")

    type: Literal["FIELD_DATA"]
