# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .option import Option
from ..._models import BaseModel
from .property_modification_metadata import PropertyModificationMetadata

__all__ = ["Property"]


class Property(BaseModel):
    """A HubSpot property"""

    description: str
    """A summary of the property's purpose."""

    field_type: str = FieldInfo(alias="fieldType")
    """Determines how the property will appear in HubSpot's UI or on a form.

    Learn more in the properties API guide.
    """

    group_name: str = FieldInfo(alias="groupName")
    """The name of the group to which the property is assigned."""

    label: str
    """The display label for the property."""

    name: str
    """The internal name for the property."""

    options: List[Option]
    """A list of valid options for the property.

    This field is required for enumerated properties.
    """

    type: str
    """The data type of the property, such as string or number."""

    archived: Optional[bool] = None
    """Whether the property is archived."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """The timestamp when the property was archived, in ISO 8601 format."""

    calculated: Optional[bool] = None
    """Whether the property is a calculated field."""

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)
    """The formula used for calculated properties."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The timestamp when the property was created, in ISO 8601 format."""

    created_user_id: Optional[str] = FieldInfo(alias="createdUserId", default=None)
    """The ID of the user who created the property."""

    data_sensitivity: Optional[Literal["highly_sensitive", "non_sensitive", "sensitive"]] = FieldInfo(
        alias="dataSensitivity", default=None
    )
    """
    Indicates the sensitivity level of the property, such as "non_sensitive",
    "sensitive", or "highly_sensitive".
    """

    date_display_hint: Optional[Literal["absolute", "absolute_with_relative", "time_since", "time_until"]] = FieldInfo(
        alias="dateDisplayHint", default=None
    )

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
    """The position of the item relative to others in the list."""

    external_options: Optional[bool] = FieldInfo(alias="externalOptions", default=None)
    """Applicable only for enumeration type properties.

    Should be set to true with a 'referencedObjectType' of 'OWNER'. Otherwise false.
    """

    form_field: Optional[bool] = FieldInfo(alias="formField", default=None)
    """Whether the property can appear on forms."""

    has_unique_value: Optional[bool] = FieldInfo(alias="hasUniqueValue", default=None)
    """Whether the property is a unique identifier property."""

    hidden: Optional[bool] = None
    """Whether or not the property will be hidden from the HubSpot UI.

    It's recommended that this be set to false for custom properties.
    """

    hubspot_defined: Optional[bool] = FieldInfo(alias="hubspotDefined", default=None)
    """A boolean value set to true for HubSpot default properties."""

    modification_metadata: Optional[PropertyModificationMetadata] = FieldInfo(
        alias="modificationMetadata", default=None
    )

    referenced_object_type: Optional[str] = FieldInfo(alias="referencedObjectType", default=None)
    """Deprecated. Use externalOptionsReferenceType instead."""

    sensitive_data_categories: Optional[List[str]] = FieldInfo(alias="sensitiveDataCategories", default=None)
    """
    When sensitiveData is true, lists the type of sensitive data contained in the
    property (e.g., "HIPAA").
    """

    show_currency_symbol: Optional[bool] = FieldInfo(alias="showCurrencySymbol", default=None)
    """Whether to show the currency symbol in HubSpot's UI."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The timestamp when the property was last updated, in ISO 8601 format."""

    updated_user_id: Optional[str] = FieldInfo(alias="updatedUserId", default=None)
