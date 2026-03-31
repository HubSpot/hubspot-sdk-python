# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ...types.files import (
    folder_search_params,
    folder_get_by_id_params,
    folder_get_by_path_params,
    folder_update_by_id_params,
    folder_update_async_by_id_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.files.folder import Folder
from ...types.files.folder_action_response import FolderActionResponse
from ...types.files.folder_update_task_locator import FolderUpdateTaskLocator

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def delete_by_id(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete folder by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/files/2026-03/folders/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_path(
        self,
        folder_path: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a folder, identified by its path.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/files/2026-03/folders/{folder_path}", folder_path=folder_path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_by_id(
        self,
        folder_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Retrieve a folder by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            path_template("/files/2026-03/folders/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, folder_get_by_id_params.FolderGetByIDParams),
            ),
            cast_to=Folder,
        )

    def get_by_path(
        self,
        folder_path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Retrieve a folder, identified by its path.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        return self._get(
            path_template("/files/2026-03/folders/{folder_path}", folder_path=folder_path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, folder_get_by_path_params.FolderGetByPathParams),
            ),
            cast_to=Folder,
        )

    def get_update_async_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderActionResponse:
        """Check status of folder update.

        Folder updates happen asynchronously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/files/2026-03/folders/update/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderActionResponse,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        id_gte: int | Omit = omit,
        id_lte: int | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        parent_folder_ids: Iterable[int] | Omit = omit,
        path: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Folder]:
        """Search for folders.

        Does not contain hidden or archived folders.

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
            "/files/2026-03/folders/search",
            page=SyncPage[Folder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_at": created_at,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "id_gte": id_gte,
                        "id_lte": id_lte,
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "parent_folder_ids": parent_folder_ids,
                        "path": path,
                        "properties": properties,
                        "sort": sort,
                        "updated_at": updated_at,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                    },
                    folder_search_params.FolderSearchParams,
                ),
            ),
            model=Folder,
        )

    def update_async_by_id(
        self,
        *,
        id: str,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateTaskLocator:
        """Update properties of folder by given ID.

        This action happens asynchronously and
        will update all of the folder's children as well.

        Args:
          id: The unique identifier of the folder to be updated.

          name: New name. If specified the folder's name and fullPath will change. All children
              of the folder will be updated accordingly.

          parent_folder_id: New parent folderId. If changed, the folder and all it's children will be moved
              into the specified folder. parentFolderId and parentFolderPath cannot be
              specified at the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/files/2026-03/folders/update/async",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                folder_update_async_by_id_params.FolderUpdateAsyncByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateTaskLocator,
        )

    def update_by_id(
        self,
        folder_id: str,
        *,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """Update a folder's properties, identified by folder ID.

        Args:
          name: New name.

        If specified the folder's name and fullPath will change. All children
              of the folder will be updated accordingly.

          parent_folder_id: New parent folderId. If changed, the folder and all it's children will be moved
              into the specified folder. parentFolderId and parentFolderPath cannot be
              specified at the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._patch(
            path_template("/files/2026-03/folders/{folder_id}", folder_id=folder_id),
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                folder_update_by_id_params.FolderUpdateByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def delete_by_id(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete folder by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/files/2026-03/folders/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_path(
        self,
        folder_path: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a folder, identified by its path.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/files/2026-03/folders/{folder_path}", folder_path=folder_path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_by_id(
        self,
        folder_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Retrieve a folder by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            path_template("/files/2026-03/folders/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"properties": properties}, folder_get_by_id_params.FolderGetByIDParams
                ),
            ),
            cast_to=Folder,
        )

    async def get_by_path(
        self,
        folder_path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Retrieve a folder, identified by its path.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        return await self._get(
            path_template("/files/2026-03/folders/{folder_path}", folder_path=folder_path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"properties": properties}, folder_get_by_path_params.FolderGetByPathParams
                ),
            ),
            cast_to=Folder,
        )

    async def get_update_async_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderActionResponse:
        """Check status of folder update.

        Folder updates happen asynchronously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/files/2026-03/folders/update/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderActionResponse,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        id_gte: int | Omit = omit,
        id_lte: int | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        parent_folder_ids: Iterable[int] | Omit = omit,
        path: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Folder, AsyncPage[Folder]]:
        """Search for folders.

        Does not contain hidden or archived folders.

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
            "/files/2026-03/folders/search",
            page=AsyncPage[Folder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_at": created_at,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "id_gte": id_gte,
                        "id_lte": id_lte,
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "parent_folder_ids": parent_folder_ids,
                        "path": path,
                        "properties": properties,
                        "sort": sort,
                        "updated_at": updated_at,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                    },
                    folder_search_params.FolderSearchParams,
                ),
            ),
            model=Folder,
        )

    async def update_async_by_id(
        self,
        *,
        id: str,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateTaskLocator:
        """Update properties of folder by given ID.

        This action happens asynchronously and
        will update all of the folder's children as well.

        Args:
          id: The unique identifier of the folder to be updated.

          name: New name. If specified the folder's name and fullPath will change. All children
              of the folder will be updated accordingly.

          parent_folder_id: New parent folderId. If changed, the folder and all it's children will be moved
              into the specified folder. parentFolderId and parentFolderPath cannot be
              specified at the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/files/2026-03/folders/update/async",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                folder_update_async_by_id_params.FolderUpdateAsyncByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateTaskLocator,
        )

    async def update_by_id(
        self,
        folder_id: str,
        *,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """Update a folder's properties, identified by folder ID.

        Args:
          name: New name.

        If specified the folder's name and fullPath will change. All children
              of the folder will be updated accordingly.

          parent_folder_id: New parent folderId. If changed, the folder and all it's children will be moved
              into the specified folder. parentFolderId and parentFolderPath cannot be
              specified at the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._patch(
            path_template("/files/2026-03/folders/{folder_id}", folder_id=folder_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                folder_update_by_id_params.FolderUpdateByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.delete_by_id = to_raw_response_wrapper(
            folders.delete_by_id,
        )
        self.delete_by_path = to_raw_response_wrapper(
            folders.delete_by_path,
        )
        self.get_by_id = to_raw_response_wrapper(
            folders.get_by_id,
        )
        self.get_by_path = to_raw_response_wrapper(
            folders.get_by_path,
        )
        self.get_update_async_status = to_raw_response_wrapper(
            folders.get_update_async_status,
        )
        self.search = to_raw_response_wrapper(
            folders.search,
        )
        self.update_async_by_id = to_raw_response_wrapper(
            folders.update_async_by_id,
        )
        self.update_by_id = to_raw_response_wrapper(
            folders.update_by_id,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.delete_by_id = async_to_raw_response_wrapper(
            folders.delete_by_id,
        )
        self.delete_by_path = async_to_raw_response_wrapper(
            folders.delete_by_path,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            folders.get_by_id,
        )
        self.get_by_path = async_to_raw_response_wrapper(
            folders.get_by_path,
        )
        self.get_update_async_status = async_to_raw_response_wrapper(
            folders.get_update_async_status,
        )
        self.search = async_to_raw_response_wrapper(
            folders.search,
        )
        self.update_async_by_id = async_to_raw_response_wrapper(
            folders.update_async_by_id,
        )
        self.update_by_id = async_to_raw_response_wrapper(
            folders.update_by_id,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.delete_by_id = to_streamed_response_wrapper(
            folders.delete_by_id,
        )
        self.delete_by_path = to_streamed_response_wrapper(
            folders.delete_by_path,
        )
        self.get_by_id = to_streamed_response_wrapper(
            folders.get_by_id,
        )
        self.get_by_path = to_streamed_response_wrapper(
            folders.get_by_path,
        )
        self.get_update_async_status = to_streamed_response_wrapper(
            folders.get_update_async_status,
        )
        self.search = to_streamed_response_wrapper(
            folders.search,
        )
        self.update_async_by_id = to_streamed_response_wrapper(
            folders.update_async_by_id,
        )
        self.update_by_id = to_streamed_response_wrapper(
            folders.update_by_id,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.delete_by_id = async_to_streamed_response_wrapper(
            folders.delete_by_id,
        )
        self.delete_by_path = async_to_streamed_response_wrapper(
            folders.delete_by_path,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            folders.get_by_id,
        )
        self.get_by_path = async_to_streamed_response_wrapper(
            folders.get_by_path,
        )
        self.get_update_async_status = async_to_streamed_response_wrapper(
            folders.get_update_async_status,
        )
        self.search = async_to_streamed_response_wrapper(
            folders.search,
        )
        self.update_async_by_id = async_to_streamed_response_wrapper(
            folders.update_async_by_id,
        )
        self.update_by_id = async_to_streamed_response_wrapper(
            folders.update_by_id,
        )
