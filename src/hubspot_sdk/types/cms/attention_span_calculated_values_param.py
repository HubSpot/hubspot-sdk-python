# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AttentionSpanCalculatedValuesParam"]


class AttentionSpanCalculatedValuesParam(TypedDict, total=False):
    total_percent_played: Required[Annotated[float, PropertyInfo(alias="totalPercentPlayed")]]

    total_seconds_played: Required[Annotated[int, PropertyInfo(alias="totalSecondsPlayed")]]
