# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .campaigns.campaigns import (
    CampaignsResource,
    AsyncCampaignsResource,
    CampaignsResourceWithRawResponse,
    AsyncCampaignsResourceWithRawResponse,
    CampaignsResourceWithStreamingResponse,
    AsyncCampaignsResourceWithStreamingResponse,
)

__all__ = ["MarketingResource", "AsyncMarketingResource"]


class MarketingResource(SyncAPIResource):
    @cached_property
    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

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


class AsyncMarketingResourceWithRawResponse:
    def __init__(self, marketing: AsyncMarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        return AsyncCampaignsResourceWithRawResponse(self._marketing.campaigns)


class MarketingResourceWithStreamingResponse:
    def __init__(self, marketing: MarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        return CampaignsResourceWithStreamingResponse(self._marketing.campaigns)


class AsyncMarketingResourceWithStreamingResponse:
    def __init__(self, marketing: AsyncMarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        return AsyncCampaignsResourceWithStreamingResponse(self._marketing.campaigns)
