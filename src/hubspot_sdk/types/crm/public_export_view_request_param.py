# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .public_crm_search_request_param import PublicCrmSearchRequestParam

__all__ = ["PublicExportViewRequestParam"]


class PublicExportViewRequestParam(TypedDict, total=False):
    export_internal_values_options: Required[
        Annotated[List[Literal["NAMES", "VALUES"]], PropertyInfo(alias="exportInternalValuesOptions")]
    ]

    export_name: Required[Annotated[str, PropertyInfo(alias="exportName")]]

    export_type: Required[Annotated[Literal["VIEW"], PropertyInfo(alias="exportType")]]

    format: Required[Literal["XLS", "XLSX", "CSV"]]

    language: Required[
        Literal["EN", "DE", "ES", "FR", "JA", "NL", "PT_BR", "IT", "PL", "SV", "FI", "ZH_TW", "DA_DK", "NO"]
    ]

    object_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectProperties")]]

    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    override_associated_objects_per_definition_per_row_limit: Required[
        Annotated[bool, PropertyInfo(alias="overrideAssociatedObjectsPerDefinitionPerRowLimit")]
    ]

    associated_object_type: Annotated[str, PropertyInfo(alias="associatedObjectType")]

    public_crm_search_request: Annotated[PublicCrmSearchRequestParam, PropertyInfo(alias="publicCrmSearchRequest")]
