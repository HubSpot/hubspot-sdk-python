# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_file_egg_param import PublicFileEggParam
from .public_social_media_egg_param import PublicSocialMediaEggParam
from .public_quick_replies_egg_param import PublicQuickRepliesEggParam

__all__ = ["PublicCommentEggParam", "Attachment"]

Attachment: TypeAlias = Union[PublicFileEggParam, PublicQuickRepliesEggParam, PublicSocialMediaEggParam]


class PublicCommentEggParam(TypedDict, total=False):
    attachments: Required[Iterable[Attachment]]

    text: Required[str]

    type: Required[Literal["COMMENT"]]

    rich_text: Annotated[str, PropertyInfo(alias="richText")]
