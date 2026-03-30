# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .smtp_tokens import (
    SmtpTokensResource,
    AsyncSmtpTokensResource,
    SmtpTokensResourceWithRawResponse,
    AsyncSmtpTokensResourceWithRawResponse,
    SmtpTokensResourceWithStreamingResponse,
    AsyncSmtpTokensResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .single_email import (
    SingleEmailResource,
    AsyncSingleEmailResource,
    SingleEmailResourceWithRawResponse,
    AsyncSingleEmailResourceWithRawResponse,
    SingleEmailResourceWithStreamingResponse,
    AsyncSingleEmailResourceWithStreamingResponse,
)

__all__ = ["TransactionalResource", "AsyncTransactionalResource"]


class TransactionalResource(SyncAPIResource):
    @cached_property
    def single_email(self) -> SingleEmailResource:
        return SingleEmailResource(self._client)

    @cached_property
    def smtp_tokens(self) -> SmtpTokensResource:
        return SmtpTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TransactionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TransactionalResourceWithStreamingResponse(self)


class AsyncTransactionalResource(AsyncAPIResource):
    @cached_property
    def single_email(self) -> AsyncSingleEmailResource:
        return AsyncSingleEmailResource(self._client)

    @cached_property
    def smtp_tokens(self) -> AsyncSmtpTokensResource:
        return AsyncSmtpTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTransactionalResourceWithStreamingResponse(self)


class TransactionalResourceWithRawResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

    @cached_property
    def single_email(self) -> SingleEmailResourceWithRawResponse:
        return SingleEmailResourceWithRawResponse(self._transactional.single_email)

    @cached_property
    def smtp_tokens(self) -> SmtpTokensResourceWithRawResponse:
        return SmtpTokensResourceWithRawResponse(self._transactional.smtp_tokens)


class AsyncTransactionalResourceWithRawResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

    @cached_property
    def single_email(self) -> AsyncSingleEmailResourceWithRawResponse:
        return AsyncSingleEmailResourceWithRawResponse(self._transactional.single_email)

    @cached_property
    def smtp_tokens(self) -> AsyncSmtpTokensResourceWithRawResponse:
        return AsyncSmtpTokensResourceWithRawResponse(self._transactional.smtp_tokens)


class TransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

    @cached_property
    def single_email(self) -> SingleEmailResourceWithStreamingResponse:
        return SingleEmailResourceWithStreamingResponse(self._transactional.single_email)

    @cached_property
    def smtp_tokens(self) -> SmtpTokensResourceWithStreamingResponse:
        return SmtpTokensResourceWithStreamingResponse(self._transactional.smtp_tokens)


class AsyncTransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

    @cached_property
    def single_email(self) -> AsyncSingleEmailResourceWithStreamingResponse:
        return AsyncSingleEmailResourceWithStreamingResponse(self._transactional.single_email)

    @cached_property
    def smtp_tokens(self) -> AsyncSmtpTokensResourceWithStreamingResponse:
        return AsyncSmtpTokensResourceWithStreamingResponse(self._transactional.smtp_tokens)
