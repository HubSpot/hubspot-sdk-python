# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ..._base_client import make_request_options
from ...types.data_studio import (
    datasource_create_params,
    datasource_update_params,
)
from ...types.data_studio.body_part_param import BodyPartParam
from ...types.data_studio.media_type_param import MediaTypeParam
from ...types.data_studio.multi_part_param import MultiPartParam
from ...types.data_studio.data_source_get_response import DataSourceGetResponse
from ...types.data_studio.content_disposition_param import ContentDispositionParam
from ...types.data_studio.form_data_body_part_param import FormDataBodyPartParam
from ...types.data_studio.parameterized_header_param import ParameterizedHeaderParam
from ...types.data_studio.data_source_update_response import DataSourceUpdateResponse

__all__ = ["DatasourceResource", "AsyncDatasourceResource"]


class DatasourceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DatasourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return DatasourceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body_parts: Iterable[BodyPartParam],
        content_disposition: ContentDispositionParam,
        entity: object,
        fields: Dict[str, Iterable[FormDataBodyPartParam]],
        headers: Dict[str, SequenceNotStr[str]],
        media_type: MediaTypeParam,
        message_body_workers: object,
        parameterized_headers: Dict[str, Iterable[ParameterizedHeaderParam]],
        providers: object,
        parent: MultiPartParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Args:
          body_parts: An array of BodyPart objects, each representing a part of the multipart form
              data.

          entity: An object representing the entity of the multipart form data, containing the
              actual data to be processed.

          fields: An object containing fields of the multipart form data, where each field can
              have multiple FormDataBodyPart items.

          headers: An object containing headers associated with the multipart form data, where each
              header can have multiple string values.

          message_body_workers: An object representing workers that process the message body of the multipart
              form data.

          parameterized_headers: An object containing parameterized headers, where each header can have multiple
              ParameterizedHeader items.

          providers: An object representing providers associated with the multipart form data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/data-studio/2026-03/data-source",
            body=maybe_transform(
                {
                    "body_parts": body_parts,
                    "content_disposition": content_disposition,
                    "entity": entity,
                    "fields": fields,
                    "headers": headers,
                    "media_type": media_type,
                    "message_body_workers": message_body_workers,
                    "parameterized_headers": parameterized_headers,
                    "providers": providers,
                    "parent": parent,
                },
                datasource_create_params.DatasourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        datasource_id: int,
        *,
        body_parts: Iterable[BodyPartParam],
        content_disposition: ContentDispositionParam,
        entity: object,
        fields: Dict[str, Iterable[FormDataBodyPartParam]],
        headers: Dict[str, SequenceNotStr[str]],
        media_type: MediaTypeParam,
        message_body_workers: object,
        parameterized_headers: Dict[str, Iterable[ParameterizedHeaderParam]],
        providers: object,
        parent: MultiPartParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceUpdateResponse:
        """
        Args:
          body_parts: An array of BodyPart objects, each representing a part of the multipart form
              data.

          entity: An object representing the entity of the multipart form data, containing the
              actual data to be processed.

          fields: An object containing fields of the multipart form data, where each field can
              have multiple FormDataBodyPart items.

          headers: An object containing headers associated with the multipart form data, where each
              header can have multiple string values.

          message_body_workers: An object representing workers that process the message body of the multipart
              form data.

          parameterized_headers: An object containing parameterized headers, where each header can have multiple
              ParameterizedHeader items.

          providers: An object representing providers associated with the multipart form data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template("/data-studio/2026-03/data-source/{datasource_id}", datasource_id=datasource_id),
            body=maybe_transform(
                {
                    "body_parts": body_parts,
                    "content_disposition": content_disposition,
                    "entity": entity,
                    "fields": fields,
                    "headers": headers,
                    "media_type": media_type,
                    "message_body_workers": message_body_workers,
                    "parameterized_headers": parameterized_headers,
                    "providers": providers,
                    "parent": parent,
                },
                datasource_update_params.DatasourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceUpdateResponse,
        )

    def delete(
        self,
        datasource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/data-studio/2026-03/data-source/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get(
        self,
        datasource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/data-studio/2026-03/data-source/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceGetResponse,
        )


class AsyncDatasourceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDatasourceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body_parts: Iterable[BodyPartParam],
        content_disposition: ContentDispositionParam,
        entity: object,
        fields: Dict[str, Iterable[FormDataBodyPartParam]],
        headers: Dict[str, SequenceNotStr[str]],
        media_type: MediaTypeParam,
        message_body_workers: object,
        parameterized_headers: Dict[str, Iterable[ParameterizedHeaderParam]],
        providers: object,
        parent: MultiPartParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          body_parts: An array of BodyPart objects, each representing a part of the multipart form
              data.

          entity: An object representing the entity of the multipart form data, containing the
              actual data to be processed.

          fields: An object containing fields of the multipart form data, where each field can
              have multiple FormDataBodyPart items.

          headers: An object containing headers associated with the multipart form data, where each
              header can have multiple string values.

          message_body_workers: An object representing workers that process the message body of the multipart
              form data.

          parameterized_headers: An object containing parameterized headers, where each header can have multiple
              ParameterizedHeader items.

          providers: An object representing providers associated with the multipart form data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/data-studio/2026-03/data-source",
            body=await async_maybe_transform(
                {
                    "body_parts": body_parts,
                    "content_disposition": content_disposition,
                    "entity": entity,
                    "fields": fields,
                    "headers": headers,
                    "media_type": media_type,
                    "message_body_workers": message_body_workers,
                    "parameterized_headers": parameterized_headers,
                    "providers": providers,
                    "parent": parent,
                },
                datasource_create_params.DatasourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        datasource_id: int,
        *,
        body_parts: Iterable[BodyPartParam],
        content_disposition: ContentDispositionParam,
        entity: object,
        fields: Dict[str, Iterable[FormDataBodyPartParam]],
        headers: Dict[str, SequenceNotStr[str]],
        media_type: MediaTypeParam,
        message_body_workers: object,
        parameterized_headers: Dict[str, Iterable[ParameterizedHeaderParam]],
        providers: object,
        parent: MultiPartParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceUpdateResponse:
        """
        Args:
          body_parts: An array of BodyPart objects, each representing a part of the multipart form
              data.

          entity: An object representing the entity of the multipart form data, containing the
              actual data to be processed.

          fields: An object containing fields of the multipart form data, where each field can
              have multiple FormDataBodyPart items.

          headers: An object containing headers associated with the multipart form data, where each
              header can have multiple string values.

          message_body_workers: An object representing workers that process the message body of the multipart
              form data.

          parameterized_headers: An object containing parameterized headers, where each header can have multiple
              ParameterizedHeader items.

          providers: An object representing providers associated with the multipart form data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template("/data-studio/2026-03/data-source/{datasource_id}", datasource_id=datasource_id),
            body=await async_maybe_transform(
                {
                    "body_parts": body_parts,
                    "content_disposition": content_disposition,
                    "entity": entity,
                    "fields": fields,
                    "headers": headers,
                    "media_type": media_type,
                    "message_body_workers": message_body_workers,
                    "parameterized_headers": parameterized_headers,
                    "providers": providers,
                    "parent": parent,
                },
                datasource_update_params.DatasourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceUpdateResponse,
        )

    async def delete(
        self,
        datasource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/data-studio/2026-03/data-source/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get(
        self,
        datasource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/data-studio/2026-03/data-source/{datasource_id}", datasource_id=datasource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceGetResponse,
        )


class DatasourceResourceWithRawResponse:
    def __init__(self, datasource: DatasourceResource) -> None:
        self._datasource = datasource

        self.create = to_custom_raw_response_wrapper(
            datasource.create,
            BinaryAPIResponse,
        )
        self.update = to_raw_response_wrapper(
            datasource.update,
        )
        self.delete = to_custom_raw_response_wrapper(
            datasource.delete,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            datasource.get,
        )


class AsyncDatasourceResourceWithRawResponse:
    def __init__(self, datasource: AsyncDatasourceResource) -> None:
        self._datasource = datasource

        self.create = async_to_custom_raw_response_wrapper(
            datasource.create,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_raw_response_wrapper(
            datasource.update,
        )
        self.delete = async_to_custom_raw_response_wrapper(
            datasource.delete,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            datasource.get,
        )


class DatasourceResourceWithStreamingResponse:
    def __init__(self, datasource: DatasourceResource) -> None:
        self._datasource = datasource

        self.create = to_custom_streamed_response_wrapper(
            datasource.create,
            StreamedBinaryAPIResponse,
        )
        self.update = to_streamed_response_wrapper(
            datasource.update,
        )
        self.delete = to_custom_streamed_response_wrapper(
            datasource.delete,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            datasource.get,
        )


class AsyncDatasourceResourceWithStreamingResponse:
    def __init__(self, datasource: AsyncDatasourceResource) -> None:
        self._datasource = datasource

        self.create = async_to_custom_streamed_response_wrapper(
            datasource.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_streamed_response_wrapper(
            datasource.update,
        )
        self.delete = async_to_custom_streamed_response_wrapper(
            datasource.delete,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            datasource.get,
        )
