# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StageReplaceParams"]


class StageReplaceParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    pipeline_id: Required[Annotated[str, PropertyInfo(alias="pipelineId")]]

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """The order for displaying this pipeline stage.

    If two pipeline stages have a matching `displayOrder`, they will be sorted
    alphabetically by label.
    """

    label: Required[str]
    """A label used to organize pipeline stages in HubSpot's UI.

    Each pipeline stage's label must be unique within that pipeline.
    """

    metadata: Dict[str, str]
    """
    A JSON object containing properties that are not present on all object
    pipelines.

    For `deals` pipelines, the `probability` field is required
    (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
    Possible values are between 0.0 and 1.0 in increments of 0.1.

    For `tickets` pipelines, the `ticketState` field is optional
    (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
    has been closed by a member of your Support team. Possible values are `OPEN` or
    `CLOSED`.
    """
