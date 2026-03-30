# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.automation.actions import revision_list_params
from ....types.automation.public_action_revision import PublicActionRevision

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

    def list(
        self,
        definition_id: str,
        *,
        app_id: int,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicActionRevision]:
        """
        Retrieve the versions of a definition by ID.

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
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get_api_list(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions",
                app_id=app_id,
                definition_id=definition_id,
            ),
            page=SyncPage[PublicActionRevision],
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
                    revision_list_params.RevisionListParams,
                ),
            ),
            model=PublicActionRevision,
        )

    def get(
        self,
        revision_id: str,
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionRevision:
        """
        Retrieve a specific revision of a definition by revision ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions/{revision_id}",
                app_id=app_id,
                definition_id=definition_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionRevision,
        )


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

    def list(
        self,
        definition_id: str,
        *,
        app_id: int,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicActionRevision, AsyncPage[PublicActionRevision]]:
        """
        Retrieve the versions of a definition by ID.

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
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get_api_list(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions",
                app_id=app_id,
                definition_id=definition_id,
            ),
            page=AsyncPage[PublicActionRevision],
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
                    revision_list_params.RevisionListParams,
                ),
            ),
            model=PublicActionRevision,
        )

    async def get(
        self,
        revision_id: str,
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionRevision:
        """
        Retrieve a specific revision of a definition by revision ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions/{revision_id}",
                app_id=app_id,
                definition_id=definition_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionRevision,
        )


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.list = to_raw_response_wrapper(
            revisions.list,
        )
        self.get = to_raw_response_wrapper(
            revisions.get,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.list = async_to_raw_response_wrapper(
            revisions.list,
        )
        self.get = async_to_raw_response_wrapper(
            revisions.get,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.list = to_streamed_response_wrapper(
            revisions.list,
        )
        self.get = to_streamed_response_wrapper(
            revisions.get,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.list = async_to_streamed_response_wrapper(
            revisions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            revisions.get,
        )
