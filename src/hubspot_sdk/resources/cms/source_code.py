# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Mapping, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.cms import (
    source_code_create_params,
    source_code_upsert_params,
    source_code_validate_params,
    source_code_get_metadata_params,
    source_code_extract_async_params,
)
from ..._base_client import make_request_options
from ...types.shared.task_locator import TaskLocator
from ...types.shared.action_response import ActionResponse
from ...types.cms.asset_file_metadata import AssetFileMetadata

__all__ = ["SourceCodeResource", "AsyncSourceCodeResource"]


class SourceCodeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourceCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SourceCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SourceCodeResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        path: str,
        *,
        environment: str,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetFileMetadata:
        """
        Upload a content file to a specified environment and path in the HubSpot CMS.
        This endpoint allows you to add new content files to your HubSpot account by
        specifying the environment and path where the file should be stored. The request
        must include a file in binary format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            body=maybe_transform(body, source_code_create_params.SourceCodeCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetFileMetadata,
        )

    def delete(
        self,
        path: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific content file from the specified environment in your HubSpot
        CMS. This operation is useful for removing outdated or unnecessary files from
        your source code repository. Ensure you have the necessary permissions to
        perform this action.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def extract_async(
        self,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """
        Initiate an asynchronous extraction of source code files in the HubSpot CMS.
        This endpoint is useful for handling large file extractions without blocking the
        client application. Upon acceptance, it returns a task locator that can be used
        to check the status of the extraction process.

        Args:
          path: The file system location where the zip file is to be extracted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/source-code/2026-03/extract/async",
            body=maybe_transform({"path": path}, source_code_extract_async_params.SourceCodeExtractAsyncParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskLocator,
        )

    def get(
        self,
        path: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Retrieve content from the specified environment and path in your HubSpot CMS.
        This endpoint allows you to access specific content files based on the
        environment and path parameters, which can be useful for managing and displaying
        content in different environments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_extraction_status(
        self,
        task_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponse:
        """
        Retrieve the status of an asynchronous task related to source code extraction.
        This endpoint is useful for checking the progress or completion of a task
        initiated through the asynchronous file extraction process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/cms/source-code/2026-03/extract/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponse,
        )

    def get_metadata(
        self,
        path: str,
        *,
        environment: str,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetFileMetadata:
        """
        Retrieve metadata for a specific file or folder within a specified environment
        in the HubSpot CMS. This endpoint is useful for obtaining detailed information
        about content files, such as their creation and update timestamps, and other
        metadata attributes.

        Args:
          properties: A comma-separated list of specific metadata properties to include in the
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return self._get(
            path_template("/cms/source-code/2026-03/{environment}/metadata/{path}", environment=environment, path=path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"properties": properties}, source_code_get_metadata_params.SourceCodeGetMetadataParams
                ),
            ),
            cast_to=AssetFileMetadata,
        )

    def upsert(
        self,
        path: str,
        *,
        environment: str,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetFileMetadata:
        """
        Update the content file in the specified environment and path within the HubSpot
        CMS. This operation allows you to upload a new file to replace the existing
        content at the given path. It is useful for managing and updating your website's
        source code files directly through the API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            body=maybe_transform(body, source_code_upsert_params.SourceCodeUpsertParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetFileMetadata,
        )

    def validate(
        self,
        path: str,
        *,
        environment: str,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Validate a source code file within a specified environment in your HubSpot
        account. This endpoint is useful for checking the correctness of code files
        before deployment or further processing. The validation process requires the
        file to be uploaded in a multipart/form-data request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/cms/source-code/2026-03/{environment}/validate/{path}", environment=environment, path=path),
            body=maybe_transform(body, source_code_validate_params.SourceCodeValidateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSourceCodeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourceCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourceCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSourceCodeResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        path: str,
        *,
        environment: str,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetFileMetadata:
        """
        Upload a content file to a specified environment and path in the HubSpot CMS.
        This endpoint allows you to add new content files to your HubSpot account by
        specifying the environment and path where the file should be stored. The request
        must include a file in binary format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            body=await async_maybe_transform(body, source_code_create_params.SourceCodeCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetFileMetadata,
        )

    async def delete(
        self,
        path: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific content file from the specified environment in your HubSpot
        CMS. This operation is useful for removing outdated or unnecessary files from
        your source code repository. Ensure you have the necessary permissions to
        perform this action.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def extract_async(
        self,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """
        Initiate an asynchronous extraction of source code files in the HubSpot CMS.
        This endpoint is useful for handling large file extractions without blocking the
        client application. Upon acceptance, it returns a task locator that can be used
        to check the status of the extraction process.

        Args:
          path: The file system location where the zip file is to be extracted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/source-code/2026-03/extract/async",
            body=await async_maybe_transform(
                {"path": path}, source_code_extract_async_params.SourceCodeExtractAsyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskLocator,
        )

    async def get(
        self,
        path: str,
        *,
        environment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve content from the specified environment and path in your HubSpot CMS.
        This endpoint allows you to access specific content files based on the
        environment and path parameters, which can be useful for managing and displaying
        content in different environments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_extraction_status(
        self,
        task_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponse:
        """
        Retrieve the status of an asynchronous task related to source code extraction.
        This endpoint is useful for checking the progress or completion of a task
        initiated through the asynchronous file extraction process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/cms/source-code/2026-03/extract/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponse,
        )

    async def get_metadata(
        self,
        path: str,
        *,
        environment: str,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetFileMetadata:
        """
        Retrieve metadata for a specific file or folder within a specified environment
        in the HubSpot CMS. This endpoint is useful for obtaining detailed information
        about content files, such as their creation and update timestamps, and other
        metadata attributes.

        Args:
          properties: A comma-separated list of specific metadata properties to include in the
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return await self._get(
            path_template("/cms/source-code/2026-03/{environment}/metadata/{path}", environment=environment, path=path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"properties": properties}, source_code_get_metadata_params.SourceCodeGetMetadataParams
                ),
            ),
            cast_to=AssetFileMetadata,
        )

    async def upsert(
        self,
        path: str,
        *,
        environment: str,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetFileMetadata:
        """
        Update the content file in the specified environment and path within the HubSpot
        CMS. This operation allows you to upload a new file to replace the existing
        content at the given path. It is useful for managing and updating your website's
        source code files directly through the API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template("/cms/source-code/2026-03/{environment}/content/{path}", environment=environment, path=path),
            body=await async_maybe_transform(body, source_code_upsert_params.SourceCodeUpsertParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetFileMetadata,
        )

    async def validate(
        self,
        path: str,
        *,
        environment: str,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Validate a source code file within a specified environment in your HubSpot
        account. This endpoint is useful for checking the correctness of code files
        before deployment or further processing. The validation process requires the
        file to be uploaded in a multipart/form-data request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not environment:
            raise ValueError(f"Expected a non-empty value for `environment` but received {environment!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/cms/source-code/2026-03/{environment}/validate/{path}", environment=environment, path=path),
            body=await async_maybe_transform(body, source_code_validate_params.SourceCodeValidateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SourceCodeResourceWithRawResponse:
    def __init__(self, source_code: SourceCodeResource) -> None:
        self._source_code = source_code

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                source_code.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_raw_response_wrapper(
            source_code.delete,
        )
        self.extract_async = to_raw_response_wrapper(
            source_code.extract_async,
        )
        self.get = to_custom_raw_response_wrapper(
            source_code.get,
            BinaryAPIResponse,
        )
        self.get_extraction_status = to_raw_response_wrapper(
            source_code.get_extraction_status,
        )
        self.get_metadata = to_raw_response_wrapper(
            source_code.get_metadata,
        )
        self.upsert = to_raw_response_wrapper(
            source_code.upsert,
        )
        self.validate = to_custom_raw_response_wrapper(
            source_code.validate,
            BinaryAPIResponse,
        )


class AsyncSourceCodeResourceWithRawResponse:
    def __init__(self, source_code: AsyncSourceCodeResource) -> None:
        self._source_code = source_code

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                source_code.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_raw_response_wrapper(
            source_code.delete,
        )
        self.extract_async = async_to_raw_response_wrapper(
            source_code.extract_async,
        )
        self.get = async_to_custom_raw_response_wrapper(
            source_code.get,
            AsyncBinaryAPIResponse,
        )
        self.get_extraction_status = async_to_raw_response_wrapper(
            source_code.get_extraction_status,
        )
        self.get_metadata = async_to_raw_response_wrapper(
            source_code.get_metadata,
        )
        self.upsert = async_to_raw_response_wrapper(
            source_code.upsert,
        )
        self.validate = async_to_custom_raw_response_wrapper(
            source_code.validate,
            AsyncBinaryAPIResponse,
        )


class SourceCodeResourceWithStreamingResponse:
    def __init__(self, source_code: SourceCodeResource) -> None:
        self._source_code = source_code

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                source_code.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_streamed_response_wrapper(
            source_code.delete,
        )
        self.extract_async = to_streamed_response_wrapper(
            source_code.extract_async,
        )
        self.get = to_custom_streamed_response_wrapper(
            source_code.get,
            StreamedBinaryAPIResponse,
        )
        self.get_extraction_status = to_streamed_response_wrapper(
            source_code.get_extraction_status,
        )
        self.get_metadata = to_streamed_response_wrapper(
            source_code.get_metadata,
        )
        self.upsert = to_streamed_response_wrapper(
            source_code.upsert,
        )
        self.validate = to_custom_streamed_response_wrapper(
            source_code.validate,
            StreamedBinaryAPIResponse,
        )


class AsyncSourceCodeResourceWithStreamingResponse:
    def __init__(self, source_code: AsyncSourceCodeResource) -> None:
        self._source_code = source_code

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                source_code.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_streamed_response_wrapper(
            source_code.delete,
        )
        self.extract_async = async_to_streamed_response_wrapper(
            source_code.extract_async,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            source_code.get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_extraction_status = async_to_streamed_response_wrapper(
            source_code.get_extraction_status,
        )
        self.get_metadata = async_to_streamed_response_wrapper(
            source_code.get_metadata,
        )
        self.upsert = async_to_streamed_response_wrapper(
            source_code.upsert,
        )
        self.validate = async_to_custom_streamed_response_wrapper(
            source_code.validate,
            AsyncStreamedBinaryAPIResponse,
        )
