# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .dependent_field_filter import DependentFieldFilter

__all__ = ["DependentField"]


class DependentField(BaseModel):
    """
    A form field that will be displayed based on what the customer entered in another field.
    """

    dependent_condition: DependentFieldFilter = FieldInfo(alias="dependentCondition")
    """A condition based on customer input"""

    dependent_field: DependentField = FieldInfo(alias="dependentField")
    """A form field used for collecting an email address."""
