# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicExportListRequestParam"]


class PublicExportListRequestParam(TypedDict, total=False):
    associated_object_type: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="associatedObjectType")]]

    export_internal_values_options: Required[
        Annotated[List[Literal["NAMES", "VALUES"]], PropertyInfo(alias="exportInternalValuesOptions")]
    ]

    export_name: Required[Annotated[str, PropertyInfo(alias="exportName")]]

    export_type: Required[Annotated[Literal["LIST"], PropertyInfo(alias="exportType")]]

    format: Required[Literal["CSV", "XLS", "XLSX"]]

    include_labeled_associations: Required[Annotated[bool, PropertyInfo(alias="includeLabeledAssociations")]]

    include_primary_display_property_for_associated_objects: Required[
        Annotated[bool, PropertyInfo(alias="includePrimaryDisplayPropertyForAssociatedObjects")]
    ]

    language: Required[
        Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ]
    ]

    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]

    object_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectProperties")]]

    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    override_associated_objects_per_definition_per_row_limit: Required[
        Annotated[bool, PropertyInfo(alias="overrideAssociatedObjectsPerDefinitionPerRowLimit")]
    ]
