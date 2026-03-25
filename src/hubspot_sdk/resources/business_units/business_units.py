# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import business_units_ as business_units
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BusinessUnitsResource", "AsyncBusinessUnitsResource"]


class BusinessUnitsResource(SyncAPIResource):
    @cached_property
    def business_units(self) -> business_units.BusinessUnitsResource:
        return business_units.BusinessUnitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BusinessUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BusinessUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BusinessUnitsResourceWithStreamingResponse(self)


class AsyncBusinessUnitsResource(AsyncAPIResource):
    @cached_property
    def business_units(self) -> business_units.AsyncBusinessUnitsResource:
        return business_units.AsyncBusinessUnitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBusinessUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBusinessUnitsResourceWithStreamingResponse(self)


class BusinessUnitsResourceWithRawResponse:
    def __init__(self, business_units: BusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_units(self) -> business_units.BusinessUnitsResourceWithRawResponse:
        return business_units.BusinessUnitsResourceWithRawResponse(self._business_units.business_units)


class AsyncBusinessUnitsResourceWithRawResponse:
    def __init__(self, business_units: AsyncBusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_units(self) -> business_units.AsyncBusinessUnitsResourceWithRawResponse:
        return business_units.AsyncBusinessUnitsResourceWithRawResponse(self._business_units.business_units)


class BusinessUnitsResourceWithStreamingResponse:
    def __init__(self, business_units: BusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_units(self) -> business_units.BusinessUnitsResourceWithStreamingResponse:
        return business_units.BusinessUnitsResourceWithStreamingResponse(self._business_units.business_units)


class AsyncBusinessUnitsResourceWithStreamingResponse:
    def __init__(self, business_units: AsyncBusinessUnitsResource) -> None:
        self._business_units = business_units

    @cached_property
    def business_units(self) -> business_units.AsyncBusinessUnitsResourceWithStreamingResponse:
        return business_units.AsyncBusinessUnitsResourceWithStreamingResponse(self._business_units.business_units)
