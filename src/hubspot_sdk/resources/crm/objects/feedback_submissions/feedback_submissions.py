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
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.crm.objects import (
    feedback_submission_get_params,
    feedback_submission_list_params,
    feedback_submission_search_params,
)
from .....types.crm.filter_group_param import FilterGroupParam
from .....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from .....types.crm.collection_response_with_total_simple_public_object import (
    CollectionResponseWithTotalSimplePublicObject,
)

__all__ = ["FeedbackSubmissionsResource", "AsyncFeedbackSubmissionsResource"]


class FeedbackSubmissionsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeedbackSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FeedbackSubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[SimplePublicObjectWithAssociations]:
        """Read a page of feedback submissions.

        Control what is returned via the
        `properties` query param.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          limit: The maximum number of results to display per page.

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored. Usage of this parameter will reduce
              the maximum number of feedback submissions that can be read by a single request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v3/objects/feedback_submissions",
            page=SyncPage[SimplePublicObjectWithAssociations],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associations": associations,
                        "limit": limit,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    feedback_submission_list_params.FeedbackSubmissionListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
        )

    def get(
        self,
        feedback_submission_id: str,
        *,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        id_property: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """Read an Object identified by `{feedbackSubmissionId}`.

        `{feedbackSubmissionId}`
        refers to the internal object ID by default, or optionally any unique property
        value as specified by the `idProperty` query param. Control what is returned via
        the `properties` query param.

        Args:
          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          id_property: The name of a property whose values are unique for this object

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feedback_submission_id:
            raise ValueError(
                f"Expected a non-empty value for `feedback_submission_id` but received {feedback_submission_id!r}"
            )
        return self._get(
            f"/crm/v3/objects/feedback_submissions/{feedback_submission_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "associations": associations,
                        "id_property": id_property,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    feedback_submission_get_params.FeedbackSubmissionGetParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    def search(
        self,
        *,
        after: str,
        filter_groups: Iterable[FilterGroupParam],
        limit: int,
        properties: SequenceNotStr[str],
        sorts: SequenceNotStr[str],
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Execute a search to retrieve feedback submissions based on defined filters,
        properties, and sorting options.

        Args:
          after: A paging cursor token for retrieving subsequent pages.

          filter_groups: Up to 6 groups of filters defining additional query criteria.

          limit: The maximum results to return, up to 200 objects.

          properties: A list of property names to include in the response.

          sorts: Specifies sorting order based on object properties.

          query: The search query string, up to 3000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/feedback_submissions/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                feedback_submission_search_params.FeedbackSubmissionSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class AsyncFeedbackSubmissionsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeedbackSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFeedbackSubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SimplePublicObjectWithAssociations, AsyncPage[SimplePublicObjectWithAssociations]]:
        """Read a page of feedback submissions.

        Control what is returned via the
        `properties` query param.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          limit: The maximum number of results to display per page.

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored. Usage of this parameter will reduce
              the maximum number of feedback submissions that can be read by a single request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v3/objects/feedback_submissions",
            page=AsyncPage[SimplePublicObjectWithAssociations],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associations": associations,
                        "limit": limit,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    feedback_submission_list_params.FeedbackSubmissionListParams,
                ),
            ),
            model=SimplePublicObjectWithAssociations,
        )

    async def get(
        self,
        feedback_submission_id: str,
        *,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        id_property: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """Read an Object identified by `{feedbackSubmissionId}`.

        `{feedbackSubmissionId}`
        refers to the internal object ID by default, or optionally any unique property
        value as specified by the `idProperty` query param. Control what is returned via
        the `properties` query param.

        Args:
          archived: Whether to return only results that have been archived.

          associations: A comma separated list of object types to retrieve associated IDs for. If any of
              the specified associations do not exist, they will be ignored.

          id_property: The name of a property whose values are unique for this object

          properties: A comma separated list of the properties to be returned in the response. If any
              of the specified properties are not present on the requested object(s), they
              will be ignored.

          properties_with_history: A comma separated list of the properties to be returned along with their history
              of previous values. If any of the specified properties are not present on the
              requested object(s), they will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feedback_submission_id:
            raise ValueError(
                f"Expected a non-empty value for `feedback_submission_id` but received {feedback_submission_id!r}"
            )
        return await self._get(
            f"/crm/v3/objects/feedback_submissions/{feedback_submission_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "associations": associations,
                        "id_property": id_property,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    feedback_submission_get_params.FeedbackSubmissionGetParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    async def search(
        self,
        *,
        after: str,
        filter_groups: Iterable[FilterGroupParam],
        limit: int,
        properties: SequenceNotStr[str],
        sorts: SequenceNotStr[str],
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Execute a search to retrieve feedback submissions based on defined filters,
        properties, and sorting options.

        Args:
          after: A paging cursor token for retrieving subsequent pages.

          filter_groups: Up to 6 groups of filters defining additional query criteria.

          limit: The maximum results to return, up to 200 objects.

          properties: A list of property names to include in the response.

          sorts: Specifies sorting order based on object properties.

          query: The search query string, up to 3000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/feedback_submissions/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "sorts": sorts,
                    "query": query,
                },
                feedback_submission_search_params.FeedbackSubmissionSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )


class FeedbackSubmissionsResourceWithRawResponse:
    def __init__(self, feedback_submissions: FeedbackSubmissionsResource) -> None:
        self._feedback_submissions = feedback_submissions

        self.list = to_raw_response_wrapper(
            feedback_submissions.list,
        )
        self.get = to_raw_response_wrapper(
            feedback_submissions.get,
        )
        self.search = to_raw_response_wrapper(
            feedback_submissions.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._feedback_submissions.batch)


class AsyncFeedbackSubmissionsResourceWithRawResponse:
    def __init__(self, feedback_submissions: AsyncFeedbackSubmissionsResource) -> None:
        self._feedback_submissions = feedback_submissions

        self.list = async_to_raw_response_wrapper(
            feedback_submissions.list,
        )
        self.get = async_to_raw_response_wrapper(
            feedback_submissions.get,
        )
        self.search = async_to_raw_response_wrapper(
            feedback_submissions.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._feedback_submissions.batch)


class FeedbackSubmissionsResourceWithStreamingResponse:
    def __init__(self, feedback_submissions: FeedbackSubmissionsResource) -> None:
        self._feedback_submissions = feedback_submissions

        self.list = to_streamed_response_wrapper(
            feedback_submissions.list,
        )
        self.get = to_streamed_response_wrapper(
            feedback_submissions.get,
        )
        self.search = to_streamed_response_wrapper(
            feedback_submissions.search,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._feedback_submissions.batch)


class AsyncFeedbackSubmissionsResourceWithStreamingResponse:
    def __init__(self, feedback_submissions: AsyncFeedbackSubmissionsResource) -> None:
        self._feedback_submissions = feedback_submissions

        self.list = async_to_streamed_response_wrapper(
            feedback_submissions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            feedback_submissions.get,
        )
        self.search = async_to_streamed_response_wrapper(
            feedback_submissions.search,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._feedback_submissions.batch)
