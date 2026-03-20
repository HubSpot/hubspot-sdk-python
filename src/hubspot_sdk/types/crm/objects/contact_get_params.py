# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ContactGetParams"]


class ContactGetParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    archived: bool
    """Whether to return only results that have been archived."""

    associations: SequenceNotStr[str]
    """A comma separated list of object types to retrieve associated IDs for.

    If any of the specified associations do not exist, they will be ignored.
    """

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
    """The name of a property whose values are unique for this object"""

    properties: SequenceNotStr[str]
    """A comma separated list of the properties to be returned in the response.

    If any of the specified properties are not present on the requested object(s),
    they will be ignored.
    """

    properties_with_history: Annotated[SequenceNotStr[str], PropertyInfo(alias="propertiesWithHistory")]
    """
    A comma separated list of the properties to be returned along with their history
    of previous values. If any of the specified properties are not present on the
    requested object(s), they will be ignored.
    """
