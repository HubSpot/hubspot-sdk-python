# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .limits import (
    LimitsResource,
    AsyncLimitsResource,
    LimitsResourceWithRawResponse,
    AsyncLimitsResourceWithRawResponse,
    LimitsResourceWithStreamingResponse,
    AsyncLimitsResourceWithStreamingResponse,
)
from .owners import (
    OwnersResource,
    AsyncOwnersResource,
    OwnersResourceWithRawResponse,
    AsyncOwnersResourceWithRawResponse,
    OwnersResourceWithStreamingResponse,
    AsyncOwnersResourceWithStreamingResponse,
)
from .exports import (
    ExportsResource,
    AsyncExportsResource,
    ExportsResourceWithRawResponse,
    AsyncExportsResourceWithRawResponse,
    ExportsResourceWithStreamingResponse,
    AsyncExportsResourceWithStreamingResponse,
)
from .imports import (
    ImportsResource,
    AsyncImportsResource,
    ImportsResourceWithRawResponse,
    AsyncImportsResourceWithRawResponse,
    ImportsResourceWithStreamingResponse,
    AsyncImportsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .pipelines import (
    PipelinesResource,
    AsyncPipelinesResource,
    PipelinesResourceWithRawResponse,
    AsyncPipelinesResourceWithRawResponse,
    PipelinesResourceWithStreamingResponse,
    AsyncPipelinesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .app_uninstalls import (
    AppUninstallsResource,
    AsyncAppUninstallsResource,
    AppUninstallsResourceWithRawResponse,
    AsyncAppUninstallsResourceWithRawResponse,
    AppUninstallsResourceWithStreamingResponse,
    AsyncAppUninstallsResourceWithStreamingResponse,
)
from .objects.objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)
from .extensions.extensions import (
    ExtensionsResource,
    AsyncExtensionsResource,
    ExtensionsResourceWithRawResponse,
    AsyncExtensionsResourceWithRawResponse,
    ExtensionsResourceWithStreamingResponse,
    AsyncExtensionsResourceWithStreamingResponse,
)
from .properties.properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from .properties_validations import (
    PropertiesValidationsResource,
    AsyncPropertiesValidationsResource,
    PropertiesValidationsResourceWithRawResponse,
    AsyncPropertiesValidationsResourceWithRawResponse,
    PropertiesValidationsResourceWithStreamingResponse,
    AsyncPropertiesValidationsResourceWithStreamingResponse,
)
from .deal_splits.deal_splits import (
    DealSplitsResource,
    AsyncDealSplitsResource,
    DealSplitsResourceWithRawResponse,
    AsyncDealSplitsResourceWithRawResponse,
    DealSplitsResourceWithStreamingResponse,
    AsyncDealSplitsResourceWithStreamingResponse,
)
from .associations.associations import (
    AssociationsResource,
    AsyncAssociationsResource,
    AssociationsResourceWithRawResponse,
    AsyncAssociationsResourceWithRawResponse,
    AssociationsResourceWithStreamingResponse,
    AsyncAssociationsResourceWithStreamingResponse,
)
from .object_library.object_library import (
    ObjectLibraryResource,
    AsyncObjectLibraryResource,
    ObjectLibraryResourceWithRawResponse,
    AsyncObjectLibraryResourceWithRawResponse,
    ObjectLibraryResourceWithStreamingResponse,
    AsyncObjectLibraryResourceWithStreamingResponse,
)
from .object_schemas.object_schemas import (
    ObjectSchemasResource,
    AsyncObjectSchemasResource,
    ObjectSchemasResourceWithRawResponse,
    AsyncObjectSchemasResourceWithRawResponse,
    ObjectSchemasResourceWithStreamingResponse,
    AsyncObjectSchemasResourceWithStreamingResponse,
)
from .associations_schema.associations_schema import (
    AssociationsSchemaResource,
    AsyncAssociationsSchemaResource,
    AssociationsSchemaResourceWithRawResponse,
    AsyncAssociationsSchemaResourceWithRawResponse,
    AssociationsSchemaResourceWithStreamingResponse,
    AsyncAssociationsSchemaResourceWithStreamingResponse,
)

__all__ = ["CrmResource", "AsyncCrmResource"]


class CrmResource(SyncAPIResource):
    @cached_property
    def app_uninstalls(self) -> AppUninstallsResource:
        return AppUninstallsResource(self._client)

    @cached_property
    def associations(self) -> AssociationsResource:
        return AssociationsResource(self._client)

    @cached_property
    def associations_schema(self) -> AssociationsSchemaResource:
        return AssociationsSchemaResource(self._client)

    @cached_property
    def deal_splits(self) -> DealSplitsResource:
        return DealSplitsResource(self._client)

    @cached_property
    def exports(self) -> ExportsResource:
        return ExportsResource(self._client)

    @cached_property
    def extensions(self) -> ExtensionsResource:
        return ExtensionsResource(self._client)

    @cached_property
    def imports(self) -> ImportsResource:
        return ImportsResource(self._client)

    @cached_property
    def limits(self) -> LimitsResource:
        return LimitsResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def object_library(self) -> ObjectLibraryResource:
        return ObjectLibraryResource(self._client)

    @cached_property
    def object_schemas(self) -> ObjectSchemasResource:
        return ObjectSchemasResource(self._client)

    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

    @cached_property
    def owners(self) -> OwnersResource:
        return OwnersResource(self._client)

    @cached_property
    def pipelines(self) -> PipelinesResource:
        return PipelinesResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def properties_validations(self) -> PropertiesValidationsResource:
        return PropertiesValidationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CrmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CrmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CrmResourceWithStreamingResponse(self)


class AsyncCrmResource(AsyncAPIResource):
    @cached_property
    def app_uninstalls(self) -> AsyncAppUninstallsResource:
        return AsyncAppUninstallsResource(self._client)

    @cached_property
    def associations(self) -> AsyncAssociationsResource:
        return AsyncAssociationsResource(self._client)

    @cached_property
    def associations_schema(self) -> AsyncAssociationsSchemaResource:
        return AsyncAssociationsSchemaResource(self._client)

    @cached_property
    def deal_splits(self) -> AsyncDealSplitsResource:
        return AsyncDealSplitsResource(self._client)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        return AsyncExportsResource(self._client)

    @cached_property
    def extensions(self) -> AsyncExtensionsResource:
        return AsyncExtensionsResource(self._client)

    @cached_property
    def imports(self) -> AsyncImportsResource:
        return AsyncImportsResource(self._client)

    @cached_property
    def limits(self) -> AsyncLimitsResource:
        return AsyncLimitsResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def object_library(self) -> AsyncObjectLibraryResource:
        return AsyncObjectLibraryResource(self._client)

    @cached_property
    def object_schemas(self) -> AsyncObjectSchemasResource:
        return AsyncObjectSchemasResource(self._client)

    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

    @cached_property
    def owners(self) -> AsyncOwnersResource:
        return AsyncOwnersResource(self._client)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResource:
        return AsyncPipelinesResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def properties_validations(self) -> AsyncPropertiesValidationsResource:
        return AsyncPropertiesValidationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCrmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCrmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCrmResourceWithStreamingResponse(self)


class CrmResourceWithRawResponse:
    def __init__(self, crm: CrmResource) -> None:
        self._crm = crm

    @cached_property
    def app_uninstalls(self) -> AppUninstallsResourceWithRawResponse:
        return AppUninstallsResourceWithRawResponse(self._crm.app_uninstalls)

    @cached_property
    def associations(self) -> AssociationsResourceWithRawResponse:
        return AssociationsResourceWithRawResponse(self._crm.associations)

    @cached_property
    def associations_schema(self) -> AssociationsSchemaResourceWithRawResponse:
        return AssociationsSchemaResourceWithRawResponse(self._crm.associations_schema)

    @cached_property
    def deal_splits(self) -> DealSplitsResourceWithRawResponse:
        return DealSplitsResourceWithRawResponse(self._crm.deal_splits)

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        return ExportsResourceWithRawResponse(self._crm.exports)

    @cached_property
    def extensions(self) -> ExtensionsResourceWithRawResponse:
        return ExtensionsResourceWithRawResponse(self._crm.extensions)

    @cached_property
    def imports(self) -> ImportsResourceWithRawResponse:
        return ImportsResourceWithRawResponse(self._crm.imports)

    @cached_property
    def limits(self) -> LimitsResourceWithRawResponse:
        return LimitsResourceWithRawResponse(self._crm.limits)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._crm.lists)

    @cached_property
    def object_library(self) -> ObjectLibraryResourceWithRawResponse:
        return ObjectLibraryResourceWithRawResponse(self._crm.object_library)

    @cached_property
    def object_schemas(self) -> ObjectSchemasResourceWithRawResponse:
        return ObjectSchemasResourceWithRawResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._crm.objects)

    @cached_property
    def owners(self) -> OwnersResourceWithRawResponse:
        return OwnersResourceWithRawResponse(self._crm.owners)

    @cached_property
    def pipelines(self) -> PipelinesResourceWithRawResponse:
        return PipelinesResourceWithRawResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._crm.properties)

    @cached_property
    def properties_validations(self) -> PropertiesValidationsResourceWithRawResponse:
        return PropertiesValidationsResourceWithRawResponse(self._crm.properties_validations)


