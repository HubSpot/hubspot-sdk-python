# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .public_comment import PublicComment
from .public_welcome_message import PublicWelcomeMessage
from .public_assignment_message import PublicAssignmentMessage
from .public_thread_inbox_change import PublicThreadInboxChange
from .public_thread_status_change import PublicThreadStatusChange
from .public_conversations_message import PublicConversationsMessage

__all__ = ["PublicMessage"]

PublicMessage: TypeAlias = Union[
    PublicConversationsMessage,
    PublicComment,
    PublicWelcomeMessage,
    PublicAssignmentMessage,
    PublicThreadStatusChange,
    PublicThreadInboxChange,
]
