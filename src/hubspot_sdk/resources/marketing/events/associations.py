# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.marketing.collection_response_with_total_public_list_no_paging import (
    CollectionResponseWithTotalPublicListNoPaging,
)

__all__ = ["AssociationsResource", "AsyncAssociationsResource"]


class AssociationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AssociationsResourceWithStreamingResponse(self)

    def list(
        self,
        marketing_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicListNoPaging:
        """
        Gets lists associated with a marketing event by marketing event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        return self._get(
            f"/marketing/v3/marketing-events/associations/{marketing_event_id}/lists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicListNoPaging,
        )

    def delete(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by marketing event id and ILS list
        id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/marketing/v3/marketing-events/associations/{marketing_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def associate(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by marketing event id and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/marketing/v3/marketing-events/associations/{marketing_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def associate_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by external account id, external event
        id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/marketing/v3/marketing-events/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by external account id, external
        event id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/marketing/v3/marketing-events/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_by_external_account(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicListNoPaging:
        """
        Gets lists associated with a marketing event by external account id and external
        event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return self._get(
            f"/marketing/v3/marketing-events/associations/{external_account_id}/{external_event_id}/lists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicListNoPaging,
        )


class AsyncAssociationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAssociationsResourceWithStreamingResponse(self)

    async def list(
        self,
        marketing_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicListNoPaging:
        """
        Gets lists associated with a marketing event by marketing event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        return await self._get(
            f"/marketing/v3/marketing-events/associations/{marketing_event_id}/lists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicListNoPaging,
        )

    async def delete(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by marketing event id and ILS list
        id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/marketing/v3/marketing-events/associations/{marketing_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def associate(
        self,
        list_id: str,
        *,
        marketing_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by marketing event id and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not marketing_event_id:
            raise ValueError(f"Expected a non-empty value for `marketing_event_id` but received {marketing_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/marketing/v3/marketing-events/associations/{marketing_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def associate_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Associates a list with a marketing event by external account id, external event
        id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/marketing/v3/marketing-events/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_external_account(
        self,
        list_id: str,
        *,
        external_account_id: str,
        external_event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disassociates a list from a marketing event by external account id, external
        event id, and ILS list id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/marketing/v3/marketing-events/associations/{external_account_id}/{external_event_id}/lists/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_by_external_account(
        self,
        external_event_id: str,
        *,
        external_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalPublicListNoPaging:
        """
        Gets lists associated with a marketing event by external account id and external
        event id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_account_id:
            raise ValueError(
                f"Expected a non-empty value for `external_account_id` but received {external_account_id!r}"
            )
        if not external_event_id:
            raise ValueError(f"Expected a non-empty value for `external_event_id` but received {external_event_id!r}")
        return await self._get(
            f"/marketing/v3/marketing-events/associations/{external_account_id}/{external_event_id}/lists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalPublicListNoPaging,
        )


class AssociationsResourceWithRawResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

        self.list = to_raw_response_wrapper(
            associations.list,
        )
        self.delete = to_raw_response_wrapper(
            associations.delete,
        )
        self.associate = to_raw_response_wrapper(
            associations.associate,
        )
        self.associate_by_external_account = to_raw_response_wrapper(
            associations.associate_by_external_account,
        )
        self.delete_by_external_account = to_raw_response_wrapper(
            associations.delete_by_external_account,
        )
        self.list_by_external_account = to_raw_response_wrapper(
            associations.list_by_external_account,
        )


class AsyncAssociationsResourceWithRawResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

        self.list = async_to_raw_response_wrapper(
            associations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            associations.delete,
        )
        self.associate = async_to_raw_response_wrapper(
            associations.associate,
        )
        self.associate_by_external_account = async_to_raw_response_wrapper(
            associations.associate_by_external_account,
        )
        self.delete_by_external_account = async_to_raw_response_wrapper(
            associations.delete_by_external_account,
        )
        self.list_by_external_account = async_to_raw_response_wrapper(
            associations.list_by_external_account,
        )


class AssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AssociationsResource) -> None:
        self._associations = associations

        self.list = to_streamed_response_wrapper(
            associations.list,
        )
        self.delete = to_streamed_response_wrapper(
            associations.delete,
        )
        self.associate = to_streamed_response_wrapper(
            associations.associate,
        )
        self.associate_by_external_account = to_streamed_response_wrapper(
            associations.associate_by_external_account,
        )
        self.delete_by_external_account = to_streamed_response_wrapper(
            associations.delete_by_external_account,
        )
        self.list_by_external_account = to_streamed_response_wrapper(
            associations.list_by_external_account,
        )


class AsyncAssociationsResourceWithStreamingResponse:
    def __init__(self, associations: AsyncAssociationsResource) -> None:
        self._associations = associations

        self.list = async_to_streamed_response_wrapper(
            associations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            associations.delete,
        )
        self.associate = async_to_streamed_response_wrapper(
            associations.associate,
        )
        self.associate_by_external_account = async_to_streamed_response_wrapper(
            associations.associate_by_external_account,
        )
        self.delete_by_external_account = async_to_streamed_response_wrapper(
            associations.delete_by_external_account,
        )
        self.list_by_external_account = async_to_streamed_response_wrapper(
            associations.list_by_external_account,
        )
