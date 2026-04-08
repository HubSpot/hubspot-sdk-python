# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ....types.cms.pages import (
    a_b_test_end_site_page_test_params,
    a_b_test_rerun_site_page_test_params,
    a_b_test_end_landing_page_test_params,
    a_b_test_rerun_landing_page_test_params,
    a_b_test_create_site_page_variation_params,
    a_b_test_create_landing_page_variation_params,
)
from ....types.cms.page_data import PageData

__all__ = ["ABTestsResource", "AsyncABTestsResource"]


class ABTestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ABTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ABTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ABTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ABTestsResourceWithStreamingResponse(self)

    def create_landing_page_variation(
        self,
        *,
        content_id: str,
        variation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageData:
        """
        Create a new A/B test variation based on the information provided in the request
        body.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/ab-test/create-variation",
            body=maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                a_b_test_create_landing_page_variation_params.ABTestCreateLandingPageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageData,
        )

    def create_site_page_variation(
        self,
        *,
        content_id: str,
        variation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageData:
        """
        Create a new A/B test variation based on the information provided in the request
        body.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/site-pages/ab-test/create-variation",
            body=maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                a_b_test_create_site_page_variation_params.ABTestCreateSitePageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageData,
        )

    def end_landing_page_test(
        self,
        *,
        ab_test_id: str,
        winner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        End an active A/B test and designate a winner.

        Args:
          ab_test_id: ID of the test to end.

          winner_id: ID of the object to designate as the test winner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/landing-pages/ab-test/end",
            body=maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "winner_id": winner_id,
                },
                a_b_test_end_landing_page_test_params.ABTestEndLandingPageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def end_site_page_test(
        self,
        *,
        ab_test_id: str,
        winner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        End an active A/B test and designate a winner.

        Args:
          ab_test_id: ID of the test to end.

          winner_id: ID of the object to designate as the test winner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/site-pages/ab-test/end",
            body=maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "winner_id": winner_id,
                },
                a_b_test_end_site_page_test_params.ABTestEndSitePageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rerun_landing_page_test(
        self,
        *,
        ab_test_id: str,
        variation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rerun a previous A/B test.

        Args:
          ab_test_id: ID of the test to rerun.

          variation_id: ID of the object to reactivate as a test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/landing-pages/ab-test/rerun",
            body=maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "variation_id": variation_id,
                },
                a_b_test_rerun_landing_page_test_params.ABTestRerunLandingPageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rerun_site_page_test(
        self,
        *,
        ab_test_id: str,
        variation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rerun a previous A/B test.

        Args:
          ab_test_id: ID of the test to rerun.

          variation_id: ID of the object to reactivate as a test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/pages/2026-03/site-pages/ab-test/rerun",
            body=maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "variation_id": variation_id,
                },
                a_b_test_rerun_site_page_test_params.ABTestRerunSitePageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncABTestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncABTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncABTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncABTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncABTestsResourceWithStreamingResponse(self)

    async def create_landing_page_variation(
        self,
        *,
        content_id: str,
        variation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageData:
        """
        Create a new A/B test variation based on the information provided in the request
        body.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/ab-test/create-variation",
            body=await async_maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                a_b_test_create_landing_page_variation_params.ABTestCreateLandingPageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageData,
        )

    async def create_site_page_variation(
        self,
        *,
        content_id: str,
        variation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageData:
        """
        Create a new A/B test variation based on the information provided in the request
        body.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/site-pages/ab-test/create-variation",
            body=await async_maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                a_b_test_create_site_page_variation_params.ABTestCreateSitePageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageData,
        )

    async def end_landing_page_test(
        self,
        *,
        ab_test_id: str,
        winner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        End an active A/B test and designate a winner.

        Args:
          ab_test_id: ID of the test to end.

          winner_id: ID of the object to designate as the test winner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/landing-pages/ab-test/end",
            body=await async_maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "winner_id": winner_id,
                },
                a_b_test_end_landing_page_test_params.ABTestEndLandingPageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def end_site_page_test(
        self,
        *,
        ab_test_id: str,
        winner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        End an active A/B test and designate a winner.

        Args:
          ab_test_id: ID of the test to end.

          winner_id: ID of the object to designate as the test winner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/site-pages/ab-test/end",
            body=await async_maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "winner_id": winner_id,
                },
                a_b_test_end_site_page_test_params.ABTestEndSitePageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rerun_landing_page_test(
        self,
        *,
        ab_test_id: str,
        variation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rerun a previous A/B test.

        Args:
          ab_test_id: ID of the test to rerun.

          variation_id: ID of the object to reactivate as a test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/landing-pages/ab-test/rerun",
            body=await async_maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "variation_id": variation_id,
                },
                a_b_test_rerun_landing_page_test_params.ABTestRerunLandingPageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rerun_site_page_test(
        self,
        *,
        ab_test_id: str,
        variation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rerun a previous A/B test.

        Args:
          ab_test_id: ID of the test to rerun.

          variation_id: ID of the object to reactivate as a test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/pages/2026-03/site-pages/ab-test/rerun",
            body=await async_maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "variation_id": variation_id,
                },
                a_b_test_rerun_site_page_test_params.ABTestRerunSitePageTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ABTestsResourceWithRawResponse:
    def __init__(self, a_b_tests: ABTestsResource) -> None:
        self._a_b_tests = a_b_tests

        self.create_landing_page_variation = to_raw_response_wrapper(
            a_b_tests.create_landing_page_variation,
        )
        self.create_site_page_variation = to_raw_response_wrapper(
            a_b_tests.create_site_page_variation,
        )
        self.end_landing_page_test = to_raw_response_wrapper(
            a_b_tests.end_landing_page_test,
        )
        self.end_site_page_test = to_raw_response_wrapper(
            a_b_tests.end_site_page_test,
        )
        self.rerun_landing_page_test = to_raw_response_wrapper(
            a_b_tests.rerun_landing_page_test,
        )
        self.rerun_site_page_test = to_raw_response_wrapper(
            a_b_tests.rerun_site_page_test,
        )