class AsyncCrmResourceWithRawResponse:
    def __init__(self, crm: AsyncCrmResource) -> None:
        self._crm = crm

    @cached_property
    def app_uninstalls(self) -> AsyncAppUninstallsResourceWithRawResponse:
        return AsyncAppUninstallsResourceWithRawResponse(self._crm.app_uninstalls)

    @cached_property
    def associations(self) -> AsyncAssociationsResourceWithRawResponse:
        return AsyncAssociationsResourceWithRawResponse(self._crm.associations)

    @cached_property
    def associations_schema(self) -> AsyncAssociationsSchemaResourceWithRawResponse:
        return AsyncAssociationsSchemaResourceWithRawResponse(self._crm.associations_schema)

    @cached_property
    def deal_splits(self) -> AsyncDealSplitsResourceWithRawResponse:
        return AsyncDealSplitsResourceWithRawResponse(self._crm.deal_splits)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        return AsyncExportsResourceWithRawResponse(self._crm.exports)

    @cached_property
    def extensions(self) -> AsyncExtensionsResourceWithRawResponse:
        return AsyncExtensionsResourceWithRawResponse(self._crm.extensions)

    @cached_property
    def imports(self) -> AsyncImportsResourceWithRawResponse:
        return AsyncImportsResourceWithRawResponse(self._crm.imports)

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithRawResponse:
        return AsyncLimitsResourceWithRawResponse(self._crm.limits)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._crm.lists)

    @cached_property
    def object_library(self) -> AsyncObjectLibraryResourceWithRawResponse:
        return AsyncObjectLibraryResourceWithRawResponse(self._crm.object_library)

    @cached_property
    def object_schemas(self) -> AsyncObjectSchemasResourceWithRawResponse:
        return AsyncObjectSchemasResourceWithRawResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._crm.objects)

    @cached_property
    def owners(self) -> AsyncOwnersResourceWithRawResponse:
        return AsyncOwnersResourceWithRawResponse(self._crm.owners)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithRawResponse:
        return AsyncPipelinesResourceWithRawResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._crm.properties)

    @cached_property
    def properties_validations(self) -> AsyncPropertiesValidationsResourceWithRawResponse:
        return AsyncPropertiesValidationsResourceWithRawResponse(self._crm.properties_validations)


