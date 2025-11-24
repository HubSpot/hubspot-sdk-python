# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .public_comment import PublicComment
from ..shared.forward_paging import ForwardPaging
from .public_welcome_message import PublicWelcomeMessage
from .public_assignment_message import PublicAssignmentMessage
from .public_thread_inbox_change import PublicThreadInboxChange
from .public_thread_status_change import PublicThreadStatusChange
from .conversations_public_conversations_message import ConversationsPublicConversationsMessage

__all__ = ["CollectionResponsePublicMessageForwardPaging", "Result"]

Result: TypeAlias = Union[
    ConversationsPublicConversationsMessage,
    PublicComment,
    PublicWelcomeMessage,
    PublicAssignmentMessage,
    PublicThreadStatusChange,
    PublicThreadInboxChange,
]


class CollectionResponsePublicMessageForwardPaging(BaseModel):
    results: List[Result]

    paging: Optional[ForwardPaging] = None