class AsyncABTestsResourceWithRawResponse:
    def __init__(self, a_b_tests: AsyncABTestsResource) -> None:
        self._a_b_tests = a_b_tests

        self.create_landing_page_variation = async_to_raw_response_wrapper(
            a_b_tests.create_landing_page_variation,
        )
        self.create_site_page_variation = async_to_raw_response_wrapper(
            a_b_tests.create_site_page_variation,
        )
        self.end_landing_page_test = async_to_raw_response_wrapper(
            a_b_tests.end_landing_page_test,
        )
        self.end_site_page_test = async_to_raw_response_wrapper(
            a_b_tests.end_site_page_test,
        )
        self.rerun_landing_page_test = async_to_raw_response_wrapper(
            a_b_tests.rerun_landing_page_test,
        )
        self.rerun_site_page_test = async_to_raw_response_wrapper(
            a_b_tests.rerun_site_page_test,
        )


class ABTestsResourceWithStreamingResponse:
    def __init__(self, a_b_tests: ABTestsResource) -> None:
        self._a_b_tests = a_b_tests

        self.create_landing_page_variation = to_streamed_response_wrapper(
            a_b_tests.create_landing_page_variation,
        )
        self.create_site_page_variation = to_streamed_response_wrapper(
            a_b_tests.create_site_page_variation,
        )
        self.end_landing_page_test = to_streamed_response_wrapper(
            a_b_tests.end_landing_page_test,
        )
        self.end_site_page_test = to_streamed_response_wrapper(
            a_b_tests.end_site_page_test,
        )
        self.rerun_landing_page_test = to_streamed_response_wrapper(
            a_b_tests.rerun_landing_page_test,
        )
        self.rerun_site_page_test = to_streamed_response_wrapper(
            a_b_tests.rerun_site_page_test,
        )


class AsyncABTestsResourceWithStreamingResponse:
    def __init__(self, a_b_tests: AsyncABTestsResource) -> None:
        self._a_b_tests = a_b_tests

        self.create_landing_page_variation = async_to_streamed_response_wrapper(
            a_b_tests.create_landing_page_variation,
        )
        self.create_site_page_variation = async_to_streamed_response_wrapper(
            a_b_tests.create_site_page_variation,
        )
        self.end_landing_page_test = async_to_streamed_response_wrapper(
            a_b_tests.end_landing_page_test,
        )
        self.end_site_page_test = async_to_streamed_response_wrapper(
            a_b_tests.end_site_page_test,
        )
        self.rerun_landing_page_test = async_to_streamed_response_wrapper(
            a_b_tests.rerun_landing_page_test,
        )
        self.rerun_site_page_test = async_to_streamed_response_wrapper(
            a_b_tests.rerun_site_page_test,
        )
