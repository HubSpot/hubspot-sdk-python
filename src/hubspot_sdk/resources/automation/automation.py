# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .sequences import (
    SequencesResource,
    AsyncSequencesResource,
    SequencesResourceWithRawResponse,
    AsyncSequencesResourceWithRawResponse,
    SequencesResourceWithStreamingResponse,
    AsyncSequencesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .actions.actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)

__all__ = ["AutomationResource", "AsyncAutomationResource"]


class AutomationResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def sequences(self) -> SequencesResource:
        return SequencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AutomationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AutomationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AutomationResourceWithStreamingResponse(self)


class AsyncAutomationResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def sequences(self) -> AsyncSequencesResource:
        return AsyncSequencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAutomationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncAutomationResourceWithStreamingResponse(self)


class AutomationResourceWithRawResponse:
    def __init__(self, automation: AutomationResource) -> None:
        self._automation = automation

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._automation.actions)

    @cached_property
    def sequences(self) -> SequencesResourceWithRawResponse:
        return SequencesResourceWithRawResponse(self._automation.sequences)


class AsyncAutomationResourceWithRawResponse:
    def __init__(self, automation: AsyncAutomationResource) -> None:
        self._automation = automation

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._automation.actions)

    @cached_property
    def sequences(self) -> AsyncSequencesResourceWithRawResponse:
        return AsyncSequencesResourceWithRawResponse(self._automation.sequences)


class AutomationResourceWithStreamingResponse:
    def __init__(self, automation: AutomationResource) -> None:
        self._automation = automation

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._automation.actions)

    @cached_property
    def sequences(self) -> SequencesResourceWithStreamingResponse:
        return SequencesResourceWithStreamingResponse(self._automation.sequences)


class AsyncAutomationResourceWithStreamingResponse:
    def __init__(self, automation: AsyncAutomationResource) -> None:
        self._automation = automation

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._automation.actions)

    @cached_property
    def sequences(self) -> AsyncSequencesResourceWithStreamingResponse:
        return AsyncSequencesResourceWithStreamingResponse(self._automation.sequences)
