# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.auth import oauth_create_token_params, oauth_revoke_token_params, oauth_introspect_token_params
from ..._base_client import make_request_options
from ...types.auth.token_info_response_base_if import TokenInfoResponseBaseIf

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)

    def create_token(
        self,
        *,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        grant_type: Literal["authorization_code", "refresh_token"] | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Authenticates a client and returns access and refresh tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/oauth/2026-03/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "code_verifier": code_verifier,
                    "grant_type": grant_type,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                oauth_create_token_params.OAuthCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def introspect_token(
        self,
        *,
        token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        token_type_hint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenInfoResponseBaseIf:
        """
        Returns validity and metadata for access and refresh tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/2026-03/token/introspect",
            body=maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "token_type_hint": token_type_hint,
                },
                oauth_introspect_token_params.OAuthIntrospectTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenInfoResponseBaseIf,
        )

    def revoke_token(
        self,
        *,
        token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        token_type_hint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/oauth/2026-03/token/revoke",
            body=maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "token_type_hint": token_type_hint,
                },
                oauth_revoke_token_params.OAuthRevokeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def create_token(
        self,
        *,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        grant_type: Literal["authorization_code", "refresh_token"] | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Authenticates a client and returns access and refresh tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/oauth/2026-03/token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "code_verifier": code_verifier,
                    "grant_type": grant_type,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                oauth_create_token_params.OAuthCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def introspect_token(
        self,
        *,
        token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        token_type_hint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenInfoResponseBaseIf:
        """
        Returns validity and metadata for access and refresh tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/2026-03/token/introspect",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "token_type_hint": token_type_hint,
                },
                oauth_introspect_token_params.OAuthIntrospectTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenInfoResponseBaseIf,
        )

    async def revoke_token(
        self,
        *,
        token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        token_type_hint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/oauth/2026-03/token/revoke",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "token_type_hint": token_type_hint,
                },
                oauth_revoke_token_params.OAuthRevokeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.create_token = to_custom_raw_response_wrapper(
            oauth.create_token,
            BinaryAPIResponse,
        )
        self.introspect_token = to_raw_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = to_custom_raw_response_wrapper(
            oauth.revoke_token,
            BinaryAPIResponse,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.create_token = async_to_custom_raw_response_wrapper(
            oauth.create_token,
            AsyncBinaryAPIResponse,
        )
        self.introspect_token = async_to_raw_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = async_to_custom_raw_response_wrapper(
            oauth.revoke_token,
            AsyncBinaryAPIResponse,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.create_token = to_custom_streamed_response_wrapper(
            oauth.create_token,
            StreamedBinaryAPIResponse,
        )
        self.introspect_token = to_streamed_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = to_custom_streamed_response_wrapper(
            oauth.revoke_token,
            StreamedBinaryAPIResponse,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.create_token = async_to_custom_streamed_response_wrapper(
            oauth.create_token,
            AsyncStreamedBinaryAPIResponse,
        )
        self.introspect_token = async_to_streamed_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = async_to_custom_streamed_response_wrapper(
            oauth.revoke_token,
            AsyncStreamedBinaryAPIResponse,
        )
