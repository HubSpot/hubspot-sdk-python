# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def oauth(self) -> OAuthResource:
        return OAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        return AsyncOAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self._auth.oauth)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self._auth.oauth)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self._auth.oauth)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self._auth.oauth)
