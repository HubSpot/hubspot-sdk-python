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
from ....types.crm.extensions import (
    cards_dev_create_params,
    cards_dev_update_params,
    cards_dev_migrate_views_params,
)
from ....types.crm.extensions.card_actions_param import CardActionsParam
from ....types.crm.extensions.public_card_response import PublicCardResponse
from ....types.crm.extensions.card_fetch_body_param import CardFetchBodyParam
from ....types.crm.extensions.card_display_body_param import CardDisplayBodyParam
from ....types.crm.extensions.public_card_list_response import PublicCardListResponse
from ....types.crm.extensions.card_fetch_body_patch_param import CardFetchBodyPatchParam
from ....types.crm.extensions.card_migrate_views_response import CardMigrateViewsResponse
from ....types.crm.extensions.integrator_card_payload_response import IntegratorCardPayloadResponse

__all__ = ["CardsDevResource", "AsyncCardsDevResource"]


class CardsDevResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardsDevResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CardsDevResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsDevResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CardsDevResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        actions: CardActionsParam,
        display: CardDisplayBodyParam,
        fetch: CardFetchBodyParam,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardResponse:
        """Args:
          title: The top-level title for this card.

        Displayed to users in the CRM UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}", app_id=app_id),
            body=maybe_transform(
                {
                    "actions": actions,
                    "display": display,
                    "fetch": fetch,
                    "title": title,
                },
                cards_dev_create_params.CardsDevCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardResponse,
        )

    def update(
        self,
        card_id: str,
        *,
        app_id: int,
        actions: CardActionsParam | Omit = omit,
        display: CardDisplayBodyParam | Omit = omit,
        fetch: CardFetchBodyPatchParam | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardResponse:
        """Args:
          title: The top-level title for this card.

        Displayed to users in the CRM UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._patch(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/{card_id}", app_id=app_id, card_id=card_id),
            body=maybe_transform(
                {
                    "actions": actions,
                    "display": display,
                    "fetch": fetch,
                    "title": title,
                },
                cards_dev_update_params.CardsDevUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardResponse,
        )

    def delete(
        self,
        card_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/{card_id}", app_id=app_id, card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardListResponse,
        )

    def get_by_id(
        self,
        card_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/{card_id}", app_id=app_id, card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardResponse,
        )

    def get_sample_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorCardPayloadResponse:
        return self._get(
            "/crm/extensions/cards-dev/2026-03/sample-response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorCardPayloadResponse,
        )

    def migrate_views(
        self,
        app_id: int,
        *,
        app_card_id: int,
        legacy_crm_card_id: int,
        helpdesk_app_card_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardMigrateViewsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/views/migrate", app_id=app_id),
            body=maybe_transform(
                {
                    "app_card_id": app_card_id,
                    "legacy_crm_card_id": legacy_crm_card_id,
                    "helpdesk_app_card_id": helpdesk_app_card_id,
                },
                cards_dev_migrate_views_params.CardsDevMigrateViewsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardMigrateViewsResponse,
        )


class AsyncCardsDevResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardsDevResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsDevResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsDevResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCardsDevResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        actions: CardActionsParam,
        display: CardDisplayBodyParam,
        fetch: CardFetchBodyParam,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardResponse:
        """Args:
          title: The top-level title for this card.

        Displayed to users in the CRM UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "display": display,
                    "fetch": fetch,
                    "title": title,
                },
                cards_dev_create_params.CardsDevCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardResponse,
        )

    async def update(
        self,
        card_id: str,
        *,
        app_id: int,
        actions: CardActionsParam | Omit = omit,
        display: CardDisplayBodyParam | Omit = omit,
        fetch: CardFetchBodyPatchParam | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardResponse:
        """Args:
          title: The top-level title for this card.

        Displayed to users in the CRM UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._patch(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/{card_id}", app_id=app_id, card_id=card_id),
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "display": display,
                    "fetch": fetch,
                    "title": title,
                },
                cards_dev_update_params.CardsDevUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardResponse,
        )

    async def delete(
        self,
        card_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/{card_id}", app_id=app_id, card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardListResponse,
        )

    async def get_by_id(
        self,
        card_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCardResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/{card_id}", app_id=app_id, card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCardResponse,
        )

    async def get_sample_response(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegratorCardPayloadResponse:
        return await self._get(
            "/crm/extensions/cards-dev/2026-03/sample-response",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegratorCardPayloadResponse,
        )

    async def migrate_views(
        self,
        app_id: int,
        *,
        app_card_id: int,
        legacy_crm_card_id: int,
        helpdesk_app_card_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardMigrateViewsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/crm/extensions/cards-dev/2026-03/{app_id}/views/migrate", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "app_card_id": app_card_id,
                    "legacy_crm_card_id": legacy_crm_card_id,
                    "helpdesk_app_card_id": helpdesk_app_card_id,
                },
                cards_dev_migrate_views_params.CardsDevMigrateViewsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardMigrateViewsResponse,
        )


class CardsDevResourceWithRawResponse:
    def __init__(self, cards_dev: CardsDevResource) -> None:
        self._cards_dev = cards_dev

        self.create = to_raw_response_wrapper(
            cards_dev.create,
        )
        self.update = to_raw_response_wrapper(
            cards_dev.update,
        )
        self.delete = to_raw_response_wrapper(
            cards_dev.delete,
        )
        self.get = to_raw_response_wrapper(
            cards_dev.get,
        )
        self.get_by_id = to_raw_response_wrapper(
            cards_dev.get_by_id,
        )
        self.get_sample_response = to_raw_response_wrapper(
            cards_dev.get_sample_response,
        )
        self.migrate_views = to_raw_response_wrapper(
            cards_dev.migrate_views,
        )


class AsyncCardsDevResourceWithRawResponse:
    def __init__(self, cards_dev: AsyncCardsDevResource) -> None:
        self._cards_dev = cards_dev

        self.create = async_to_raw_response_wrapper(
            cards_dev.create,
        )
        self.update = async_to_raw_response_wrapper(
            cards_dev.update,
        )
        self.delete = async_to_raw_response_wrapper(
            cards_dev.delete,
        )
        self.get = async_to_raw_response_wrapper(
            cards_dev.get,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            cards_dev.get_by_id,
        )
        self.get_sample_response = async_to_raw_response_wrapper(
            cards_dev.get_sample_response,
        )
        self.migrate_views = async_to_raw_response_wrapper(
            cards_dev.migrate_views,
        )


class CardsDevResourceWithStreamingResponse:
    def __init__(self, cards_dev: CardsDevResource) -> None:
        self._cards_dev = cards_dev

        self.create = to_streamed_response_wrapper(
            cards_dev.create,
        )
        self.update = to_streamed_response_wrapper(
            cards_dev.update,
        )
        self.delete = to_streamed_response_wrapper(
            cards_dev.delete,
        )
        self.get = to_streamed_response_wrapper(
            cards_dev.get,
        )
        self.get_by_id = to_streamed_response_wrapper(
            cards_dev.get_by_id,
        )
        self.get_sample_response = to_streamed_response_wrapper(
            cards_dev.get_sample_response,
        )
        self.migrate_views = to_streamed_response_wrapper(
            cards_dev.migrate_views,
        )


class AsyncCardsDevResourceWithStreamingResponse:
    def __init__(self, cards_dev: AsyncCardsDevResource) -> None:
        self._cards_dev = cards_dev

        self.create = async_to_streamed_response_wrapper(
            cards_dev.create,
        )
        self.update = async_to_streamed_response_wrapper(
            cards_dev.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            cards_dev.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            cards_dev.get,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            cards_dev.get_by_id,
        )
        self.get_sample_response = async_to_streamed_response_wrapper(
            cards_dev.get_sample_response,
        )
        self.migrate_views = async_to_streamed_response_wrapper(
            cards_dev.migrate_views,
        )
