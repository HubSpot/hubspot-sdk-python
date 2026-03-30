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
from ...._base_client import make_request_options
from ....types.marketing.campaigns import asset_list_params
from ....types.marketing.collection_response_public_campaign_asset_forward_paging import (
    CollectionResponsePublicCampaignAssetForwardPaging,
)

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def update(
        self,
        asset_id: str,
        *,
        campaign_guid: str,
        asset_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Associate a specified asset with a campaign.

        Using the API, you can create
        associations for the following asset types: ads, blog posts, calls, case
        studies, CTAs, CTAs (legacy), external website pages, feedback surveys, forms,
        files, knowledge base articles, landing pages, marketing email, marketing
        events, meetings, playbooks, podcast episodes, sales documents, sales emails,
        sequences, SMS, social posts, static lists, videos, website pages, and
        workflows.

        For other asset types, it is recommended to manage your associations directly in
        the campaign tool in HubSpot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not asset_type:
            raise ValueError(f"Expected a non-empty value for `asset_type` but received {asset_type!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/assets/{asset_type}/{asset_id}",
                campaign_guid=campaign_guid,
                asset_type=asset_type,
                asset_id=asset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        asset_type: str,
        *,
        campaign_guid: str,
        after: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicCampaignAssetForwardPaging:
        """This endpoint lists all assets of the campaign by asset type.

        The assetType
        parameter is required, and each request can only fetch assets of a single type.
        Asset metrics can also be fetched along with the assets; they are available only
        if start and end dates are provided.

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
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not asset_type:
            raise ValueError(f"Expected a non-empty value for `asset_type` but received {asset_type!r}")
        return self._get(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/assets/{asset_type}",
                campaign_guid=campaign_guid,
                asset_type=asset_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "end_date": end_date,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=CollectionResponsePublicCampaignAssetForwardPaging,
        )

    def delete(
        self,
        asset_id: str,
        *,
        campaign_guid: str,
        asset_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Disassociate a specified asset from a campaign.

        Using the API, you can remove
        associations for the following asset types: ads, blog posts, calls, case
        studies, CTAs, CTAs (legacy), external website pages, feedback surveys, forms,
        files, knowledge base articles, landing pages, marketing email, marketing
        events, meetings, playbooks, podcast episodes, sales documents, sales emails,
        sequences, SMS, social posts, static lists, videos, website pages, and
        workflows.

        For other asset types, it is recommended to manage your associations directly in
        the campaign tool in HubSpot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not asset_type:
            raise ValueError(f"Expected a non-empty value for `asset_type` but received {asset_type!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/assets/{asset_type}/{asset_id}",
                campaign_guid=campaign_guid,
                asset_type=asset_type,
                asset_id=asset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def update(
        self,
        asset_id: str,
        *,
        campaign_guid: str,
        asset_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Associate a specified asset with a campaign.

        Using the API, you can create
        associations for the following asset types: ads, blog posts, calls, case
        studies, CTAs, CTAs (legacy), external website pages, feedback surveys, forms,
        files, knowledge base articles, landing pages, marketing email, marketing
        events, meetings, playbooks, podcast episodes, sales documents, sales emails,
        sequences, SMS, social posts, static lists, videos, website pages, and
        workflows.

        For other asset types, it is recommended to manage your associations directly in
        the campaign tool in HubSpot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not asset_type:
            raise ValueError(f"Expected a non-empty value for `asset_type` but received {asset_type!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/assets/{asset_type}/{asset_id}",
                campaign_guid=campaign_guid,
                asset_type=asset_type,
                asset_id=asset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        asset_type: str,
        *,
        campaign_guid: str,
        after: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicCampaignAssetForwardPaging:
        """This endpoint lists all assets of the campaign by asset type.

        The assetType
        parameter is required, and each request can only fetch assets of a single type.
        Asset metrics can also be fetched along with the assets; they are available only
        if start and end dates are provided.

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
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not asset_type:
            raise ValueError(f"Expected a non-empty value for `asset_type` but received {asset_type!r}")
        return await self._get(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/assets/{asset_type}",
                campaign_guid=campaign_guid,
                asset_type=asset_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "end_date": end_date,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=CollectionResponsePublicCampaignAssetForwardPaging,
        )

    async def delete(
        self,
        asset_id: str,
        *,
        campaign_guid: str,
        asset_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Disassociate a specified asset from a campaign.

        Using the API, you can remove
        associations for the following asset types: ads, blog posts, calls, case
        studies, CTAs, CTAs (legacy), external website pages, feedback surveys, forms,
        files, knowledge base articles, landing pages, marketing email, marketing
        events, meetings, playbooks, podcast episodes, sales documents, sales emails,
        sequences, SMS, social posts, static lists, videos, website pages, and
        workflows.

        For other asset types, it is recommended to manage your associations directly in
        the campaign tool in HubSpot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_guid:
            raise ValueError(f"Expected a non-empty value for `campaign_guid` but received {campaign_guid!r}")
        if not asset_type:
            raise ValueError(f"Expected a non-empty value for `asset_type` but received {asset_type!r}")
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/marketing/campaigns/2026-03/{campaign_guid}/assets/{asset_type}/{asset_id}",
                campaign_guid=campaign_guid,
                asset_type=asset_type,
                asset_id=asset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.list = to_raw_response_wrapper(
            assets.list,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.list = async_to_raw_response_wrapper(
            assets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.list = to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )
