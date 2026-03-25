# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .case_change_test_extension_data import CaseChangeTestExtensionData
from .option_decorators_extension_data import OptionDecoratorsExtensionData
from .required_properties_extension_data import RequiredPropertiesExtensionData
from .soft_required_properties_extension_data import SoftRequiredPropertiesExtensionData

__all__ = ["ExtensionData"]


class ExtensionData(BaseModel):
    extension_status_map: Dict[str, Literal["OK", "ERROR", "TIMEOUT"]] = FieldInfo(alias="extensionStatusMap")

    tags: List[str]

    case_change_test_extension_data: Optional[CaseChangeTestExtensionData] = FieldInfo(
        alias="caseChangeTestExtensionData", default=None
    )

    option_decorators_extension_data: Optional[OptionDecoratorsExtensionData] = FieldInfo(
        alias="optionDecoratorsExtensionData", default=None
    )

    required_properties_extension_data: Optional[RequiredPropertiesExtensionData] = FieldInfo(
        alias="requiredPropertiesExtensionData", default=None
    )

    soft_required_properties_extension_data: Optional[SoftRequiredPropertiesExtensionData] = FieldInfo(
        alias="softRequiredPropertiesExtensionData", default=None
    )
