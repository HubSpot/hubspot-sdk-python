# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .single_send import (
    SingleSendResource,
    AsyncSingleSendResource,
    SingleSendResourceWithRawResponse,
    AsyncSingleSendResourceWithRawResponse,
    SingleSendResourceWithStreamingResponse,
    AsyncSingleSendResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def single_send(self) -> SingleSendResource:
        return SingleSendResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def single_send(self) -> AsyncSingleSendResource:
        return AsyncSingleSendResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

    @cached_property
    def single_send(self) -> SingleSendResourceWithRawResponse:
        return SingleSendResourceWithRawResponse(self._emails.single_send)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

    @cached_property
    def single_send(self) -> AsyncSingleSendResourceWithRawResponse:
        return AsyncSingleSendResourceWithRawResponse(self._emails.single_send)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

    @cached_property
    def single_send(self) -> SingleSendResourceWithStreamingResponse:
        return SingleSendResourceWithStreamingResponse(self._emails.single_send)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

    @cached_property
    def single_send(self) -> AsyncSingleSendResourceWithStreamingResponse:
        return AsyncSingleSendResourceWithStreamingResponse(self._emails.single_send)
