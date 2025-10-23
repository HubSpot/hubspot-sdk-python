# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserGetParams"]


class UserGetParams(TypedDict, total=False):
    id_property: Annotated[Literal["USER_ID", "EMAIL"], PropertyInfo(alias="idProperty")]
    """The name of a property with unique user values.

    Valid values are `USER_ID`(default) or `EMAIL`
    """
