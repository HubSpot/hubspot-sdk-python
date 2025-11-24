# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicThreadAssociations"]


class PublicThreadAssociations(BaseModel):
    associated_ticket_id: Optional[str] = FieldInfo(alias="associatedTicketId", default=None)
