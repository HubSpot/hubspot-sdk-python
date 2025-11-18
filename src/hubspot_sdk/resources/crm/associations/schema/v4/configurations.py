# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ......_types import Body, Query, Headers, NotGiven, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.crm.batch_response_void import BatchResponseVoid
from ......types.crm.associations.schema.v4 import (
    configuration_batch_create_params,
    configuration_batch_delete_params,
    configuration_batch_update_params,
)
from ......types.crm.associations.schema.public_association_spec_param import PublicAssociationSpecParam
from ......types.crm.associations.schema.batch_response_public_association_definition_user_configuration import (
    BatchResponsePublicAssociationDefinitionUserConfiguration,
)
from ......types.crm.associations.schema.public_association_definition_configuration_create_request_param import (
    PublicAssociationDefinitionConfigurationCreateRequestParam,
)
from ......types.crm.associations.schema.public_association_definition_configuration_update_request_param import (
    PublicAssociationDefinitionConfigurationUpdateRequestParam,
)
from ......types.crm.associations.schema.collection_response_public_association_definition_user_configuration import (
    CollectionResponsePublicAssociationDefinitionUserConfiguration,
)
from ......types.crm.associations.schema.batch_response_public_association_definition_configuration_update_result import (
    BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
)

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAssociationDefinitionUserConfiguration:
        return self._get(
            "/crm/associations/v4/definitions/configurations/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfiguration,
        )

    def batch_create(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationDefinitionConfigurationCreateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationDefinitionUserConfiguration:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}/batch/create",
            body=maybe_transform({"inputs": inputs}, configuration_batch_create_params.ConfigurationBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationDefinitionUserConfiguration,
        )

    def batch_delete(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationSpecParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseVoid:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}/batch/purge",
            body=maybe_transform({"inputs": inputs}, configuration_batch_delete_params.ConfigurationBatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseVoid,
        )

    def batch_update(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationDefinitionConfigurationUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationDefinitionConfigurationUpdateResult:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}/batch/update",
            body=maybe_transform({"inputs": inputs}, configuration_batch_update_params.ConfigurationBatchUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
        )

    def get_by_object_types(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAssociationDefinitionUserConfiguration:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._get(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfiguration,
        )


class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAssociationDefinitionUserConfiguration:
        return await self._get(
            "/crm/associations/v4/definitions/configurations/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfiguration,
        )

    async def batch_create(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationDefinitionConfigurationCreateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationDefinitionUserConfiguration:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, configuration_batch_create_params.ConfigurationBatchCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationDefinitionUserConfiguration,
        )

    async def batch_delete(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationSpecParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseVoid:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}/batch/purge",
            body=await async_maybe_transform(
                {"inputs": inputs}, configuration_batch_delete_params.ConfigurationBatchDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseVoid,
        )

    async def batch_update(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationDefinitionConfigurationUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationDefinitionConfigurationUpdateResult:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}/batch/update",
            body=await async_maybe_transform(
                {"inputs": inputs}, configuration_batch_update_params.ConfigurationBatchUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
        )

    async def get_by_object_types(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAssociationDefinitionUserConfiguration:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._get(
            f"/crm/associations/v4/definitions/configurations/{from_object_type}/{to_object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfiguration,
        )


class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.list = to_raw_response_wrapper(
            configurations.list,
        )
        self.batch_create = to_raw_response_wrapper(
            configurations.batch_create,
        )
        self.batch_delete = to_raw_response_wrapper(
            configurations.batch_delete,
        )
        self.batch_update = to_raw_response_wrapper(
            configurations.batch_update,
        )
        self.get_by_object_types = to_raw_response_wrapper(
            configurations.get_by_object_types,
        )


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.list = async_to_raw_response_wrapper(
            configurations.list,
        )
        self.batch_create = async_to_raw_response_wrapper(
            configurations.batch_create,
        )
        self.batch_delete = async_to_raw_response_wrapper(
            configurations.batch_delete,
        )
        self.batch_update = async_to_raw_response_wrapper(
            configurations.batch_update,
        )
        self.get_by_object_types = async_to_raw_response_wrapper(
            configurations.get_by_object_types,
        )


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.list = to_streamed_response_wrapper(
            configurations.list,
        )
        self.batch_create = to_streamed_response_wrapper(
            configurations.batch_create,
        )
        self.batch_delete = to_streamed_response_wrapper(
            configurations.batch_delete,
        )
        self.batch_update = to_streamed_response_wrapper(
            configurations.batch_update,
        )
        self.get_by_object_types = to_streamed_response_wrapper(
            configurations.get_by_object_types,
        )


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.list = async_to_streamed_response_wrapper(
            configurations.list,
        )
        self.batch_create = async_to_streamed_response_wrapper(
            configurations.batch_create,
        )
        self.batch_delete = async_to_streamed_response_wrapper(
            configurations.batch_delete,
        )
        self.batch_update = async_to_streamed_response_wrapper(
            configurations.batch_update,
        )
        self.get_by_object_types = async_to_streamed_response_wrapper(
            configurations.get_by_object_types,
        )
