# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ParameterizedHeaderParam"]


class ParameterizedHeaderParam(TypedDict, total=False):
    parameters: Required[Dict[str, str]]
    """
    An object containing additional parameters for the header, where each key is a
    parameter name and each value is a string representing the parameter's value.
    """

    value: Required[str]
    """A string representing the main value of the header."""
