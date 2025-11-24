# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, cast
from datetime import datetime

import httpx

from ...._types import (
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
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
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
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cms.hubdb import (
    table_get_params,
    table_list_params,
    table_create_params,
    table_export_params,
    table_get_draft_params,
    table_unpublish_params,
    table_list_draft_params,
    table_clone_draft_params,
    table_reset_draft_params,
    table_export_draft_params,
    table_import_draft_params,
    table_update_draft_params,
    table_publish_draft_params,
)
from ....types.cms.import_result import ImportResult
from ....types.cms.hub_db_table_v3 import HubDBTableV3
from ....types.cms.column_request_param import ColumnRequestParam

__all__ = ["TablesResource", "AsyncTablesResource"]


class TablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TablesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allow_child_tables: bool,
        allow_public_api_access: bool,
        columns: Iterable[ColumnRequestParam],
        dynamic_meta_tags: Dict[str, int],
        enable_child_table_pages: bool,
        label: str,
        name: str,
        use_for_pages: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Creates a new draft HubDB table given a JSON schema.

        The table name and label
        should be unique for each account.

        Args:
          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          label: Label of the table

          name: Name of the table

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/hubdb/tables",
            body=maybe_transform(
                {
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "label": label,
                    "name": name,
                    "use_for_pages": use_for_pages,
                },
                table_create_params.TableCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> SyncPage[HubDBTableV3]:
        """
        Returns the details for the published version of each table defined in an
        account, including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          content_type: Specifies the content type for the response.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the tables.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables",
            page=SyncPage[HubDBTableV3],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    table_list_params.TableListParams,
                ),
            ),
            model=HubDBTableV3,
        )

    def delete(
        self,
        table_id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive (soft delete) an existing HubDB table.

        This archives both the published
        and draft versions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clone_draft(
        self,
        table_id_or_name: str,
        *,
        copy_rows: bool,
        is_hubspot_defined: bool,
        new_label: str | Omit = omit,
        new_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Clone an existing HubDB table.

        The `newName` and `newLabel` of the new table can
        be sent as JSON in the request body. This will create the cloned table as a
        draft.

        Args:
          copy_rows: Specifies whether to copy the rows during clone

          new_label: The new label for the cloned table

          new_name: The new name for the cloned table

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/clone",
            body=maybe_transform(
                {
                    "copy_rows": copy_rows,
                    "is_hubspot_defined": is_hubspot_defined,
                    "new_label": new_label,
                    "new_name": new_name,
                },
                table_clone_draft_params.TableCloneDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    def delete_version(
        self,
        version_id: int,
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
        Delete a specific version of a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def export(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Exports the published version of a table in a specified format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, table_export_params.TableExportParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_draft(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Exports the draft version of a table to CSV / EXCEL format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, table_export_draft_params.TableExportDraftParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Returns the details for the published version of the specified table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        **Note:** This endpoint can be accessed without any authentication if the table
        is set to be allowed for public access. To do so, you'll need to include the
        HubSpot account ID in a `portalId` query parameter.

        Args:
          archived: Set this to `true` to return details for an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the tables.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    table_get_params.TableGetParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def get_draft(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Get the details for the draft version of a specific HubDB table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        Args:
          archived: Set this to `true` to return an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the table.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    table_get_draft_params.TableGetDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def import_draft(
        self,
        table_id_or_name: str,
        *,
        config: str | Omit = omit,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportResult:
        """Import the contents of a CSV file into an existing HubDB table.

        The data will
        always be imported into the draft version of the table. Use the `/publish`
        endpoint to push these changes to the published version. This endpoint takes a
        multi-part POST request. The first part will be a set of JSON-formatted options
        for the import and you can specify this with the name as `config`. The second
        part will be the CSV file you want to import and you can specify this with the
        name as `file`. Refer the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#importing-tables)
        to check the details and format of the JSON-formatted options for the import.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        body = deepcopy_minimal(
            {
                "config": config,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/import",
            body=maybe_transform(body, table_import_draft_params.TableImportDraftParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
        )

    def list_draft(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> SyncPage[HubDBTableV3]:
        """
        Returns the details for each draft table defined in the specified account,
        including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          content_type: Specifies the content type for the response.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          is_get_localized_schema: Indicates whether to retrieve the localized schema.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables/draft",
            page=SyncPage[HubDBTableV3],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    table_list_draft_params.TableListDraftParams,
                ),
            ),
            model=HubDBTableV3,
        )

    def publish_draft(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Publishes the table by copying the data and table schema changes from draft
        version to the published version, meaning any website pages using data from the
        table will be updated.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/publish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, table_publish_draft_params.TablePublishDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def reset_draft(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Replaces the data in the draft version of the table with values from the
        published version. Any unpublished changes in the draft will be lost after this
        call is made.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, table_reset_draft_params.TableResetDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def unpublish(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Unpublishes the table, meaning any website pages using data from the table will
        not render any data.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/unpublish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, table_unpublish_params.TableUnpublishParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def update_draft(
        self,
        table_id_or_name: str,
        *,
        allow_child_tables: bool,
        allow_public_api_access: bool,
        columns: Iterable[ColumnRequestParam],
        dynamic_meta_tags: Dict[str, int],
        enable_child_table_pages: bool,
        label: str,
        name: str,
        use_for_pages: bool,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Update an existing HubDB table.

        You can use this endpoint to add or remove
        columns to the table as well as restore an archived table. Tables updated using
        the endpoint will only modify the draft verion of the table. Use the `/publish`
        endpoint to push all the changes to the published version. To restore a table,
        include the query parameter `archived=true` and `"archived": false` in the json
        body. **Note:** You need to include all the columns in the input when you are
        adding/removing/updating a column. If you do not include an already existing
        column in the request, it will be deleted.

        Args:
          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          label: Label of the table

          name: Name of the table

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

          archived: Specifies whether to return archived tables. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the table.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._patch(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            body=maybe_transform(
                {
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "label": label,
                    "name": name,
                    "use_for_pages": use_for_pages,
                },
                table_update_draft_params.TableUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    table_update_draft_params.TableUpdateDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )


class AsyncTablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTablesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allow_child_tables: bool,
        allow_public_api_access: bool,
        columns: Iterable[ColumnRequestParam],
        dynamic_meta_tags: Dict[str, int],
        enable_child_table_pages: bool,
        label: str,
        name: str,
        use_for_pages: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Creates a new draft HubDB table given a JSON schema.

        The table name and label
        should be unique for each account.

        Args:
          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          label: Label of the table

          name: Name of the table

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/hubdb/tables",
            body=await async_maybe_transform(
                {
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "label": label,
                    "name": name,
                    "use_for_pages": use_for_pages,
                },
                table_create_params.TableCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> AsyncPaginator[HubDBTableV3, AsyncPage[HubDBTableV3]]:
        """
        Returns the details for the published version of each table defined in an
        account, including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          content_type: Specifies the content type for the response.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the tables.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables",
            page=AsyncPage[HubDBTableV3],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    table_list_params.TableListParams,
                ),
            ),
            model=HubDBTableV3,
        )

    async def delete(
        self,
        table_id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive (soft delete) an existing HubDB table.

        This archives both the published
        and draft versions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clone_draft(
        self,
        table_id_or_name: str,
        *,
        copy_rows: bool,
        is_hubspot_defined: bool,
        new_label: str | Omit = omit,
        new_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Clone an existing HubDB table.

        The `newName` and `newLabel` of the new table can
        be sent as JSON in the request body. This will create the cloned table as a
        draft.

        Args:
          copy_rows: Specifies whether to copy the rows during clone

          new_label: The new label for the cloned table

          new_name: The new name for the cloned table

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/clone",
            body=await async_maybe_transform(
                {
                    "copy_rows": copy_rows,
                    "is_hubspot_defined": is_hubspot_defined,
                    "new_label": new_label,
                    "new_name": new_name,
                },
                table_clone_draft_params.TableCloneDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    async def delete_version(
        self,
        version_id: int,
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
        Delete a specific version of a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def export(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Exports the published version of a table in a specified format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, table_export_params.TableExportParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_draft(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Exports the draft version of a table to CSV / EXCEL format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, table_export_draft_params.TableExportDraftParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Returns the details for the published version of the specified table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        **Note:** This endpoint can be accessed without any authentication if the table
        is set to be allowed for public access. To do so, you'll need to include the
        HubSpot account ID in a `portalId` query parameter.

        Args:
          archived: Set this to `true` to return details for an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the tables.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    table_get_params.TableGetParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def get_draft(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Get the details for the draft version of a specific HubDB table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        Args:
          archived: Set this to `true` to return an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the table.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    table_get_draft_params.TableGetDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def import_draft(
        self,
        table_id_or_name: str,
        *,
        config: str | Omit = omit,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportResult:
        """Import the contents of a CSV file into an existing HubDB table.

        The data will
        always be imported into the draft version of the table. Use the `/publish`
        endpoint to push these changes to the published version. This endpoint takes a
        multi-part POST request. The first part will be a set of JSON-formatted options
        for the import and you can specify this with the name as `config`. The second
        part will be the CSV file you want to import and you can specify this with the
        name as `file`. Refer the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#importing-tables)
        to check the details and format of the JSON-formatted options for the import.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        body = deepcopy_minimal(
            {
                "config": config,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/import",
            body=await async_maybe_transform(body, table_import_draft_params.TableImportDraftParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
        )

    def list_draft(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> AsyncPaginator[HubDBTableV3, AsyncPage[HubDBTableV3]]:
        """
        Returns the details for each draft table defined in the specified account,
        including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          content_type: Specifies the content type for the response.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          is_get_localized_schema: Indicates whether to retrieve the localized schema.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables/draft",
            page=AsyncPage[HubDBTableV3],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    table_list_draft_params.TableListDraftParams,
                ),
            ),
            model=HubDBTableV3,
        )

    async def publish_draft(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Publishes the table by copying the data and table schema changes from draft
        version to the published version, meaning any website pages using data from the
        table will be updated.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/publish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, table_publish_draft_params.TablePublishDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def reset_draft(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Replaces the data in the draft version of the table with values from the
        published version. Any unpublished changes in the draft will be lost after this
        call is made.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, table_reset_draft_params.TableResetDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def unpublish(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Unpublishes the table, meaning any website pages using data from the table will
        not render any data.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/unpublish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, table_unpublish_params.TableUnpublishParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def update_draft(
        self,
        table_id_or_name: str,
        *,
        allow_child_tables: bool,
        allow_public_api_access: bool,
        columns: Iterable[ColumnRequestParam],
        dynamic_meta_tags: Dict[str, int],
        enable_child_table_pages: bool,
        label: str,
        name: str,
        use_for_pages: bool,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """Update an existing HubDB table.

        You can use this endpoint to add or remove
        columns to the table as well as restore an archived table. Tables updated using
        the endpoint will only modify the draft verion of the table. Use the `/publish`
        endpoint to push all the changes to the published version. To restore a table,
        include the query parameter `archived=true` and `"archived": false` in the json
        body. **Note:** You need to include all the columns in the input when you are
        adding/removing/updating a column. If you do not include an already existing
        column in the request, it will be deleted.

        Args:
          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          label: Label of the table

          name: Name of the table

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

          archived: Specifies whether to return archived tables. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          is_get_localized_schema: Indicates whether to retrieve the localized schema for the table.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._patch(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            body=await async_maybe_transform(
                {
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "label": label,
                    "name": name,
                    "use_for_pages": use_for_pages,
                },
                table_update_draft_params.TableUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    table_update_draft_params.TableUpdateDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )


class TablesResourceWithRawResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.create = to_raw_response_wrapper(
            tables.create,
        )
        self.list = to_raw_response_wrapper(
            tables.list,
        )
        self.delete = to_raw_response_wrapper(
            tables.delete,
        )
        self.clone_draft = to_raw_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = to_raw_response_wrapper(
            tables.delete_version,
        )
        self.export = to_custom_raw_response_wrapper(
            tables.export,
            BinaryAPIResponse,
        )
        self.export_draft = to_custom_raw_response_wrapper(
            tables.export_draft,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            tables.get,
        )
        self.get_draft = to_raw_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = to_raw_response_wrapper(
            tables.import_draft,
        )
        self.list_draft = to_raw_response_wrapper(
            tables.list_draft,
        )
        self.publish_draft = to_raw_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = to_raw_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = to_raw_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = to_raw_response_wrapper(
            tables.update_draft,
        )


class AsyncTablesResourceWithRawResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.create = async_to_raw_response_wrapper(
            tables.create,
        )
        self.list = async_to_raw_response_wrapper(
            tables.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tables.delete,
        )
        self.clone_draft = async_to_raw_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = async_to_raw_response_wrapper(
            tables.delete_version,
        )
        self.export = async_to_custom_raw_response_wrapper(
            tables.export,
            AsyncBinaryAPIResponse,
        )
        self.export_draft = async_to_custom_raw_response_wrapper(
            tables.export_draft,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            tables.get,
        )
        self.get_draft = async_to_raw_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = async_to_raw_response_wrapper(
            tables.import_draft,
        )
        self.list_draft = async_to_raw_response_wrapper(
            tables.list_draft,
        )
        self.publish_draft = async_to_raw_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = async_to_raw_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = async_to_raw_response_wrapper(
            tables.update_draft,
        )


class TablesResourceWithStreamingResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.create = to_streamed_response_wrapper(
            tables.create,
        )
        self.list = to_streamed_response_wrapper(
            tables.list,
        )
        self.delete = to_streamed_response_wrapper(
            tables.delete,
        )
        self.clone_draft = to_streamed_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = to_streamed_response_wrapper(
            tables.delete_version,
        )
        self.export = to_custom_streamed_response_wrapper(
            tables.export,
            StreamedBinaryAPIResponse,
        )
        self.export_draft = to_custom_streamed_response_wrapper(
            tables.export_draft,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            tables.get,
        )
        self.get_draft = to_streamed_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = to_streamed_response_wrapper(
            tables.import_draft,
        )
        self.list_draft = to_streamed_response_wrapper(
            tables.list_draft,
        )
        self.publish_draft = to_streamed_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = to_streamed_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = to_streamed_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = to_streamed_response_wrapper(
            tables.update_draft,
        )


class AsyncTablesResourceWithStreamingResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.create = async_to_streamed_response_wrapper(
            tables.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tables.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tables.delete,
        )
        self.clone_draft = async_to_streamed_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = async_to_streamed_response_wrapper(
            tables.delete_version,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            tables.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_draft = async_to_custom_streamed_response_wrapper(
            tables.export_draft,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            tables.get,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = async_to_streamed_response_wrapper(
            tables.import_draft,
        )
        self.list_draft = async_to_streamed_response_wrapper(
            tables.list_draft,
        )
        self.publish_draft = async_to_streamed_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            tables.update_draft,
        )
