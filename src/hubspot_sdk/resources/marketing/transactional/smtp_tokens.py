# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.marketing.transactional import smtp_token_list_params, smtp_token_create_params
from ....types.marketing.smtp_api_token_view import SmtpAPITokenView

__all__ = ["SmtpTokensResource", "AsyncSmtpTokensResource"]


class SmtpTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmtpTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SmtpTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmtpTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SmtpTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        campaign_name: str,
        create_contact: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmtpAPITokenView:
        """
        Create a SMTP API token.

        Args:
          campaign_name: A name for the campaign tied to the SMTP API token.

          create_contact: Indicates whether a contact should be created for email recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/transactional/2026-03/smtp-tokens",
            body=maybe_transform(
                {
                    "campaign_name": campaign_name,
                    "create_contact": create_contact,
                },
                smtp_token_create_params.SmtpTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmtpAPITokenView,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        campaign_name: str | Omit = omit,
        email_campaign_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[SmtpAPITokenView]:
        """
        Query multiple SMTP API tokens by campaign name or a single token by
        emailCampaignId.

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
        return self._get_api_list(
            "/marketing/transactional/2026-03/smtp-tokens",
            page=SyncPage[SmtpAPITokenView],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "campaign_name": campaign_name,
                        "email_campaign_id": email_campaign_id,
                        "limit": limit,
                    },
                    smtp_token_list_params.SmtpTokenListParams,
                ),
            ),
            model=SmtpAPITokenView,
        )

    def delete(
        self,
        token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a single token by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/marketing/transactional/2026-03/smtp-tokens/{token_id}", token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmtpAPITokenView:
        """
        Query a single token by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        return self._get(
            path_template("/marketing/transactional/2026-03/smtp-tokens/{token_id}", token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmtpAPITokenView,
        )

    def reset_password(
        self,
        token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmtpAPITokenView:
        """Allows the creation of a replacement password for a given token.

        Once the
        password is successfully reset, the old password for the token will be invalid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        return self._post(
            path_template("/marketing/transactional/2026-03/smtp-tokens/{token_id}/password-reset", token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmtpAPITokenView,
        )


class AsyncSmtpTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmtpTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSmtpTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmtpTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSmtpTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        campaign_name: str,
        create_contact: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmtpAPITokenView:
        """
        Create a SMTP API token.

        Args:
          campaign_name: A name for the campaign tied to the SMTP API token.

          create_contact: Indicates whether a contact should be created for email recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/transactional/2026-03/smtp-tokens",
            body=await async_maybe_transform(
                {
                    "campaign_name": campaign_name,
                    "create_contact": create_contact,
                },
                smtp_token_create_params.SmtpTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmtpAPITokenView,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        campaign_name: str | Omit = omit,
        email_campaign_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SmtpAPITokenView, AsyncPage[SmtpAPITokenView]]:
        """
        Query multiple SMTP API tokens by campaign name or a single token by
        emailCampaignId.

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
        return self._get_api_list(
            "/marketing/transactional/2026-03/smtp-tokens",
            page=AsyncPage[SmtpAPITokenView],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "campaign_name": campaign_name,
                        "email_campaign_id": email_campaign_id,
                        "limit": limit,
                    },
                    smtp_token_list_params.SmtpTokenListParams,
                ),
            ),
            model=SmtpAPITokenView,
        )

    async def delete(
        self,
        token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a single token by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/marketing/transactional/2026-03/smtp-tokens/{token_id}", token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmtpAPITokenView:
        """
        Query a single token by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        return await self._get(
            path_template("/marketing/transactional/2026-03/smtp-tokens/{token_id}", token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmtpAPITokenView,
        )

    async def reset_password(
        self,
        token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmtpAPITokenView:
        """Allows the creation of a replacement password for a given token.

        Once the
        password is successfully reset, the old password for the token will be invalid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        return await self._post(
            path_template("/marketing/transactional/2026-03/smtp-tokens/{token_id}/password-reset", token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmtpAPITokenView,
        )


class SmtpTokensResourceWithRawResponse:
    def __init__(self, smtp_tokens: SmtpTokensResource) -> None:
        self._smtp_tokens = smtp_tokens

        self.create = to_raw_response_wrapper(
            smtp_tokens.create,
        )
        self.list = to_raw_response_wrapper(
            smtp_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            smtp_tokens.delete,
        )
        self.get = to_raw_response_wrapper(
            smtp_tokens.get,
        )
        self.reset_password = to_raw_response_wrapper(
            smtp_tokens.reset_password,
        )


class AsyncSmtpTokensResourceWithRawResponse:
    def __init__(self, smtp_tokens: AsyncSmtpTokensResource) -> None:
        self._smtp_tokens = smtp_tokens

        self.create = async_to_raw_response_wrapper(
            smtp_tokens.create,
        )
        self.list = async_to_raw_response_wrapper(
            smtp_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            smtp_tokens.delete,
        )
        self.get = async_to_raw_response_wrapper(
            smtp_tokens.get,
        )
        self.reset_password = async_to_raw_response_wrapper(
            smtp_tokens.reset_password,
        )


class SmtpTokensResourceWithStreamingResponse:
    def __init__(self, smtp_tokens: SmtpTokensResource) -> None:
        self._smtp_tokens = smtp_tokens

        self.create = to_streamed_response_wrapper(
            smtp_tokens.create,
        )
        self.list = to_streamed_response_wrapper(
            smtp_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            smtp_tokens.delete,
        )
        self.get = to_streamed_response_wrapper(
            smtp_tokens.get,
        )
        self.reset_password = to_streamed_response_wrapper(
            smtp_tokens.reset_password,
        )


class AsyncSmtpTokensResourceWithStreamingResponse:
    def __init__(self, smtp_tokens: AsyncSmtpTokensResource) -> None:
        self._smtp_tokens = smtp_tokens

        self.create = async_to_streamed_response_wrapper(
            smtp_tokens.create,
        )
        self.list = async_to_streamed_response_wrapper(
            smtp_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            smtp_tokens.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            smtp_tokens.get,
        )
        self.reset_password = async_to_streamed_response_wrapper(
            smtp_tokens.reset_password,
        )
