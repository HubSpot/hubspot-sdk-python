# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.cms.pages import (
    folder_get_params,
    folder_list_params,
    folder_create_params,
    folder_delete_params,
    folder_update_params,
    folder_batch_get_params,
    folder_list_revisions_params,
)
from ....types.cms.content_folder import ContentFolder
from ....types.cms.content_folder_version import ContentFolderVersion
from ....types.cms.batch_response_content_folder import BatchResponseContentFolder

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Create a new folder for landing pages.

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          created: The timestamp indicating when the content folder was created.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          updated: The timestamp indicating when the content folder was last updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/folders",
            body=maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )

    def update(
        self,
        object_id: str,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """Partially update a landing page folder, specified by the folder ID.

        You only
        need to specify the details values that you are modifying.

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          created: The timestamp indicating when the content folder was created.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          updated: The timestamp indicating when the content folder was last updated.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}", object_id=object_id),
            body=maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, folder_update_params.FolderUpdateParams),
            ),
            cast_to=ContentFolder,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ContentFolder]:
        """Get the list of Landing Page Folders.

        Supports paging and filtering. This method
        would be useful for an integration that examined these models and used an
        external service to suggest edits.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          created_after: Filter folders created after the specified date and time.

          created_at: Filter folders by their exact creation date and time.

          limit: The maximum number of results to display per page.

          property: Specify a property to include in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/pages/2026-03/landing-pages/folders",
            page=SyncPage[ContentFolder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    folder_list_params.FolderListParams,
                ),
            ),
            model=ContentFolder,
        )

    def delete(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a landing page folder, specified by its ID.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, folder_delete_params.FolderDeleteParams),
            ),
            cast_to=NoneType,
        )

    def batch_get(
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
    ) -> BatchResponseContentFolder:
        """
        Retrieve a batch of landing page folders as identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/read",
            body=maybe_transform({"inputs": inputs}, folder_batch_get_params.FolderBatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, folder_batch_get_params.FolderBatchGetParams),
            ),
            cast_to=BatchResponseContentFolder,
        )

    def get(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Retrieve a landing page folder, specified by its ID.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "property": property,
                    },
                    folder_get_params.FolderGetParams,
                ),
            ),
            cast_to=ContentFolder,
        )

    def get_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolderVersion:
        """
        Retrieve a previous version of a folder, specified by the folder ID and revision
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            path_template(
                "/cms/pages/2026-03/landing-pages/folders/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolderVersion,
        )

    def list_revisions(
        self,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[ContentFolderVersion]:
        """
        Retrieves all the previous versions of a landing page folder.

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
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}/revisions", object_id=object_id),
            page=SyncPage[ContentFolderVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    folder_list_revisions_params.FolderListRevisionsParams,
                ),
            ),
            model=ContentFolderVersion,
        )

    def restore_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Takes a specified version of a landing page folder and restores it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._post(
            path_template(
                "/cms/pages/2026-03/landing-pages/folders/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Create a new folder for landing pages.

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          created: The timestamp indicating when the content folder was created.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          updated: The timestamp indicating when the content folder was last updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/folders",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )

    async def update(
        self,
        object_id: str,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """Partially update a landing page folder, specified by the folder ID.

        You only
        need to specify the details values that you are modifying.

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          created: The timestamp indicating when the content folder was created.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          updated: The timestamp indicating when the content folder was last updated.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}", object_id=object_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, folder_update_params.FolderUpdateParams),
            ),
            cast_to=ContentFolder,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContentFolder, AsyncPage[ContentFolder]]:
        """Get the list of Landing Page Folders.

        Supports paging and filtering. This method
        would be useful for an integration that examined these models and used an
        external service to suggest edits.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          created_after: Filter folders created after the specified date and time.

          created_at: Filter folders by their exact creation date and time.

          limit: The maximum number of results to display per page.

          property: Specify a property to include in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/pages/2026-03/landing-pages/folders",
            page=AsyncPage[ContentFolder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    folder_list_params.FolderListParams,
                ),
            ),
            model=ContentFolder,
        )

    async def delete(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a landing page folder, specified by its ID.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, folder_delete_params.FolderDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def batch_get(
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
    ) -> BatchResponseContentFolder:
        """
        Retrieve a batch of landing page folders as identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/folders/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, folder_batch_get_params.FolderBatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, folder_batch_get_params.FolderBatchGetParams),
            ),
            cast_to=BatchResponseContentFolder,
        )

    async def get(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Retrieve a landing page folder, specified by its ID.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "property": property,
                    },
                    folder_get_params.FolderGetParams,
                ),
            ),
            cast_to=ContentFolder,
        )

    async def get_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolderVersion:
        """
        Retrieve a previous version of a folder, specified by the folder ID and revision
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            path_template(
                "/cms/pages/2026-03/landing-pages/folders/{object_id}/revisions/{revision_id}",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolderVersion,
        )

    def list_revisions(
        self,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContentFolderVersion, AsyncPage[ContentFolderVersion]]:
        """
        Retrieves all the previous versions of a landing page folder.

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
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            path_template("/cms/pages/2026-03/landing-pages/folders/{object_id}/revisions", object_id=object_id),
            page=AsyncPage[ContentFolderVersion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    folder_list_revisions_params.FolderListRevisionsParams,
                ),
            ),
            model=ContentFolderVersion,
        )

    async def restore_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Takes a specified version of a landing page folder and restores it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._post(
            path_template(
                "/cms/pages/2026-03/landing-pages/folders/{object_id}/revisions/{revision_id}/restore",
                object_id=object_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.update = to_raw_response_wrapper(
            folders.update,
        )
        self.list = to_raw_response_wrapper(
            folders.list,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.batch_get = to_raw_response_wrapper(
            folders.batch_get,
        )
        self.get = to_raw_response_wrapper(
            folders.get,
        )
        self.get_revision = to_raw_response_wrapper(
            folders.get_revision,
        )
        self.list_revisions = to_raw_response_wrapper(
            folders.list_revisions,
        )
        self.restore_revision = to_raw_response_wrapper(
            folders.restore_revision,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.update = async_to_raw_response_wrapper(
            folders.update,
        )
        self.list = async_to_raw_response_wrapper(
            folders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.batch_get = async_to_raw_response_wrapper(
            folders.batch_get,
        )
        self.get = async_to_raw_response_wrapper(
            folders.get,
        )
        self.get_revision = async_to_raw_response_wrapper(
            folders.get_revision,
        )
        self.list_revisions = async_to_raw_response_wrapper(
            folders.list_revisions,
        )
        self.restore_revision = async_to_raw_response_wrapper(
            folders.restore_revision,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.update = to_streamed_response_wrapper(
            folders.update,
        )
        self.list = to_streamed_response_wrapper(
            folders.list,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.batch_get = to_streamed_response_wrapper(
            folders.batch_get,
        )
        self.get = to_streamed_response_wrapper(
            folders.get,
        )
        self.get_revision = to_streamed_response_wrapper(
            folders.get_revision,
        )
        self.list_revisions = to_streamed_response_wrapper(
            folders.list_revisions,
        )
        self.restore_revision = to_streamed_response_wrapper(
            folders.restore_revision,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.update = async_to_streamed_response_wrapper(
            folders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            folders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.batch_get = async_to_streamed_response_wrapper(
            folders.batch_get,
        )
        self.get = async_to_streamed_response_wrapper(
            folders.get,
        )
        self.get_revision = async_to_streamed_response_wrapper(
            folders.get_revision,
        )
        self.list_revisions = async_to_streamed_response_wrapper(
            folders.list_revisions,
        )
        self.restore_revision = async_to_streamed_response_wrapper(
            folders.restore_revision,
        )
