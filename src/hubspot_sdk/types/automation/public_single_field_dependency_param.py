# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicSingleFieldDependencyParam"]


class PublicSingleFieldDependencyParam(TypedDict, total=False):
    controlling_field_name: Required[Annotated[str, PropertyInfo(alias="controllingFieldName")]]
    """The name of the field that controls the dependency."""

    dependency_type: Required[Annotated[Literal["SINGLE_FIELD"], PropertyInfo(alias="dependencyType")]]
    """The type of dependency, with the default value being 'SINGLE_FIELD'."""

    dependent_field_names: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="dependentFieldNames")]]
