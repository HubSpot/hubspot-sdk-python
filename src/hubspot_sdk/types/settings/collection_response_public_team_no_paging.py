# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_team import PublicTeam

__all__ = ["CollectionResponsePublicTeamNoPaging"]


class CollectionResponsePublicTeamNoPaging(BaseModel):
    results: List[PublicTeam]
