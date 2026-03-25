# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .create_audio_object_request_param import CreateAudioObjectRequestParam
from .create_image_object_request_param import CreateImageObjectRequestParam
from .create_other_object_request_param import CreateOtherObjectRequestParam
from .create_video_object_request_param import CreateVideoObjectRequestParam
from .create_document_object_request_param import CreateDocumentObjectRequestParam

__all__ = ["CreateMBObjectRequestParam"]

CreateMBObjectRequestParam: TypeAlias = Union[
    CreateVideoObjectRequestParam,
    CreateOtherObjectRequestParam,
    CreateAudioObjectRequestParam,
    CreateImageObjectRequestParam,
    CreateDocumentObjectRequestParam,
]
