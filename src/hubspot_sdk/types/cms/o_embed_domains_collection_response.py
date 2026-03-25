# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .integrator_o_embed_domain_model import IntegratorOEmbedDomainModel

__all__ = ["OEmbedDomainsCollectionResponse"]


class OEmbedDomainsCollectionResponse(BaseModel):
    results: List[IntegratorOEmbedDomainModel]

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
