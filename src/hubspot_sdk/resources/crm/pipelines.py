# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import (
    pipeline_create_params,
    pipeline_delete_params,
    pipeline_update_params,
    pipeline_create_stage_params,
    pipeline_update_stage_params,
    pipeline_update_all_properties_params,
    pipeline_update_stage_all_properties_params,
)
from ..._base_client import make_request_options
from ...types.crm.pipeline import Pipeline
from ...types.crm.pipeline_stage import PipelineStage
from ...types.crm.pipeline_stage_input_param import PipelineStageInputParam
from ...types.crm.collection_response_pipeline_no_paging import CollectionResponsePipelineNoPaging
from ...types.crm.collection_response_pipeline_stage_no_paging import CollectionResponsePipelineStageNoPaging
from ...types.crm.collection_response_public_audit_info_no_paging import CollectionResponsePublicAuditInfoNoPaging

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return PipelinesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: str,
        *,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        pipeline_id: str | Omit = omit,
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
            path_template("/crm/pipelines/2026-03/{object_type}", object_type=object_type),
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                    "pipeline_id": pipeline_id,
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
            ),
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
            path_template("/crm/pipelines/2026-03/{object_type}", object_type=object_type),
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
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
                    pipeline_delete_params.PipelineDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def create_stage(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str],
        stage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Create a pipeline stage

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages",
                object_type=object_type,
                pipeline_id=pipeline_id,
            ),
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                    "stage_id": stage_id,
                },
                pipeline_create_stage_params.PipelineCreateStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def delete_stage(
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
        Delete a pipeline stage

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def get_stage(
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
        Return a pipeline stage by ID

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def list_audit(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/audit",
                object_type=object_type,
                pipeline_id=pipeline_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    def list_stage_audit(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}/audit",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    def list_stages(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages",
                object_type=object_type,
                pipeline_id=pipeline_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineStageNoPaging,
        )

    def update_all_properties(
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
          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          stages: The stages associated with the pipeline. They can be retrieved and updated via
              the pipeline stages endpoints.

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
            ),
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_update_all_properties_params.PipelineUpdateAllPropertiesParams,
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
                    pipeline_update_all_properties_params.PipelineUpdateAllPropertiesParams,
                ),
            ),
            cast_to=Pipeline,
        )

    def update_stage(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                },
                pipeline_update_stage_params.PipelineUpdateStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def update_stage_all_properties(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                pipeline_update_stage_all_properties_params.PipelineUpdateStageAllPropertiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPipelinesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: str,
        *,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        pipeline_id: str | Omit = omit,
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
            path_template("/crm/pipelines/2026-03/{object_type}", object_type=object_type),
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                    "pipeline_id": pipeline_id,
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
            ),
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
            path_template("/crm/pipelines/2026-03/{object_type}", object_type=object_type),
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
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
                    pipeline_delete_params.PipelineDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def create_stage(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str],
        stage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Create a pipeline stage

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages",
                object_type=object_type,
                pipeline_id=pipeline_id,
            ),
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                    "stage_id": stage_id,
                },
                pipeline_create_stage_params.PipelineCreateStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def delete_stage(
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
        Delete a pipeline stage

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def get_stage(
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
        Return a pipeline stage by ID

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def list_audit(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/audit",
                object_type=object_type,
                pipeline_id=pipeline_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    async def list_stage_audit(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}/audit",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    async def list_stages(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages",
                object_type=object_type,
                pipeline_id=pipeline_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineStageNoPaging,
        )

    async def update_all_properties(
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
          display_order: The order for displaying this pipeline stage. If two pipeline stages have a
              matching `displayOrder`, they will be sorted alphabetically by label.

          label: A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's
              label must be unique within that pipeline.

          stages: The stages associated with the pipeline. They can be retrieved and updated via
              the pipeline stages endpoints.

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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}", object_type=object_type, pipeline_id=pipeline_id
            ),
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_update_all_properties_params.PipelineUpdateAllPropertiesParams,
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
                    pipeline_update_all_properties_params.PipelineUpdateAllPropertiesParams,
                ),
            ),
            cast_to=Pipeline,
        )

    async def update_stage(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                },
                pipeline_update_stage_params.PipelineUpdateStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def update_stage_all_properties(
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
            path_template(
                "/crm/pipelines/2026-03/{object_type}/{pipeline_id}/stages/{stage_id}",
                object_type=object_type,
                pipeline_id=pipeline_id,
                stage_id=stage_id,
            ),
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                pipeline_update_stage_all_properties_params.PipelineUpdateStageAllPropertiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
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
        self.create_stage = to_raw_response_wrapper(
            pipelines.create_stage,
        )
        self.delete_stage = to_raw_response_wrapper(
            pipelines.delete_stage,
        )
        self.get = to_raw_response_wrapper(
            pipelines.get,
        )
        self.get_stage = to_raw_response_wrapper(
            pipelines.get_stage,
        )
        self.list_audit = to_raw_response_wrapper(
            pipelines.list_audit,
        )
        self.list_stage_audit = to_raw_response_wrapper(
            pipelines.list_stage_audit,
        )
        self.list_stages = to_raw_response_wrapper(
            pipelines.list_stages,
        )
        self.update_all_properties = to_raw_response_wrapper(
            pipelines.update_all_properties,
        )
        self.update_stage = to_raw_response_wrapper(
            pipelines.update_stage,
        )
        self.update_stage_all_properties = to_raw_response_wrapper(
            pipelines.update_stage_all_properties,
        )


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
        self.create_stage = async_to_raw_response_wrapper(
            pipelines.create_stage,
        )
        self.delete_stage = async_to_raw_response_wrapper(
            pipelines.delete_stage,
        )
        self.get = async_to_raw_response_wrapper(
            pipelines.get,
        )
        self.get_stage = async_to_raw_response_wrapper(
            pipelines.get_stage,
        )
        self.list_audit = async_to_raw_response_wrapper(
            pipelines.list_audit,
        )
        self.list_stage_audit = async_to_raw_response_wrapper(
            pipelines.list_stage_audit,
        )
        self.list_stages = async_to_raw_response_wrapper(
            pipelines.list_stages,
        )
        self.update_all_properties = async_to_raw_response_wrapper(
            pipelines.update_all_properties,
        )
        self.update_stage = async_to_raw_response_wrapper(
            pipelines.update_stage,
        )
        self.update_stage_all_properties = async_to_raw_response_wrapper(
            pipelines.update_stage_all_properties,
        )


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
        self.create_stage = to_streamed_response_wrapper(
            pipelines.create_stage,
        )
        self.delete_stage = to_streamed_response_wrapper(
            pipelines.delete_stage,
        )
        self.get = to_streamed_response_wrapper(
            pipelines.get,
        )
        self.get_stage = to_streamed_response_wrapper(
            pipelines.get_stage,
        )
        self.list_audit = to_streamed_response_wrapper(
            pipelines.list_audit,
        )
        self.list_stage_audit = to_streamed_response_wrapper(
            pipelines.list_stage_audit,
        )
        self.list_stages = to_streamed_response_wrapper(
            pipelines.list_stages,
        )
        self.update_all_properties = to_streamed_response_wrapper(
            pipelines.update_all_properties,
        )
        self.update_stage = to_streamed_response_wrapper(
            pipelines.update_stage,
        )
        self.update_stage_all_properties = to_streamed_response_wrapper(
            pipelines.update_stage_all_properties,
        )


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
        self.create_stage = async_to_streamed_response_wrapper(
            pipelines.create_stage,
        )
        self.delete_stage = async_to_streamed_response_wrapper(
            pipelines.delete_stage,
        )
        self.get = async_to_streamed_response_wrapper(
            pipelines.get,
        )
        self.get_stage = async_to_streamed_response_wrapper(
            pipelines.get_stage,
        )
        self.list_audit = async_to_streamed_response_wrapper(
            pipelines.list_audit,
        )
        self.list_stage_audit = async_to_streamed_response_wrapper(
            pipelines.list_stage_audit,
        )
        self.list_stages = async_to_streamed_response_wrapper(
            pipelines.list_stages,
        )
        self.update_all_properties = async_to_streamed_response_wrapper(
            pipelines.update_all_properties,
        )
        self.update_stage = async_to_streamed_response_wrapper(
            pipelines.update_stage,
        )
        self.update_stage_all_properties = async_to_streamed_response_wrapper(
            pipelines.update_stage_all_properties,
        )
