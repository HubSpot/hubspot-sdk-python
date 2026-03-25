# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactNameParam"]


class ContactNameParam(TypedDict, total=False):
    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]

    prefix: str

    suffix: str
