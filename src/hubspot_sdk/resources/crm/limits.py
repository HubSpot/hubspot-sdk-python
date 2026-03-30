# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import limit_get_association_label_limits_params
from ..._base_client import make_request_options
from ...types.crm.record_limit_response import RecordLimitResponse
from ...types.crm.pipeline_limit_response import PipelineLimitResponse
from ...types.crm.custom_object_limit_response import CustomObjectLimitResponse
from ...types.crm.custom_property_limit_response import CustomPropertyLimitResponse
from ...types.crm.association_record_limit_response import AssociationRecordLimitResponse
from ...types.crm.calculated_property_limit_response import CalculatedPropertyLimitResponse
from ...types.crm.collection_response_association_label_limit_response_no_paging import (
    CollectionResponseAssociationLabelLimitResponseNoPaging,
)
from ...types.crm.collection_response_object_type_near_or_at_association_limit_no_paging import (
    CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
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

    def get_association_label_limits(
        self,
        *,
        from_object_type_id: str | Omit = omit,
        to_object_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseAssociationLabelLimitResponseNoPaging:
        """
        Returns limits and usage for custom association labels

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/limits/2026-03/associations/labels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_object_type_id": from_object_type_id,
                        "to_object_type_id": to_object_type_id,
                    },
                    limit_get_association_label_limits_params.LimitGetAssociationLabelLimitsParams,
                ),
            ),
            cast_to=CollectionResponseAssociationLabelLimitResponseNoPaging,
        )

    def get_association_records_limits_by_object_type(
        self,
        to_object_type_id: str,
        *,
        from_object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssociationRecordLimitResponse:
        """
        Returns records approaching or at association limits between two objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type_id:
            raise ValueError(
                f"Expected a non-empty value for `from_object_type_id` but received {from_object_type_id!r}"
            )
        if not to_object_type_id:
            raise ValueError(f"Expected a non-empty value for `to_object_type_id` but received {to_object_type_id!r}")
        return self._get(
            path_template(
                "/crm/limits/2026-03/associations/records/{from_object_type_id}/{to_object_type_id}",
                from_object_type_id=from_object_type_id,
                to_object_type_id=to_object_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationRecordLimitResponse,
        )

    def get_association_records_limits_from_objects(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging:
        """Returns objects with records approaching or at association limits"""
        return self._get(
            "/crm/limits/2026-03/associations/records/from",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
        )

    def get_association_records_limits_to_objects(
        self,
        from_object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging:
        """
        Returns objects for which the from object has records approaching or at
        association limits

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type_id:
            raise ValueError(
                f"Expected a non-empty value for `from_object_type_id` but received {from_object_type_id!r}"
            )
        return self._get(
            path_template(
                "/crm/limits/2026-03/associations/records/{from_object_type_id}/to",
                from_object_type_id=from_object_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
        )

    def get_calculated_property_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalculatedPropertyLimitResponse:
        """Returns overall limit and per object usage for calculated properties"""
        return self._get(
            "/crm/limits/2026-03/calculated-properties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalculatedPropertyLimitResponse,
        )

    def get_custom_object_type_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomObjectLimitResponse:
        """Returns limits and usage for custom object schemas"""
        return self._get(
            "/crm/limits/2026-03/custom-object-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomObjectLimitResponse,
        )

    def get_custom_property_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomPropertyLimitResponse:
        """Returns limits and usage per object for custom properties"""
        return self._get(
            "/crm/limits/2026-03/custom-properties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomPropertyLimitResponse,
        )

    def get_pipeline_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineLimitResponse:
        """Returns limits and usage per object for pipelines"""
        return self._get(
            "/crm/limits/2026-03/pipelines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineLimitResponse,
        )

    def get_record_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordLimitResponse:
        """Returns limits and usage per object for records"""
        return self._get(
            "/crm/limits/2026-03/records",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordLimitResponse,
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

    async def get_association_label_limits(
        self,
        *,
        from_object_type_id: str | Omit = omit,
        to_object_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseAssociationLabelLimitResponseNoPaging:
        """
        Returns limits and usage for custom association labels

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/limits/2026-03/associations/labels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_object_type_id": from_object_type_id,
                        "to_object_type_id": to_object_type_id,
                    },
                    limit_get_association_label_limits_params.LimitGetAssociationLabelLimitsParams,
                ),
            ),
            cast_to=CollectionResponseAssociationLabelLimitResponseNoPaging,
        )

    async def get_association_records_limits_by_object_type(
        self,
        to_object_type_id: str,
        *,
        from_object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssociationRecordLimitResponse:
        """
        Returns records approaching or at association limits between two objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type_id:
            raise ValueError(
                f"Expected a non-empty value for `from_object_type_id` but received {from_object_type_id!r}"
            )
        if not to_object_type_id:
            raise ValueError(f"Expected a non-empty value for `to_object_type_id` but received {to_object_type_id!r}")
        return await self._get(
            path_template(
                "/crm/limits/2026-03/associations/records/{from_object_type_id}/{to_object_type_id}",
                from_object_type_id=from_object_type_id,
                to_object_type_id=to_object_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociationRecordLimitResponse,
        )

    async def get_association_records_limits_from_objects(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging:
        """Returns objects with records approaching or at association limits"""
        return await self._get(
            "/crm/limits/2026-03/associations/records/from",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
        )

    async def get_association_records_limits_to_objects(
        self,
        from_object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging:
        """
        Returns objects for which the from object has records approaching or at
        association limits

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type_id:
            raise ValueError(
                f"Expected a non-empty value for `from_object_type_id` but received {from_object_type_id!r}"
            )
        return await self._get(
            path_template(
                "/crm/limits/2026-03/associations/records/{from_object_type_id}/to",
                from_object_type_id=from_object_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
        )

    async def get_calculated_property_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalculatedPropertyLimitResponse:
        """Returns overall limit and per object usage for calculated properties"""
        return await self._get(
            "/crm/limits/2026-03/calculated-properties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalculatedPropertyLimitResponse,
        )

    async def get_custom_object_type_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomObjectLimitResponse:
        """Returns limits and usage for custom object schemas"""
        return await self._get(
            "/crm/limits/2026-03/custom-object-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomObjectLimitResponse,
        )

    async def get_custom_property_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomPropertyLimitResponse:
        """Returns limits and usage per object for custom properties"""
        return await self._get(
            "/crm/limits/2026-03/custom-properties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomPropertyLimitResponse,
        )

    async def get_pipeline_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineLimitResponse:
        """Returns limits and usage per object for pipelines"""
        return await self._get(
            "/crm/limits/2026-03/pipelines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineLimitResponse,
        )

    async def get_record_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordLimitResponse:
        """Returns limits and usage per object for records"""
        return await self._get(
            "/crm/limits/2026-03/records",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordLimitResponse,
        )


class LimitsResourceWithRawResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.get_association_label_limits = to_raw_response_wrapper(
            limits.get_association_label_limits,
        )
        self.get_association_records_limits_by_object_type = to_raw_response_wrapper(
            limits.get_association_records_limits_by_object_type,
        )
        self.get_association_records_limits_from_objects = to_raw_response_wrapper(
            limits.get_association_records_limits_from_objects,
        )
        self.get_association_records_limits_to_objects = to_raw_response_wrapper(
            limits.get_association_records_limits_to_objects,
        )
        self.get_calculated_property_limits = to_raw_response_wrapper(
            limits.get_calculated_property_limits,
        )
        self.get_custom_object_type_limits = to_raw_response_wrapper(
            limits.get_custom_object_type_limits,
        )
        self.get_custom_property_limits = to_raw_response_wrapper(
            limits.get_custom_property_limits,
        )
        self.get_pipeline_limits = to_raw_response_wrapper(
            limits.get_pipeline_limits,
        )
        self.get_record_limits = to_raw_response_wrapper(
            limits.get_record_limits,
        )


class AsyncLimitsResourceWithRawResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.get_association_label_limits = async_to_raw_response_wrapper(
            limits.get_association_label_limits,
        )
        self.get_association_records_limits_by_object_type = async_to_raw_response_wrapper(
            limits.get_association_records_limits_by_object_type,
        )
        self.get_association_records_limits_from_objects = async_to_raw_response_wrapper(
            limits.get_association_records_limits_from_objects,
        )
        self.get_association_records_limits_to_objects = async_to_raw_response_wrapper(
            limits.get_association_records_limits_to_objects,
        )
        self.get_calculated_property_limits = async_to_raw_response_wrapper(
            limits.get_calculated_property_limits,
        )
        self.get_custom_object_type_limits = async_to_raw_response_wrapper(
            limits.get_custom_object_type_limits,
        )
        self.get_custom_property_limits = async_to_raw_response_wrapper(
            limits.get_custom_property_limits,
        )
        self.get_pipeline_limits = async_to_raw_response_wrapper(
            limits.get_pipeline_limits,
        )
        self.get_record_limits = async_to_raw_response_wrapper(
            limits.get_record_limits,
        )


class LimitsResourceWithStreamingResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.get_association_label_limits = to_streamed_response_wrapper(
            limits.get_association_label_limits,
        )
        self.get_association_records_limits_by_object_type = to_streamed_response_wrapper(
            limits.get_association_records_limits_by_object_type,
        )
        self.get_association_records_limits_from_objects = to_streamed_response_wrapper(
            limits.get_association_records_limits_from_objects,
        )
        self.get_association_records_limits_to_objects = to_streamed_response_wrapper(
            limits.get_association_records_limits_to_objects,
        )
        self.get_calculated_property_limits = to_streamed_response_wrapper(
            limits.get_calculated_property_limits,
        )
        self.get_custom_object_type_limits = to_streamed_response_wrapper(
            limits.get_custom_object_type_limits,
        )
        self.get_custom_property_limits = to_streamed_response_wrapper(
            limits.get_custom_property_limits,
        )
        self.get_pipeline_limits = to_streamed_response_wrapper(
            limits.get_pipeline_limits,
        )
        self.get_record_limits = to_streamed_response_wrapper(
            limits.get_record_limits,
        )


class AsyncLimitsResourceWithStreamingResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.get_association_label_limits = async_to_streamed_response_wrapper(
            limits.get_association_label_limits,
        )
        self.get_association_records_limits_by_object_type = async_to_streamed_response_wrapper(
            limits.get_association_records_limits_by_object_type,
        )
        self.get_association_records_limits_from_objects = async_to_streamed_response_wrapper(
            limits.get_association_records_limits_from_objects,
        )
        self.get_association_records_limits_to_objects = async_to_streamed_response_wrapper(
            limits.get_association_records_limits_to_objects,
        )
        self.get_calculated_property_limits = async_to_streamed_response_wrapper(
            limits.get_calculated_property_limits,
        )
        self.get_custom_object_type_limits = async_to_streamed_response_wrapper(
            limits.get_custom_object_type_limits,
        )
        self.get_custom_property_limits = async_to_streamed_response_wrapper(
            limits.get_custom_property_limits,
        )
        self.get_pipeline_limits = async_to_streamed_response_wrapper(
            limits.get_pipeline_limits,
        )
        self.get_record_limits = async_to_streamed_response_wrapper(
            limits.get_record_limits,
        )
