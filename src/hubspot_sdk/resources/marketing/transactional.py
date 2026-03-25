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
from ...types.marketing import transactional_send_params
from ...types.marketing.email_send_status_view import EmailSendStatusView
from ...types.marketing.public_single_send_email_param import PublicSingleSendEmailParam

__all__ = ["TransactionalResource", "AsyncTransactionalResource"]


class TransactionalResource(SyncAPIResource):
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

    def send(
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
        Args:
          contact_properties: The contactProperties field is a map of contact property values. Each contact
              property value contains a name and value property. Each property will get set on
              the contact record and will be visible in the template under {{ contact.NAME }}.
              Use these properties when you want to set a contact property while you’re
              sending the email. For example, when sending a reciept you may want to set a
              last_paid_date property, as the sending of the receipt will have information
              about the last payment.

          custom_properties: The customProperties field is a map of property values. Each property value
              contains a name and value property. Each property will be visible in the
              template under {{ custom.NAME }}. Note: Custom properties do not currently
              support arrays. To provide a listing in an email, one workaround is to build an
              HTML list (either with tables or ul) and specify it as a custom property.

          email_id: The content ID for the transactional email, which can be found in email tool UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/transactional/2026-03/single-email/send",
            body=maybe_transform(
                {
                    "contact_properties": contact_properties,
                    "custom_properties": custom_properties,
                    "email_id": email_id,
                    "message": message,
                },
                transactional_send_params.TransactionalSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendStatusView,
        )


class AsyncTransactionalResource(AsyncAPIResource):
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

    async def send(
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
        Args:
          contact_properties: The contactProperties field is a map of contact property values. Each contact
              property value contains a name and value property. Each property will get set on
              the contact record and will be visible in the template under {{ contact.NAME }}.
              Use these properties when you want to set a contact property while you’re
              sending the email. For example, when sending a reciept you may want to set a
              last_paid_date property, as the sending of the receipt will have information
              about the last payment.

          custom_properties: The customProperties field is a map of property values. Each property value
              contains a name and value property. Each property will be visible in the
              template under {{ custom.NAME }}. Note: Custom properties do not currently
              support arrays. To provide a listing in an email, one workaround is to build an
              HTML list (either with tables or ul) and specify it as a custom property.

          email_id: The content ID for the transactional email, which can be found in email tool UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/transactional/2026-03/single-email/send",
            body=await async_maybe_transform(
                {
                    "contact_properties": contact_properties,
                    "custom_properties": custom_properties,
                    "email_id": email_id,
                    "message": message,
                },
                transactional_send_params.TransactionalSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendStatusView,
        )


class TransactionalResourceWithRawResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

        self.send = to_raw_response_wrapper(
            transactional.send,
        )


class AsyncTransactionalResourceWithRawResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

        self.send = async_to_raw_response_wrapper(
            transactional.send,
        )


class TransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

        self.send = to_streamed_response_wrapper(
            transactional.send,
        )


class AsyncTransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

        self.send = async_to_streamed_response_wrapper(
            transactional.send,
        )
