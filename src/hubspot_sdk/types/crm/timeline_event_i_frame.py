# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimelineEventIFrame"]


class TimelineEventIFrame(BaseModel):
    header_label: str = FieldInfo(alias="headerLabel")
    """The label of the modal window that displays the iframe contents."""

    height: int
    """The height of the modal window in pixels."""

    link_label: str = FieldInfo(alias="linkLabel")
    """The text displaying the link that will display the iframe."""

    url: str
    """The URI of the iframe contents."""

    width: int
    """The width of the modal window in pixels."""
