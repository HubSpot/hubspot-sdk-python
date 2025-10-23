# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cms.hubdb.rows import (
    batch_get_batch_params,
    batch_clone_batch_params,
    batch_purge_batch_params,
    batch_create_batch_params,
    batch_update_batch_params,
    batch_replace_batch_params,
    batch_get_draft_batch_params,
)
from .....types.cms.hub_db_table_row_v3_request_param import HubDBTableRowV3RequestParam
from .....types.cms.batch_response_hub_db_table_row_v3 import BatchResponseHubDBTableRowV3
from .....types.cms.hub_db_table_row_batch_clone_request_param import HubDBTableRowBatchCloneRequestParam
from .....types.cms.hub_db_table_row_v3_batch_update_request_param import HubDBTableRowV3BatchUpdateRequestParam

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def clone_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowBatchCloneRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Clones rows in the draft version of the specified table, given a set of row ids.
        Maximum of 100 row ids per call.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/clone",
            body=maybe_transform({"inputs": inputs}, batch_clone_batch_params.BatchCloneBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def create_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3RequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Creates rows in the draft version of the specified table, given an array of row
        objects. Maximum of 100 row object per call. See the overview section for more
        details with an example.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/create",
            body=maybe_transform({"inputs": inputs}, batch_create_batch_params.BatchCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def get_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Returns rows in the published version of the specified table, given a set of row
        IDs. **Note:** This endpoint can be accessed without any authentication if the
        table is set to be allowed for public access.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_batch_params.BatchGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def get_draft_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Returns rows in the draft version of the specified table, given a set of row
        IDs.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/read",
            body=maybe_transform({"inputs": inputs}, batch_get_draft_batch_params.BatchGetDraftBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def purge_batch(
        self,
        table_id_or_name: str,
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
        Permanently deletes rows from the draft version of the table, given a set of row
        IDs. Maximum of 100 row IDs per call.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/purge",
            body=maybe_transform({"inputs": inputs}, batch_purge_batch_params.BatchPurgeBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Replaces multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PUT /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/replace",
            body=maybe_transform({"inputs": inputs}, batch_replace_batch_params.BatchReplaceBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def update_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Updates multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PATCH /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/update",
            body=maybe_transform({"inputs": inputs}, batch_update_batch_params.BatchUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def clone_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowBatchCloneRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Clones rows in the draft version of the specified table, given a set of row ids.
        Maximum of 100 row ids per call.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/clone",
            body=await async_maybe_transform({"inputs": inputs}, batch_clone_batch_params.BatchCloneBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def create_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3RequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Creates rows in the draft version of the specified table, given an array of row
        objects. Maximum of 100 row object per call. See the overview section for more
        details with an example.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/create",
            body=await async_maybe_transform({"inputs": inputs}, batch_create_batch_params.BatchCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def get_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Returns rows in the published version of the specified table, given a set of row
        IDs. **Note:** This endpoint can be accessed without any authentication if the
        table is set to be allowed for public access.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_get_batch_params.BatchGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def get_draft_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Returns rows in the draft version of the specified table, given a set of row
        IDs.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, batch_get_draft_batch_params.BatchGetDraftBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def purge_batch(
        self,
        table_id_or_name: str,
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
        Permanently deletes rows from the draft version of the table, given a set of row
        IDs. Maximum of 100 row IDs per call.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/purge",
            body=await async_maybe_transform({"inputs": inputs}, batch_purge_batch_params.BatchPurgeBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Replaces multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PUT /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/replace",
            body=await async_maybe_transform({"inputs": inputs}, batch_replace_batch_params.BatchReplaceBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def update_batch(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Updates multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PATCH /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, batch_update_batch_params.BatchUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.clone_batch = to_raw_response_wrapper(
            batch.clone_batch,
        )
        self.create_batch = to_raw_response_wrapper(
            batch.create_batch,
        )
        self.get_batch = to_raw_response_wrapper(
            batch.get_batch,
        )
        self.get_draft_batch = to_raw_response_wrapper(
            batch.get_draft_batch,
        )
        self.purge_batch = to_raw_response_wrapper(
            batch.purge_batch,
        )
        self.replace_batch = to_raw_response_wrapper(
            batch.replace_batch,
        )
        self.update_batch = to_raw_response_wrapper(
            batch.update_batch,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.clone_batch = async_to_raw_response_wrapper(
            batch.clone_batch,
        )
        self.create_batch = async_to_raw_response_wrapper(
            batch.create_batch,
        )
        self.get_batch = async_to_raw_response_wrapper(
            batch.get_batch,
        )
        self.get_draft_batch = async_to_raw_response_wrapper(
            batch.get_draft_batch,
        )
        self.purge_batch = async_to_raw_response_wrapper(
            batch.purge_batch,
        )
        self.replace_batch = async_to_raw_response_wrapper(
            batch.replace_batch,
        )
        self.update_batch = async_to_raw_response_wrapper(
            batch.update_batch,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.clone_batch = to_streamed_response_wrapper(
            batch.clone_batch,
        )
        self.create_batch = to_streamed_response_wrapper(
            batch.create_batch,
        )
        self.get_batch = to_streamed_response_wrapper(
            batch.get_batch,
        )
        self.get_draft_batch = to_streamed_response_wrapper(
            batch.get_draft_batch,
        )
        self.purge_batch = to_streamed_response_wrapper(
            batch.purge_batch,
        )
        self.replace_batch = to_streamed_response_wrapper(
            batch.replace_batch,
        )
        self.update_batch = to_streamed_response_wrapper(
            batch.update_batch,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.clone_batch = async_to_streamed_response_wrapper(
            batch.clone_batch,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            batch.create_batch,
        )
        self.get_batch = async_to_streamed_response_wrapper(
            batch.get_batch,
        )
        self.get_draft_batch = async_to_streamed_response_wrapper(
            batch.get_draft_batch,
        )
        self.purge_batch = async_to_streamed_response_wrapper(
            batch.purge_batch,
        )
        self.replace_batch = async_to_streamed_response_wrapper(
            batch.replace_batch,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            batch.update_batch,
        )
