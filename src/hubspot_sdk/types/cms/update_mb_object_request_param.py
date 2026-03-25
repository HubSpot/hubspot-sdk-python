# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .update_audio_object_request_param import UpdateAudioObjectRequestParam
from .update_image_object_request_param import UpdateImageObjectRequestParam
from .update_other_object_request_param import UpdateOtherObjectRequestParam
from .update_video_object_request_param import UpdateVideoObjectRequestParam
from .update_document_object_request_param import UpdateDocumentObjectRequestParam

__all__ = ["UpdateMBObjectRequestParam"]

UpdateMBObjectRequestParam: TypeAlias = Union[
    UpdateVideoObjectRequestParam,
    UpdateOtherObjectRequestParam,
    UpdateAudioObjectRequestParam,
    UpdateImageObjectRequestParam,
    UpdateDocumentObjectRequestParam,
]
