# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .definitions import (
    DefinitionsResource,
    AsyncDefinitionsResource,
    DefinitionsResourceWithRawResponse,
    AsyncDefinitionsResourceWithRawResponse,
    DefinitionsResourceWithStreamingResponse,
    AsyncDefinitionsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .statuses.statuses import (
    StatusesResource,
    AsyncStatusesResource,
    StatusesResourceWithRawResponse,
    AsyncStatusesResourceWithRawResponse,
    StatusesResourceWithStreamingResponse,
    AsyncStatusesResourceWithStreamingResponse,
)
from ...types.communication_preferences import (
    communication_preference_get_statuses_params,
    communication_preference_update_status_params,
    communication_preference_generate_links_params,
    communication_preference_unsubscribe_all_params,
    communication_preference_get_unsubscribe_all_status_params,
)
from ...types.communication_preferences.link_generation_response import LinkGenerationResponse
from ...types.communication_preferences.action_response_with_results_public_status import (
    ActionResponseWithResultsPublicStatus,
)
from ...types.communication_preferences.action_response_with_results_public_wide_status import (
    ActionResponseWithResultsPublicWideStatus,
)

__all__ = ["CommunicationPreferencesResource", "AsyncCommunicationPreferencesResource"]


class CommunicationPreferencesResource(SyncAPIResource):
    @cached_property
    def definitions(self) -> DefinitionsResource:
        return DefinitionsResource(self._client)

    @cached_property
    def statuses(self) -> StatusesResource:
        return StatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommunicationPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommunicationPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunicationPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CommunicationPreferencesResourceWithStreamingResponse(self)

    def generate_links(
        self,
        *,
        channel: Literal["EMAIL"],
        subscriber_id_string: str,
        business_unit_id: int | Omit = omit,
        language: str | Omit = omit,
        subscription_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkGenerationResponse:
        """Generate communication preference links for a subscriber.

        This endpoint allows
        you to create URLs for managing preferences and unsubscribing, tailored to a
        specific subscriber. It is useful for integrating communication preference
        management into your applications.

        Args:
          subscriber_id_string: A string representing the unique identifier of the subscriber. This property is
              required.

          language: The language in which the generated link should be presented, represented as a
              string.

          subscription_id: The unique identifier for the subscription, represented as an integer in int64
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/2026-03/links/generate",
            body=maybe_transform(
                {
                    "subscriber_id_string": subscriber_id_string,
                    "language": language,
                    "subscription_id": subscription_id,
                },
                communication_preference_generate_links_params.CommunicationPreferenceGenerateLinksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    communication_preference_generate_links_params.CommunicationPreferenceGenerateLinksParams,
                ),
            ),
            cast_to=LinkGenerationResponse,
        )

    def get_statuses(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Retrieve a contact's current email subscription preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._get(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}",
                subscriber_id_string=subscriber_id_string,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    communication_preference_get_statuses_params.CommunicationPreferenceGetStatusesParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    def get_unsubscribe_all_status(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicWideStatus:
        """Check whether a contact has unsubscribed from all email subscriptions.

        If a
        contact has not opted out of all communications, the response `results` array
        will be empty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._get(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}/unsubscribe-all",
                subscriber_id_string=subscriber_id_string,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    communication_preference_get_unsubscribe_all_status_params.CommunicationPreferenceGetUnsubscribeAllStatusParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicWideStatus,
        )

    def unsubscribe_all(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Unsubscribe a contact from all email subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._post(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}/unsubscribe-all",
                subscriber_id_string=subscriber_id_string,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    communication_preference_unsubscribe_all_params.CommunicationPreferenceUnsubscribeAllParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    def update_status(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        status_state: Literal["NOT_SPECIFIED", "SUBSCRIBED", "UNSUBSCRIBED"],
        subscription_id: int,
        legal_basis: Literal[
            "CONSENT_WITH_NOTICE",
            "LEGITIMATE_INTEREST_CLIENT",
            "LEGITIMATE_INTEREST_OTHER",
            "LEGITIMATE_INTEREST_PQL",
            "NON_GDPR",
            "PERFORMANCE_OF_CONTRACT",
            "PROCESS_AND_STORE",
        ]
        | Omit = omit,
        legal_basis_explanation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Set the subscription status of a specific contact.

        Args:
          channel: The type of communication channel, with 'EMAIL' as the only supported option.

          status_state: The current subscription status of the contact, which can be 'SUBSCRIBED',
              'UNSUBSCRIBED', or 'NOT_SPECIFIED'.

          subscription_id: The unique identifier of the subscription to be updated.

          legal_basis: The legal basis for communication, with options including
              'LEGITIMATE_INTEREST_PQL', 'LEGITIMATE_INTEREST_CLIENT',
              'PERFORMANCE_OF_CONTRACT', 'CONSENT_WITH_NOTICE', 'NON_GDPR',
              'PROCESS_AND_STORE', and 'LEGITIMATE_INTEREST_OTHER'.

          legal_basis_explanation: An explanation for the legal basis used for communication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._post(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}",
                subscriber_id_string=subscriber_id_string,
            ),
            body=maybe_transform(
                {
                    "channel": channel,
                    "status_state": status_state,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                communication_preference_update_status_params.CommunicationPreferenceUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )


class AsyncCommunicationPreferencesResource(AsyncAPIResource):
    @cached_property
    def definitions(self) -> AsyncDefinitionsResource:
        return AsyncDefinitionsResource(self._client)

    @cached_property
    def statuses(self) -> AsyncStatusesResource:
        return AsyncStatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommunicationPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommunicationPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunicationPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCommunicationPreferencesResourceWithStreamingResponse(self)

    async def generate_links(
        self,
        *,
        channel: Literal["EMAIL"],
        subscriber_id_string: str,
        business_unit_id: int | Omit = omit,
        language: str | Omit = omit,
        subscription_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkGenerationResponse:
        """Generate communication preference links for a subscriber.

        This endpoint allows
        you to create URLs for managing preferences and unsubscribing, tailored to a
        specific subscriber. It is useful for integrating communication preference
        management into your applications.

        Args:
          subscriber_id_string: A string representing the unique identifier of the subscriber. This property is
              required.

          language: The language in which the generated link should be presented, represented as a
              string.

          subscription_id: The unique identifier for the subscription, represented as an integer in int64
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/2026-03/links/generate",
            body=await async_maybe_transform(
                {
                    "subscriber_id_string": subscriber_id_string,
                    "language": language,
                    "subscription_id": subscription_id,
                },
                communication_preference_generate_links_params.CommunicationPreferenceGenerateLinksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    communication_preference_generate_links_params.CommunicationPreferenceGenerateLinksParams,
                ),
            ),
            cast_to=LinkGenerationResponse,
        )

    async def get_statuses(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Retrieve a contact's current email subscription preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._get(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}",
                subscriber_id_string=subscriber_id_string,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    communication_preference_get_statuses_params.CommunicationPreferenceGetStatusesParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    async def get_unsubscribe_all_status(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicWideStatus:
        """Check whether a contact has unsubscribed from all email subscriptions.

        If a
        contact has not opted out of all communications, the response `results` array
        will be empty.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._get(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}/unsubscribe-all",
                subscriber_id_string=subscriber_id_string,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    communication_preference_get_unsubscribe_all_status_params.CommunicationPreferenceGetUnsubscribeAllStatusParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicWideStatus,
        )

    async def unsubscribe_all(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Unsubscribe a contact from all email subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._post(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}/unsubscribe-all",
                subscriber_id_string=subscriber_id_string,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    communication_preference_unsubscribe_all_params.CommunicationPreferenceUnsubscribeAllParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    async def update_status(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        status_state: Literal["NOT_SPECIFIED", "SUBSCRIBED", "UNSUBSCRIBED"],
        subscription_id: int,
        legal_basis: Literal[
            "CONSENT_WITH_NOTICE",
            "LEGITIMATE_INTEREST_CLIENT",
            "LEGITIMATE_INTEREST_OTHER",
            "LEGITIMATE_INTEREST_PQL",
            "NON_GDPR",
            "PERFORMANCE_OF_CONTRACT",
            "PROCESS_AND_STORE",
        ]
        | Omit = omit,
        legal_basis_explanation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Set the subscription status of a specific contact.

        Args:
          channel: The type of communication channel, with 'EMAIL' as the only supported option.

          status_state: The current subscription status of the contact, which can be 'SUBSCRIBED',
              'UNSUBSCRIBED', or 'NOT_SPECIFIED'.

          subscription_id: The unique identifier of the subscription to be updated.

          legal_basis: The legal basis for communication, with options including
              'LEGITIMATE_INTEREST_PQL', 'LEGITIMATE_INTEREST_CLIENT',
              'PERFORMANCE_OF_CONTRACT', 'CONSENT_WITH_NOTICE', 'NON_GDPR',
              'PROCESS_AND_STORE', and 'LEGITIMATE_INTEREST_OTHER'.

          legal_basis_explanation: An explanation for the legal basis used for communication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._post(
            path_template(
                "/communication-preferences/2026-03/statuses/{subscriber_id_string}",
                subscriber_id_string=subscriber_id_string,
            ),
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "status_state": status_state,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                communication_preference_update_status_params.CommunicationPreferenceUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )


class CommunicationPreferencesResourceWithRawResponse:
    def __init__(self, communication_preferences: CommunicationPreferencesResource) -> None:
        self._communication_preferences = communication_preferences

        self.generate_links = to_raw_response_wrapper(
            communication_preferences.generate_links,
        )
        self.get_statuses = to_raw_response_wrapper(
            communication_preferences.get_statuses,
        )
        self.get_unsubscribe_all_status = to_raw_response_wrapper(
            communication_preferences.get_unsubscribe_all_status,
        )
        self.unsubscribe_all = to_raw_response_wrapper(
            communication_preferences.unsubscribe_all,
        )
        self.update_status = to_raw_response_wrapper(
            communication_preferences.update_status,
        )

    @cached_property
    def definitions(self) -> DefinitionsResourceWithRawResponse:
        return DefinitionsResourceWithRawResponse(self._communication_preferences.definitions)

    @cached_property
    def statuses(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self._communication_preferences.statuses)


class AsyncCommunicationPreferencesResourceWithRawResponse:
    def __init__(self, communication_preferences: AsyncCommunicationPreferencesResource) -> None:
        self._communication_preferences = communication_preferences

        self.generate_links = async_to_raw_response_wrapper(
            communication_preferences.generate_links,
        )
        self.get_statuses = async_to_raw_response_wrapper(
            communication_preferences.get_statuses,
        )
        self.get_unsubscribe_all_status = async_to_raw_response_wrapper(
            communication_preferences.get_unsubscribe_all_status,
        )
        self.unsubscribe_all = async_to_raw_response_wrapper(
            communication_preferences.unsubscribe_all,
        )
        self.update_status = async_to_raw_response_wrapper(
            communication_preferences.update_status,
        )

    @cached_property
    def definitions(self) -> AsyncDefinitionsResourceWithRawResponse:
        return AsyncDefinitionsResourceWithRawResponse(self._communication_preferences.definitions)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self._communication_preferences.statuses)


class CommunicationPreferencesResourceWithStreamingResponse:
    def __init__(self, communication_preferences: CommunicationPreferencesResource) -> None:
        self._communication_preferences = communication_preferences

        self.generate_links = to_streamed_response_wrapper(
            communication_preferences.generate_links,
        )
        self.get_statuses = to_streamed_response_wrapper(
            communication_preferences.get_statuses,
        )
        self.get_unsubscribe_all_status = to_streamed_response_wrapper(
            communication_preferences.get_unsubscribe_all_status,
        )
        self.unsubscribe_all = to_streamed_response_wrapper(
            communication_preferences.unsubscribe_all,
        )
        self.update_status = to_streamed_response_wrapper(
            communication_preferences.update_status,
        )

    @cached_property
    def definitions(self) -> DefinitionsResourceWithStreamingResponse:
        return DefinitionsResourceWithStreamingResponse(self._communication_preferences.definitions)

    @cached_property
    def statuses(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self._communication_preferences.statuses)


class AsyncCommunicationPreferencesResourceWithStreamingResponse:
    def __init__(self, communication_preferences: AsyncCommunicationPreferencesResource) -> None:
        self._communication_preferences = communication_preferences

        self.generate_links = async_to_streamed_response_wrapper(
            communication_preferences.generate_links,
        )
        self.get_statuses = async_to_streamed_response_wrapper(
            communication_preferences.get_statuses,
        )
        self.get_unsubscribe_all_status = async_to_streamed_response_wrapper(
            communication_preferences.get_unsubscribe_all_status,
        )
        self.unsubscribe_all = async_to_streamed_response_wrapper(
            communication_preferences.unsubscribe_all,
        )
        self.update_status = async_to_streamed_response_wrapper(
            communication_preferences.update_status,
        )

    @cached_property
    def definitions(self) -> AsyncDefinitionsResourceWithStreamingResponse:
        return AsyncDefinitionsResourceWithStreamingResponse(self._communication_preferences.definitions)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self._communication_preferences.statuses)
