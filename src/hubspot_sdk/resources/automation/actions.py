# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.automation import (
    action_list_params,
    action_create_params,
    action_update_params,
    action_complete_params,
    action_complete_batch_params,
    action_create_or_replace_params,
    action_create_requires_object_params,
    action_create_or_replace_by_function_type_params,
)
from ...types.automation.public_action_function import PublicActionFunction
from ...types.automation.public_action_revision import PublicActionRevision
from ...types.automation.public_action_definition import PublicActionDefinition
from ...types.automation.public_action_labels_param import PublicActionLabelsParam
from ...types.automation.public_action_function_param import PublicActionFunctionParam
from ...types.automation.output_field_definition_param import OutputFieldDefinitionParam
from ...types.automation.public_action_function_identifier import PublicActionFunctionIdentifier
from ...types.automation.public_input_field_definition_param import PublicInputFieldDefinitionParam
from ...types.automation.public_object_request_options_param import PublicObjectRequestOptionsParam
from ...types.automation.callback_completion_batch_request_param import CallbackCompletionBatchRequestParam
from ...types.automation.public_execution_translation_rule_param import PublicExecutionTranslationRuleParam
from ...types.automation.public_action_definition_requires_object_response import (
    PublicActionDefinitionRequiresObjectResponse,
)

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        action_url: str,
        functions: Iterable[PublicActionFunctionParam],
        input_fields: Iterable[PublicInputFieldDefinitionParam],
        labels: Dict[str, PublicActionLabelsParam],
        object_types: SequenceNotStr[str],
        published: bool,
        archived_at: int | Omit = omit,
        execution_rules: Iterable[PublicExecutionTranslationRuleParam] | Omit = omit,
        input_field_dependencies: Iterable[action_create_params.InputFieldDependency] | Omit = omit,
        object_request_options: PublicObjectRequestOptionsParam | Omit = omit,
        output_fields: Iterable[OutputFieldDefinitionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/automation/actions/2026-03/{app_id}", app_id=app_id),
            body=maybe_transform(
                {
                    "action_url": action_url,
                    "functions": functions,
                    "input_fields": input_fields,
                    "labels": labels,
                    "object_types": object_types,
                    "published": published,
                    "archived_at": archived_at,
                    "execution_rules": execution_rules,
                    "input_field_dependencies": input_field_dependencies,
                    "object_request_options": object_request_options,
                    "output_fields": output_fields,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinition,
        )

    def update(
        self,
        definition_id: str,
        *,
        app_id: int,
        action_url: str | Omit = omit,
        execution_rules: Iterable[PublicExecutionTranslationRuleParam] | Omit = omit,
        input_field_dependencies: Iterable[action_update_params.InputFieldDependency] | Omit = omit,
        input_fields: Iterable[PublicInputFieldDefinitionParam] | Omit = omit,
        labels: Dict[str, PublicActionLabelsParam] | Omit = omit,
        object_request_options: PublicObjectRequestOptionsParam | Omit = omit,
        object_types: SequenceNotStr[str] | Omit = omit,
        output_fields: Iterable[OutputFieldDefinitionParam] | Omit = omit,
        published: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._patch(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}", app_id=app_id, definition_id=definition_id
            ),
            body=maybe_transform(
                {
                    "action_url": action_url,
                    "execution_rules": execution_rules,
                    "input_field_dependencies": input_field_dependencies,
                    "input_fields": input_fields,
                    "labels": labels,
                    "object_request_options": object_request_options,
                    "object_types": object_types,
                    "output_fields": output_fields,
                    "published": published,
                },
                action_update_params.ActionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinition,
        )

    def list(
        self,
        definition_id: str,
        *,
        app_id: int,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicActionRevision]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get_api_list(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions",
                app_id=app_id,
                definition_id=definition_id,
            ),
            page=SyncPage[PublicActionRevision],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            model=PublicActionRevision,
        )

    def delete(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
                function_id=function_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def complete(
        self,
        callback_id: str,
        *,
        output_fields: Dict[str, str],
        typed_outputs: object,
        failure_reason_type: str | Omit = omit,
        request_context: action_complete_params.RequestContext | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not callback_id:
            raise ValueError(f"Expected a non-empty value for `callback_id` but received {callback_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/automation/actions/callbacks/2026-03/{callback_id}/complete", callback_id=callback_id),
            body=maybe_transform(
                {
                    "output_fields": output_fields,
                    "typed_outputs": typed_outputs,
                    "failure_reason_type": failure_reason_type,
                    "request_context": request_context,
                },
                action_complete_params.ActionCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def complete_batch(
        self,
        *,
        inputs: Iterable[CallbackCompletionBatchRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/automation/actions/callbacks/2026-03/complete",
            body=maybe_transform({"inputs": inputs}, action_complete_batch_params.ActionCompleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_or_replace(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._put(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
                function_id=function_id,
            ),
            body=maybe_transform(body, action_create_or_replace_params.ActionCreateOrReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    def create_or_replace_by_function_type(
        self,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        *,
        app_id: int,
        definition_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return self._put(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
            ),
            body=maybe_transform(
                body, action_create_or_replace_by_function_type_params.ActionCreateOrReplaceByFunctionTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    def create_requires_object(
        self,
        definition_id: str,
        *,
        app_id: int,
        requires_object: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/requires-object",
                app_id=app_id,
                definition_id=definition_id,
            ),
            body=maybe_transform(
                {"requires_object": requires_object},
                action_create_requires_object_params.ActionCreateRequiresObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_function_type(
        self,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        revision_id: str,
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionRevision:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions/{revision_id}",
                app_id=app_id,
                definition_id=definition_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionRevision,
        )

    def get_by_function_type(
        self,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunction:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunction,
        )

    def get_requires_object(
        self,
        definition_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinitionRequiresObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/requires-object",
                app_id=app_id,
                definition_id=definition_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinitionRequiresObjectResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        action_url: str,
        functions: Iterable[PublicActionFunctionParam],
        input_fields: Iterable[PublicInputFieldDefinitionParam],
        labels: Dict[str, PublicActionLabelsParam],
        object_types: SequenceNotStr[str],
        published: bool,
        archived_at: int | Omit = omit,
        execution_rules: Iterable[PublicExecutionTranslationRuleParam] | Omit = omit,
        input_field_dependencies: Iterable[action_create_params.InputFieldDependency] | Omit = omit,
        object_request_options: PublicObjectRequestOptionsParam | Omit = omit,
        output_fields: Iterable[OutputFieldDefinitionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/automation/actions/2026-03/{app_id}", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "action_url": action_url,
                    "functions": functions,
                    "input_fields": input_fields,
                    "labels": labels,
                    "object_types": object_types,
                    "published": published,
                    "archived_at": archived_at,
                    "execution_rules": execution_rules,
                    "input_field_dependencies": input_field_dependencies,
                    "object_request_options": object_request_options,
                    "output_fields": output_fields,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinition,
        )

    async def update(
        self,
        definition_id: str,
        *,
        app_id: int,
        action_url: str | Omit = omit,
        execution_rules: Iterable[PublicExecutionTranslationRuleParam] | Omit = omit,
        input_field_dependencies: Iterable[action_update_params.InputFieldDependency] | Omit = omit,
        input_fields: Iterable[PublicInputFieldDefinitionParam] | Omit = omit,
        labels: Dict[str, PublicActionLabelsParam] | Omit = omit,
        object_request_options: PublicObjectRequestOptionsParam | Omit = omit,
        object_types: SequenceNotStr[str] | Omit = omit,
        output_fields: Iterable[OutputFieldDefinitionParam] | Omit = omit,
        published: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinition:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return await self._patch(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}", app_id=app_id, definition_id=definition_id
            ),
            body=await async_maybe_transform(
                {
                    "action_url": action_url,
                    "execution_rules": execution_rules,
                    "input_field_dependencies": input_field_dependencies,
                    "input_fields": input_fields,
                    "labels": labels,
                    "object_request_options": object_request_options,
                    "object_types": object_types,
                    "output_fields": output_fields,
                    "published": published,
                },
                action_update_params.ActionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinition,
        )

    def list(
        self,
        definition_id: str,
        *,
        app_id: int,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicActionRevision, AsyncPage[PublicActionRevision]]:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get_api_list(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions",
                app_id=app_id,
                definition_id=definition_id,
            ),
            page=AsyncPage[PublicActionRevision],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            model=PublicActionRevision,
        )

    async def delete(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
                function_id=function_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def complete(
        self,
        callback_id: str,
        *,
        output_fields: Dict[str, str],
        typed_outputs: object,
        failure_reason_type: str | Omit = omit,
        request_context: action_complete_params.RequestContext | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not callback_id:
            raise ValueError(f"Expected a non-empty value for `callback_id` but received {callback_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/automation/actions/callbacks/2026-03/{callback_id}/complete", callback_id=callback_id),
            body=await async_maybe_transform(
                {
                    "output_fields": output_fields,
                    "typed_outputs": typed_outputs,
                    "failure_reason_type": failure_reason_type,
                    "request_context": request_context,
                },
                action_complete_params.ActionCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def complete_batch(
        self,
        *,
        inputs: Iterable[CallbackCompletionBatchRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/automation/actions/callbacks/2026-03/complete",
            body=await async_maybe_transform(
                {"inputs": inputs}, action_complete_batch_params.ActionCompleteBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_or_replace(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._put(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
                function_id=function_id,
            ),
            body=await async_maybe_transform(body, action_create_or_replace_params.ActionCreateOrReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    async def create_or_replace_by_function_type(
        self,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        *,
        app_id: int,
        definition_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return await self._put(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
            ),
            body=await async_maybe_transform(
                body, action_create_or_replace_by_function_type_params.ActionCreateOrReplaceByFunctionTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    async def create_requires_object(
        self,
        definition_id: str,
        *,
        app_id: int,
        requires_object: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/requires-object",
                app_id=app_id,
                definition_id=definition_id,
            ),
            body=await async_maybe_transform(
                {"requires_object": requires_object},
                action_create_requires_object_params.ActionCreateRequiresObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_function_type(
        self,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        revision_id: str,
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionRevision:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/revisions/{revision_id}",
                app_id=app_id,
                definition_id=definition_id,
                revision_id=revision_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionRevision,
        )

    async def get_by_function_type(
        self,
        function_type: Literal[
            "POST_ACTION_EXECUTION", "POST_FETCH_OPTIONS", "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunction:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return await self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/functions/{function_type}",
                app_id=app_id,
                definition_id=definition_id,
                function_type=function_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunction,
        )

    async def get_requires_object(
        self,
        definition_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinitionRequiresObjectResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return await self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}/requires-object",
                app_id=app_id,
                definition_id=definition_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinitionRequiresObjectResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_raw_response_wrapper(
            actions.create,
        )
        self.update = to_raw_response_wrapper(
            actions.update,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )
        self.delete = to_raw_response_wrapper(
            actions.delete,
        )
        self.complete = to_raw_response_wrapper(
            actions.complete,
        )
        self.complete_batch = to_raw_response_wrapper(
            actions.complete_batch,
        )
        self.create_or_replace = to_raw_response_wrapper(
            actions.create_or_replace,
        )
        self.create_or_replace_by_function_type = to_raw_response_wrapper(
            actions.create_or_replace_by_function_type,
        )
        self.create_requires_object = to_raw_response_wrapper(
            actions.create_requires_object,
        )
        self.delete_by_function_type = to_raw_response_wrapper(
            actions.delete_by_function_type,
        )
        self.get = to_raw_response_wrapper(
            actions.get,
        )
        self.get_by_function_type = to_raw_response_wrapper(
            actions.get_by_function_type,
        )
        self.get_requires_object = to_raw_response_wrapper(
            actions.get_requires_object,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_raw_response_wrapper(
            actions.create,
        )
        self.update = async_to_raw_response_wrapper(
            actions.update,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            actions.delete,
        )
        self.complete = async_to_raw_response_wrapper(
            actions.complete,
        )
        self.complete_batch = async_to_raw_response_wrapper(
            actions.complete_batch,
        )
        self.create_or_replace = async_to_raw_response_wrapper(
            actions.create_or_replace,
        )
        self.create_or_replace_by_function_type = async_to_raw_response_wrapper(
            actions.create_or_replace_by_function_type,
        )
        self.create_requires_object = async_to_raw_response_wrapper(
            actions.create_requires_object,
        )
        self.delete_by_function_type = async_to_raw_response_wrapper(
            actions.delete_by_function_type,
        )
        self.get = async_to_raw_response_wrapper(
            actions.get,
        )
        self.get_by_function_type = async_to_raw_response_wrapper(
            actions.get_by_function_type,
        )
        self.get_requires_object = async_to_raw_response_wrapper(
            actions.get_requires_object,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_streamed_response_wrapper(
            actions.create,
        )
        self.update = to_streamed_response_wrapper(
            actions.update,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.delete = to_streamed_response_wrapper(
            actions.delete,
        )
        self.complete = to_streamed_response_wrapper(
            actions.complete,
        )
        self.complete_batch = to_streamed_response_wrapper(
            actions.complete_batch,
        )
        self.create_or_replace = to_streamed_response_wrapper(
            actions.create_or_replace,
        )
        self.create_or_replace_by_function_type = to_streamed_response_wrapper(
            actions.create_or_replace_by_function_type,
        )
        self.create_requires_object = to_streamed_response_wrapper(
            actions.create_requires_object,
        )
        self.delete_by_function_type = to_streamed_response_wrapper(
            actions.delete_by_function_type,
        )
        self.get = to_streamed_response_wrapper(
            actions.get,
        )
        self.get_by_function_type = to_streamed_response_wrapper(
            actions.get_by_function_type,
        )
        self.get_requires_object = to_streamed_response_wrapper(
            actions.get_requires_object,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_streamed_response_wrapper(
            actions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            actions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            actions.delete,
        )
        self.complete = async_to_streamed_response_wrapper(
            actions.complete,
        )
        self.complete_batch = async_to_streamed_response_wrapper(
            actions.complete_batch,
        )
        self.create_or_replace = async_to_streamed_response_wrapper(
            actions.create_or_replace,
        )
        self.create_or_replace_by_function_type = async_to_streamed_response_wrapper(
            actions.create_or_replace_by_function_type,
        )
        self.create_requires_object = async_to_streamed_response_wrapper(
            actions.create_requires_object,
        )
        self.delete_by_function_type = async_to_streamed_response_wrapper(
            actions.delete_by_function_type,
        )
        self.get = async_to_streamed_response_wrapper(
            actions.get,
        )
        self.get_by_function_type = async_to_streamed_response_wrapper(
            actions.get_by_function_type,
        )
        self.get_requires_object = async_to_streamed_response_wrapper(
            actions.get_requires_object,
        )
