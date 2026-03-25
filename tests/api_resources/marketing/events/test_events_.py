# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.marketing import MarketingEventDefaultResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_by_external_event_id(self, client: Hubspot) -> None:
        event = client.marketing.events.events.cancel_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_by_external_event_id(self, client: Hubspot) -> None:
        response = client.marketing.events.events.with_raw_response.cancel_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_by_external_event_id(self, client: Hubspot) -> None:
        with client.marketing.events.events.with_streaming_response.cancel_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_by_external_event_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.events.with_raw_response.cancel_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_by_external_event_id(self, client: Hubspot) -> None:
        event = client.marketing.events.events.complete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_by_external_event_id(self, client: Hubspot) -> None:
        response = client.marketing.events.events.with_raw_response.complete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_by_external_event_id(self, client: Hubspot) -> None:
        with client.marketing.events.events.with_streaming_response.complete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete_by_external_event_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.events.with_raw_response.complete_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
                end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        event = await async_client.marketing.events.events.cancel_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.events.with_raw_response.cancel_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.events.with_streaming_response.cancel_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.events.with_raw_response.cancel_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        event = await async_client.marketing.events.events.complete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.events.with_raw_response.complete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.events.with_streaming_response.complete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(MarketingEventDefaultResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete_by_external_event_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.events.with_raw_response.complete_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
                end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            )
