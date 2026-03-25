# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.app_webhooks import (
    SubscriptionResponse,
    SubscriptionListResponse,
    BatchResponseSubscriptionResponse,
)
from hubspot_sdk.types.crm.extensions import SettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAppWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_update_subscriptions(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.batch_update_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_update_subscriptions(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.batch_update_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(BatchResponseSubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_update_subscriptions(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.batch_update_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(BatchResponseSubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_subscription(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_subscription_with_all_params(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
            event_type_name="eventTypeName",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_subscription(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_subscription(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_settings(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.delete_settings(
            0,
        )
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_settings(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.delete_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_settings(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.delete_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert app_webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_subscription(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.delete_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_subscription(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_subscription(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert app_webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_settings(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.get_settings(
            0,
        )
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_settings(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_settings(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(SettingsResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscription(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.get_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscription(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.get_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscription(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.get_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscriptions(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.list_subscriptions(
            0,
        )
        assert_matches_type(SubscriptionListResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscriptions(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.list_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(SubscriptionListResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.list_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(SubscriptionListResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(SettingsResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_subscription(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.update_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_subscription_with_all_params(self, client: Hubspot) -> None:
        app_webhook = client.app_webhooks.update_subscription(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_subscription(self, client: Hubspot) -> None:
        response = client.app_webhooks.with_raw_response.update_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = response.parse()
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_subscription(self, client: Hubspot) -> None:
        with client.app_webhooks.with_streaming_response.update_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = response.parse()
            assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAppWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_update_subscriptions(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.batch_update_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_update_subscriptions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.batch_update_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(BatchResponseSubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_update_subscriptions(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.batch_update_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(BatchResponseSubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_subscription(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_subscription_with_all_params(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
            event_type_name="eventTypeName",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_settings(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.delete_settings(
            0,
        )
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.delete_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.delete_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert app_webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_subscription(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.delete_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert app_webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert app_webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_settings(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.get_settings(
            0,
        )
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(SettingsResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscription(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.get_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.get_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.get_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.list_subscriptions(
            0,
        )
        assert_matches_type(SubscriptionListResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.list_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(SubscriptionListResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.list_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(SubscriptionListResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(SettingsResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(SettingsResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_subscription(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.update_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_subscription_with_all_params(self, async_client: AsyncHubspot) -> None:
        app_webhook = await async_client.app_webhooks.update_subscription(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.app_webhooks.with_raw_response.update_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_webhook = await response.parse()
        assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.app_webhooks.with_streaming_response.update_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_webhook = await response.parse()
            assert_matches_type(SubscriptionResponse, app_webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
