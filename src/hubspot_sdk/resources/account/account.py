# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .activity import (
    ActivityResource,
    AsyncActivityResource,
    ActivityResourceWithRawResponse,
    AsyncActivityResourceWithRawResponse,
    ActivityResourceWithStreamingResponse,
    AsyncActivityResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    @cached_property
    def activity(self) -> ActivityResource:
        return ActivityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)


class AsyncAccountResource(AsyncAPIResource):
    @cached_property
    def activity(self) -> AsyncActivityResource:
        return AsyncActivityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

    @cached_property
    def activity(self) -> ActivityResourceWithRawResponse:
        return ActivityResourceWithRawResponse(self._account.activity)


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

    @cached_property
    def activity(self) -> AsyncActivityResourceWithRawResponse:
        return AsyncActivityResourceWithRawResponse(self._account.activity)


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

    @cached_property
    def activity(self) -> ActivityResourceWithStreamingResponse:
        return ActivityResourceWithStreamingResponse(self._account.activity)


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

    @cached_property
    def activity(self) -> AsyncActivityResourceWithStreamingResponse:
        return AsyncActivityResourceWithStreamingResponse(self._account.activity)
