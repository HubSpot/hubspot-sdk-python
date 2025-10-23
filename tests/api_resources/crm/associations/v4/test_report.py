# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.associations import ReportCreationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_request_high_usage_report(self, client: HubSpot) -> None:
        report = client.crm.associations.v4.report.request_high_usage_report(
            0,
        )
        assert_matches_type(ReportCreationResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_request_high_usage_report(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.report.with_raw_response.request_high_usage_report(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCreationResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_request_high_usage_report(self, client: HubSpot) -> None:
        with client.crm.associations.v4.report.with_streaming_response.request_high_usage_report(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCreationResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_request_high_usage_report(self, async_client: AsyncHubSpot) -> None:
        report = await async_client.crm.associations.v4.report.request_high_usage_report(
            0,
        )
        assert_matches_type(ReportCreationResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_request_high_usage_report(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.report.with_raw_response.request_high_usage_report(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCreationResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_request_high_usage_report(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.report.with_streaming_response.request_high_usage_report(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCreationResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
