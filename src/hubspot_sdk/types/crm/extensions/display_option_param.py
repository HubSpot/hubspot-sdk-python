# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DisplayOptionParam"]


class DisplayOptionParam(TypedDict, total=False):
    """Option definition for STATUS dataTypes."""

    label: Required[str]
    """The text that will be displayed to users for this option."""

    name: Required[str]
    """JSON-friendly unique name for option."""

    type: Required[Literal["DANGER", "DEFAULT", "INFO", "SUCCESS", "WARNING"]]
    """The type of status."""
