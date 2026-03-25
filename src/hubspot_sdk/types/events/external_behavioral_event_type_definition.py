# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .property import Property
from ..._models import BaseModel
from .association_definition import AssociationDefinition
from .behavioral_event_type_definition_labels import BehavioralEventTypeDefinitionLabels
from .external_object_resolution_mapping_response import ExternalObjectResolutionMappingResponse

__all__ = ["ExternalBehavioralEventTypeDefinition"]


class ExternalBehavioralEventTypeDefinition(BaseModel):
    id: str

    archived: bool

    associations: List[AssociationDefinition]

    fully_qualified_name: str = FieldInfo(alias="fullyQualifiedName")

    labels: BehavioralEventTypeDefinitionLabels

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    properties: List[Property]

    combo_event_rules: Optional["ComboEventRuleBranch"] = FieldInfo(alias="comboEventRules", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_user_id: Optional[int] = FieldInfo(alias="createdUserId", default=None)

    custom_matching_id: Optional[ExternalObjectResolutionMappingResponse] = FieldInfo(
        alias="customMatchingId", default=None
    )

    description: Optional[str] = None

    primary_object: Optional[str] = FieldInfo(alias="primaryObject", default=None)

    primary_object_id: Optional[str] = FieldInfo(alias="primaryObjectId", default=None)

    tracking_type: Optional[
        Literal[
            "APP_EVENT",
            "AUTOCAPTURE_EVENT",
            "CLICKED_ELEMENT",
            "COMBO_EVENT",
            "CUSTOM_SCRIPT",
            "IMPORT",
            "MANUAL",
            "PROPERTY_CHANGE",
            "VISITED_URL",
            "WEBHOOK",
        ]
    ] = FieldInfo(alias="trackingType", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_user_id: Optional[int] = FieldInfo(alias="updatedUserId", default=None)


from .combo_event_rule_branch import ComboEventRuleBranch
