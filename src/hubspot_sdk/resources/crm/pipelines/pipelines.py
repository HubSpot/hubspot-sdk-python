# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .stages import (
    StagesResource,
    AsyncStagesResource,
    StagesResourceWithRawResponse,
    AsyncStagesResourceWithRawResponse,
    StagesResourceWithStreamingResponse,
    AsyncStagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.crm import (
    pipeline_create_params,
    pipeline_delete_params,
    pipeline_update_params,
    pipeline_replace_params,
)
from ...._base_client import make_request_options
from ....types.crm.pipeline import Pipeline
from ....types.crm.pipeline_stage_input_param import PipelineStageInputParam
from ....types.crm.collection_response_pipeline_no_paging import CollectionResponsePipelineNoPaging
from ....types.crm.collection_response_public_audit_info_no_paging import CollectionResponsePublicAuditInfoNoPaging

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def stages(self) -> StagesResource:
        return StagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PipelinesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: str,
        *,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """Create a new pipeline with the provided property values.

        The entire pipeline
        object, including its unique ID, will be returned in the response.

        Args:
          display_order: The order for displaying this pipeline. If two pipelines have a matching
              `displayOrder`, they will be sorted alphabetically by label.

          label: A unique label used to organize pipelines in HubSpot's UI

          stages: Pipeline stage inputs used to create the new or replacement pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm/v3/pipelines/{object_type}",
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def update(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        validate_deal_stage_usages_before_delete: bool | Omit = omit,
        validate_references_before_delete: bool | Omit = omit,
        archived: bool | Omit = omit,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """Perform a partial update of the pipeline identified by `{pipelineId}`.

        The
        updated pipeline will be returned in the response.

        Args:
          archived: Whether the pipeline is archived. This property should only be provided when
              restoring an archived pipeline. If it's provided in any other call, the request
              will fail and a `400 Bad Request` will be returned.

          display_order: The order for displaying this pipeline. If two pipelines have a matching
              `displayOrder`, they will be sorted alphabetically by label.

          label: A unique label used to organize pipelines in HubSpot's UI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._patch(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "validate_deal_stage_usages_before_delete": validate_deal_stage_usages_before_delete,
                        "validate_references_before_delete": validate_references_before_delete,
                    },
                    pipeline_update_params.PipelineUpdateParams,
                ),
            ),
            cast_to=Pipeline,
        )

    def list(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePipelineNoPaging:
        """
        Return all pipelines for the object type specified by `{objectType}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineNoPaging,
        )

    def delete(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        validate_deal_stage_usages_before_delete: bool | Omit = omit,
        validate_references_before_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "validate_deal_stage_usages_before_delete": validate_deal_stage_usages_before_delete,
                        "validate_references_before_delete": validate_references_before_delete,
                    },
                    pipeline_delete_params.PipelineDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Return a single pipeline object identified by its unique `{pipelineId}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def get_audit(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAuditInfoNoPaging:
        """
        Return a reverse chronological list of all mutations that have occurred on the
        pipeline identified by `{pipelineId}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    def replace(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        validate_deal_stage_usages_before_delete: bool | Omit = omit,
        validate_references_before_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Replace a pipeline

        Args:
          display_order: The order for displaying this pipeline. If two pipelines have a matching
              `displayOrder`, they will be sorted alphabetically by label.

          label: A unique label used to organize pipelines in HubSpot's UI

          stages: Pipeline stage inputs used to create the new or replacement pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._put(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_replace_params.PipelineReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "validate_deal_stage_usages_before_delete": validate_deal_stage_usages_before_delete,
                        "validate_references_before_delete": validate_references_before_delete,
                    },
                    pipeline_replace_params.PipelineReplaceParams,
                ),
            ),
            cast_to=Pipeline,
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def stages(self) -> AsyncStagesResource:
        return AsyncStagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPipelinesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: str,
        *,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """Create a new pipeline with the provided property values.

        The entire pipeline
        object, including its unique ID, will be returned in the response.

        Args:
          display_order: The order for displaying this pipeline. If two pipelines have a matching
              `displayOrder`, they will be sorted alphabetically by label.

          label: A unique label used to organize pipelines in HubSpot's UI

          stages: Pipeline stage inputs used to create the new or replacement pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm/v3/pipelines/{object_type}",
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def update(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        validate_deal_stage_usages_before_delete: bool | Omit = omit,
        validate_references_before_delete: bool | Omit = omit,
        archived: bool | Omit = omit,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """Perform a partial update of the pipeline identified by `{pipelineId}`.

        The
        updated pipeline will be returned in the response.

        Args:
          archived: Whether the pipeline is archived. This property should only be provided when
              restoring an archived pipeline. If it's provided in any other call, the request
              will fail and a `400 Bad Request` will be returned.

          display_order: The order for displaying this pipeline. If two pipelines have a matching
              `displayOrder`, they will be sorted alphabetically by label.

          label: A unique label used to organize pipelines in HubSpot's UI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._patch(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "validate_deal_stage_usages_before_delete": validate_deal_stage_usages_before_delete,
                        "validate_references_before_delete": validate_references_before_delete,
                    },
                    pipeline_update_params.PipelineUpdateParams,
                ),
            ),
            cast_to=Pipeline,
        )

    async def list(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePipelineNoPaging:
        """
        Return all pipelines for the object type specified by `{objectType}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineNoPaging,
        )

    async def delete(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        validate_deal_stage_usages_before_delete: bool | Omit = omit,
        validate_references_before_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "validate_deal_stage_usages_before_delete": validate_deal_stage_usages_before_delete,
                        "validate_references_before_delete": validate_references_before_delete,
                    },
                    pipeline_delete_params.PipelineDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Return a single pipeline object identified by its unique `{pipelineId}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def get_audit(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAuditInfoNoPaging:
        """
        Return a reverse chronological list of all mutations that have occurred on the
        pipeline identified by `{pipelineId}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    async def replace(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        validate_deal_stage_usages_before_delete: bool | Omit = omit,
        validate_references_before_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Replace a pipeline

        Args:
          display_order: The order for displaying this pipeline. If two pipelines have a matching
              `displayOrder`, they will be sorted alphabetically by label.

          label: A unique label used to organize pipelines in HubSpot's UI

          stages: Pipeline stage inputs used to create the new or replacement pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._put(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}",
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_replace_params.PipelineReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "validate_deal_stage_usages_before_delete": validate_deal_stage_usages_before_delete,
                        "validate_references_before_delete": validate_references_before_delete,
                    },
                    pipeline_replace_params.PipelineReplaceParams,
                ),
            ),
            cast_to=Pipeline,
        )


class PipelinesResourceWithRawResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_raw_response_wrapper(
            pipelines.create,
        )
        self.update = to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get = to_raw_response_wrapper(
            pipelines.get,
        )
        self.get_audit = to_raw_response_wrapper(
            pipelines.get_audit,
        )
        self.replace = to_raw_response_wrapper(
            pipelines.replace,
        )

    @cached_property
    def stages(self) -> StagesResourceWithRawResponse:
        return StagesResourceWithRawResponse(self._pipelines.stages)


class AsyncPipelinesResourceWithRawResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_raw_response_wrapper(
            pipelines.create,
        )
        self.update = async_to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pipelines.get,
        )
        self.get_audit = async_to_raw_response_wrapper(
            pipelines.get_audit,
        )
        self.replace = async_to_raw_response_wrapper(
            pipelines.replace,
        )

    @cached_property
    def stages(self) -> AsyncStagesResourceWithRawResponse:
        return AsyncStagesResourceWithRawResponse(self._pipelines.stages)


class PipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_streamed_response_wrapper(
            pipelines.create,
        )
        self.update = to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get = to_streamed_response_wrapper(
            pipelines.get,
        )
        self.get_audit = to_streamed_response_wrapper(
            pipelines.get_audit,
        )
        self.replace = to_streamed_response_wrapper(
            pipelines.replace,
        )

    @cached_property
    def stages(self) -> StagesResourceWithStreamingResponse:
        return StagesResourceWithStreamingResponse(self._pipelines.stages)


class AsyncPipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_streamed_response_wrapper(
            pipelines.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pipelines.get,
        )
        self.get_audit = async_to_streamed_response_wrapper(
            pipelines.get_audit,
        )
        self.replace = async_to_streamed_response_wrapper(
            pipelines.replace,
        )

    @cached_property
    def stages(self) -> AsyncStagesResourceWithStreamingResponse:
        return AsyncStagesResourceWithStreamingResponse(self._pipelines.stages)
