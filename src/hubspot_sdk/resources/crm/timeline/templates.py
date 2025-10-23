# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.timeline import template_create_params, template_update_params
from ....types.crm.timeline_event_template import TimelineEventTemplate
from ....types.crm.timeline_event_template_token_param import TimelineEventTemplateTokenParam
from ....types.crm.collection_response_timeline_event_template_no_paging import (
    CollectionResponseTimelineEventTemplateNoPaging,
)

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        name: str,
        object_type: str,
        tokens: Iterable[TimelineEventTemplateTokenParam],
        detail_template: str | Omit = omit,
        header_template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplate:
        """
        Event templates define the general structure for a custom timeline event, and
        enable you to send event data to HubSpot. A template includes formatted copy for
        its heading and details, as well as any custom property definitions. A single
        app can include up to 750 event templates.<br/><Warning>the `v1` and `v3`
        timeline events APIs are only available for app partners with existing `v1`/`v3`
        timeline events defined in their public app. <ul><li>If your app doesn't include
        any timeline events yet, requests to this endpoint will fail. Instead, you can
        get started on
        [latest version of the developer platform](/apps/developer-platform/build-apps/overview).
        Note that you'll need to request approval before you can define app events for
        your app. Learn more in the
        [app events overview](/apps/developer-platform/add-features/app-events/overview).</li><li>If
        your app includes a `v1`/`v3` timeline event, learn how to
        [migrate it to the developer platform](/apps/developer-platform/add-features/app-events/create-and-manage-event-types#migrate-an-existing-timeline-event-type).
        You don't need to request approval before migrating existing event
        types.</li></ul>If you're not an app partner, you can send custom event data to
        HubSpot using the
        [custom events API](/api-reference/events-manage-event-definitions-v3/guide).</Warning>

        Args:
          name: The template name.

          object_type: The type of CRM object this template is for. [Contacts, companies, tickets, and
              deals] are supported.

          tokens: A collection of tokens that can be used as custom properties on the event and to
              create fully fledged CRM objects.

          detail_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline when you expand the details.

          header_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline as a header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/integrators/timeline/v3/{app_id}/event-templates",
            body=maybe_transform(
                {
                    "name": name,
                    "object_type": object_type,
                    "tokens": tokens,
                    "detail_template": detail_template,
                    "header_template": header_template,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplate,
        )

    def update(
        self,
        event_template_id: str,
        *,
        app_id: int,
        id: str,
        name: str,
        tokens: Iterable[TimelineEventTemplateTokenParam],
        detail_template: str | Omit = omit,
        header_template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplate:
        """
        Update an existing event template, specified by ID.

        Args:
          id: The template ID.

          name: The template name.

          tokens: A collection of tokens that can be used as custom properties on the event and to
              create fully fledged CRM objects.

          detail_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline when you expand the details.

          header_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline as a header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        return self._put(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "tokens": tokens,
                    "detail_template": detail_template,
                    "header_template": header_template,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplate,
        )

    def list(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseTimelineEventTemplateNoPaging:
        """
        Retrieve all templates defined for an app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/integrators/timeline/v3/{app_id}/event-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseTimelineEventTemplateNoPaging,
        )

    def delete(
        self,
        event_template_id: str,
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
        Delete an event type template by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        event_template_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplate:
        """
        Retrieve an event type template by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        return self._get(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplate,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        name: str,
        object_type: str,
        tokens: Iterable[TimelineEventTemplateTokenParam],
        detail_template: str | Omit = omit,
        header_template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplate:
        """
        Event templates define the general structure for a custom timeline event, and
        enable you to send event data to HubSpot. A template includes formatted copy for
        its heading and details, as well as any custom property definitions. A single
        app can include up to 750 event templates.<br/><Warning>the `v1` and `v3`
        timeline events APIs are only available for app partners with existing `v1`/`v3`
        timeline events defined in their public app. <ul><li>If your app doesn't include
        any timeline events yet, requests to this endpoint will fail. Instead, you can
        get started on
        [latest version of the developer platform](/apps/developer-platform/build-apps/overview).
        Note that you'll need to request approval before you can define app events for
        your app. Learn more in the
        [app events overview](/apps/developer-platform/add-features/app-events/overview).</li><li>If
        your app includes a `v1`/`v3` timeline event, learn how to
        [migrate it to the developer platform](/apps/developer-platform/add-features/app-events/create-and-manage-event-types#migrate-an-existing-timeline-event-type).
        You don't need to request approval before migrating existing event
        types.</li></ul>If you're not an app partner, you can send custom event data to
        HubSpot using the
        [custom events API](/api-reference/events-manage-event-definitions-v3/guide).</Warning>

        Args:
          name: The template name.

          object_type: The type of CRM object this template is for. [Contacts, companies, tickets, and
              deals] are supported.

          tokens: A collection of tokens that can be used as custom properties on the event and to
              create fully fledged CRM objects.

          detail_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline when you expand the details.

          header_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline as a header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/integrators/timeline/v3/{app_id}/event-templates",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_type": object_type,
                    "tokens": tokens,
                    "detail_template": detail_template,
                    "header_template": header_template,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplate,
        )

    async def update(
        self,
        event_template_id: str,
        *,
        app_id: int,
        id: str,
        name: str,
        tokens: Iterable[TimelineEventTemplateTokenParam],
        detail_template: str | Omit = omit,
        header_template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplate:
        """
        Update an existing event template, specified by ID.

        Args:
          id: The template ID.

          name: The template name.

          tokens: A collection of tokens that can be used as custom properties on the event and to
              create fully fledged CRM objects.

          detail_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline when you expand the details.

          header_template: This uses Markdown syntax with Handlebars and event-specific data to render HTML
              on a timeline as a header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        return await self._put(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "tokens": tokens,
                    "detail_template": detail_template,
                    "header_template": header_template,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplate,
        )

    async def list(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseTimelineEventTemplateNoPaging:
        """
        Retrieve all templates defined for an app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/integrators/timeline/v3/{app_id}/event-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseTimelineEventTemplateNoPaging,
        )

    async def delete(
        self,
        event_template_id: str,
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
        Delete an event type template by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        event_template_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimelineEventTemplate:
        """
        Retrieve an event type template by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_template_id:
            raise ValueError(f"Expected a non-empty value for `event_template_id` but received {event_template_id!r}")
        return await self._get(
            f"/integrators/timeline/v3/{app_id}/event-templates/{event_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimelineEventTemplate,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.update = to_raw_response_wrapper(
            templates.update,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )
        self.get = to_raw_response_wrapper(
            templates.get,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.update = async_to_raw_response_wrapper(
            templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            templates.get,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.update = to_streamed_response_wrapper(
            templates.update,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )
        self.get = to_streamed_response_wrapper(
            templates.get,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.update = async_to_streamed_response_wrapper(
            templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            templates.get,
        )
