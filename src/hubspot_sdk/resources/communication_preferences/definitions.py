# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.communication_preferences import definition_list_params
from ...types.communication_preferences.action_response_with_results_subscription_definition import (
    ActionResponseWithResultsSubscriptionDefinition,
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

    def list(
        self,
        *,
        business_unit_id: int | Omit = omit,
        include_translations: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsSubscriptionDefinition:
        """
        Get a list of subscription status definitions from the account.

        Args:
          business_unit_id: An integer representing the ID of the business unit for which to retrieve
              subscription definitions.

          include_translations: A boolean indicating whether to include translations of the communication
              preferences definitions in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/communication-preferences/2026-03/definitions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "business_unit_id": business_unit_id,
                        "include_translations": include_translations,
                    },
                    definition_list_params.DefinitionListParams,
                ),
            ),
            cast_to=ActionResponseWithResultsSubscriptionDefinition,
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

    async def list(
        self,
        *,
        business_unit_id: int | Omit = omit,
        include_translations: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsSubscriptionDefinition:
        """
        Get a list of subscription status definitions from the account.

        Args:
          business_unit_id: An integer representing the ID of the business unit for which to retrieve
              subscription definitions.

          include_translations: A boolean indicating whether to include translations of the communication
              preferences definitions in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/communication-preferences/2026-03/definitions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "business_unit_id": business_unit_id,
                        "include_translations": include_translations,
                    },
                    definition_list_params.DefinitionListParams,
                ),
            ),
            cast_to=ActionResponseWithResultsSubscriptionDefinition,
        )


class DefinitionsResourceWithRawResponse:
    def __init__(self, definitions: DefinitionsResource) -> None:
        self._definitions = definitions

        self.list = to_raw_response_wrapper(
            definitions.list,
        )


class AsyncDefinitionsResourceWithRawResponse:
    def __init__(self, definitions: AsyncDefinitionsResource) -> None:
        self._definitions = definitions

        self.list = async_to_raw_response_wrapper(
            definitions.list,
        )


class DefinitionsResourceWithStreamingResponse:
    def __init__(self, definitions: DefinitionsResource) -> None:
        self._definitions = definitions

        self.list = to_streamed_response_wrapper(
            definitions.list,
        )


class AsyncDefinitionsResourceWithStreamingResponse:
    def __init__(self, definitions: AsyncDefinitionsResource) -> None:
        self._definitions = definitions

        self.list = async_to_streamed_response_wrapper(
            definitions.list,
        )
