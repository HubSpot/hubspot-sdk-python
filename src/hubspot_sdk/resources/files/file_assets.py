# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
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
    file_asset_get_params,
    file_asset_create_params,
    file_asset_search_params,
    file_asset_update_params,
    file_asset_upload_params,
    file_asset_replace_params,
    file_asset_get_by_path_params,
    file_asset_get_signed_url_params,
    file_asset_import_from_url_async_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.files.file import File
from ...types.files.folder import Folder
from ...types.files.file_stat import FileStat
from ...types.files.signed_url import SignedURL
from ...types.files.file_action_response import FileActionResponse
from ...types.files.import_from_url_task_locator import ImportFromURLTaskLocator

__all__ = ["FileAssetsResource", "AsyncFileAssetsResource"]


class FileAssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FileAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return FileAssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parent_folder_id: str | Omit = omit,
        parent_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Creates a folder.

        Args:
          name: Desired name for the folder.

          parent_folder_id: FolderId of the parent of the created folder. If not specified, the folder will
              be created at the root level. parentFolderId and parentFolderPath cannot be set
              at the same time.

          parent_path: Path of the parent of the created folder. If not specified the folder will be
              created at the root level. parentFolderPath and parentFolderId cannot be set at
              the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/files/2026-03/folders",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_path": parent_path,
                },
                file_asset_create_params.FileAssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    def update(
        self,
        file_id: str,
        *,
        clear_expires: bool,
        access: Literal[
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "HIDDEN_SENSITIVE",
            "PRIVATE",
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "SENSITIVE",
        ]
        | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        name: str | Omit = omit,
        parent_folder_id: str | Omit = omit,
        parent_folder_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Update properties of file by ID.

        Args:
          access: NONE: Do not run any duplicate validation. REJECT: Reject the upload if a
              duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload
              a new file and return the found duplicate instead.

          is_usable_in_content: Mark whether the file should be used in new content or not.

          name: New name for the file.

          parent_folder_id: FolderId where the file should be moved to. folderId and folderPath parameters
              cannot be set at the same time.

          parent_folder_path: Folder path where the file should be moved to. folderId and folderPath
              parameters cannot be set at the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            body=maybe_transform(
                {
                    "clear_expires": clear_expires,
                    "access": access,
                    "expires_at": expires_at,
                    "is_usable_in_content": is_usable_in_content,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_folder_path": parent_folder_path,
                },
                file_asset_update_params.FileAssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def gdpr_delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file in accordance with GDPR regulations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/files/2026-03/files/{file_id}/gdpr-delete", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        file_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve a file by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, file_asset_get_params.FileAssetGetParams),
            ),
            cast_to=File,
        )

    def get_by_path(
        self,
        path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileStat:
        """
        Retrieve a file by its path.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return self._get(
            path_template("/files/2026-03/files/stat/{path}", path=path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"properties": properties}, file_asset_get_by_path_params.FileAssetGetByPathParams
                ),
            ),
            cast_to=FileStat,
        )

    def get_import_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileActionResponse:
        """
        Check the status of requested import.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/files/2026-03/files/import-from-url/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileActionResponse,
        )

    def get_signed_url(
        self,
        file_id: str,
        *,
        expiration_seconds: int | Omit = omit,
        size: Literal["icon", "medium", "preview", "thumb"] | Omit = omit,
        upscale: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedURL:
        """
        Generates signed URL that allows temporary access to a private file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/files/2026-03/files/{file_id}/signed-url", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiration_seconds": expiration_seconds,
                        "size": size,
                        "upscale": upscale,
                    },
                    file_asset_get_signed_url_params.FileAssetGetSignedURLParams,
                ),
            ),
            cast_to=SignedURL,
        )

    def import_from_url_async(
        self,
        *,
        access: Literal[
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "HIDDEN_SENSITIVE",
            "PRIVATE",
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "SENSITIVE",
        ],
        duplicate_validation_scope: Literal["ENTIRE_PORTAL", "EXACT_FOLDER"],
        duplicate_validation_strategy: Literal["NONE", "REJECT", "RETURN_EXISTING"],
        overwrite: bool,
        expires_at: Union[str, datetime] | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        name: str | Omit = omit,
        ttl: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportFromURLTaskLocator:
        """
        Asynchronously imports the file at the given URL into the file manager.

        Args:
          access: PUBLIC_INDEXABLE: File is publicly accessible by anyone who has the URL. Search
              engines can index the file. PUBLIC_NOT_INDEXABLE: File is publicly accessible by
              anyone who has the URL. Search engines _can't_ index the file. PRIVATE: File is
              NOT publicly accessible. Requires a signed URL to see content. Search engines
              _can't_ index the file.

          duplicate_validation_scope:
              ENTIRE_PORTAL: Look for a duplicate file in the entire account. EXACT_FOLDER:
              Look for a duplicate file in the provided folder.

          duplicate_validation_strategy: NONE: Do not run any duplicate validation. REJECT: Reject the upload if a
              duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload
              a new file and return the found duplicate instead.

          overwrite: If true, will overwrite existing file if one with the same name and extension
              exists in the given folder. The overwritten file will be deleted and the
              uploaded file will take its place with a new ID. If unset or set as false, the
              new file's name will be updated to prevent colliding with existing file if one
              exists with the same path, name, and extension

          expires_at: Specifies the date and time when the file will expire.

          folder_id: One of folderId or folderPath is required. Destination folderId for the uploaded
              file.

          folder_path: One of folderPath or folderId is required. Destination folder path for the
              uploaded file. If the folder path does not exist, there will be an attempt to
              create the folder path.

          name: Name to give the resulting file in the file manager.

          ttl: Time to live. If specified the file will be deleted after the given time frame.
              If left unset, the file will exist indefinitely

          url: URL to download the new file from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/files/2026-03/files/import-from-url/async",
            body=maybe_transform(
                {
                    "access": access,
                    "duplicate_validation_scope": duplicate_validation_scope,
                    "duplicate_validation_strategy": duplicate_validation_strategy,
                    "overwrite": overwrite,
                    "expires_at": expires_at,
                    "folder_id": folder_id,
                    "folder_path": folder_path,
                    "name": name,
                    "ttl": ttl,
                    "url": url,
                },
                file_asset_import_from_url_async_params.FileAssetImportFromURLAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportFromURLTaskLocator,
        )

    def replace(
        self,
        file_id: str,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """Replace existing file data with new file data.

        Can be used to change image
        content without having to upload a new file and update all references.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            body=maybe_transform(body, file_asset_replace_params.FileAssetReplaceParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        allows_anonymous_access: bool | Omit = omit,
        before: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        encoding: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        expires_at_gte: Union[str, datetime] | Omit = omit,
        expires_at_lte: Union[str, datetime] | Omit = omit,
        extension: str | Omit = omit,
        file_md5: str | Omit = omit,
        height: int | Omit = omit,
        height_gte: int | Omit = omit,
        height_lte: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lte: int | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        parent_folder_ids: Iterable[int] | Omit = omit,
        path: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        size: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_lte: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        type: str | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        url: str | Omit = omit,
        width: int | Omit = omit,
        width_gte: int | Omit = omit,
        width_lte: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[File]:
        """Search through files in the file manager.

        Does not display hidden or archived
        files.

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
            "/files/2026-03/files/search",
            page=SyncPage[File],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "allows_anonymous_access": allows_anonymous_access,
                        "before": before,
                        "created_at": created_at,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "encoding": encoding,
                        "expires_at": expires_at,
                        "expires_at_gte": expires_at_gte,
                        "expires_at_lte": expires_at_lte,
                        "extension": extension,
                        "file_md5": file_md5,
                        "height": height,
                        "height_gte": height_gte,
                        "height_lte": height_lte,
                        "id_gte": id_gte,
                        "id_lte": id_lte,
                        "ids": ids,
                        "is_usable_in_content": is_usable_in_content,
                        "limit": limit,
                        "name": name,
                        "parent_folder_ids": parent_folder_ids,
                        "path": path,
                        "properties": properties,
                        "size": size,
                        "size_gte": size_gte,
                        "size_lte": size_lte,
                        "sort": sort,
                        "type": type,
                        "updated_at": updated_at,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                        "url": url,
                        "width": width,
                        "width_gte": width_gte,
                        "width_lte": width_lte,
                    },
                    file_asset_search_params.FileAssetSearchParams,
                ),
            ),
            model=File,
        )

    def upload(
        self,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        file_name: str | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload a single file with content specified in request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "file_name": file_name,
                "folder_id": folder_id,
                "folder_path": folder_path,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/2026-03/files",
            body=maybe_transform(body, file_asset_upload_params.FileAssetUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )


class AsyncFileAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFileAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parent_folder_id: str | Omit = omit,
        parent_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folder:
        """
        Creates a folder.

        Args:
          name: Desired name for the folder.

          parent_folder_id: FolderId of the parent of the created folder. If not specified, the folder will
              be created at the root level. parentFolderId and parentFolderPath cannot be set
              at the same time.

          parent_path: Path of the parent of the created folder. If not specified the folder will be
              created at the root level. parentFolderPath and parentFolderId cannot be set at
              the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/files/2026-03/folders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_path": parent_path,
                },
                file_asset_create_params.FileAssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Folder,
        )

    async def update(
        self,
        file_id: str,
        *,
        clear_expires: bool,
        access: Literal[
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "HIDDEN_SENSITIVE",
            "PRIVATE",
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "SENSITIVE",
        ]
        | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        name: str | Omit = omit,
        parent_folder_id: str | Omit = omit,
        parent_folder_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Update properties of file by ID.

        Args:
          access: NONE: Do not run any duplicate validation. REJECT: Reject the upload if a
              duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload
              a new file and return the found duplicate instead.

          is_usable_in_content: Mark whether the file should be used in new content or not.

          name: New name for the file.

          parent_folder_id: FolderId where the file should be moved to. folderId and folderPath parameters
              cannot be set at the same time.

          parent_folder_path: Folder path where the file should be moved to. folderId and folderPath
              parameters cannot be set at the same time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            body=await async_maybe_transform(
                {
                    "clear_expires": clear_expires,
                    "access": access,
                    "expires_at": expires_at,
                    "is_usable_in_content": is_usable_in_content,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_folder_path": parent_folder_path,
                },
                file_asset_update_params.FileAssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def gdpr_delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file in accordance with GDPR regulations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/files/2026-03/files/{file_id}/gdpr-delete", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        file_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve a file by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"properties": properties}, file_asset_get_params.FileAssetGetParams),
            ),
            cast_to=File,
        )

    async def get_by_path(
        self,
        path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileStat:
        """
        Retrieve a file by its path.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return await self._get(
            path_template("/files/2026-03/files/stat/{path}", path=path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"properties": properties}, file_asset_get_by_path_params.FileAssetGetByPathParams
                ),
            ),
            cast_to=FileStat,
        )

    async def get_import_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileActionResponse:
        """
        Check the status of requested import.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/files/2026-03/files/import-from-url/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileActionResponse,
        )

    async def get_signed_url(
        self,
        file_id: str,
        *,
        expiration_seconds: int | Omit = omit,
        size: Literal["icon", "medium", "preview", "thumb"] | Omit = omit,
        upscale: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedURL:
        """
        Generates signed URL that allows temporary access to a private file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/files/2026-03/files/{file_id}/signed-url", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiration_seconds": expiration_seconds,
                        "size": size,
                        "upscale": upscale,
                    },
                    file_asset_get_signed_url_params.FileAssetGetSignedURLParams,
                ),
            ),
            cast_to=SignedURL,
        )

    async def import_from_url_async(
        self,
        *,
        access: Literal[
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "HIDDEN_SENSITIVE",
            "PRIVATE",
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "SENSITIVE",
        ],
        duplicate_validation_scope: Literal["ENTIRE_PORTAL", "EXACT_FOLDER"],
        duplicate_validation_strategy: Literal["NONE", "REJECT", "RETURN_EXISTING"],
        overwrite: bool,
        expires_at: Union[str, datetime] | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        name: str | Omit = omit,
        ttl: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportFromURLTaskLocator:
        """
        Asynchronously imports the file at the given URL into the file manager.

        Args:
          access: PUBLIC_INDEXABLE: File is publicly accessible by anyone who has the URL. Search
              engines can index the file. PUBLIC_NOT_INDEXABLE: File is publicly accessible by
              anyone who has the URL. Search engines _can't_ index the file. PRIVATE: File is
              NOT publicly accessible. Requires a signed URL to see content. Search engines
              _can't_ index the file.

          duplicate_validation_scope:
              ENTIRE_PORTAL: Look for a duplicate file in the entire account. EXACT_FOLDER:
              Look for a duplicate file in the provided folder.

          duplicate_validation_strategy: NONE: Do not run any duplicate validation. REJECT: Reject the upload if a
              duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload
              a new file and return the found duplicate instead.

          overwrite: If true, will overwrite existing file if one with the same name and extension
              exists in the given folder. The overwritten file will be deleted and the
              uploaded file will take its place with a new ID. If unset or set as false, the
              new file's name will be updated to prevent colliding with existing file if one
              exists with the same path, name, and extension

          expires_at: Specifies the date and time when the file will expire.

          folder_id: One of folderId or folderPath is required. Destination folderId for the uploaded
              file.

          folder_path: One of folderPath or folderId is required. Destination folder path for the
              uploaded file. If the folder path does not exist, there will be an attempt to
              create the folder path.

          name: Name to give the resulting file in the file manager.

          ttl: Time to live. If specified the file will be deleted after the given time frame.
              If left unset, the file will exist indefinitely

          url: URL to download the new file from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/files/2026-03/files/import-from-url/async",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "duplicate_validation_scope": duplicate_validation_scope,
                    "duplicate_validation_strategy": duplicate_validation_strategy,
                    "overwrite": overwrite,
                    "expires_at": expires_at,
                    "folder_id": folder_id,
                    "folder_path": folder_path,
                    "name": name,
                    "ttl": ttl,
                    "url": url,
                },
                file_asset_import_from_url_async_params.FileAssetImportFromURLAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportFromURLTaskLocator,
        )

    async def replace(
        self,
        file_id: str,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """Replace existing file data with new file data.

        Can be used to change image
        content without having to upload a new file and update all references.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template("/files/2026-03/files/{file_id}", file_id=file_id),
            body=await async_maybe_transform(body, file_asset_replace_params.FileAssetReplaceParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        allows_anonymous_access: bool | Omit = omit,
        before: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        encoding: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        expires_at_gte: Union[str, datetime] | Omit = omit,
        expires_at_lte: Union[str, datetime] | Omit = omit,
        extension: str | Omit = omit,
        file_md5: str | Omit = omit,
        height: int | Omit = omit,
        height_gte: int | Omit = omit,
        height_lte: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lte: int | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        parent_folder_ids: Iterable[int] | Omit = omit,
        path: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        size: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_lte: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        type: str | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        url: str | Omit = omit,
        width: int | Omit = omit,
        width_gte: int | Omit = omit,
        width_lte: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[File, AsyncPage[File]]:
        """Search through files in the file manager.

        Does not display hidden or archived
        files.

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
            "/files/2026-03/files/search",
            page=AsyncPage[File],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "allows_anonymous_access": allows_anonymous_access,
                        "before": before,
                        "created_at": created_at,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "encoding": encoding,
                        "expires_at": expires_at,
                        "expires_at_gte": expires_at_gte,
                        "expires_at_lte": expires_at_lte,
                        "extension": extension,
                        "file_md5": file_md5,
                        "height": height,
                        "height_gte": height_gte,
                        "height_lte": height_lte,
                        "id_gte": id_gte,
                        "id_lte": id_lte,
                        "ids": ids,
                        "is_usable_in_content": is_usable_in_content,
                        "limit": limit,
                        "name": name,
                        "parent_folder_ids": parent_folder_ids,
                        "path": path,
                        "properties": properties,
                        "size": size,
                        "size_gte": size_gte,
                        "size_lte": size_lte,
                        "sort": sort,
                        "type": type,
                        "updated_at": updated_at,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                        "url": url,
                        "width": width,
                        "width_gte": width_gte,
                        "width_lte": width_lte,
                    },
                    file_asset_search_params.FileAssetSearchParams,
                ),
            ),
            model=File,
        )

    async def upload(
        self,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        file_name: str | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload a single file with content specified in request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "file_name": file_name,
                "folder_id": folder_id,
                "folder_path": folder_path,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files/2026-03/files",
            body=await async_maybe_transform(body, file_asset_upload_params.FileAssetUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )


class FileAssetsResourceWithRawResponse:
    def __init__(self, file_assets: FileAssetsResource) -> None:
        self._file_assets = file_assets

        self.create = to_raw_response_wrapper(
            file_assets.create,
        )
        self.update = to_raw_response_wrapper(
            file_assets.update,
        )
        self.delete = to_raw_response_wrapper(
            file_assets.delete,
        )
        self.gdpr_delete = to_raw_response_wrapper(
            file_assets.gdpr_delete,
        )
        self.get = to_raw_response_wrapper(
            file_assets.get,
        )
        self.get_by_path = to_raw_response_wrapper(
            file_assets.get_by_path,
        )
        self.get_import_task_status = to_raw_response_wrapper(
            file_assets.get_import_task_status,
        )
        self.get_signed_url = to_raw_response_wrapper(
            file_assets.get_signed_url,
        )
        self.import_from_url_async = to_raw_response_wrapper(
            file_assets.import_from_url_async,
        )
        self.replace = to_raw_response_wrapper(
            file_assets.replace,
        )
        self.search = to_raw_response_wrapper(
            file_assets.search,
        )
        self.upload = to_raw_response_wrapper(
            file_assets.upload,
        )


class AsyncFileAssetsResourceWithRawResponse:
    def __init__(self, file_assets: AsyncFileAssetsResource) -> None:
        self._file_assets = file_assets

        self.create = async_to_raw_response_wrapper(
            file_assets.create,
        )
        self.update = async_to_raw_response_wrapper(
            file_assets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            file_assets.delete,
        )
        self.gdpr_delete = async_to_raw_response_wrapper(
            file_assets.gdpr_delete,
        )
        self.get = async_to_raw_response_wrapper(
            file_assets.get,
        )
        self.get_by_path = async_to_raw_response_wrapper(
            file_assets.get_by_path,
        )
        self.get_import_task_status = async_to_raw_response_wrapper(
            file_assets.get_import_task_status,
        )
        self.get_signed_url = async_to_raw_response_wrapper(
            file_assets.get_signed_url,
        )
        self.import_from_url_async = async_to_raw_response_wrapper(
            file_assets.import_from_url_async,
        )
        self.replace = async_to_raw_response_wrapper(
            file_assets.replace,
        )
        self.search = async_to_raw_response_wrapper(
            file_assets.search,
        )
        self.upload = async_to_raw_response_wrapper(
            file_assets.upload,
        )


class FileAssetsResourceWithStreamingResponse:
    def __init__(self, file_assets: FileAssetsResource) -> None:
        self._file_assets = file_assets

        self.create = to_streamed_response_wrapper(
            file_assets.create,
        )
        self.update = to_streamed_response_wrapper(
            file_assets.update,
        )
        self.delete = to_streamed_response_wrapper(
            file_assets.delete,
        )
        self.gdpr_delete = to_streamed_response_wrapper(
            file_assets.gdpr_delete,
        )
        self.get = to_streamed_response_wrapper(
            file_assets.get,
        )
        self.get_by_path = to_streamed_response_wrapper(
            file_assets.get_by_path,
        )
        self.get_import_task_status = to_streamed_response_wrapper(
            file_assets.get_import_task_status,
        )
        self.get_signed_url = to_streamed_response_wrapper(
            file_assets.get_signed_url,
        )
        self.import_from_url_async = to_streamed_response_wrapper(
            file_assets.import_from_url_async,
        )
        self.replace = to_streamed_response_wrapper(
            file_assets.replace,
        )
        self.search = to_streamed_response_wrapper(
            file_assets.search,
        )
        self.upload = to_streamed_response_wrapper(
            file_assets.upload,
        )


class AsyncFileAssetsResourceWithStreamingResponse:
    def __init__(self, file_assets: AsyncFileAssetsResource) -> None:
        self._file_assets = file_assets

        self.create = async_to_streamed_response_wrapper(
            file_assets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            file_assets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            file_assets.delete,
        )
        self.gdpr_delete = async_to_streamed_response_wrapper(
            file_assets.gdpr_delete,
        )
        self.get = async_to_streamed_response_wrapper(
            file_assets.get,
        )
        self.get_by_path = async_to_streamed_response_wrapper(
            file_assets.get_by_path,
        )
        self.get_import_task_status = async_to_streamed_response_wrapper(
            file_assets.get_import_task_status,
        )
        self.get_signed_url = async_to_streamed_response_wrapper(
            file_assets.get_signed_url,
        )
        self.import_from_url_async = async_to_streamed_response_wrapper(
            file_assets.import_from_url_async,
        )
        self.replace = async_to_streamed_response_wrapper(
            file_assets.replace,
        )
        self.search = async_to_streamed_response_wrapper(
            file_assets.search,
        )
        self.upload = async_to_streamed_response_wrapper(
            file_assets.upload,
        )
