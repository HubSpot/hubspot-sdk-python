# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIConnection"]


class APIConnection(BaseModel):
    edge_type: str = FieldInfo(alias="edgeType")

    next_action_id: str = FieldInfo(alias="nextActionId")
