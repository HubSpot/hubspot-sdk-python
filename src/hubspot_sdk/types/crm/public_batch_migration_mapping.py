# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_migration_mapping import PublicMigrationMapping

__all__ = ["PublicBatchMigrationMapping"]


class PublicBatchMigrationMapping(BaseModel):
    legacy_list_ids_to_ids_mapping: List[PublicMigrationMapping] = FieldInfo(alias="legacyListIdsToIdsMapping")

    missing_legacy_list_ids: List[str] = FieldInfo(alias="missingLegacyListIds")
    """A list of legacy list ids that were passed in but not found.

    It will be empty if no id's are missing
    """
