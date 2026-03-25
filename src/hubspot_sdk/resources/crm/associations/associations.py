# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
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
from ....types.crm.report_creation_response import ReportCreationResponse
from ....types.crm.labels_between_object_pair import LabelsBetweenObjectPair
from ....types.shared_params.association_spec import AssociationSpec

__all__ = ["AssociationsResource", "AsyncAssociationsResource"]


class AssociationsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AssociationsResourceWithStreamingResponse(self)

    def delete_associations(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/crm/objects/2026-03/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
                object_type=object_type,
                object_id=object_id,
                to_object_type=to_object_type,
                to_object_id=to_object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def request_high_usage_report(
        self,
        user_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCreationResponse:
        """
        Requests a report of all objects in the portal which have a high usage of
        associations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/crm/associations/2026-03/usage/high-usage-report/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCreationResponse,
        )

    def update_association_labels(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        body: Iterable[AssociationSpec],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelsBetweenObjectPair:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return self._put(
            path_template(
                "/crm/objects/2026-03/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
                object_type=object_type,
                object_id=object_id,
                to_object_type=to_object_type,
                to_object_id=to_object_id,
            ),
            body=maybe_transform(body, Iterable[AssociationSpec]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelsBetweenObjectPair,
        )


class AsyncAssociationsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAssociationsResourceWithStreamingResponse(self)

    async def delete_associations(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/crm/objects/2026-03/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
                object_type=object_type,
                object_id=object_id,
                to_object_type=to_object_type,
                to_object_id=to_object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def request_high_usage_report(
        self,
        user_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCreationResponse:
        """
        Requests a report of all objects in the portal which have a high usage of
        associations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/crm/associations/2026-03/usage/high-usage-report/{user_id}", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCreationResponse,
        )

    async def update_association_labels(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        body: Iterable[AssociationSpec],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelsBetweenObjectPair:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return await self._put(
            path_template(
                "/crm/objects/2026-03/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
                object_type=object_type,
                object_id=object_id,
                to_object_type=to_object_type,
                to_object_id=to_object_id,
            ),
            body=await async_maybe_transform(body, Iterable[AssociationSpec]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelsBetweenObjectPair,
        )


class AssociationsResourceWithRawResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

        self.delete_associations = to_raw_response_wrapper(
            associations.delete_associations,
        )
        self.request_high_usage_report = to_raw_response_wrapper(
            associations.request_high_usage_report,
        )
        self.update_association_labels = to_raw_response_wrapper(
            associations.update_association_labels,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._associations.batch)


class AsyncAssociationsResourceWithRawResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

        self.delete_associations = async_to_raw_response_wrapper(
            associations.delete_associations,
        )
        self.request_high_usage_report = async_to_raw_response_wrapper(
            associations.request_high_usage_report,
        )
        self.update_association_labels = async_to_raw_response_wrapper(
            associations.update_association_labels,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._associations.batch)


class AssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

        self.delete_associations = to_streamed_response_wrapper(
            associations.delete_associations,
        )
        self.request_high_usage_report = to_streamed_response_wrapper(
            associations.request_high_usage_report,
        )
        self.update_association_labels = to_streamed_response_wrapper(
            associations.update_association_labels,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._associations.batch)


class AsyncAssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

        self.delete_associations = async_to_streamed_response_wrapper(
            associations.delete_associations,
        )
        self.request_high_usage_report = async_to_streamed_response_wrapper(
            associations.request_high_usage_report,
        )
        self.update_association_labels = async_to_streamed_response_wrapper(
            associations.update_association_labels,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._associations.batch)
