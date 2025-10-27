# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailCloneParams"]


class EmailCloneParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the email to be cloned."""

    clone_name: Annotated[str, PropertyInfo(alias="cloneName")]
    """The name to assign to the cloned email."""

    language: str
    """The language code for the cloned email, such as 'en' for English."""
