# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimelineEventIFrameParam"]


class TimelineEventIFrameParam(TypedDict, total=False):
    header_label: Required[Annotated[str, PropertyInfo(alias="headerLabel")]]
    """The label of the modal window that displays the iframe contents."""

    height: Required[int]
    """The height of the modal window in pixels."""

    link_label: Required[Annotated[str, PropertyInfo(alias="linkLabel")]]
    """The text displaying the link that will display the iframe."""

    url: Required[str]
    """The URI of the iframe contents."""

    width: Required[int]
    """The width of the modal window in pixels."""
