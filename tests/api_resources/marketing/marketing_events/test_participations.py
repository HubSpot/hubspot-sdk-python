# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import (
    AttendanceCounters,
    CollectionResponseWithTotalParticipationBreakdownForwardPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParticipations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_external_account_and_event_id(self, client: HubSpot) -> None:
        participation = client.marketing.marketing_events.participations.get_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_external_account_and_event_id(self, client: HubSpot) -> None:
        response = (
            client.marketing.marketing_events.participations.with_raw_response.get_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = response.parse()
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_external_account_and_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.participations.with_streaming_response.get_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = response.parse()
            assert_matches_type(AttendanceCounters, participation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_external_account_and_event_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.marketing.marketing_events.participations.with_raw_response.get_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.participations.with_raw_response.get_by_external_account_and_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_id(self, client: HubSpot) -> None:
        participation = client.marketing.marketing_events.participations.get_by_id(
            0,
        )
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.participations.with_raw_response.get_by_id(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = response.parse()
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.participations.with_streaming_response.get_by_id(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = response.parse()
            assert_matches_type(AttendanceCounters, participation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_breakdown_by_contact(self, client: HubSpot) -> None:
        participation = client.marketing.marketing_events.participations.list_breakdown_by_contact(
            contact_identifier="contactIdentifier",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_breakdown_by_contact_with_all_params(self, client: HubSpot) -> None:
        participation = client.marketing.marketing_events.participations.list_breakdown_by_contact(
            contact_identifier="contactIdentifier",
            after="after",
            limit=0,
            state="state",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_breakdown_by_contact(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_contact(
            contact_identifier="contactIdentifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = response.parse()
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_breakdown_by_contact(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.participations.with_streaming_response.list_breakdown_by_contact(
            contact_identifier="contactIdentifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = response.parse()
            assert_matches_type(
                CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_breakdown_by_contact(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_identifier` but received ''"):
            client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_contact(
                contact_identifier="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_breakdown_by_external_account_and_event_id(self, client: HubSpot) -> None:
        participation = (
            client.marketing.marketing_events.participations.list_breakdown_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
            )
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_breakdown_by_external_account_and_event_id_with_all_params(self, client: HubSpot) -> None:
        participation = (
            client.marketing.marketing_events.participations.list_breakdown_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                after="after",
                contact_identifier="contactIdentifier",
                limit=0,
                state="state",
            )
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_breakdown_by_external_account_and_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = response.parse()
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_breakdown_by_external_account_and_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.participations.with_streaming_response.list_breakdown_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = response.parse()
            assert_matches_type(
                CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_breakdown_by_external_account_and_event_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_external_account_and_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_breakdown_by_id(self, client: HubSpot) -> None:
        participation = client.marketing.marketing_events.participations.list_breakdown_by_id(
            marketing_event_id=0,
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_breakdown_by_id_with_all_params(self, client: HubSpot) -> None:
        participation = client.marketing.marketing_events.participations.list_breakdown_by_id(
            marketing_event_id=0,
            after="after",
            contact_identifier="contactIdentifier",
            limit=0,
            state="state",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_breakdown_by_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_id(
            marketing_event_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = response.parse()
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_breakdown_by_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.participations.with_streaming_response.list_breakdown_by_id(
            marketing_event_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = response.parse()
            assert_matches_type(
                CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncParticipations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_external_account_and_event_id(self, async_client: AsyncHubSpot) -> None:
        participation = (
            await async_client.marketing.marketing_events.participations.get_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
            )
        )
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_external_account_and_event_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.participations.with_raw_response.get_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = await response.parse()
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_external_account_and_event_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.participations.with_streaming_response.get_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = await response.parse()
            assert_matches_type(AttendanceCounters, participation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_external_account_and_event_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.marketing.marketing_events.participations.with_raw_response.get_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.participations.with_raw_response.get_by_external_account_and_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncHubSpot) -> None:
        participation = await async_client.marketing.marketing_events.participations.get_by_id(
            0,
        )
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.participations.with_raw_response.get_by_id(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = await response.parse()
        assert_matches_type(AttendanceCounters, participation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.participations.with_streaming_response.get_by_id(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = await response.parse()
            assert_matches_type(AttendanceCounters, participation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_breakdown_by_contact(self, async_client: AsyncHubSpot) -> None:
        participation = await async_client.marketing.marketing_events.participations.list_breakdown_by_contact(
            contact_identifier="contactIdentifier",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_breakdown_by_contact_with_all_params(self, async_client: AsyncHubSpot) -> None:
        participation = await async_client.marketing.marketing_events.participations.list_breakdown_by_contact(
            contact_identifier="contactIdentifier",
            after="after",
            limit=0,
            state="state",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_breakdown_by_contact(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_contact(
                contact_identifier="contactIdentifier",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = await response.parse()
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_breakdown_by_contact(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.marketing.marketing_events.participations.with_streaming_response.list_breakdown_by_contact(
                contact_identifier="contactIdentifier",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = await response.parse()
            assert_matches_type(
                CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_breakdown_by_contact(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_identifier` but received ''"):
            await async_client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_contact(
                contact_identifier="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_breakdown_by_external_account_and_event_id(self, async_client: AsyncHubSpot) -> None:
        participation = await async_client.marketing.marketing_events.participations.list_breakdown_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_breakdown_by_external_account_and_event_id_with_all_params(
        self, async_client: AsyncHubSpot
    ) -> None:
        participation = await async_client.marketing.marketing_events.participations.list_breakdown_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            after="after",
            contact_identifier="contactIdentifier",
            limit=0,
            state="state",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_breakdown_by_external_account_and_event_id(
        self, async_client: AsyncHubSpot
    ) -> None:
        response = await async_client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = await response.parse()
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_breakdown_by_external_account_and_event_id(
        self, async_client: AsyncHubSpot
    ) -> None:
        async with async_client.marketing.marketing_events.participations.with_streaming_response.list_breakdown_by_external_account_and_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = await response.parse()
            assert_matches_type(
                CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_breakdown_by_external_account_and_event_id(
        self, async_client: AsyncHubSpot
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_external_account_and_event_id(
                external_event_id="externalEventId",
                external_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_external_account_and_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_breakdown_by_id(self, async_client: AsyncHubSpot) -> None:
        participation = await async_client.marketing.marketing_events.participations.list_breakdown_by_id(
            marketing_event_id=0,
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_breakdown_by_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        participation = await async_client.marketing.marketing_events.participations.list_breakdown_by_id(
            marketing_event_id=0,
            after="after",
            contact_identifier="contactIdentifier",
            limit=0,
            state="state",
        )
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_breakdown_by_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.participations.with_raw_response.list_breakdown_by_id(
            marketing_event_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participation = await response.parse()
        assert_matches_type(
            CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_breakdown_by_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.participations.with_streaming_response.list_breakdown_by_id(
            marketing_event_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participation = await response.parse()
            assert_matches_type(
                CollectionResponseWithTotalParticipationBreakdownForwardPaging, participation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
