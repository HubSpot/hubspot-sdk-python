# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .emails import (
    EmailsResource,
    AsyncEmailsResource,
    EmailsResourceWithRawResponse,
    AsyncEmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
    AsyncEmailsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .single_send import (
    SingleSendResource,
    AsyncSingleSendResource,
    SingleSendResourceWithRawResponse,
    AsyncSingleSendResourceWithRawResponse,
    SingleSendResourceWithStreamingResponse,
    AsyncSingleSendResourceWithStreamingResponse,
)
from .campaigns.campaigns import (
    CampaignsResource,
    AsyncCampaignsResource,
    CampaignsResourceWithRawResponse,
    AsyncCampaignsResourceWithRawResponse,
    CampaignsResourceWithStreamingResponse,
    AsyncCampaignsResourceWithStreamingResponse,
)
from .transactional.transactional import (
    TransactionalResource,
    AsyncTransactionalResource,
    TransactionalResourceWithRawResponse,
    AsyncTransactionalResourceWithRawResponse,
    TransactionalResourceWithStreamingResponse,
    AsyncTransactionalResourceWithStreamingResponse,
)
from .marketing_events.marketing_events import (
    MarketingEventsResource,
    AsyncMarketingEventsResource,
    MarketingEventsResourceWithRawResponse,
    AsyncMarketingEventsResourceWithRawResponse,
    MarketingEventsResourceWithStreamingResponse,
    AsyncMarketingEventsResourceWithStreamingResponse,
)

__all__ = ["MarketingResource", "AsyncMarketingResource"]


class MarketingResource(SyncAPIResource):
    @cached_property
    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def marketing_events(self) -> MarketingEventsResource:
        return MarketingEventsResource(self._client)

    @cached_property
    def single_send(self) -> SingleSendResource:
        return SingleSendResource(self._client)

    @cached_property
    def transactional(self) -> TransactionalResource:
        return TransactionalResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MarketingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return MarketingResourceWithStreamingResponse(self)


class AsyncMarketingResource(AsyncAPIResource):
    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        return AsyncCampaignsResource(self._client)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def marketing_events(self) -> AsyncMarketingEventsResource:
        return AsyncMarketingEventsResource(self._client)

    @cached_property
    def single_send(self) -> AsyncSingleSendResource:
        return AsyncSingleSendResource(self._client)

    @cached_property
    def transactional(self) -> AsyncTransactionalResource:
        return AsyncTransactionalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMarketingResourceWithStreamingResponse(self)


class MarketingResourceWithRawResponse:
    def __init__(self, marketing: MarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        return CampaignsResourceWithRawResponse(self._marketing.campaigns)

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._marketing.emails)

    @cached_property
    def marketing_events(self) -> MarketingEventsResourceWithRawResponse:
        return MarketingEventsResourceWithRawResponse(self._marketing.marketing_events)

    @cached_property
    def single_send(self) -> SingleSendResourceWithRawResponse:
        return SingleSendResourceWithRawResponse(self._marketing.single_send)

    @cached_property
    def transactional(self) -> TransactionalResourceWithRawResponse:
        return TransactionalResourceWithRawResponse(self._marketing.transactional)


class AsyncMarketingResourceWithRawResponse:
    def __init__(self, marketing: AsyncMarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        return AsyncCampaignsResourceWithRawResponse(self._marketing.campaigns)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._marketing.emails)

    @cached_property
    def marketing_events(self) -> AsyncMarketingEventsResourceWithRawResponse:
        return AsyncMarketingEventsResourceWithRawResponse(self._marketing.marketing_events)

    @cached_property
    def single_send(self) -> AsyncSingleSendResourceWithRawResponse:
        return AsyncSingleSendResourceWithRawResponse(self._marketing.single_send)

    @cached_property
    def transactional(self) -> AsyncTransactionalResourceWithRawResponse:
        return AsyncTransactionalResourceWithRawResponse(self._marketing.transactional)


class MarketingResourceWithStreamingResponse:
    def __init__(self, marketing: MarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        return CampaignsResourceWithStreamingResponse(self._marketing.campaigns)

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._marketing.emails)

    @cached_property
    def marketing_events(self) -> MarketingEventsResourceWithStreamingResponse:
        return MarketingEventsResourceWithStreamingResponse(self._marketing.marketing_events)

    @cached_property
    def single_send(self) -> SingleSendResourceWithStreamingResponse:
        return SingleSendResourceWithStreamingResponse(self._marketing.single_send)

    @cached_property
    def transactional(self) -> TransactionalResourceWithStreamingResponse:
        return TransactionalResourceWithStreamingResponse(self._marketing.transactional)


class AsyncMarketingResourceWithStreamingResponse:
    def __init__(self, marketing: AsyncMarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        return AsyncCampaignsResourceWithStreamingResponse(self._marketing.campaigns)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._marketing.emails)

    @cached_property
    def marketing_events(self) -> AsyncMarketingEventsResourceWithStreamingResponse:
        return AsyncMarketingEventsResourceWithStreamingResponse(self._marketing.marketing_events)

    @cached_property
    def single_send(self) -> AsyncSingleSendResourceWithStreamingResponse:
        return AsyncSingleSendResourceWithStreamingResponse(self._marketing.single_send)

    @cached_property
    def transactional(self) -> AsyncTransactionalResourceWithStreamingResponse:
        return AsyncTransactionalResourceWithStreamingResponse(self._marketing.transactional)
