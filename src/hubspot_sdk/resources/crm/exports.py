# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import export_create_async_params
from ..._base_client import make_request_options
from ...types.shared.task_locator import TaskLocator
from ...types.crm.public_export_response import PublicExportResponse
from ...types.crm.public_crm_search_request_param import PublicCrmSearchRequestParam
from ...types.crm.action_response_with_single_result_uri import ActionResponseWithSingleResultUri

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    @overload
    def create_async(
        self,
        *,
        associated_object_type: SequenceNotStr[str],
        export_internal_values_options: List[Literal["NAMES", "VALUES"]],
        export_name: str,
        export_type: Literal["VIEW"],
        format: Literal["CSV", "XLS", "XLSX"],
        include_labeled_associations: bool,
        include_primary_display_property_for_associated_objects: bool,
        language: Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ],
        object_properties: SequenceNotStr[str],
        object_type: str,
        override_associated_objects_per_definition_per_row_limit: bool,
        public_crm_search_request: PublicCrmSearchRequestParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """
        Begins exporting CRM data for the portal as specified in the request body

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_async(
        self,
        *,
        associated_object_type: SequenceNotStr[str],
        export_internal_values_options: List[Literal["NAMES", "VALUES"]],
        export_name: str,
        export_type: Literal["LIST"],
        format: Literal["CSV", "XLS", "XLSX"],
        include_labeled_associations: bool,
        include_primary_display_property_for_associated_objects: bool,
        language: Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ],
        list_id: str,
        object_properties: SequenceNotStr[str],
        object_type: str,
        override_associated_objects_per_definition_per_row_limit: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """
        Begins exporting CRM data for the portal as specified in the request body

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "associated_object_type",
            "export_internal_values_options",
            "export_name",
            "export_type",
            "format",
            "include_labeled_associations",
            "include_primary_display_property_for_associated_objects",
            "language",
            "object_properties",
            "object_type",
            "override_associated_objects_per_definition_per_row_limit",
        ],
        [
            "associated_object_type",
            "export_internal_values_options",
            "export_name",
            "export_type",
            "format",
            "include_labeled_associations",
            "include_primary_display_property_for_associated_objects",
            "language",
            "list_id",
            "object_properties",
            "object_type",
            "override_associated_objects_per_definition_per_row_limit",
        ],
    )
    def create_async(
        self,
        *,
        associated_object_type: SequenceNotStr[str],
        export_internal_values_options: List[Literal["NAMES", "VALUES"]],
        export_name: str,
        export_type: Literal["VIEW"] | Literal["LIST"],
        format: Literal["CSV", "XLS", "XLSX"],
        include_labeled_associations: bool,
        include_primary_display_property_for_associated_objects: bool,
        language: Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ],
        object_properties: SequenceNotStr[str],
        object_type: str,
        override_associated_objects_per_definition_per_row_limit: bool,
        public_crm_search_request: PublicCrmSearchRequestParam | Omit = omit,
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        return self._post(
            "/crm/exports/2026-03/export/async",
            body=maybe_transform(
                {
                    "associated_object_type": associated_object_type,
                    "export_internal_values_options": export_internal_values_options,
                    "export_name": export_name,
                    "export_type": export_type,
                    "format": format,
                    "include_labeled_associations": include_labeled_associations,
                    "include_primary_display_property_for_associated_objects": include_primary_display_property_for_associated_objects,
                    "language": language,
                    "object_properties": object_properties,
                    "object_type": object_type,
                    "override_associated_objects_per_definition_per_row_limit": override_associated_objects_per_definition_per_row_limit,
                    "public_crm_search_request": public_crm_search_request,
                    "list_id": list_id,
                },
                export_create_async_params.ExportCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskLocator,
        )

    def get(
        self,
        export_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicExportResponse:
        """
        Retrieve detailed information about a specific CRM export, including its current
        state and properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/crm/exports/2026-03/export/{export_id}", export_id=export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicExportResponse,
        )

    def get_status(
        self,
        task_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithSingleResultUri:
        """
        Returns the status of the export with taskId, including the URL of the resulting
        file if the export status is COMPLETE

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/crm/exports/2026-03/export/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponseWithSingleResultUri,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    @overload
    async def create_async(
        self,
        *,
        associated_object_type: SequenceNotStr[str],
        export_internal_values_options: List[Literal["NAMES", "VALUES"]],
        export_name: str,
        export_type: Literal["VIEW"],
        format: Literal["CSV", "XLS", "XLSX"],
        include_labeled_associations: bool,
        include_primary_display_property_for_associated_objects: bool,
        language: Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ],
        object_properties: SequenceNotStr[str],
        object_type: str,
        override_associated_objects_per_definition_per_row_limit: bool,
        public_crm_search_request: PublicCrmSearchRequestParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """
        Begins exporting CRM data for the portal as specified in the request body

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_async(
        self,
        *,
        associated_object_type: SequenceNotStr[str],
        export_internal_values_options: List[Literal["NAMES", "VALUES"]],
        export_name: str,
        export_type: Literal["LIST"],
        format: Literal["CSV", "XLS", "XLSX"],
        include_labeled_associations: bool,
        include_primary_display_property_for_associated_objects: bool,
        language: Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ],
        list_id: str,
        object_properties: SequenceNotStr[str],
        object_type: str,
        override_associated_objects_per_definition_per_row_limit: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        """
        Begins exporting CRM data for the portal as specified in the request body

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "associated_object_type",
            "export_internal_values_options",
            "export_name",
            "export_type",
            "format",
            "include_labeled_associations",
            "include_primary_display_property_for_associated_objects",
            "language",
            "object_properties",
            "object_type",
            "override_associated_objects_per_definition_per_row_limit",
        ],
        [
            "associated_object_type",
            "export_internal_values_options",
            "export_name",
            "export_type",
            "format",
            "include_labeled_associations",
            "include_primary_display_property_for_associated_objects",
            "language",
            "list_id",
            "object_properties",
            "object_type",
            "override_associated_objects_per_definition_per_row_limit",
        ],
    )
    async def create_async(
        self,
        *,
        associated_object_type: SequenceNotStr[str],
        export_internal_values_options: List[Literal["NAMES", "VALUES"]],
        export_name: str,
        export_type: Literal["VIEW"] | Literal["LIST"],
        format: Literal["CSV", "XLS", "XLSX"],
        include_labeled_associations: bool,
        include_primary_display_property_for_associated_objects: bool,
        language: Literal[
            "AF_ZA",
            "AR_EG",
            "BG",
            "BN",
            "CA_ES",
            "CS",
            "DA_DK",
            "DE",
            "EL_GR",
            "EN",
            "EN_GB",
            "ES",
            "ES_MX",
            "ET_EE",
            "FI",
            "FR",
            "FR_CA",
            "HE_IL",
            "HI_IN",
            "HR",
            "HU",
            "ID",
            "IT",
            "JA",
            "KO_KR",
            "LT_LT",
            "MS",
            "NL",
            "NO",
            "PL",
            "PT_BR",
            "PT_PT",
            "RO",
            "RU",
            "SK_SK",
            "SL",
            "SV",
            "TH",
            "TL",
            "TR",
            "UK",
            "VI_VN",
            "ZH_CN",
            "ZH_HK",
            "ZH_TW",
        ],
        object_properties: SequenceNotStr[str],
        object_type: str,
        override_associated_objects_per_definition_per_row_limit: bool,
        public_crm_search_request: PublicCrmSearchRequestParam | Omit = omit,
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskLocator:
        return await self._post(
            "/crm/exports/2026-03/export/async",
            body=await async_maybe_transform(
                {
                    "associated_object_type": associated_object_type,
                    "export_internal_values_options": export_internal_values_options,
                    "export_name": export_name,
                    "export_type": export_type,
                    "format": format,
                    "include_labeled_associations": include_labeled_associations,
                    "include_primary_display_property_for_associated_objects": include_primary_display_property_for_associated_objects,
                    "language": language,
                    "object_properties": object_properties,
                    "object_type": object_type,
                    "override_associated_objects_per_definition_per_row_limit": override_associated_objects_per_definition_per_row_limit,
                    "public_crm_search_request": public_crm_search_request,
                    "list_id": list_id,
                },
                export_create_async_params.ExportCreateAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskLocator,
        )

    async def get(
        self,
        export_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicExportResponse:
        """
        Retrieve detailed information about a specific CRM export, including its current
        state and properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/crm/exports/2026-03/export/{export_id}", export_id=export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicExportResponse,
        )

    async def get_status(
        self,
        task_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithSingleResultUri:
        """
        Returns the status of the export with taskId, including the URL of the resulting
        file if the export status is COMPLETE

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/crm/exports/2026-03/export/async/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponseWithSingleResultUri,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create_async = to_raw_response_wrapper(
            exports.create_async,
        )
        self.get = to_raw_response_wrapper(
            exports.get,
        )
        self.get_status = to_raw_response_wrapper(
            exports.get_status,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create_async = async_to_raw_response_wrapper(
            exports.create_async,
        )
        self.get = async_to_raw_response_wrapper(
            exports.get,
        )
        self.get_status = async_to_raw_response_wrapper(
            exports.get_status,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create_async = to_streamed_response_wrapper(
            exports.create_async,
        )
        self.get = to_streamed_response_wrapper(
            exports.get,
        )
        self.get_status = to_streamed_response_wrapper(
            exports.get_status,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create_async = async_to_streamed_response_wrapper(
            exports.create_async,
        )
        self.get = async_to_streamed_response_wrapper(
            exports.get,
        )
        self.get_status = async_to_streamed_response_wrapper(
            exports.get_status,
        )
