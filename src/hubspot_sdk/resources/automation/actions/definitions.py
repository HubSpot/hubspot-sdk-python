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
from ....types.automation.actions import (
    definition_get_params,
    definition_list_params,
    definition_create_params,
    definition_update_params,
    definition_create_requires_object_params,
)
from ....types.automation.public_action_definition import PublicActionDefinition
from ....types.automation.public_action_labels_param import PublicActionLabelsParam
from ....types.automation.public_action_function_param import PublicActionFunctionParam
from ....types.automation.output_field_definition_param import OutputFieldDefinitionParam
from ....types.automation.public_input_field_definition_param import PublicInputFieldDefinitionParam
from ....types.automation.public_object_request_options_param import PublicObjectRequestOptionsParam
from ....types.automation.public_execution_translation_rule_param import PublicExecutionTranslationRuleParam
from ....types.automation.public_action_definition_requires_object_response import (
    PublicActionDefinitionRequiresObjectResponse,
)

__all__ = ["DefinitionsResource", "AsyncDefinitionsResource"]


class DefinitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return DefinitionsResourceWithStreamingResponse(self)

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
        input_field_dependencies: Iterable[definition_create_params.InputFieldDependency] | Omit = omit,
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
        Create a new custom workflow action.

        Args:
          action_url: The URL endpoint where the action is executed.

          labels: Holds various labels associated with the action, including names and
              descriptions.

          published: Indicates whether the action is published and available for use.

          archived_at: The timestamp indicating when the action was archived.

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
                definition_create_params.DefinitionCreateParams,
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
        input_field_dependencies: Iterable[definition_update_params.InputFieldDependency] | Omit = omit,
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
        Update an existing action definition by ID.

        Args:
          action_url: The URL endpoint where the action is executed.

          labels: Contains labels for the action, including names and descriptions.

          published: Indicates whether the action is published and available for use.

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
                definition_update_params.DefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinition,
        )

    def list(
        self,
        app_id: int,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicActionDefinition]:
        """
        Retrieve custom workflow action definitions by app ID.

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
        return self._get_api_list(
            path_template("/automation/actions/2026-03/{app_id}", app_id=app_id),
            page=SyncPage[PublicActionDefinition],
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
                    },
                    definition_list_params.DefinitionListParams,
                ),
            ),
            model=PublicActionDefinition,
        )

    def delete(
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
    ) -> None:
        """
        Delete an action definition by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}", app_id=app_id, definition_id=definition_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Set whether a custom action definition requires an object.

        Args:
          requires_object: Indicates whether a custom action definition requires an associated object.

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
                definition_create_requires_object_params.DefinitionCreateRequiresObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        definition_id: str,
        *,
        app_id: int,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinition:
        """
        Retrieve a custom workflow action definition by ID.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}", app_id=app_id, definition_id=definition_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, definition_get_params.DefinitionGetParams),
            ),
            cast_to=PublicActionDefinition,
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
        Retrieve whether a custom action definition requires an object.

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


class AsyncDefinitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDefinitionsResourceWithStreamingResponse(self)

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
        input_field_dependencies: Iterable[definition_create_params.InputFieldDependency] | Omit = omit,
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
        Create a new custom workflow action.

        Args:
          action_url: The URL endpoint where the action is executed.

          labels: Holds various labels associated with the action, including names and
              descriptions.

          published: Indicates whether the action is published and available for use.

          archived_at: The timestamp indicating when the action was archived.

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
                definition_create_params.DefinitionCreateParams,
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
        input_field_dependencies: Iterable[definition_update_params.InputFieldDependency] | Omit = omit,
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
        Update an existing action definition by ID.

        Args:
          action_url: The URL endpoint where the action is executed.

          labels: Contains labels for the action, including names and descriptions.

          published: Indicates whether the action is published and available for use.

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
                definition_update_params.DefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionDefinition,
        )

    def list(
        self,
        app_id: int,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicActionDefinition, AsyncPage[PublicActionDefinition]]:
        """
        Retrieve custom workflow action definitions by app ID.

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
        return self._get_api_list(
            path_template("/automation/actions/2026-03/{app_id}", app_id=app_id),
            page=AsyncPage[PublicActionDefinition],
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
                    },
                    definition_list_params.DefinitionListParams,
                ),
            ),
            model=PublicActionDefinition,
        )

    async def delete(
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
    ) -> None:
        """
        Delete an action definition by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}", app_id=app_id, definition_id=definition_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Set whether a custom action definition requires an object.

        Args:
          requires_object: Indicates whether a custom action definition requires an associated object.

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
                definition_create_requires_object_params.DefinitionCreateRequiresObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        definition_id: str,
        *,
        app_id: int,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionDefinition:
        """
        Retrieve a custom workflow action definition by ID.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return await self._get(
            path_template(
                "/automation/actions/2026-03/{app_id}/{definition_id}", app_id=app_id, definition_id=definition_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, definition_get_params.DefinitionGetParams),
            ),
            cast_to=PublicActionDefinition,
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
        Retrieve whether a custom action definition requires an object.

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


