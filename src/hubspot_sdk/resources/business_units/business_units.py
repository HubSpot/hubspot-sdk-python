# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .business_unit_entries import (
    BusinessUnitEntriesResource,
    AsyncBusinessUnitEntriesResource,
    BusinessUnitEntriesResourceWithRawResponse,
    AsyncBusinessUnitEntriesResourceWithRawResponse,
    BusinessUnitEntriesResourceWithStreamingResponse,
    AsyncBusinessUnitEntriesResourceWithStreamingResponse,
)

__all__ = ["BusinessUnitsResource", "AsyncBusinessUnitsResource"]


class BusinessUnitsResource(SyncAPIResource):
    @cached_property
    def business_unit_entries(self) -> BusinessUnitEntriesResource:
        return BusinessUnitEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BusinessUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BusinessUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return BusinessUnitsResourceWithStreamingResponse(self)


class AsyncBusinessUnitsResource(AsyncAPIResource):
    @cached_property
    def business_unit_entries(self) -> AsyncBusinessUnitEntriesResource:
        return AsyncBusinessUnitEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBusinessUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBusinessUnitsResourceWithStreamingResponse(self)


class BusinessUnitsResourceWithRawResponse:
    def __init__(self, business_units: BusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_unit_entries(self) -> BusinessUnitEntriesResourceWithRawResponse:
        return BusinessUnitEntriesResourceWithRawResponse(self._business_units.business_unit_entries)


class AsyncBusinessUnitsResourceWithRawResponse:
    def __init__(self, business_units: AsyncBusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_unit_entries(self) -> AsyncBusinessUnitEntriesResourceWithRawResponse:
        return AsyncBusinessUnitEntriesResourceWithRawResponse(self._business_units.business_unit_entries)


class BusinessUnitsResourceWithStreamingResponse:
    def __init__(self, business_units: BusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_unit_entries(self) -> BusinessUnitEntriesResourceWithStreamingResponse:
        return BusinessUnitEntriesResourceWithStreamingResponse(self._business_units.business_unit_entries)


class AsyncBusinessUnitsResourceWithStreamingResponse:
    def __init__(self, business_units: AsyncBusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_unit_entries(self) -> AsyncBusinessUnitEntriesResourceWithStreamingResponse:
        return AsyncBusinessUnitEntriesResourceWithStreamingResponse(self._business_units.business_unit_entries)
