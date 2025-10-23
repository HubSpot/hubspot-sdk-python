# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .object_token import ObjectToken
from .i_frame_action_body import IFrameActionBody
from .action_hook_action_body import ActionHookActionBody

__all__ = ["IntegratorObjectResult", "Action"]

Action: TypeAlias = Union[ActionHookActionBody, IFrameActionBody]


class IntegratorObjectResult(BaseModel):
    id: str

    actions: List[Action]

    title: str

    tokens: List[ObjectToken]

    link_url: Optional[str] = FieldInfo(alias="linkUrl", default=None)
