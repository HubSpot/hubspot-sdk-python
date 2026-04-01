# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.associations_schema import limit_batch_delete_params, limit_batch_update_params
from ....types.crm.public_association_spec_param import PublicAssociationSpecParam
from ....types.crm.public_association_definition_configuration_update_request_param import (
    PublicAssociationDefinitionConfigurationUpdateRequestParam,
)
from ....types.crm.batch_response_public_association_definition_configuration_update_result import (
    BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
)
from ....types.crm.collection_response_public_association_definition_user_configuration_no_paging import (
    CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
)

__all__ = ["LimitsResource", "AsyncLimitsResource"]


class LimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return LimitsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging:
        """
        Retrieve all configured association limits between objects, which include
        details about how different CRM object types are associated with each other.
        """
        return self._get(
            "/crm/associations/2026-03/definitions/configurations/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
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
    ) -> None:
        """
        Batch delete limits that have been defined for association types between two
        object types.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}/batch/purge",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, limit_batch_delete_params.LimitBatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Batch update association limits that have been configured between two object
        types.

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
            path_template(
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}/batch/update",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, limit_batch_update_params.LimitBatchUpdateParams),
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
    ) -> CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging:
        """
        Retrieve the configuration details for associations between two specified CRM
        object types. Use this endpoint to understand limits that have been set for
        specific association types.

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
            path_template(
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
        )


class AsyncLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncLimitsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging:
        """
        Retrieve all configured association limits between objects, which include
        details about how different CRM object types are associated with each other.
        """
        return await self._get(
            "/crm/associations/2026-03/definitions/configurations/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
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
    ) -> None:
        """
        Batch delete limits that have been defined for association types between two
        object types.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}/batch/purge",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, limit_batch_delete_params.LimitBatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Batch update association limits that have been configured between two object
        types.

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
            path_template(
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}/batch/update",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, limit_batch_update_params.LimitBatchUpdateParams),
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
    ) -> CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging:
        """
        Retrieve the configuration details for associations between two specified CRM
        object types. Use this endpoint to understand limits that have been set for
        specific association types.

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
            path_template(
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
        )


class LimitsResourceWithRawResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.list = to_raw_response_wrapper(
            limits.list,
        )
        self.batch_delete = to_raw_response_wrapper(
            limits.batch_delete,
        )
        self.batch_update = to_raw_response_wrapper(
            limits.batch_update,
        )
        self.get_by_object_types = to_raw_response_wrapper(
            limits.get_by_object_types,
        )


class AsyncLimitsResourceWithRawResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.list = async_to_raw_response_wrapper(
            limits.list,
        )
        self.batch_delete = async_to_raw_response_wrapper(
            limits.batch_delete,
        )
        self.batch_update = async_to_raw_response_wrapper(
            limits.batch_update,
        )
        self.get_by_object_types = async_to_raw_response_wrapper(
            limits.get_by_object_types,
        )


class LimitsResourceWithStreamingResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.list = to_streamed_response_wrapper(
            limits.list,
        )
        self.batch_delete = to_streamed_response_wrapper(
            limits.batch_delete,
        )
        self.batch_update = to_streamed_response_wrapper(
            limits.batch_update,
        )
        self.get_by_object_types = to_streamed_response_wrapper(
            limits.get_by_object_types,
        )


class AsyncLimitsResourceWithStreamingResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.list = async_to_streamed_response_wrapper(
            limits.list,
        )
        self.batch_delete = async_to_streamed_response_wrapper(
            limits.batch_delete,
        )
        self.batch_update = async_to_streamed_response_wrapper(
            limits.batch_update,
        )
        self.get_by_object_types = async_to_streamed_response_wrapper(
            limits.get_by_object_types,
        )
