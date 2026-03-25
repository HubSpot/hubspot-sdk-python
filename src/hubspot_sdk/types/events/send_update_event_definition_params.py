# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SendUpdateEventDefinitionParams"]


class SendUpdateEventDefinitionParams(TypedDict, total=False):
    description: str
    """A description of the event that will be shown as help text in HubSpot."""

    label: str
    """Human readable label for the event. Used in HubSpot UI"""
