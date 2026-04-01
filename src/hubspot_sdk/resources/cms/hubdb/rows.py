# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

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
from ....types.cms.hubdb import (
    row_get_params,
    row_list_params,
    row_create_params,
    row_get_batch_params,
    row_get_draft_params,
    row_clone_batch_params,
    row_clone_draft_params,
    row_purge_batch_params,
    row_create_batch_params,
    row_update_batch_params,
    row_update_draft_params,
    row_replace_batch_params,
    row_replace_draft_params,
    row_get_draft_batch_params,
)
from ....types.cms.variant_param import VariantParam
from ....types.cms.hub_db_table_row_v3 import HubDBTableRowV3
from ....types.cms.hub_db_table_row_v3_request_param import HubDBTableRowV3RequestParam
from ....types.cms.batch_response_hub_db_table_row_v3 import BatchResponseHubDBTableRowV3
from ....types.cms.hub_db_table_row_batch_clone_request_param import HubDBTableRowBatchCloneRequestParam
from ....types.cms.hub_db_table_row_v3_batch_update_request_param import HubDBTableRowV3BatchUpdateRequestParam

__all__ = ["RowsResource", "AsyncRowsResource"]


class RowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return RowsResourceWithStreamingResponse(self)

    def create(
        self,
        table_id_or_name: str,
        *,
        child_table_id: int,
        display_index: int,
        values: Dict[str, VariantParam],
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Add a new row to a HubDB table.

        New rows will be added to the draft version of
        the table. Use the `/publish` endpoint to push these changes to published
        version.

        Args:
          child_table_id: Specifies the value for the column child table id

          display_index: The index position for displaying the row within the table.

          values: List of key value pairs with the column name and column value

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            path_template("/cms/hubdb/2026-03/tables/{table_id_or_name}/rows", table_id_or_name=table_id_or_name),
            body=maybe_transform(
                {
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "values": values,
                    "name": name,
                    "path": path,
                },
                row_create_params.RowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def list(
        self,
        table_id_or_name: str,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[object]:
        """Returns a set of rows in the published version of the specified table.

        Row
        results can be filtered and sorted. Filtering and sorting options will be sent
        as query parameters to the API request. For example, by adding the query
        parameters `column1__gt=5&sort=-column1`, API returns the rows with values for
        column `column1` greater than 5 and in the descending order of `column1` values.
        Refer to the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#filtering-and-sorting-table-rows)
        for detailed filtering and sorting options. **Note:** This endpoint can be
        accessed without any authentication, if the table is set to be allowed for
        public access.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get_api_list(
            path_template("/cms/hubdb/2026-03/tables/{table_id_or_name}/rows", table_id_or_name=table_id_or_name),
            page=SyncPage[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "limit": limit,
                        "offset": offset,
                        "properties": properties,
                        "sort": sort,
                    },
                    row_list_params.RowListParams,
                ),
            ),
            model=object,
        )

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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/clone", table_id_or_name=table_id_or_name
            ),
            body=maybe_transform({"inputs": inputs}, row_clone_batch_params.RowCloneBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def clone_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Clones a single row in the draft version of a table.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._post(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft/clone",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, row_clone_draft_params.RowCloneDraftParams),
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/create",
                table_id_or_name=table_id_or_name,
            ),
            body=maybe_transform({"inputs": inputs}, row_create_batch_params.RowCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def delete_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a row from a table's draft version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Get a single row by ID from the published version of a table.

        **Note:** This
        endpoint can be accessed without any authentication, if the table is set to be
        allowed for public access.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._get(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, row_get_params.RowGetParams),
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/batch/read", table_id_or_name=table_id_or_name
            ),
            body=maybe_transform({"inputs": inputs}, row_get_batch_params.RowGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def get_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Get a single row by ID from a table's draft version.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._get(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, row_get_draft_params.RowGetDraftParams),
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/read", table_id_or_name=table_id_or_name
            ),
            body=maybe_transform({"inputs": inputs}, row_get_draft_batch_params.RowGetDraftBatchParams),
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
        Permanently delete rows from the draft version of a table, given a set of row
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/purge", table_id_or_name=table_id_or_name
            ),
            body=maybe_transform({"inputs": inputs}, row_purge_batch_params.RowPurgeBatchParams),
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/replace",
                table_id_or_name=table_id_or_name,
            ),
            body=maybe_transform({"inputs": inputs}, row_replace_batch_params.RowReplaceBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def replace_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        child_table_id: int,
        display_index: int,
        values: Dict[str, VariantParam],
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Replace a single row in the draft version of a table.

        All column values must be
        specified. If a column has a value in the target table and this request doesn't
        define that value, it will be deleted. See the "Create a row" endpoint for
        instructions on how to format the JSON row definitions.

        Args:
          child_table_id: Specifies the value for the column child table id

          display_index: The index position for displaying the row within the table.

          values: List of key value pairs with the column name and column value

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._put(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            body=maybe_transform(
                {
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "values": values,
                    "name": name,
                    "path": path,
                },
                row_replace_draft_params.RowReplaceDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/update",
                table_id_or_name=table_id_or_name,
            ),
            body=maybe_transform({"inputs": inputs}, row_update_batch_params.RowUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def update_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        child_table_id: int,
        display_index: int,
        values: Dict[str, VariantParam],
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Partially update a single row in the table's draft version.

        All the column
        values need not be specified. Only the columns or fields that needs to be
        modified can be specified. See the "Create a row" endpoint for instructions on
        how to format the JSON row definitions.

        Args:
          child_table_id: Specifies the value for the column child table id

          display_index: The index position for displaying the row within the table.

          values: List of key value pairs with the column name and column value

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._patch(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            body=maybe_transform(
                {
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "values": values,
                    "name": name,
                    "path": path,
                },
                row_update_draft_params.RowUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )


class AsyncRowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRowsResourceWithStreamingResponse(self)

    async def create(
        self,
        table_id_or_name: str,
        *,
        child_table_id: int,
        display_index: int,
        values: Dict[str, VariantParam],
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Add a new row to a HubDB table.

        New rows will be added to the draft version of
        the table. Use the `/publish` endpoint to push these changes to published
        version.

        Args:
          child_table_id: Specifies the value for the column child table id

          display_index: The index position for displaying the row within the table.

          values: List of key value pairs with the column name and column value

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            path_template("/cms/hubdb/2026-03/tables/{table_id_or_name}/rows", table_id_or_name=table_id_or_name),
            body=await async_maybe_transform(
                {
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "values": values,
                    "name": name,
                    "path": path,
                },
                row_create_params.RowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def list(
        self,
        table_id_or_name: str,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[object, AsyncPage[object]]:
        """Returns a set of rows in the published version of the specified table.

        Row
        results can be filtered and sorted. Filtering and sorting options will be sent
        as query parameters to the API request. For example, by adding the query
        parameters `column1__gt=5&sort=-column1`, API returns the rows with values for
        column `column1` greater than 5 and in the descending order of `column1` values.
        Refer to the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#filtering-and-sorting-table-rows)
        for detailed filtering and sorting options. **Note:** This endpoint can be
        accessed without any authentication, if the table is set to be allowed for
        public access.

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get_api_list(
            path_template("/cms/hubdb/2026-03/tables/{table_id_or_name}/rows", table_id_or_name=table_id_or_name),
            page=AsyncPage[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "limit": limit,
                        "offset": offset,
                        "properties": properties,
                        "sort": sort,
                    },
                    row_list_params.RowListParams,
                ),
            ),
            model=object,
        )

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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/clone", table_id_or_name=table_id_or_name
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_clone_batch_params.RowCloneBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def clone_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Clones a single row in the draft version of a table.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._post(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft/clone",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, row_clone_draft_params.RowCloneDraftParams),
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/create",
                table_id_or_name=table_id_or_name,
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_create_batch_params.RowCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def delete_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a row from a table's draft version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Get a single row by ID from the published version of a table.

        **Note:** This
        endpoint can be accessed without any authentication, if the table is set to be
        allowed for public access.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._get(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, row_get_params.RowGetParams),
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/batch/read", table_id_or_name=table_id_or_name
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_get_batch_params.RowGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def get_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Get a single row by ID from a table's draft version.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._get(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, row_get_draft_params.RowGetDraftParams),
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/read", table_id_or_name=table_id_or_name
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_get_draft_batch_params.RowGetDraftBatchParams),
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
        Permanently delete rows from the draft version of a table, given a set of row
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/purge", table_id_or_name=table_id_or_name
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_purge_batch_params.RowPurgeBatchParams),
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/replace",
                table_id_or_name=table_id_or_name,
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_replace_batch_params.RowReplaceBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def replace_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        child_table_id: int,
        display_index: int,
        values: Dict[str, VariantParam],
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Replace a single row in the draft version of a table.

        All column values must be
        specified. If a column has a value in the target table and this request doesn't
        define that value, it will be deleted. See the "Create a row" endpoint for
        instructions on how to format the JSON row definitions.

        Args:
          child_table_id: Specifies the value for the column child table id

          display_index: The index position for displaying the row within the table.

          values: List of key value pairs with the column name and column value

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._put(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            body=await async_maybe_transform(
                {
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "values": values,
                    "name": name,
                    "path": path,
                },
                row_replace_draft_params.RowReplaceDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
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
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/draft/batch/update",
                table_id_or_name=table_id_or_name,
            ),
            body=await async_maybe_transform({"inputs": inputs}, row_update_batch_params.RowUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def update_draft(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        child_table_id: int,
        display_index: int,
        values: Dict[str, VariantParam],
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """Partially update a single row in the table's draft version.

        All the column
        values need not be specified. Only the columns or fields that needs to be
        modified can be specified. See the "Create a row" endpoint for instructions on
        how to format the JSON row definitions.

        Args:
          child_table_id: Specifies the value for the column child table id

          display_index: The index position for displaying the row within the table.

          values: List of key value pairs with the column name and column value

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._patch(
            path_template(
                "/cms/hubdb/2026-03/tables/{table_id_or_name}/rows/{row_id}/draft",
                table_id_or_name=table_id_or_name,
                row_id=row_id,
            ),
            body=await async_maybe_transform(
                {
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "values": values,
                    "name": name,
                    "path": path,
                },
                row_update_draft_params.RowUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )


class RowsResourceWithRawResponse:
    def __init__(self, rows: RowsResource) -> None:
        self._rows = rows

        self.create = to_raw_response_wrapper(
            rows.create,
        )
        self.list = to_raw_response_wrapper(
            rows.list,
        )
        self.clone_batch = to_raw_response_wrapper(
            rows.clone_batch,
        )
        self.clone_draft = to_raw_response_wrapper(
            rows.clone_draft,
        )
        self.create_batch = to_raw_response_wrapper(
            rows.create_batch,
        )
        self.delete_draft = to_raw_response_wrapper(
            rows.delete_draft,
        )
        self.get = to_raw_response_wrapper(
            rows.get,
        )
        self.get_batch = to_raw_response_wrapper(
            rows.get_batch,
        )
        self.get_draft = to_raw_response_wrapper(
            rows.get_draft,
        )
        self.get_draft_batch = to_raw_response_wrapper(
            rows.get_draft_batch,
        )
        self.purge_batch = to_raw_response_wrapper(
            rows.purge_batch,
        )
        self.replace_batch = to_raw_response_wrapper(
            rows.replace_batch,
        )
        self.replace_draft = to_raw_response_wrapper(
            rows.replace_draft,
        )
        self.update_batch = to_raw_response_wrapper(
            rows.update_batch,
        )
        self.update_draft = to_raw_response_wrapper(
            rows.update_draft,
        )


class AsyncRowsResourceWithRawResponse:
    def __init__(self, rows: AsyncRowsResource) -> None:
        self._rows = rows

        self.create = async_to_raw_response_wrapper(
            rows.create,
        )
        self.list = async_to_raw_response_wrapper(
            rows.list,
        )
        self.clone_batch = async_to_raw_response_wrapper(
            rows.clone_batch,
        )
        self.clone_draft = async_to_raw_response_wrapper(
            rows.clone_draft,
        )
        self.create_batch = async_to_raw_response_wrapper(
            rows.create_batch,
        )
        self.delete_draft = async_to_raw_response_wrapper(
            rows.delete_draft,
        )
        self.get = async_to_raw_response_wrapper(
            rows.get,
        )
        self.get_batch = async_to_raw_response_wrapper(
            rows.get_batch,
        )
        self.get_draft = async_to_raw_response_wrapper(
            rows.get_draft,
        )
        self.get_draft_batch = async_to_raw_response_wrapper(
            rows.get_draft_batch,
        )
        self.purge_batch = async_to_raw_response_wrapper(
            rows.purge_batch,
        )
        self.replace_batch = async_to_raw_response_wrapper(
            rows.replace_batch,
        )
        self.replace_draft = async_to_raw_response_wrapper(
            rows.replace_draft,
        )
        self.update_batch = async_to_raw_response_wrapper(
            rows.update_batch,
        )
        self.update_draft = async_to_raw_response_wrapper(
            rows.update_draft,
        )


class RowsResourceWithStreamingResponse:
    def __init__(self, rows: RowsResource) -> None:
        self._rows = rows

        self.create = to_streamed_response_wrapper(
            rows.create,
        )
        self.list = to_streamed_response_wrapper(
            rows.list,
        )
        self.clone_batch = to_streamed_response_wrapper(
            rows.clone_batch,
        )
        self.clone_draft = to_streamed_response_wrapper(
            rows.clone_draft,
        )
        self.create_batch = to_streamed_response_wrapper(
            rows.create_batch,
        )
        self.delete_draft = to_streamed_response_wrapper(
            rows.delete_draft,
        )
        self.get = to_streamed_response_wrapper(
            rows.get,
        )
        self.get_batch = to_streamed_response_wrapper(
            rows.get_batch,
        )
        self.get_draft = to_streamed_response_wrapper(
            rows.get_draft,
        )
        self.get_draft_batch = to_streamed_response_wrapper(
            rows.get_draft_batch,
        )
        self.purge_batch = to_streamed_response_wrapper(
            rows.purge_batch,
        )
        self.replace_batch = to_streamed_response_wrapper(
            rows.replace_batch,
        )
        self.replace_draft = to_streamed_response_wrapper(
            rows.replace_draft,
        )
        self.update_batch = to_streamed_response_wrapper(
            rows.update_batch,
        )
        self.update_draft = to_streamed_response_wrapper(
            rows.update_draft,
        )


class AsyncRowsResourceWithStreamingResponse:
    def __init__(self, rows: AsyncRowsResource) -> None:
        self._rows = rows

        self.create = async_to_streamed_response_wrapper(
            rows.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rows.list,
        )
        self.clone_batch = async_to_streamed_response_wrapper(
            rows.clone_batch,
        )
        self.clone_draft = async_to_streamed_response_wrapper(
            rows.clone_draft,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            rows.create_batch,
        )
        self.delete_draft = async_to_streamed_response_wrapper(
            rows.delete_draft,
        )
        self.get = async_to_streamed_response_wrapper(
            rows.get,
        )
        self.get_batch = async_to_streamed_response_wrapper(
            rows.get_batch,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            rows.get_draft,
        )
        self.get_draft_batch = async_to_streamed_response_wrapper(
            rows.get_draft_batch,
        )
        self.purge_batch = async_to_streamed_response_wrapper(
            rows.purge_batch,
        )
        self.replace_batch = async_to_streamed_response_wrapper(
            rows.replace_batch,
        )
        self.replace_draft = async_to_streamed_response_wrapper(
            rows.replace_draft,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            rows.update_batch,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            rows.update_draft,
        )
