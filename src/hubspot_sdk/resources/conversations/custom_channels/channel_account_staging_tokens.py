# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.conversations.custom_channels import channel_account_staging_token_update_params
from ....types.conversations.public_delivery_identifier_param import PublicDeliveryIdentifierParam
from ....types.conversations.custom_channels.channel_account_staging_token_update_response import (
    ChannelAccountStagingTokenUpdateResponse,
)

__all__ = ["ChannelAccountStagingTokensResource", "AsyncChannelAccountStagingTokensResource"]


class ChannelAccountStagingTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelAccountStagingTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChannelAccountStagingTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelAccountStagingTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ChannelAccountStagingTokensResourceWithStreamingResponse(self)

    def update(
        self,
        account_token: str,
        *,
        channel_id: str,
        account_name: str,
        delivery_identifier: PublicDeliveryIdentifierParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelAccountStagingTokenUpdateResponse:
        """
        Update a channel account staging token's account name and delivery identifier.
        This information will be applied to the channel account created from this
        staging token. This is used for public apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._patch(
            f"/conversations/v3/custom-channels/{channel_id}/channel-account-staging-tokens/{account_token}",
            body=maybe_transform(
                {
                    "account_name": account_name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_staging_token_update_params.ChannelAccountStagingTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelAccountStagingTokenUpdateResponse,
        )


class AsyncChannelAccountStagingTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelAccountStagingTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelAccountStagingTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelAccountStagingTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncChannelAccountStagingTokensResourceWithStreamingResponse(self)

    async def update(
        self,
        account_token: str,
        *,
        channel_id: str,
        account_name: str,
        delivery_identifier: PublicDeliveryIdentifierParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelAccountStagingTokenUpdateResponse:
        """
        Update a channel account staging token's account name and delivery identifier.
        This information will be applied to the channel account created from this
        staging token. This is used for public apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._patch(
            f"/conversations/v3/custom-channels/{channel_id}/channel-account-staging-tokens/{account_token}",
            body=await async_maybe_transform(
                {
                    "account_name": account_name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_staging_token_update_params.ChannelAccountStagingTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelAccountStagingTokenUpdateResponse,
        )


class ChannelAccountStagingTokensResourceWithRawResponse:
    def __init__(self, channel_account_staging_tokens: ChannelAccountStagingTokensResource) -> None:
        self._channel_account_staging_tokens = channel_account_staging_tokens

        self.update = to_raw_response_wrapper(
            channel_account_staging_tokens.update,
        )


class AsyncChannelAccountStagingTokensResourceWithRawResponse:
    def __init__(self, channel_account_staging_tokens: AsyncChannelAccountStagingTokensResource) -> None:
        self._channel_account_staging_tokens = channel_account_staging_tokens

        self.update = async_to_raw_response_wrapper(
            channel_account_staging_tokens.update,
        )


class ChannelAccountStagingTokensResourceWithStreamingResponse:
    def __init__(self, channel_account_staging_tokens: ChannelAccountStagingTokensResource) -> None:
        self._channel_account_staging_tokens = channel_account_staging_tokens

        self.update = to_streamed_response_wrapper(
            channel_account_staging_tokens.update,
        )


class AsyncChannelAccountStagingTokensResourceWithStreamingResponse:
    def __init__(self, channel_account_staging_tokens: AsyncChannelAccountStagingTokensResource) -> None:
        self._channel_account_staging_tokens = channel_account_staging_tokens

        self.update = async_to_streamed_response_wrapper(
            channel_account_staging_tokens.update,
        )
