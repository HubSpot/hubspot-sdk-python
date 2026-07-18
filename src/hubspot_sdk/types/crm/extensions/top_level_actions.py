# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from .i_frame_action_body import IFrameActionBody
from .action_hook_action_body import ActionHookActionBody

__all__ = ["TopLevelActions", "Secondary", "Primary"]

Secondary: TypeAlias = Annotated[Union[ActionHookActionBody, IFrameActionBody], PropertyInfo(discriminator="type")]

Primary: TypeAlias = Annotated[Union[ActionHookActionBody, IFrameActionBody], PropertyInfo(discriminator="type")]


class TopLevelActions(BaseModel):
    secondary: List[Secondary]
    """
    Specifies a list of secondary actions for a card, each of which can be an action
    hook or an iframe.
    """

    primary: Optional[Primary] = None
    """
    Defines the primary action for a card, which can be either an action hook or an
    iframe.
    """

    settings: Optional[IFrameActionBody] = None