class DefinitionsResourceWithRawResponse:
    def __init__(self, definitions: DefinitionsResource) -> None:
        self._definitions = definitions

        self.create = to_raw_response_wrapper(
            definitions.create,
        )
        self.update = to_raw_response_wrapper(
            definitions.update,
        )
        self.list = to_raw_response_wrapper(
            definitions.list,
        )
        self.delete = to_raw_response_wrapper(
            definitions.delete,
        )
        self.create_requires_object = to_raw_response_wrapper(
            definitions.create_requires_object,
        )
        self.get = to_raw_response_wrapper(
            definitions.get,
        )
        self.get_requires_object = to_raw_response_wrapper(
            definitions.get_requires_object,
        )


class AsyncDefinitionsResourceWithRawResponse:
    def __init__(self, definitions: AsyncDefinitionsResource) -> None:
        self._definitions = definitions

        self.create = async_to_raw_response_wrapper(
            definitions.create,
        )
        self.update = async_to_raw_response_wrapper(
            definitions.update,
        )
        self.list = async_to_raw_response_wrapper(
            definitions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            definitions.delete,
        )
        self.create_requires_object = async_to_raw_response_wrapper(
            definitions.create_requires_object,
        )
        self.get = async_to_raw_response_wrapper(
            definitions.get,
        )
        self.get_requires_object = async_to_raw_response_wrapper(
            definitions.get_requires_object,
        )


class DefinitionsResourceWithStreamingResponse:
    def __init__(self, definitions: DefinitionsResource) -> None:
        self._definitions = definitions

        self.create = to_streamed_response_wrapper(
            definitions.create,
        )
        self.update = to_streamed_response_wrapper(
            definitions.update,
        )
        self.list = to_streamed_response_wrapper(
            definitions.list,
        )
        self.delete = to_streamed_response_wrapper(
            definitions.delete,
        )
        self.create_requires_object = to_streamed_response_wrapper(
            definitions.create_requires_object,
        )
        self.get = to_streamed_response_wrapper(
            definitions.get,
        )
        self.get_requires_object = to_streamed_response_wrapper(
            definitions.get_requires_object,
        )


class AsyncDefinitionsResourceWithStreamingResponse:
    def __init__(self, definitions: AsyncDefinitionsResource) -> None:
        self._definitions = definitions

        self.create = async_to_streamed_response_wrapper(
            definitions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            definitions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            definitions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            definitions.delete,
        )
        self.create_requires_object = async_to_streamed_response_wrapper(
            definitions.create_requires_object,
        )
        self.get = async_to_streamed_response_wrapper(
            definitions.get,
        )
        self.get_requires_object = async_to_streamed_response_wrapper(
            definitions.get_requires_object,
        )
