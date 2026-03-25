# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .media_type_param import MediaTypeParam
from .content_disposition_param import ContentDispositionParam
from .parameterized_header_param import ParameterizedHeaderParam
from .form_data_content_disposition_param import FormDataContentDispositionParam

__all__ = ["FormDataBodyPartParam"]


class FormDataBodyPartParam(TypedDict, total=False):
    content_disposition: Required[Annotated[ContentDispositionParam, PropertyInfo(alias="contentDisposition")]]

    entity: Required[object]
    """
    An object representing the entity of the form data part, which contains the
    actual data being submitted.
    """

    form_data_content_disposition: Required[
        Annotated[FormDataContentDispositionParam, PropertyInfo(alias="formDataContentDisposition")]
    ]

    headers: Required[Dict[str, SequenceNotStr[str]]]
    """
    An object containing the headers associated with this form data part, where each
    header can have multiple string values.
    """

    media_type: Required[Annotated[MediaTypeParam, PropertyInfo(alias="mediaType")]]

    message_body_workers: Required[Annotated[object, PropertyInfo(alias="messageBodyWorkers")]]
    """
    An object representing the message body workers, which are responsible for
    processing the body of the message.
    """

    name: Required[str]
    """
    The name of the form data part, typically used to identify the part within the
    multipart request.
    """

    parameterized_headers: Required[
        Annotated[Dict[str, Iterable[ParameterizedHeaderParam]], PropertyInfo(alias="parameterizedHeaders")]
    ]
    """
    An object containing parameterized headers, where each header can have multiple
    values represented as ParameterizedHeader objects.
    """

    providers: Required[object]
    """An object representing the providers associated with this form data part."""

    simple: Required[bool]
    """
    A boolean indicating whether the form data part is simple, typically meaning it
    does not contain complex nested structures.
    """

    value: Required[str]
    """
    The string value of the form data part, representing the actual data being
    submitted as a string.
    """

    parent: "MultiPartParam"


from .multi_part_param import MultiPartParam
