# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PreResolvedContactParam"]


class PreResolvedContactParam(TypedDict, total=False):
    contact_properties_leading_to_match: Required[
        Annotated[SequenceNotStr[str], PropertyInfo(alias="contactPropertiesLeadingToMatch")]
    ]

    contact_vid: Required[Annotated[int, PropertyInfo(alias="contactVid")]]
