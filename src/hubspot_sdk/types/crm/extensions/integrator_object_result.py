# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel
from .object_token import ObjectToken
from .i_frame_action_body import IFrameActionBody
from .action_hook_action_body import ActionHookActionBody

__all__ = ["IntegratorObjectResult", "Action"]

Action: TypeAlias = Annotated[Union[ActionHookActionBody, IFrameActionBody], PropertyInfo(discriminator="type")]


class IntegratorObjectResult(BaseModel):
    id: str
    """The unique identifier for the card."""

    actions: List[Action]
    """
    A list of actions associated with the card, which can include action hooks,
    confirmation action hooks, or iframes.
    """

    title: str
    """The top-level title for this card. Displayed to users in the CRM UI."""

    tokens: List[ObjectToken]
    """A collection of tokens representing specific properties related to the card."""

    link_url: Optional[str] = FieldInfo(alias="linkUrl", default=None)
    """A URL used on the title of the card"""
