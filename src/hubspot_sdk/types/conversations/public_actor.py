# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .bot_actor import BotActor
from .llm_actor import LlmActor
from .agent_actor import AgentActor
from .email_actor import EmailActor
from .system_actor import SystemActor
from .visitor_actor import VisitorActor
from .integrator_actor import IntegratorActor

__all__ = ["PublicActor"]

PublicActor: TypeAlias = Union[AgentActor, BotActor, IntegratorActor, SystemActor, VisitorActor, EmailActor, LlmActor]
