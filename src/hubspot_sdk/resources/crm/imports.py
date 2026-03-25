# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import import_list_params, import_create_params, import_list_errors_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.action_response import ActionResponse
from ...types.crm.public_import_error import PublicImportError
from ...types.crm.public_import_response import PublicImportResponse

__all__ = ["ImportsResource", "AsyncImportsResource"]


class ImportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ImportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: FileTypes | Omit = omit,
        import_request: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicImportResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "import_request": import_request,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/crm/imports/2026-03",
            body=maybe_transform(body, import_create_params.ImportCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicImportResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicImportResponse]:
        """
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
        return self._get_api_list(
            "/crm/imports/2026-03",
            page=SyncPage[PublicImportResponse],
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
                    import_list_params.ImportListParams,
                ),
            ),
            model=PublicImportResponse,
        )

    def cancel(
        self,
        import_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/crm/imports/2026-03/{import_id}/cancel", import_id=import_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponse,
        )

    def get(
        self,
        import_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicImportResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/crm/imports/2026-03/{import_id}", import_id=import_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicImportResponse,
        )

    def list_errors(
        self,
        import_id: int,
        *,
        after: str | Omit = omit,
        include_error_message: bool | Omit = omit,
        include_row_data: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicImportError]:
        """
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
        return self._get_api_list(
            path_template("/crm/imports/2026-03/{import_id}/errors", import_id=import_id),
            page=SyncPage[PublicImportError],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_error_message": include_error_message,
                        "include_row_data": include_row_data,
                        "limit": limit,
                    },
                    import_list_errors_params.ImportListErrorsParams,
                ),
            ),
            model=PublicImportError,
        )


class AsyncImportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncImportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: FileTypes | Omit = omit,
        import_request: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicImportResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "import_request": import_request,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/crm/imports/2026-03",
            body=await async_maybe_transform(body, import_create_params.ImportCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicImportResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicImportResponse, AsyncPage[PublicImportResponse]]:
        """
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
        return self._get_api_list(
            "/crm/imports/2026-03",
            page=AsyncPage[PublicImportResponse],
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
                    import_list_params.ImportListParams,
                ),
            ),
            model=PublicImportResponse,
        )

    async def cancel(
        self,
        import_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/crm/imports/2026-03/{import_id}/cancel", import_id=import_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponse,
        )

    async def get(
        self,
        import_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicImportResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/crm/imports/2026-03/{import_id}", import_id=import_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicImportResponse,
        )

    def list_errors(
        self,
        import_id: int,
        *,
        after: str | Omit = omit,
        include_error_message: bool | Omit = omit,
        include_row_data: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicImportError, AsyncPage[PublicImportError]]:
        """
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
        return self._get_api_list(
            path_template("/crm/imports/2026-03/{import_id}/errors", import_id=import_id),
            page=AsyncPage[PublicImportError],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "include_error_message": include_error_message,
                        "include_row_data": include_row_data,
                        "limit": limit,
                    },
                    import_list_errors_params.ImportListErrorsParams,
                ),
            ),
            model=PublicImportError,
        )


class ImportsResourceWithRawResponse:
    def __init__(self, imports: ImportsResource) -> None:
        self._imports = imports

        self.create = to_raw_response_wrapper(
            imports.create,
        )
        self.list = to_raw_response_wrapper(
            imports.list,
        )
        self.cancel = to_raw_response_wrapper(
            imports.cancel,
        )
        self.get = to_raw_response_wrapper(
            imports.get,
        )
        self.list_errors = to_raw_response_wrapper(
            imports.list_errors,
        )


class AsyncImportsResourceWithRawResponse:
    def __init__(self, imports: AsyncImportsResource) -> None:
        self._imports = imports

        self.create = async_to_raw_response_wrapper(
            imports.create,
        )
        self.list = async_to_raw_response_wrapper(
            imports.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            imports.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            imports.get,
        )
        self.list_errors = async_to_raw_response_wrapper(
            imports.list_errors,
        )


class ImportsResourceWithStreamingResponse:
    def __init__(self, imports: ImportsResource) -> None:
        self._imports = imports

        self.create = to_streamed_response_wrapper(
            imports.create,
        )
        self.list = to_streamed_response_wrapper(
            imports.list,
        )
        self.cancel = to_streamed_response_wrapper(
            imports.cancel,
        )
        self.get = to_streamed_response_wrapper(
            imports.get,
        )
        self.list_errors = to_streamed_response_wrapper(
            imports.list_errors,
        )


class AsyncImportsResourceWithStreamingResponse:
    def __init__(self, imports: AsyncImportsResource) -> None:
        self._imports = imports

        self.create = async_to_streamed_response_wrapper(
            imports.create,
        )
        self.list = async_to_streamed_response_wrapper(
            imports.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            imports.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            imports.get,
        )
        self.list_errors = async_to_streamed_response_wrapper(
            imports.list_errors,
        )
