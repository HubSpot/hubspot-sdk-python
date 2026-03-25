# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .media_type_param import MediaTypeParam
from .content_disposition_param import ContentDispositionParam
from .parameterized_header_param import ParameterizedHeaderParam

__all__ = ["DatasourceCreateParams"]


class DatasourceCreateParams(TypedDict, total=False):
    body_parts: Required[Annotated[Iterable["BodyPartParam"], PropertyInfo(alias="bodyParts")]]
    """
    An array of BodyPart objects, each representing a part of the multipart form
    data.
    """

    content_disposition: Required[Annotated[ContentDispositionParam, PropertyInfo(alias="contentDisposition")]]

    entity: Required[object]
    """
    An object representing the entity of the multipart form data, containing the
    actual data to be processed.
    """

    fields: Required[Dict[str, Iterable["FormDataBodyPartParam"]]]
    """
    An object containing fields of the multipart form data, where each field can
    have multiple FormDataBodyPart items.
    """

    headers: Required[Dict[str, SequenceNotStr[str]]]
    """
    An object containing headers associated with the multipart form data, where each
    header can have multiple string values.
    """

    media_type: Required[Annotated[MediaTypeParam, PropertyInfo(alias="mediaType")]]

    message_body_workers: Required[Annotated[object, PropertyInfo(alias="messageBodyWorkers")]]
    """
    An object representing workers that process the message body of the multipart
    form data.
    """

    parameterized_headers: Required[
        Annotated[Dict[str, Iterable[ParameterizedHeaderParam]], PropertyInfo(alias="parameterizedHeaders")]
    ]
    """
    An object containing parameterized headers, where each header can have multiple
    ParameterizedHeader items.
    """

    providers: Required[object]
    """An object representing providers associated with the multipart form data."""

    parent: "MultiPartParam"


from .body_part_param import BodyPartParam
from .multi_part_param import MultiPartParam
from .form_data_body_part_param import FormDataBodyPartParam
