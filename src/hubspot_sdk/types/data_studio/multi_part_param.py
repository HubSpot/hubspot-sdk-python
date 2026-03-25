# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .media_type_param import MediaTypeParam
from .content_disposition_param import ContentDispositionParam
from .parameterized_header_param import ParameterizedHeaderParam

__all__ = ["MultiPartParam"]


class MultiPartParam(TypedDict, total=False):
    body_parts: Required[Annotated[Iterable["BodyPartParam"], PropertyInfo(alias="bodyParts")]]
    """
    An array of BodyPart objects, each representing a distinct part of the multipart
    entity.
    """

    content_disposition: Required[Annotated[ContentDispositionParam, PropertyInfo(alias="contentDisposition")]]

    entity: Required[object]
    """An object that holds the main content or payload of the multipart entity."""

    headers: Required[Dict[str, SequenceNotStr[str]]]
    """
    An object containing a map of header names to their respective values, where
    each value is an array of strings.
    """

    media_type: Required[Annotated[MediaTypeParam, PropertyInfo(alias="mediaType")]]

    message_body_workers: Required[Annotated[object, PropertyInfo(alias="messageBodyWorkers")]]
    """
    An object that may contain workers for processing the message body, though its
    specific properties are not detailed.
    """

    parameterized_headers: Required[
        Annotated[Dict[str, Iterable[ParameterizedHeaderParam]], PropertyInfo(alias="parameterizedHeaders")]
    ]
    """
    An object containing a map of header names to arrays of ParameterizedHeader
    objects, which include additional parameters for each header.
    """

    providers: Required[object]
    """
    An object that may contain providers related to the multipart entity, though its
    specific properties are not detailed.
    """

    parent: "MultiPartParam"


from .body_part_param import BodyPartParam
