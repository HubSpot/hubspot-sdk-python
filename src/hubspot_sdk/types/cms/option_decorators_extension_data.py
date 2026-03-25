# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .option_decorations import OptionDecorations

__all__ = ["OptionDecoratorsExtensionData"]


class OptionDecoratorsExtensionData(BaseModel):
    option_decorators: Dict[str, OptionDecorations] = FieldInfo(alias="optionDecorators")

    option_decorator_style: Literal["LABEL_ONLY", "LABEL_WITH_BADGE", "LABEL_WITH_COLOR"] = FieldInfo(
        alias="optionDecoratorStyle"
    )
