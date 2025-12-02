# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .file_operations import (
    FileOperationsResource,
    AsyncFileOperationsResource,
    FileOperationsResourceWithRawResponse,
    AsyncFileOperationsResourceWithRawResponse,
    FileOperationsResourceWithStreamingResponse,
    AsyncFileOperationsResourceWithStreamingResponse,
)

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def file_operations(self) -> FileOperationsResource:
        return FileOperationsResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def file_operations(self) -> AsyncFileOperationsResource:
        return AsyncFileOperationsResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

    @cached_property
    def file_operations(self) -> FileOperationsResourceWithRawResponse:
        return FileOperationsResourceWithRawResponse(self._files.file_operations)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._files.folders)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

    @cached_property
    def file_operations(self) -> AsyncFileOperationsResourceWithRawResponse:
        return AsyncFileOperationsResourceWithRawResponse(self._files.file_operations)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._files.folders)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

    @cached_property
    def file_operations(self) -> FileOperationsResourceWithStreamingResponse:
        return FileOperationsResourceWithStreamingResponse(self._files.file_operations)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._files.folders)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

    @cached_property
    def file_operations(self) -> AsyncFileOperationsResourceWithStreamingResponse:
        return AsyncFileOperationsResourceWithStreamingResponse(self._files.file_operations)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._files.folders)
