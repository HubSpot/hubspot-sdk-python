# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicConditionalSingleFieldDependency"]


class PublicConditionalSingleFieldDependency(BaseModel):
    controlling_field_name: str = FieldInfo(alias="controllingFieldName")
    """The name of the field that determines the dependency."""

    controlling_field_value: str = FieldInfo(alias="controllingFieldValue")
    """The value of the controlling field that triggers the dependency."""

    dependency_type: Literal["CONDITIONAL_SINGLE_FIELD"] = FieldInfo(alias="dependencyType")
    """The type of dependency, with the default value being CONDITIONAL_SINGLE_FIELD."""

    dependent_field_names: List[str] = FieldInfo(alias="dependentFieldNames")
