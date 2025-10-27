# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MetricsCounters"]


class MetricsCounters(BaseModel):
    influenced_contacts: int = FieldInfo(alias="influencedContacts")

    new_contacts_first_touch: int = FieldInfo(alias="newContactsFirstTouch")

    new_contacts_last_touch: int = FieldInfo(alias="newContactsLastTouch")

    sessions: int
