# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.webhooks_journal import (
    JournalSubscriptionResponse,
    JournalCollectionResponseSubscriptionResponseNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.create(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.create(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.create(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.list()
        assert_matches_type(JournalCollectionResponseSubscriptionResponseNoPaging, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalCollectionResponseSubscriptionResponseNoPaging, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalCollectionResponseSubscriptionResponseNoPaging, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.delete(
            0,
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_for_portal(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.delete_for_portal(
            0,
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_for_portal(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.delete_for_portal(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_for_portal(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.delete_for_portal(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        subscription = client.webhooks_journal.subscriptions.get(
            0,
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.webhooks_journal.subscriptions.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.webhooks_journal.subscriptions.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.create(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.create(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.create(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.create(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.create(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.create(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.list()
        assert_matches_type(JournalCollectionResponseSubscriptionResponseNoPaging, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalCollectionResponseSubscriptionResponseNoPaging, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalCollectionResponseSubscriptionResponseNoPaging, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.delete(
            0,
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_for_portal(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.delete_for_portal(
            0,
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_for_portal(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.delete_for_portal(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_for_portal(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.delete_for_portal(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        subscription = await async_client.webhooks_journal.subscriptions.get(
            0,
        )
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.subscriptions.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.subscriptions.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(JournalSubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
