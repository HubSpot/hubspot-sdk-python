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
from .report import (
    ReportResource,
    AsyncReportResource,
    ReportResourceWithRawResponse,
    AsyncReportResourceWithRawResponse,
    ReportResourceWithStreamingResponse,
    AsyncReportResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncPage, AsyncPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.crm.associations import v4_list_params
from .....types.crm.multi_associated_object_with_label import MultiAssociatedObjectWithLabel
from .....types.crm.associations.association_spec_1_param import AssociationSpec1Param
from .....types.crm.batch_response_public_default_association import BatchResponsePublicDefaultAssociation
from .....types.crm.created_response_labels_between_object_pair import CreatedResponseLabelsBetweenObjectPair

__all__ = ["V4Resource", "AsyncV4Resource"]


class V4Resource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def report(self) -> ReportResource:
        return ReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> V4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return V4ResourceWithStreamingResponse(self)

    def create(
        self,
        to_object_id: str,
        *,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicDefaultAssociation:
        """
        Create the default (most generic) association type between two object types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not from_object_id:
            raise ValueError(f"Expected a non-empty value for `from_object_id` but received {from_object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return self._put(
            f"/crm/v4/objects/{from_object_type}/{from_object_id}/associations/default/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicDefaultAssociation,
        )

    def update(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        body: Iterable[AssociationSpec1Param],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponseLabelsBetweenObjectPair:
        """
        Set association labels between two records.

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
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            body=maybe_transform(body, Iterable[AssociationSpec1Param]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponseLabelsBetweenObjectPair,
        )

    def list(
        self,
        to_object_type: str,
        *,
        object_type: str,
        object_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[MultiAssociatedObjectWithLabel]:
        """List all associations of an object by object type.

        Limit 500 per call.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

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
        return self._get_api_list(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}",
            page=SyncPage[MultiAssociatedObjectWithLabel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    v4_list_params.V4ListParams,
                ),
            ),
            model=MultiAssociatedObjectWithLabel,
        )

    def delete(
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
        deletes all associations between two records.

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
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV4Resource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def report(self) -> AsyncReportResource:
        return AsyncReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncV4ResourceWithStreamingResponse(self)

    async def create(
        self,
        to_object_id: str,
        *,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicDefaultAssociation:
        """
        Create the default (most generic) association type between two object types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not from_object_id:
            raise ValueError(f"Expected a non-empty value for `from_object_id` but received {from_object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return await self._put(
            f"/crm/v4/objects/{from_object_type}/{from_object_id}/associations/default/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicDefaultAssociation,
        )

    async def update(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        body: Iterable[AssociationSpec1Param],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponseLabelsBetweenObjectPair:
        """
        Set association labels between two records.

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
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            body=await async_maybe_transform(body, Iterable[AssociationSpec1Param]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponseLabelsBetweenObjectPair,
        )

    def list(
        self,
        to_object_type: str,
        *,
        object_type: str,
        object_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MultiAssociatedObjectWithLabel, AsyncPage[MultiAssociatedObjectWithLabel]]:
        """List all associations of an object by object type.

        Limit 500 per call.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

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
        return self._get_api_list(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}",
            page=AsyncPage[MultiAssociatedObjectWithLabel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    v4_list_params.V4ListParams,
                ),
            ),
            model=MultiAssociatedObjectWithLabel,
        )

    async def delete(
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
        deletes all associations between two records.

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
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V4ResourceWithRawResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.create = to_raw_response_wrapper(
            v4.create,
        )
        self.update = to_raw_response_wrapper(
            v4.update,
        )
        self.list = to_raw_response_wrapper(
            v4.list,
        )
        self.delete = to_raw_response_wrapper(
            v4.delete,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._v4.batch)

    @cached_property
    def report(self) -> ReportResourceWithRawResponse:
        return ReportResourceWithRawResponse(self._v4.report)


class AsyncV4ResourceWithRawResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.create = async_to_raw_response_wrapper(
            v4.create,
        )
        self.update = async_to_raw_response_wrapper(
            v4.update,
        )
        self.list = async_to_raw_response_wrapper(
            v4.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v4.delete,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._v4.batch)

    @cached_property
    def report(self) -> AsyncReportResourceWithRawResponse:
        return AsyncReportResourceWithRawResponse(self._v4.report)


class V4ResourceWithStreamingResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.create = to_streamed_response_wrapper(
            v4.create,
        )
        self.update = to_streamed_response_wrapper(
            v4.update,
        )
        self.list = to_streamed_response_wrapper(
            v4.list,
        )
        self.delete = to_streamed_response_wrapper(
            v4.delete,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._v4.batch)

    @cached_property
    def report(self) -> ReportResourceWithStreamingResponse:
        return ReportResourceWithStreamingResponse(self._v4.report)


class AsyncV4ResourceWithStreamingResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.create = async_to_streamed_response_wrapper(
            v4.create,
        )
        self.update = async_to_streamed_response_wrapper(
            v4.update,
        )
        self.list = async_to_streamed_response_wrapper(
            v4.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v4.delete,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._v4.batch)

    @cached_property
    def report(self) -> AsyncReportResourceWithStreamingResponse:
        return AsyncReportResourceWithStreamingResponse(self._v4.report)
