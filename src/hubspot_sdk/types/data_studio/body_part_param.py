# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .media_type_param import MediaTypeParam
from .content_disposition_param import ContentDispositionParam
from .parameterized_header_param import ParameterizedHeaderParam

__all__ = ["BodyPartParam"]


class BodyPartParam(TypedDict, total=False):
    content_disposition: Required[Annotated[ContentDispositionParam, PropertyInfo(alias="contentDisposition")]]

    entity: Required[object]
    """An object representing the actual content or payload of the body part."""

    headers: Required[Dict[str, SequenceNotStr[str]]]
    """
    An object containing the headers associated with this body part, where each
    header can have multiple string values.
    """

    media_type: Required[Annotated[MediaTypeParam, PropertyInfo(alias="mediaType")]]

    message_body_workers: Required[Annotated[object, PropertyInfo(alias="messageBodyWorkers")]]
    """An object representing workers that handle the processing of the message body."""

    parameterized_headers: Required[
        Annotated[Dict[str, Iterable[ParameterizedHeaderParam]], PropertyInfo(alias="parameterizedHeaders")]
    ]
    """
    An object containing headers with parameters, where each header can have
    multiple ParameterizedHeader objects.
    """

    providers: Required[object]
    """
    An object representing providers that supply additional handling or processing
    for the body part.
    """

    parent: "MultiPartParam"


from .multi_part_param import MultiPartParam
