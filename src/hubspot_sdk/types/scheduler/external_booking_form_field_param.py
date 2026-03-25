# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalBookingFormFieldParam"]


class ExternalBookingFormFieldParam(TypedDict, total=False):
    name: Required[str]
    """The name of the form field."""

    value: Required[str]
    """The value associated with the form field."""
