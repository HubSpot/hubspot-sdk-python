# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.conversations.custom_channels import (
    channel_account_list_params,
    channel_account_create_params,
    channel_account_update_params,
    channel_account_update_staging_token_params,
)
from ....types.conversations.public_channel_account import PublicChannelAccount
from ....types.conversations.public_delivery_identifier_param import PublicDeliveryIdentifierParam
from ....types.conversations.public_channel_account_staging_token import PublicChannelAccountStagingToken

__all__ = ["ChannelAccountsResource", "AsyncChannelAccountsResource"]


class ChannelAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChannelAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ChannelAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        channel_id: int,
        *,
        authorized: bool,
        inbox_id: str,
        name: str,
        delivery_identifier: PublicDeliveryIdentifierParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """Create a new account for a channel.

        Multiple accounts can communicate over a
        single channel using different delivery identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts", channel_id=channel_id
            ),
            body=maybe_transform(
                {
                    "authorized": authorized,
                    "inbox_id": inbox_id,
                    "name": name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_create_params.ChannelAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelAccount,
        )

    def update(
        self,
        channel_account_id: int,
        *,
        channel_id: int,
        authorized: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """
        This API is used to update the name of the channel account and it's isAuthorized
        status. Setting to isAuthorized flag to False disables the channel account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts/{channel_account_id}",
                channel_id=channel_id,
                channel_account_id=channel_account_id,
            ),
            body=maybe_transform(
                {
                    "authorized": authorized,
                    "name": name,
                },
                channel_account_update_params.ChannelAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelAccount,
        )

    def list(
        self,
        channel_id: int,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        default_page_length: int | Omit = omit,
        delivery_identifier_type: List[
            Literal["HS_EMAIL_ADDRESS", "HS_PHONE_NUMBER", "HS_SHORT_CODE", "CHANNEL_SPECIFIC_OPAQUE_ID"]
        ]
        | Omit = omit,
        delivery_identifier_value: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicChannelAccount]:
        """
        Retrieve a list of accounts for a custom channel.

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
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts", channel_id=channel_id
            ),
            page=SyncPage[PublicChannelAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "default_page_length": default_page_length,
                        "delivery_identifier_type": delivery_identifier_type,
                        "delivery_identifier_value": delivery_identifier_value,
                        "limit": limit,
                        "sort": sort,
                    },
                    channel_account_list_params.ChannelAccountListParams,
                ),
            ),
            model=PublicChannelAccount,
        )

    def update_staging_token(
        self,
        account_token: str,
        *,
        channel_id: int,
        account_name: str,
        delivery_identifier: PublicDeliveryIdentifierParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccountStagingToken:
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
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._patch(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-account-staging-tokens/{account_token}",
                channel_id=channel_id,
                account_token=account_token,
            ),
            body=maybe_transform(
                {
                    "account_name": account_name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_update_staging_token_params.ChannelAccountUpdateStagingTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelAccountStagingToken,
        )


class AsyncChannelAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncChannelAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        channel_id: int,
        *,
        authorized: bool,
        inbox_id: str,
        name: str,
        delivery_identifier: PublicDeliveryIdentifierParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """Create a new account for a channel.

        Multiple accounts can communicate over a
        single channel using different delivery identifiers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts", channel_id=channel_id
            ),
            body=await async_maybe_transform(
                {
                    "authorized": authorized,
                    "inbox_id": inbox_id,
                    "name": name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_create_params.ChannelAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelAccount,
        )

    async def update(
        self,
        channel_account_id: int,
        *,
        channel_id: int,
        authorized: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccount:
        """
        This API is used to update the name of the channel account and it's isAuthorized
        status. Setting to isAuthorized flag to False disables the channel account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts/{channel_account_id}",
                channel_id=channel_id,
                channel_account_id=channel_account_id,
            ),
            body=await async_maybe_transform(
                {
                    "authorized": authorized,
                    "name": name,
                },
                channel_account_update_params.ChannelAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelAccount,
        )

    def list(
        self,
        channel_id: int,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        default_page_length: int | Omit = omit,
        delivery_identifier_type: List[
            Literal["HS_EMAIL_ADDRESS", "HS_PHONE_NUMBER", "HS_SHORT_CODE", "CHANNEL_SPECIFIC_OPAQUE_ID"]
        ]
        | Omit = omit,
        delivery_identifier_value: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicChannelAccount, AsyncPage[PublicChannelAccount]]:
        """
        Retrieve a list of accounts for a custom channel.

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
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-accounts", channel_id=channel_id
            ),
            page=AsyncPage[PublicChannelAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "default_page_length": default_page_length,
                        "delivery_identifier_type": delivery_identifier_type,
                        "delivery_identifier_value": delivery_identifier_value,
                        "limit": limit,
                        "sort": sort,
                    },
                    channel_account_list_params.ChannelAccountListParams,
                ),
            ),
            model=PublicChannelAccount,
        )

    async def update_staging_token(
        self,
        account_token: str,
        *,
        channel_id: int,
        account_name: str,
        delivery_identifier: PublicDeliveryIdentifierParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicChannelAccountStagingToken:
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
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._patch(
            path_template(
                "/conversations/custom-channels/2026-03/{channel_id}/channel-account-staging-tokens/{account_token}",
                channel_id=channel_id,
                account_token=account_token,
            ),
            body=await async_maybe_transform(
                {
                    "account_name": account_name,
                    "delivery_identifier": delivery_identifier,
                },
                channel_account_update_staging_token_params.ChannelAccountUpdateStagingTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicChannelAccountStagingToken,
        )


class ChannelAccountsResourceWithRawResponse:
    def __init__(self, channel_accounts: ChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = to_raw_response_wrapper(
            channel_accounts.create,
        )
        self.update = to_raw_response_wrapper(
            channel_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            channel_accounts.list,
        )
        self.update_staging_token = to_raw_response_wrapper(
            channel_accounts.update_staging_token,
        )


class AsyncChannelAccountsResourceWithRawResponse:
    def __init__(self, channel_accounts: AsyncChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = async_to_raw_response_wrapper(
            channel_accounts.create,
        )
        self.update = async_to_raw_response_wrapper(
            channel_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            channel_accounts.list,
        )
        self.update_staging_token = async_to_raw_response_wrapper(
            channel_accounts.update_staging_token,
        )


class ChannelAccountsResourceWithStreamingResponse:
    def __init__(self, channel_accounts: ChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = to_streamed_response_wrapper(
            channel_accounts.create,
        )
        self.update = to_streamed_response_wrapper(
            channel_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            channel_accounts.list,
        )
        self.update_staging_token = to_streamed_response_wrapper(
            channel_accounts.update_staging_token,
        )


class AsyncChannelAccountsResourceWithStreamingResponse:
    def __init__(self, channel_accounts: AsyncChannelAccountsResource) -> None:
        self._channel_accounts = channel_accounts

        self.create = async_to_streamed_response_wrapper(
            channel_accounts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            channel_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            channel_accounts.list,
        )
        self.update_staging_token = async_to_streamed_response_wrapper(
            channel_accounts.update_staging_token,
        )
