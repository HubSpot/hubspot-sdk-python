# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

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
from ...._base_client import make_request_options
from ....types.crm.pipelines import stage_create_params, stage_update_params, stage_replace_params
from ....types.crm.pipeline_stage import PipelineStage
from ....types.crm.collection_response_pipeline_stage_no_paging import CollectionResponsePipelineStageNoPaging
from ....types.crm.collection_response_public_audit_info_no_paging import CollectionResponsePublicAuditInfoNoPaging

__all__ = ["StagesResource", "AsyncStagesResource"]


class StagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return StagesResourceWithStreamingResponse(self)

    def create(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Create a new stage within the specified pipeline.

        Args:
          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          metadata: A JSON object containing properties that are not present on all object
              pipelines.

              For `deals` pipelines, the `probability` field is required
              (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
              Possible values are between 0.0 and 1.0 in increments of 0.1.

              For `tickets` pipelines, the `ticketState` field is optional
              (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
              has been closed by a member of your Support team. Possible values are `OPEN` or
              `CLOSED`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._post(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages",
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                stage_create_params.StageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def update(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        metadata: Dict[str, str],
        archived: bool | Omit = omit,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Perform a partial update on a specific stage of a pipeline.

        Args:
          metadata: A JSON object containing properties that are not present on all object
              pipelines.

              For `deals` pipelines, the `probability` field is required
              (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
              Possible values are between 0.0 and 1.0 in increments of 0.1.

              For `tickets` pipelines, the `ticketState` field is optional
              (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
              has been closed by a member of your Support team. Possible values are `OPEN` or
              `CLOSED`.

          archived: Whether the pipeline is archived.

          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._patch(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                },
                stage_update_params.StageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def list(
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
    ) -> CollectionResponsePipelineStageNoPaging:
        """
        Return all the stages associated with the pipeline identified by `{pipelineId}`.

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
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineStageNoPaging,
        )

    def delete(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific stage from a pipeline.

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
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Retrieve a specific stage from a pipeline using its ID.

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
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def get_audit(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAuditInfoNoPaging:
        """
        Return a reverse chronological list of all mutations that have occurred on the
        pipeline stage identified by `{stageId}`.

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
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    def replace(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Replace all the properties of an existing pipeline stage with the values
        provided. The updated stage will be returned in the response.

        Args:
          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          metadata: A JSON object containing properties that are not present on all object
              pipelines.

              For `deals` pipelines, the `probability` field is required
              (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
              Possible values are between 0.0 and 1.0 in increments of 0.1.

              For `tickets` pipelines, the `ticketState` field is optional
              (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
              has been closed by a member of your Support team. Possible values are `OPEN` or
              `CLOSED`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._put(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                stage_replace_params.StageReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )


class AsyncStagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncStagesResourceWithStreamingResponse(self)

    async def create(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Create a new stage within the specified pipeline.

        Args:
          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          metadata: A JSON object containing properties that are not present on all object
              pipelines.

              For `deals` pipelines, the `probability` field is required
              (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
              Possible values are between 0.0 and 1.0 in increments of 0.1.

              For `tickets` pipelines, the `ticketState` field is optional
              (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
              has been closed by a member of your Support team. Possible values are `OPEN` or
              `CLOSED`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._post(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages",
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                stage_create_params.StageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def update(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        metadata: Dict[str, str],
        archived: bool | Omit = omit,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Perform a partial update on a specific stage of a pipeline.

        Args:
          metadata: A JSON object containing properties that are not present on all object
              pipelines.

              For `deals` pipelines, the `probability` field is required
              (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
              Possible values are between 0.0 and 1.0 in increments of 0.1.

              For `tickets` pipelines, the `ticketState` field is optional
              (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
              has been closed by a member of your Support team. Possible values are `OPEN` or
              `CLOSED`.

          archived: Whether the pipeline is archived.

          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._patch(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                },
                stage_update_params.StageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def list(
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
    ) -> CollectionResponsePipelineStageNoPaging:
        """
        Return all the stages associated with the pipeline identified by `{pipelineId}`.

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
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineStageNoPaging,
        )

    async def delete(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific stage from a pipeline.

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
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Retrieve a specific stage from a pipeline using its ID.

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
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def get_audit(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAuditInfoNoPaging:
        """
        Return a reverse chronological list of all mutations that have occurred on the
        pipeline stage identified by `{stageId}`.

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
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    async def replace(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Replace all the properties of an existing pipeline stage with the values
        provided. The updated stage will be returned in the response.

        Args:
          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          metadata: A JSON object containing properties that are not present on all object
              pipelines.

              For `deals` pipelines, the `probability` field is required
              (`{ "probability": 0.5 }`), and represents the likelihood a deal will close.
              Possible values are between 0.0 and 1.0 in increments of 0.1.

              For `tickets` pipelines, the `ticketState` field is optional
              (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or
              has been closed by a member of your Support team. Possible values are `OPEN` or
              `CLOSED`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._put(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                stage_replace_params.StageReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )


class StagesResourceWithRawResponse:
    def __init__(self, stages: StagesResource) -> None:
        self._stages = stages

        self.create = to_raw_response_wrapper(
            stages.create,
        )
        self.update = to_raw_response_wrapper(
            stages.update,
        )
        self.list = to_raw_response_wrapper(
            stages.list,
        )
        self.delete = to_raw_response_wrapper(
            stages.delete,
        )
        self.get = to_raw_response_wrapper(
            stages.get,
        )
        self.get_audit = to_raw_response_wrapper(
            stages.get_audit,
        )
        self.replace = to_raw_response_wrapper(
            stages.replace,
        )


class AsyncStagesResourceWithRawResponse:
    def __init__(self, stages: AsyncStagesResource) -> None:
        self._stages = stages

        self.create = async_to_raw_response_wrapper(
            stages.create,
        )
        self.update = async_to_raw_response_wrapper(
            stages.update,
        )
        self.list = async_to_raw_response_wrapper(
            stages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            stages.delete,
        )
        self.get = async_to_raw_response_wrapper(
            stages.get,
        )
        self.get_audit = async_to_raw_response_wrapper(
            stages.get_audit,
        )
        self.replace = async_to_raw_response_wrapper(
            stages.replace,
        )


class StagesResourceWithStreamingResponse:
    def __init__(self, stages: StagesResource) -> None:
        self._stages = stages

        self.create = to_streamed_response_wrapper(
            stages.create,
        )
        self.update = to_streamed_response_wrapper(
            stages.update,
        )
        self.list = to_streamed_response_wrapper(
            stages.list,
        )
        self.delete = to_streamed_response_wrapper(
            stages.delete,
        )
        self.get = to_streamed_response_wrapper(
            stages.get,
        )
        self.get_audit = to_streamed_response_wrapper(
            stages.get_audit,
        )
        self.replace = to_streamed_response_wrapper(
            stages.replace,
        )


class AsyncStagesResourceWithStreamingResponse:
    def __init__(self, stages: AsyncStagesResource) -> None:
        self._stages = stages

        self.create = async_to_streamed_response_wrapper(
            stages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            stages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            stages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            stages.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            stages.get,
        )
        self.get_audit = async_to_streamed_response_wrapper(
            stages.get_audit,
        )
        self.replace = async_to_streamed_response_wrapper(
            stages.replace,
        )
