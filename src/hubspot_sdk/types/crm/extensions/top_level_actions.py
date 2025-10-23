# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .i_frame_action_body import IFrameActionBody
from .action_hook_action_body import ActionHookActionBody

__all__ = ["TopLevelActions", "Secondary", "Primary"]

Secondary: TypeAlias = Union[ActionHookActionBody, IFrameActionBody]

Primary: TypeAlias = Union[ActionHookActionBody, IFrameActionBody]


class TopLevelActions(BaseModel):
    secondary: List[Secondary]

    primary: Optional[Primary] = None

    settings: Optional[IFrameActionBody] = None