class CrmResourceWithStreamingResponse:
    def __init__(self, crm: CrmResource) -> None:
        self._crm = crm

    @cached_property
    def app_uninstalls(self) -> AppUninstallsResourceWithStreamingResponse:
        return AppUninstallsResourceWithStreamingResponse(self._crm.app_uninstalls)

    @cached_property
    def associations(self) -> AssociationsResourceWithStreamingResponse:
        return AssociationsResourceWithStreamingResponse(self._crm.associations)

    @cached_property
    def associations_schema(self) -> AssociationsSchemaResourceWithStreamingResponse:
        return AssociationsSchemaResourceWithStreamingResponse(self._crm.associations_schema)

    @cached_property
    def deal_splits(self) -> DealSplitsResourceWithStreamingResponse:
        return DealSplitsResourceWithStreamingResponse(self._crm.deal_splits)

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        return ExportsResourceWithStreamingResponse(self._crm.exports)

    @cached_property
    def extensions(self) -> ExtensionsResourceWithStreamingResponse:
        return ExtensionsResourceWithStreamingResponse(self._crm.extensions)

    @cached_property
    def imports(self) -> ImportsResourceWithStreamingResponse:
        return ImportsResourceWithStreamingResponse(self._crm.imports)

    @cached_property
    def limits(self) -> LimitsResourceWithStreamingResponse:
        return LimitsResourceWithStreamingResponse(self._crm.limits)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._crm.lists)

    @cached_property
    def object_library(self) -> ObjectLibraryResourceWithStreamingResponse:
        return ObjectLibraryResourceWithStreamingResponse(self._crm.object_library)

    @cached_property
    def object_schemas(self) -> ObjectSchemasResourceWithStreamingResponse:
        return ObjectSchemasResourceWithStreamingResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._crm.objects)

    @cached_property
    def owners(self) -> OwnersResourceWithStreamingResponse:
        return OwnersResourceWithStreamingResponse(self._crm.owners)

    @cached_property
    def pipelines(self) -> PipelinesResourceWithStreamingResponse:
        return PipelinesResourceWithStreamingResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._crm.properties)

    @cached_property
    def properties_validations(self) -> PropertiesValidationsResourceWithStreamingResponse:
        return PropertiesValidationsResourceWithStreamingResponse(self._crm.properties_validations)


