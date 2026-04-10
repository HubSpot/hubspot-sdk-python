# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.marketing import single_send_create_params
from ...types.marketing.email_send_status_view import EmailSendStatusView
from ...types.marketing.public_single_send_email_param import PublicSingleSendEmailParam

__all__ = ["SingleSendResource", "AsyncSingleSendResource"]


class SingleSendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SingleSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SingleSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SingleSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return SingleSendResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        contact_properties: Dict[str, str],
        custom_properties: Dict[str, object],
        email_id: int,
        message: PublicSingleSendEmailParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendStatusView:
        """
        Send a template email to a specific recipient.

        Args:
          contact_properties: The contactProperties field is a map of contact property values. Each contact
              property value contains a name and value property. Each property will get set on
              the contact record and will be visible in the template under {{ contact.NAME }}.
              Use these properties when you want to set a contact property while you’re
              sending the email. For example, when sending a receipt you may want to set a
              last_paid_date property, as the sending of the receipt will have information
              about the last payment.

          custom_properties: The customProperties field is a map of property values. Each property value
              contains a name and value property. Each property will be visible in the
              template under {{ custom.NAME }}. Note: Custom properties do not currently
              support arrays. To provide a listing in an email, one workaround is to build an
              HTML list (either with tables or ul) and specify it as a custom property.

          email_id: The content ID for the email, which can be found in email tool UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/email-campaigns/2026-03/single-send",
            body=maybe_transform(
                {
                    "contact_properties": contact_properties,
                    "custom_properties": custom_properties,
                    "email_id": email_id,
                    "message": message,
                },
                single_send_create_params.SingleSendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendStatusView,
        )


class AsyncSingleSendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSingleSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSingleSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSingleSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSingleSendResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        contact_properties: Dict[str, str],
        custom_properties: Dict[str, object],
        email_id: int,
        message: PublicSingleSendEmailParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendStatusView:
        """
        Send a template email to a specific recipient.

        Args:
          contact_properties: The contactProperties field is a map of contact property values. Each contact
              property value contains a name and value property. Each property will get set on
              the contact record and will be visible in the template under {{ contact.NAME }}.
              Use these properties when you want to set a contact property while you’re
              sending the email. For example, when sending a receipt you may want to set a
              last_paid_date property, as the sending of the receipt will have information
              about the last payment.

          custom_properties: The customProperties field is a map of property values. Each property value
              contains a name and value property. Each property will be visible in the
              template under {{ custom.NAME }}. Note: Custom properties do not currently
              support arrays. To provide a listing in an email, one workaround is to build an
              HTML list (either with tables or ul) and specify it as a custom property.

          email_id: The content ID for the email, which can be found in email tool UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/email-campaigns/2026-03/single-send",
            body=await async_maybe_transform(
                {
                    "contact_properties": contact_properties,
                    "custom_properties": custom_properties,
                    "email_id": email_id,
                    "message": message,
                },
                single_send_create_params.SingleSendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendStatusView,
        )


class SingleSendResourceWithRawResponse:
    def __init__(self, single_send: SingleSendResource) -> None:
        self._single_send = single_send

        self.create = to_raw_response_wrapper(
            single_send.create,
        )


class AsyncSingleSendResourceWithRawResponse:
    def __init__(self, single_send: AsyncSingleSendResource) -> None:
        self._single_send = single_send

        self.create = async_to_raw_response_wrapper(
            single_send.create,
        )


class SingleSendResourceWithStreamingResponse:
    def __init__(self, single_send: SingleSendResource) -> None:
        self._single_send = single_send

        self.create = to_streamed_response_wrapper(
            single_send.create,
        )


class AsyncSingleSendResourceWithStreamingResponse:
    def __init__(self, single_send: AsyncSingleSendResource) -> None:
        self._single_send = single_send

        self.create = async_to_streamed_response_wrapper(
            single_send.create,
        )
