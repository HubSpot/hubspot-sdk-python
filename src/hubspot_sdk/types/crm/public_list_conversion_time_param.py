# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .public_list_conversion_date_param import PublicListConversionDateParam
from .public_list_conversion_inactivity_param import PublicListConversionInactivityParam

__all__ = ["PublicListConversionTimeParam"]

PublicListConversionTimeParam: TypeAlias = Union[PublicListConversionDateParam, PublicListConversionInactivityParam]
