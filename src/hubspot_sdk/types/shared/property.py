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
    """A description of the property that will be shown as help text in HubSpot."""

    field_type: str = FieldInfo(alias="fieldType")
    """Controls how the property appears in HubSpot."""

    group_name: str = FieldInfo(alias="groupName")
    """The name of the property group the property belongs to."""

    label: str
    """A human-readable property label that will be shown in HubSpot."""

    name: str
    """
    The internal property name, which must be used when referencing the property via
    the API.
    """

    options: List[Option]
    """A list of valid options for the property.

    This field is required for enumerated properties, but will be empty for other
    property types.
    """

    type: str
    """The property data type."""

    archived: Optional[bool] = None
    """Whether or not the property is archived."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """When the property was archived."""

    calculated: Optional[bool] = None
    """
    For default properties, true indicates that the property is calculated by a
    HubSpot process. It has no effect for custom properties.
    """

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)
    """The formula used for calculated properties."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the property was created"""

    created_user_id: Optional[str] = FieldInfo(alias="createdUserId", default=None)
    """The internal ID of the user who created the property in HubSpot.

    This field may not exist if the property was created outside of HubSpot.
    """

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
    """
    Controls how date properties are displayed in the HubSpot UI, with options such
    as 'absolute', 'absolute_with_relative', 'time_since', and 'time_until'.
    """

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
    """
    The order that this property should be displayed in the HubSpot UI relative to
    other properties for this object type. Properties are displayed in order
    starting with the lowest positive integer value. A value of -1 will cause the
    property to be displayed **after** any positive values.
    """

    external_options: Optional[bool] = FieldInfo(alias="externalOptions", default=None)
    """
    For default properties, true indicates that the options are stored externally to
    the property settings.
    """

    form_field: Optional[bool] = FieldInfo(alias="formField", default=None)
    """Whether or not the property can be used in a HubSpot form."""

    has_unique_value: Optional[bool] = FieldInfo(alias="hasUniqueValue", default=None)
    """Whether or not the property's value must be unique.

    Once set, this can't be changed.
    """

    hidden: Optional[bool] = None
    """Hidden options won't be shown in HubSpot."""

    hubspot_defined: Optional[bool] = FieldInfo(alias="hubspotDefined", default=None)
    """This will be true for default object properties built into HubSpot."""

    modification_metadata: Optional[PropertyModificationMetadata] = FieldInfo(
        alias="modificationMetadata", default=None
    )

    referenced_object_type: Optional[str] = FieldInfo(alias="referencedObjectType", default=None)
    """If this property is related to other object(s), they'll be listed here."""

    sensitive_data_categories: Optional[List[str]] = FieldInfo(alias="sensitiveDataCategories", default=None)
    """
    When sensitiveData is true, lists the type of sensitive data contained in the
    property (e.g., "HIPAA").
    """

    show_currency_symbol: Optional[bool] = FieldInfo(alias="showCurrencySymbol", default=None)
    """
    Whether the property will display the currency symbol set in the account
    settings.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the object type was last updated."""

    updated_user_id: Optional[str] = FieldInfo(alias="updatedUserId", default=None)
    """The internal user ID of the user who updated the property in HubSpot.

    This field may not exist if the property was updated outside of HubSpot.
    """
