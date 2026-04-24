# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.cms.pages import (
    batch_create_folders_params,
    batch_delete_folders_params,
    batch_get_site_pages_params,
    batch_update_folders_params,
    batch_create_site_pages_params,
    batch_delete_site_pages_params,
    batch_get_landing_pages_params,
    batch_update_site_pages_params,
    batch_create_landing_pages_params,
    batch_delete_landing_pages_params,
    batch_update_landing_pages_params,
)
from ....types.cms.pages_page_param import PagesPageParam
from ....types.cms.batch_response_page import BatchResponsePage
from ....types.cms.content_folder_param import ContentFolderParam
from ....types.cms.batch_response_content_folder import BatchResponseContentFolder

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create_folders(
        self,
        *,
        inputs: Iterable[ContentFolderParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Create a batch of folders as detailed in the request body.

        Args:
          inputs: Content folders to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_folders_params.BatchCreateFoldersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseContentFolder,
        )

    def create_landing_pages(
        self,
        *,
        inputs: Iterable[PagesPageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Create a batch of landing pages as detailed in the request body.

        Args:
          inputs: Pages to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_landing_pages_params.BatchCreateLandingPagesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePage,
        )

    def create_site_pages(
        self,
        *,
        inputs: Iterable[PagesPageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Create a batch of website pages as specified in the request body.

        Args:
          inputs: Pages to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/site-pages/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_site_pages_params.BatchCreateSitePagesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePage,
        )

    def delete_folders(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a batch of folders as specified in the request body.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/archive",
            body=maybe_transform({"inputs": inputs}, batch_delete_folders_params.BatchDeleteFoldersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_landing_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete landing pages specified by ID in the request body.

        Note: this is not the
        same as the dashboard `archive` function. To perform a dashboard `archive` send
        an normal update with the `archivedInDashboard` field set to `true`.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/landing-pages/batch/archive",
            body=maybe_transform({"inputs": inputs}, batch_delete_landing_pages_params.BatchDeleteLandingPagesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_site_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a batch of website pages as specified in the request body.

        Note that this
        is not the same as the dashboard `archive` function. To perform a dashboard
        `archive` send an normal update with the `archivedInDashboard` field set to
        `true`.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/site-pages/batch/archive",
            body=maybe_transform({"inputs": inputs}, batch_delete_site_pages_params.BatchDeleteSitePagesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_landing_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Retrieve a batch of landing pages as specified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_landing_pages_params.BatchGetLandingPagesParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, batch_get_landing_pages_params.BatchGetLandingPagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    def get_site_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Retrieve a batch of website pages as specified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/site-pages/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_site_pages_params.BatchGetSitePagesParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, batch_get_site_pages_params.BatchGetSitePagesParams),
            ),
            cast_to=BatchResponsePage,
        )

    def update_folders(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Update a batch of landing page folders as specified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_folders_params.BatchUpdateFoldersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, batch_update_folders_params.BatchUpdateFoldersParams),
            ),
            cast_to=BatchResponseContentFolder,
        )

    def update_landing_pages(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Update a batch of landing pages as specified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_landing_pages_params.BatchUpdateLandingPagesParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, batch_update_landing_pages_params.BatchUpdateLandingPagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    def update_site_pages(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Update a batch of website pages as specified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/site-pages/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_site_pages_params.BatchUpdateSitePagesParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, batch_update_site_pages_params.BatchUpdateSitePagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create_folders(
        self,
        *,
        inputs: Iterable[ContentFolderParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Create a batch of folders as detailed in the request body.

        Args:
          inputs: Content folders to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, batch_create_folders_params.BatchCreateFoldersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseContentFolder,
        )

    async def create_landing_pages(
        self,
        *,
        inputs: Iterable[PagesPageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Create a batch of landing pages as detailed in the request body.

        Args:
          inputs: Pages to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_create_landing_pages_params.BatchCreateLandingPagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePage,
        )

    async def create_site_pages(
        self,
        *,
        inputs: Iterable[PagesPageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Create a batch of website pages as specified in the request body.

        Args:
          inputs: Pages to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/site-pages/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_create_site_pages_params.BatchCreateSitePagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePage,
        )

    async def delete_folders(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a batch of folders as specified in the request body.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, batch_delete_folders_params.BatchDeleteFoldersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_landing_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete landing pages specified by ID in the request body.

        Note: this is not the
        same as the dashboard `archive` function. To perform a dashboard `archive` send
        an normal update with the `archivedInDashboard` field set to `true`.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/landing-pages/batch/archive",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_delete_landing_pages_params.BatchDeleteLandingPagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_site_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a batch of website pages as specified in the request body.

        Note that this
        is not the same as the dashboard `archive` function. To perform a dashboard
        `archive` send an normal update with the `archivedInDashboard` field set to
        `true`.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/site-pages/batch/archive",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_delete_site_pages_params.BatchDeleteSitePagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_landing_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Retrieve a batch of landing pages as specified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_get_landing_pages_params.BatchGetLandingPagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, batch_get_landing_pages_params.BatchGetLandingPagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    async def get_site_pages(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Retrieve a batch of website pages as specified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/site-pages/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_get_site_pages_params.BatchGetSitePagesParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, batch_get_site_pages_params.BatchGetSitePagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    async def update_folders(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Update a batch of landing page folders as specified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, batch_update_folders_params.BatchUpdateFoldersParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, batch_update_folders_params.BatchUpdateFoldersParams
                ),
            ),
            cast_to=BatchResponseContentFolder,
        )

    async def update_landing_pages(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Update a batch of landing pages as specified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/batch/update",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_update_landing_pages_params.BatchUpdateLandingPagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, batch_update_landing_pages_params.BatchUpdateLandingPagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    async def update_site_pages(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Update a batch of website pages as specified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/site-pages/batch/update",
            body=await async_maybe_transform(
                {"inputs": inputs}, batch_update_site_pages_params.BatchUpdateSitePagesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, batch_update_site_pages_params.BatchUpdateSitePagesParams
                ),
            ),
            cast_to=BatchResponsePage,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create_folders = to_raw_response_wrapper(
            batch.create_folders,
        )
        self.create_landing_pages = to_raw_response_wrapper(
            batch.create_landing_pages,
        )
        self.create_site_pages = to_raw_response_wrapper(
            batch.create_site_pages,
        )
        self.delete_folders = to_raw_response_wrapper(
            batch.delete_folders,
        )
        self.delete_landing_pages = to_raw_response_wrapper(
            batch.delete_landing_pages,
        )
        self.delete_site_pages = to_raw_response_wrapper(
            batch.delete_site_pages,
        )
        self.get_landing_pages = to_raw_response_wrapper(
            batch.get_landing_pages,
        )
        self.get_site_pages = to_raw_response_wrapper(
            batch.get_site_pages,
        )
        self.update_folders = to_raw_response_wrapper(
            batch.update_folders,
        )
        self.update_landing_pages = to_raw_response_wrapper(
            batch.update_landing_pages,
        )
        self.update_site_pages = to_raw_response_wrapper(
            batch.update_site_pages,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create_folders = async_to_raw_response_wrapper(
            batch.create_folders,
        )
        self.create_landing_pages = async_to_raw_response_wrapper(
            batch.create_landing_pages,
        )
        self.create_site_pages = async_to_raw_response_wrapper(
            batch.create_site_pages,
        )
        self.delete_folders = async_to_raw_response_wrapper(
            batch.delete_folders,
        )
        self.delete_landing_pages = async_to_raw_response_wrapper(
            batch.delete_landing_pages,
        )
        self.delete_site_pages = async_to_raw_response_wrapper(
            batch.delete_site_pages,
        )
        self.get_landing_pages = async_to_raw_response_wrapper(
            batch.get_landing_pages,
        )
        self.get_site_pages = async_to_raw_response_wrapper(
            batch.get_site_pages,
        )
        self.update_folders = async_to_raw_response_wrapper(
            batch.update_folders,
        )
        self.update_landing_pages = async_to_raw_response_wrapper(
            batch.update_landing_pages,
        )
        self.update_site_pages = async_to_raw_response_wrapper(
            batch.update_site_pages,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create_folders = to_streamed_response_wrapper(
            batch.create_folders,
        )
        self.create_landing_pages = to_streamed_response_wrapper(
            batch.create_landing_pages,
        )
        self.create_site_pages = to_streamed_response_wrapper(
            batch.create_site_pages,
        )
        self.delete_folders = to_streamed_response_wrapper(
            batch.delete_folders,
        )
        self.delete_landing_pages = to_streamed_response_wrapper(
            batch.delete_landing_pages,
        )
        self.delete_site_pages = to_streamed_response_wrapper(
            batch.delete_site_pages,
        )
        self.get_landing_pages = to_streamed_response_wrapper(
            batch.get_landing_pages,
        )
        self.get_site_pages = to_streamed_response_wrapper(
            batch.get_site_pages,
        )
        self.update_folders = to_streamed_response_wrapper(
            batch.update_folders,
        )
        self.update_landing_pages = to_streamed_response_wrapper(
            batch.update_landing_pages,
        )
        self.update_site_pages = to_streamed_response_wrapper(
            batch.update_site_pages,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create_folders = async_to_streamed_response_wrapper(
            batch.create_folders,
        )
        self.create_landing_pages = async_to_streamed_response_wrapper(
            batch.create_landing_pages,
        )
        self.create_site_pages = async_to_streamed_response_wrapper(
            batch.create_site_pages,
        )
        self.delete_folders = async_to_streamed_response_wrapper(
            batch.delete_folders,
        )
        self.delete_landing_pages = async_to_streamed_response_wrapper(
            batch.delete_landing_pages,
        )
        self.delete_site_pages = async_to_streamed_response_wrapper(
            batch.delete_site_pages,
        )
        self.get_landing_pages = async_to_streamed_response_wrapper(
            batch.get_landing_pages,
        )
        self.get_site_pages = async_to_streamed_response_wrapper(
            batch.get_site_pages,
        )
        self.update_folders = async_to_streamed_response_wrapper(
            batch.update_folders,
        )
        self.update_landing_pages = async_to_streamed_response_wrapper(
            batch.update_landing_pages,
        )
        self.update_site_pages = async_to_streamed_response_wrapper(
            batch.update_site_pages,
        )
