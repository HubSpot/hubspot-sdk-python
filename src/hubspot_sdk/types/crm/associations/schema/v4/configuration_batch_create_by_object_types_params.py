# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo
from ..public_association_definition_configuration_create_request_param import (
    PublicAssociationDefinitionConfigurationCreateRequestParam,
)

__all__ = ["ConfigurationBatchCreateByObjectTypesParams"]


class ConfigurationBatchCreateByObjectTypesParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    inputs: Required[Iterable[PublicAssociationDefinitionConfigurationCreateRequestParam]]
