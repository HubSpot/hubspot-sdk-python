# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

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
from ....types.crm.timeline import token_create_params, token_update_params
from ....types.crm.timeline_event_template_token import TimelineEventTemplateToken
from ....types.crm.timeline_event_template_token_option_param import TimelineEventTemplateTokenOptionParam

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TokensResourceWithStreamingResponse(self)

    def create(
        self,
        event_template_id: str,
        *,
        app_id: int,
        label: str,
        name: str,
        type: Literal["date", "enumeration", "number", "string"],
        created_at: Union[str, datetime] | Omit = omit,
        object_property_name: str | Omit = omit,
        options: Iterable[TimelineEventTemplateTokenOptionParam] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplateToken:
        """
        Update an existing event type template with new tokens.

        Args:
          label: Used for list segmentation and reporting.

          name: The name of the token referenced in the templates. This must be unique for the
              specific template. It may only contain alphanumeric characters, periods, dashes,
              or underscores (. - \\__).

          type: The data type of the token. You can currently choose from [string, number, date,
              enumeration].

          created_at: The date and time that the Event Template Token was created, as an ISO 8601
              timestamp. Will be null if the template was created before Feb 18th, 2020.

          object_property_name: The name of the CRM object property. This will populate the CRM object property
              associated with the event. With enough of these, you can fully build CRM objects
              via the Timeline API.

          options: If type is `enumeration`, we should have a list of options to choose from.

          updated_at: The date and time that the Event Template Token was last updated, as an ISO 8601
              timestamp. Will be null if the template was created before Feb 18th, 2020.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        return self._post(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}/tokens",
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "type": type,
                    "created_at": created_at,
                    "object_property_name": object_property_name,
                    "options": options,
                    "updated_at": updated_at,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplateToken,
        )

    def update(
        self,
        token_name: str,
        *,
        app_id: int,
        event_template_id: str,
        label: str,
        object_property_name: str | Omit = omit,
        options: Iterable[TimelineEventTemplateTokenOptionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplateToken:
        """
        Update an event type template token, specified by token name.

        Args:
          label: Used for list segmentation and reporting.

          object_property_name: The name of the CRM object property. This will populate the CRM object property
              associated with the event. With enough of these, you can fully build CRM objects
              via the Timeline API.

          options: If type is `enumeration`, we should have a list of options to choose from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not token_name:
            raise ValueError(f"Expected a non-empty value for `token_name` but received {token_name!r}")
        return self._put(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}/tokens/{token_name}",
            body=maybe_transform(
                {
                    "label": label,
                    "object_property_name": object_property_name,
                    "options": options,
                },
                token_update_params.TokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplateToken,
        )

    def delete(
        self,
        token_name: str,
        *,
        app_id: int,
        event_template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing token from a specific event type template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not token_name:
            raise ValueError(f"Expected a non-empty value for `token_name` but received {token_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}/tokens/{token_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        event_template_id: str,
        *,
        app_id: int,
        label: str,
        name: str,
        type: Literal["date", "enumeration", "number", "string"],
        created_at: Union[str, datetime] | Omit = omit,
        object_property_name: str | Omit = omit,
        options: Iterable[TimelineEventTemplateTokenOptionParam] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplateToken:
        """
        Update an existing event type template with new tokens.

        Args:
          label: Used for list segmentation and reporting.

          name: The name of the token referenced in the templates. This must be unique for the
              specific template. It may only contain alphanumeric characters, periods, dashes,
              or underscores (. - \\__).

          type: The data type of the token. You can currently choose from [string, number, date,
              enumeration].

          created_at: The date and time that the Event Template Token was created, as an ISO 8601
              timestamp. Will be null if the template was created before Feb 18th, 2020.

          object_property_name: The name of the CRM object property. This will populate the CRM object property
              associated with the event. With enough of these, you can fully build CRM objects
              via the Timeline API.

          options: If type is `enumeration`, we should have a list of options to choose from.

          updated_at: The date and time that the Event Template Token was last updated, as an ISO 8601
              timestamp. Will be null if the template was created before Feb 18th, 2020.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        return await self._post(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}/tokens",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "type": type,
                    "created_at": created_at,
                    "object_property_name": object_property_name,
                    "options": options,
                    "updated_at": updated_at,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplateToken,
        )

    async def update(
        self,
        token_name: str,
        *,
        app_id: int,
        event_template_id: str,
        label: str,
        object_property_name: str | Omit = omit,
        options: Iterable[TimelineEventTemplateTokenOptionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplateToken:
        """
        Update an event type template token, specified by token name.

        Args:
          label: Used for list segmentation and reporting.

          object_property_name: The name of the CRM object property. This will populate the CRM object property
              associated with the event. With enough of these, you can fully build CRM objects
              via the Timeline API.

          options: If type is `enumeration`, we should have a list of options to choose from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not token_name:
            raise ValueError(f"Expected a non-empty value for `token_name` but received {token_name!r}")
        return await self._put(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}/tokens/{token_name}",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "object_property_name": object_property_name,
                    "options": options,
                },
                token_update_params.TokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplateToken,
        )

    async def delete(
        self,
        token_name: str,
        *,
        app_id: int,
        event_template_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing token from a specific event type template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        if not token_name:
            raise ValueError(f"Expected a non-empty value for `token_name` but received {token_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}/tokens/{token_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.create = to_raw_response_wrapper(
            tokens.create,
        )
        self.update = to_raw_response_wrapper(
            tokens.update,
        )
        self.delete = to_raw_response_wrapper(
            tokens.delete,
        )


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.create = async_to_raw_response_wrapper(
            tokens.create,
        )
        self.update = async_to_raw_response_wrapper(
            tokens.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tokens.delete,
        )


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.create = to_streamed_response_wrapper(
            tokens.create,
        )
        self.update = to_streamed_response_wrapper(
            tokens.update,
        )
        self.delete = to_streamed_response_wrapper(
            tokens.delete,
        )


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.create = async_to_streamed_response_wrapper(
            tokens.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tokens.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tokens.delete,
        )
