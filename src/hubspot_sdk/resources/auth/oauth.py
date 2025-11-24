# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import oauth_create_access_token_params
from ..._base_client import make_request_options
from ...types.auth.token_response_if import TokenResponseIf
from ...types.auth.access_token_info_response import AccessTokenInfoResponse
from ...types.auth.refresh_token_info_response import RefreshTokenInfoResponse

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

    def create_access_token(
        self,
        *,
        query_client_secret: str | Omit = omit,
        query_refresh_token: str | Omit = omit,
        client_id: str | Omit = omit,
        body_client_secret: str | Omit = omit,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        grant_type: Literal["authorization_code", "client_credentials", "refresh_token"] | Omit = omit,
        redirect_uri: str | Omit = omit,
        body_refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponseIf:
        """
        Use a
        [previously obtained refresh token](#get-oauth-2.0-access-and-refresh-tokens) to
        generate a new access token.

        Access tokens are short lived. You can check the `expires_in` parameter when
        generating an access token to determine its lifetime (in seconds). If you need
        offline access to HubSpot data, store the refresh token you get when
        [initiating your OAuth integration](https://developers.hubspot.com/docs/guides/api/app-management/oauth-tokens#initiating-oauth-access)
        and use it to generate a new access token once the initial one expires.

        Note: HubSpot access tokens will fluctuate in size as the information that's
        encoded in them changes over time. It's recommended to allow for tokens to be up
        to 300 characters to account for any potential changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/v1/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "body_client_secret": body_client_secret,
                    "code": code,
                    "code_verifier": code_verifier,
                    "grant_type": grant_type,
                    "redirect_uri": redirect_uri,
                    "body_refresh_token": body_refresh_token,
                    "scope": scope,
                },
                oauth_create_access_token_params.OAuthCreateAccessTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query_client_secret": query_client_secret,
                        "query_refresh_token": query_refresh_token,
                    },
                    oauth_create_access_token_params.OAuthCreateAccessTokenParams,
                ),
            ),
            cast_to=TokenResponseIf,
        )

    @typing_extensions.deprecated("deprecated")
    def delete_refresh_token(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a refresh token, typically after a user uninstalls your app.

        Access
        tokens generated with the refresh token will not be affected.

        This will not uninstall the application from HubSpot or inhibit data syncing
        between an account and the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/oauth/v1/refresh-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def get_access_token(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenInfoResponse:
        """
        Retrieve a token's metadata, including the email address of the user that the
        token was created for and the ID of the account it's associated with.

        Note: HubSpot access tokens will fluctuate in size as the information that's
        encoded in them changes over time. It's recommended to allow for tokens to be up
        to 300 characters to account for any potential changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._get(
            f"/oauth/v1/access-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenInfoResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_refresh_token(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RefreshTokenInfoResponse:
        """
        Retrieve a refresh token's metadata, including the email address of the user
        that the token was created for and the ID of the account it's associated with.
        Learn more about
        [refresh tokens](https://developers.hubspot.com/docs/guides/api/app-management/oauth-tokens#generate-initial-access-and-refresh-tokens).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._get(
            f"/oauth/v1/refresh-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefreshTokenInfoResponse,
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

    async def create_access_token(
        self,
        *,
        query_client_secret: str | Omit = omit,
        query_refresh_token: str | Omit = omit,
        client_id: str | Omit = omit,
        body_client_secret: str | Omit = omit,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        grant_type: Literal["authorization_code", "client_credentials", "refresh_token"] | Omit = omit,
        redirect_uri: str | Omit = omit,
        body_refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponseIf:
        """
        Use a
        [previously obtained refresh token](#get-oauth-2.0-access-and-refresh-tokens) to
        generate a new access token.

        Access tokens are short lived. You can check the `expires_in` parameter when
        generating an access token to determine its lifetime (in seconds). If you need
        offline access to HubSpot data, store the refresh token you get when
        [initiating your OAuth integration](https://developers.hubspot.com/docs/guides/api/app-management/oauth-tokens#initiating-oauth-access)
        and use it to generate a new access token once the initial one expires.

        Note: HubSpot access tokens will fluctuate in size as the information that's
        encoded in them changes over time. It's recommended to allow for tokens to be up
        to 300 characters to account for any potential changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/v1/token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "body_client_secret": body_client_secret,
                    "code": code,
                    "code_verifier": code_verifier,
                    "grant_type": grant_type,
                    "redirect_uri": redirect_uri,
                    "body_refresh_token": body_refresh_token,
                    "scope": scope,
                },
                oauth_create_access_token_params.OAuthCreateAccessTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query_client_secret": query_client_secret,
                        "query_refresh_token": query_refresh_token,
                    },
                    oauth_create_access_token_params.OAuthCreateAccessTokenParams,
                ),
            ),
            cast_to=TokenResponseIf,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete_refresh_token(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a refresh token, typically after a user uninstalls your app.

        Access
        tokens generated with the refresh token will not be affected.

        This will not uninstall the application from HubSpot or inhibit data syncing
        between an account and the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/oauth/v1/refresh-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_access_token(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenInfoResponse:
        """
        Retrieve a token's metadata, including the email address of the user that the
        token was created for and the ID of the account it's associated with.

        Note: HubSpot access tokens will fluctuate in size as the information that's
        encoded in them changes over time. It's recommended to allow for tokens to be up
        to 300 characters to account for any potential changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._get(
            f"/oauth/v1/access-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenInfoResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_refresh_token(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RefreshTokenInfoResponse:
        """
        Retrieve a refresh token's metadata, including the email address of the user
        that the token was created for and the ID of the account it's associated with.
        Learn more about
        [refresh tokens](https://developers.hubspot.com/docs/guides/api/app-management/oauth-tokens#generate-initial-access-and-refresh-tokens).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._get(
            f"/oauth/v1/refresh-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefreshTokenInfoResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.create_access_token = to_raw_response_wrapper(
            oauth.create_access_token,
        )
        self.delete_refresh_token = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                oauth.delete_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_access_token = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                oauth.get_access_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_refresh_token = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                oauth.get_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.create_access_token = async_to_raw_response_wrapper(
            oauth.create_access_token,
        )
        self.delete_refresh_token = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                oauth.delete_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_access_token = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                oauth.get_access_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_refresh_token = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                oauth.get_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.create_access_token = to_streamed_response_wrapper(
            oauth.create_access_token,
        )
        self.delete_refresh_token = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                oauth.delete_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_access_token = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                oauth.get_access_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_refresh_token = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                oauth.get_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.create_access_token = async_to_streamed_response_wrapper(
            oauth.create_access_token,
        )
        self.delete_refresh_token = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                oauth.delete_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_access_token = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                oauth.get_access_token,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_refresh_token = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                oauth.get_refresh_token,  # pyright: ignore[reportDeprecated],
            )
        )