class AsyncCrmResourceWithStreamingResponse:
    def __init__(self, crm: AsyncCrmResource) -> None:
        self._crm = crm

    @cached_property
    def app_uninstalls(self) -> AsyncAppUninstallsResourceWithStreamingResponse:
        return AsyncAppUninstallsResourceWithStreamingResponse(self._crm.app_uninstalls)

    @cached_property
    def associations(self) -> AsyncAssociationsResourceWithStreamingResponse:
        return AsyncAssociationsResourceWithStreamingResponse(self._crm.associations)

    @cached_property
    def associations_schema(self) -> AsyncAssociationsSchemaResourceWithStreamingResponse:
        return AsyncAssociationsSchemaResourceWithStreamingResponse(self._crm.associations_schema)

    @cached_property
    def deal_splits(self) -> AsyncDealSplitsResourceWithStreamingResponse:
        return AsyncDealSplitsResourceWithStreamingResponse(self._crm.deal_splits)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        return AsyncExportsResourceWithStreamingResponse(self._crm.exports)

    @cached_property
    def extensions(self) -> AsyncExtensionsResourceWithStreamingResponse:
        return AsyncExtensionsResourceWithStreamingResponse(self._crm.extensions)

    @cached_property
    def imports(self) -> AsyncImportsResourceWithStreamingResponse:
        return AsyncImportsResourceWithStreamingResponse(self._crm.imports)

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithStreamingResponse:
        return AsyncLimitsResourceWithStreamingResponse(self._crm.limits)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._crm.lists)

    @cached_property
    def object_library(self) -> AsyncObjectLibraryResourceWithStreamingResponse:
        return AsyncObjectLibraryResourceWithStreamingResponse(self._crm.object_library)

    @cached_property
    def object_schemas(self) -> AsyncObjectSchemasResourceWithStreamingResponse:
        return AsyncObjectSchemasResourceWithStreamingResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._crm.objects)

    @cached_property
    def owners(self) -> AsyncOwnersResourceWithStreamingResponse:
        return AsyncOwnersResourceWithStreamingResponse(self._crm.owners)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithStreamingResponse:
        return AsyncPipelinesResourceWithStreamingResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._crm.properties)

    @cached_property
    def properties_validations(self) -> AsyncPropertiesValidationsResourceWithStreamingResponse:
        return AsyncPropertiesValidationsResourceWithStreamingResponse(self._crm.properties_validations)
