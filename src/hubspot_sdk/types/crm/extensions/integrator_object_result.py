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
    """The unique identifier for the card."""

    actions: List[Action]
    """
    A list of actions associated with the card, which can include action hooks,
    confirmation action hooks, or iframes.
    """

    title: str
    """The title of the object card, displayed to users."""

    tokens: List[ObjectToken]
    """A collection of tokens representing specific properties related to the card."""

    link_url: Optional[str] = FieldInfo(alias="linkUrl", default=None)
    """A URL used on the title of the card"""
