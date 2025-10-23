# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.lists import mapping_get_id_mapping_params
from ....types.crm.public_migration_mapping import PublicMigrationMapping
from ....types.crm.public_batch_migration_mapping import PublicBatchMigrationMapping

__all__ = ["MappingResource", "AsyncMappingResource"]


class MappingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MappingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MappingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MappingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MappingResourceWithStreamingResponse(self)

    def batch_create_id_mapping(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBatchMigrationMapping:
        """This API allows translation of a batch of legacy list id's to list id's.

        This
        allows for a maximum of 10,000 id's. This is a temporary API allowed for mapping
        old id's to new id's and will expire on May 30th, 2025.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/lists/idmapping",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBatchMigrationMapping,
        )

    def get_id_mapping(
        self,
        *,
        legacy_list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicMigrationMapping:
        """This API allows translation of legacy list id to list id.

        This is a temporary
        API allowed for mapping old id's to new id's and will expire on May 30th, 2025.

        Args:
          legacy_list_id: The legacy list id from lists v1 API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/v3/lists/idmapping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"legacy_list_id": legacy_list_id}, mapping_get_id_mapping_params.MappingGetIDMappingParams
                ),
            ),
            cast_to=PublicMigrationMapping,
        )


class AsyncMappingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMappingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMappingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMappingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMappingResourceWithStreamingResponse(self)

    async def batch_create_id_mapping(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBatchMigrationMapping:
        """This API allows translation of a batch of legacy list id's to list id's.

        This
        allows for a maximum of 10,000 id's. This is a temporary API allowed for mapping
        old id's to new id's and will expire on May 30th, 2025.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/lists/idmapping",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBatchMigrationMapping,
        )

    async def get_id_mapping(
        self,
        *,
        legacy_list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicMigrationMapping:
        """This API allows translation of legacy list id to list id.

        This is a temporary
        API allowed for mapping old id's to new id's and will expire on May 30th, 2025.

        Args:
          legacy_list_id: The legacy list id from lists v1 API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/v3/lists/idmapping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"legacy_list_id": legacy_list_id}, mapping_get_id_mapping_params.MappingGetIDMappingParams
                ),
            ),
            cast_to=PublicMigrationMapping,
        )


class MappingResourceWithRawResponse:
    def __init__(self, mapping: MappingResource) -> None:
        self._mapping = mapping

        self.batch_create_id_mapping = to_raw_response_wrapper(
            mapping.batch_create_id_mapping,
        )
        self.get_id_mapping = to_raw_response_wrapper(
            mapping.get_id_mapping,
        )


class AsyncMappingResourceWithRawResponse:
    def __init__(self, mapping: AsyncMappingResource) -> None:
        self._mapping = mapping

        self.batch_create_id_mapping = async_to_raw_response_wrapper(
            mapping.batch_create_id_mapping,
        )
        self.get_id_mapping = async_to_raw_response_wrapper(
            mapping.get_id_mapping,
        )


class MappingResourceWithStreamingResponse:
    def __init__(self, mapping: MappingResource) -> None:
        self._mapping = mapping

        self.batch_create_id_mapping = to_streamed_response_wrapper(
            mapping.batch_create_id_mapping,
        )
        self.get_id_mapping = to_streamed_response_wrapper(
            mapping.get_id_mapping,
        )


class AsyncMappingResourceWithStreamingResponse:
    def __init__(self, mapping: AsyncMappingResource) -> None:
        self._mapping = mapping

        self.batch_create_id_mapping = async_to_streamed_response_wrapper(
            mapping.batch_create_id_mapping,
        )
        self.get_id_mapping = async_to_streamed_response_wrapper(
            mapping.get_id_mapping,
        )
