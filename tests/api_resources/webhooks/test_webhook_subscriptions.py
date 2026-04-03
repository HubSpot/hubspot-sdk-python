# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.webhooks import (
    FilterResponse,
    SettingsResponse,
    FilterCreateResponse,
    SubscriptionResponse,
    SubscriptionResponse1,
    SnapshotStatusResponse,
    SubscriptionListResponse,
    CrmObjectSnapshotBatchResponse,
    CollectionResponseSubscriptionResponseNoPaging,
    WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_crm_snapshot(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_crm_snapshot(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        )
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_crm_snapshot(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_crm_snapshot(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_crm_snapshot(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_crm_snapshot(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(CrmObjectSnapshotBatchResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_1(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_1(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_1(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_2(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_2(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_2(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_3(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_3(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_3(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_4(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_4(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_4(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_subscription(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_subscription_with_all_params(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
            event_type_name="eventTypeName",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_subscription(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_subscription(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_subscription_filter(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.create_subscription_filter(
            filter={
                "conditions": [
                    {
                        "filter_type": "CRM_OBJECT_PROPERTY",
                        "operator": "CONTAINS",
                        "property": "property",
                    }
                ]
            },
            subscription_id=0,
        )
        assert_matches_type(FilterCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_subscription_filter(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.create_subscription_filter(
            filter={
                "conditions": [
                    {
                        "filter_type": "CRM_OBJECT_PROPERTY",
                        "operator": "CONTAINS",
                        "property": "property",
                    }
                ]
            },
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(FilterCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_subscription_filter(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.create_subscription_filter(
            filter={
                "conditions": [
                    {
                        "filter_type": "CRM_OBJECT_PROPERTY",
                        "operator": "CONTAINS",
                        "property": "property",
                    }
                ]
            },
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(FilterCreateResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_journal_subscription(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.delete_journal_subscription(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_journal_subscription(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.delete_journal_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_journal_subscription(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.delete_journal_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_portal_subscriptions(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.delete_portal_subscriptions(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_portal_subscriptions(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.delete_portal_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_portal_subscriptions(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.delete_portal_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_settings(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.delete_settings(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_settings(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.delete_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_settings(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.delete_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_subscription(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.delete_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_subscription(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_subscription(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_subscription_filter(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.delete_subscription_filter(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_subscription_filter(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.delete_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_subscription_filter(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.delete_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_journal_earliest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_earliest()
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_journal_earliest_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_earliest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_journal_earliest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = client.webhooks.webhook_subscriptions.with_raw_response.get_journal_earliest()

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_journal_earliest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with (
            client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_earliest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, StreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_journal_latest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_latest()
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_journal_latest_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_latest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_journal_latest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = client.webhooks.webhook_subscriptions.with_raw_response.get_journal_latest()

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_journal_latest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_latest() as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, StreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_journal_next_by_offset(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_next_by_offset(
            offset="offset",
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_journal_next_by_offset_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_next_by_offset(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_journal_next_by_offset(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = client.webhooks.webhook_subscriptions.with_raw_response.get_journal_next_by_offset(
            offset="offset",
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_journal_next_by_offset(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_next_by_offset(
            offset="offset",
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, StreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_journal_next_by_offset(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.webhook_subscriptions.with_raw_response.get_journal_next_by_offset(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_status(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_journal_status(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_journal_status(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_journal_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            client.webhooks.webhook_subscriptions.with_raw_response.get_journal_status(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_local_journal_earliest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_earliest()
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_local_journal_earliest_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_earliest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_local_journal_earliest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_earliest()

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_local_journal_earliest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with (
            client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_earliest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, StreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_local_journal_latest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_latest()
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_local_journal_latest_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_latest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_local_journal_latest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_latest()

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_local_journal_latest(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with (
            client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_latest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, StreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_local_journal_next_by_offset(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_next_by_offset(
            offset="offset",
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_local_journal_next_by_offset_with_all_params(
        self, client: Hubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_next_by_offset(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_local_journal_next_by_offset(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_next_by_offset(
            offset="offset",
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_local_journal_next_by_offset(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_next_by_offset(
            offset="offset",
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, StreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_local_journal_next_by_offset(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_next_by_offset(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_local_journal_status(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_local_journal_status(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_local_journal_status(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_local_journal_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_settings(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.get_settings(
            0,
        )
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_settings(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_settings(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscription(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.get_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscription(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.get_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscription(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscription_filter(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.get_subscription_filter(
            0,
        )
        assert_matches_type(FilterResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscription_filter(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.get_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(FilterResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscription_filter(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(FilterResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscription_filter_for_subscription(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.get_subscription_filter_for_subscription(
            0,
        )
        assert_matches_type(
            WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse, webhook_subscription, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscription_filter_for_subscription(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.get_subscription_filter_for_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(
            WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse, webhook_subscription, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscription_filter_for_subscription(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.get_subscription_filter_for_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(
                WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse, webhook_subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_journal_subscriptions(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.list_journal_subscriptions()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_journal_subscriptions(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.list_journal_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_journal_subscriptions(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.list_journal_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscriptions(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.list_subscriptions(
            0,
        )
        assert_matches_type(SubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscriptions(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.list_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.list_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionListResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_subscription(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.update_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_subscription_with_all_params(self, client: Hubspot) -> None:
        webhook_subscription = client.webhooks.webhook_subscriptions.update_subscription(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_subscription(self, client: Hubspot) -> None:
        response = client.webhooks.webhook_subscriptions.with_raw_response.update_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_subscription(self, client: Hubspot) -> None:
        with client.webhooks.webhook_subscriptions.with_streaming_response.update_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhookSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_crm_snapshot(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_crm_snapshot(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        )
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_crm_snapshot(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_crm_snapshot(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_crm_snapshot(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.create_crm_snapshot(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(CrmObjectSnapshotBatchResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_1(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_1(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_2(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_2(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_3(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_3(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_3(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_4(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_journal_subscription()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_4(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_journal_subscription()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_4(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.create_journal_subscription()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse1, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_subscription(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_subscription_with_all_params(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
            event_type_name="eventTypeName",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.create_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_subscription_filter(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.create_subscription_filter(
            filter={
                "conditions": [
                    {
                        "filter_type": "CRM_OBJECT_PROPERTY",
                        "operator": "CONTAINS",
                        "property": "property",
                    }
                ]
            },
            subscription_id=0,
        )
        assert_matches_type(FilterCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_subscription_filter(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.create_subscription_filter(
            filter={
                "conditions": [
                    {
                        "filter_type": "CRM_OBJECT_PROPERTY",
                        "operator": "CONTAINS",
                        "property": "property",
                    }
                ]
            },
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(FilterCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_subscription_filter(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.create_subscription_filter(
            filter={
                "conditions": [
                    {
                        "filter_type": "CRM_OBJECT_PROPERTY",
                        "operator": "CONTAINS",
                        "property": "property",
                    }
                ]
            },
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(FilterCreateResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_journal_subscription(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.delete_journal_subscription(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_journal_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.delete_journal_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_journal_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.delete_journal_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_portal_subscriptions(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.delete_portal_subscriptions(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_portal_subscriptions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.delete_portal_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_portal_subscriptions(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.delete_portal_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_settings(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.delete_settings(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.delete_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.delete_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_subscription(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.delete_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.delete_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_subscription_filter(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.delete_subscription_filter(
            0,
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_subscription_filter(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.delete_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_subscription_filter(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.delete_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_journal_earliest(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_earliest()
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_journal_earliest_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_earliest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_journal_earliest(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = (
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_journal_earliest()
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_journal_earliest(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_earliest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_journal_latest(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_latest()
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_journal_latest_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_latest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_journal_latest(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_journal_latest()

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_journal_latest(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_latest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_journal_next_by_offset(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_next_by_offset(
            offset="offset",
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_journal_next_by_offset_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_next_by_offset(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_journal_next_by_offset(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = (
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_journal_next_by_offset(
                offset="offset",
            )
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_journal_next_by_offset(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_next_by_offset(
            offset="offset",
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_journal_next_by_offset(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_journal_next_by_offset(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_status(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_journal_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_journal_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_journal_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_journal_status(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_local_journal_earliest(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_earliest()
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_local_journal_earliest_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_earliest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_local_journal_earliest(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = (
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_earliest()
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_local_journal_earliest(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_earliest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_local_journal_latest(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_latest()
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_local_journal_latest_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_latest(
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_local_journal_latest(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = (
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_latest()
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_local_journal_latest(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_latest()
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_local_journal_next_by_offset(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_next_by_offset(
            offset="offset",
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_local_journal_next_by_offset_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_next_by_offset(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook_subscription.is_closed
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert cast(Any, webhook_subscription.is_closed) is True
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_local_journal_next_by_offset(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook_subscription = (
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_next_by_offset(
                offset="offset",
            )
        )

        assert webhook_subscription.is_closed is True
        assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook_subscription.json() == {"foo": "bar"}
        assert isinstance(webhook_subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_local_journal_next_by_offset(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_next_by_offset(
            offset="offset",
        ) as webhook_subscription:
            assert not webhook_subscription.is_closed
            assert webhook_subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook_subscription.json() == {"foo": "bar"}
            assert cast(Any, webhook_subscription.is_closed) is True
            assert isinstance(webhook_subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook_subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_local_journal_next_by_offset(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_next_by_offset(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_local_journal_status(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_local_journal_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_local_journal_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_local_journal_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            await async_client.webhooks.webhook_subscriptions.with_raw_response.get_local_journal_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_settings(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_settings(
            0,
        )
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscription(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscription_filter(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.get_subscription_filter(
            0,
        )
        assert_matches_type(FilterResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscription_filter(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(FilterResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscription_filter(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(FilterResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscription_filter_for_subscription(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = (
            await async_client.webhooks.webhook_subscriptions.get_subscription_filter_for_subscription(
                0,
            )
        )
        assert_matches_type(
            WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse, webhook_subscription, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscription_filter_for_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.get_subscription_filter_for_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(
            WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse, webhook_subscription, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscription_filter_for_subscription(
        self, async_client: AsyncHubspot
    ) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.get_subscription_filter_for_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(
                WebhookSubscriptionGetSubscriptionFilterForSubscriptionResponse, webhook_subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_journal_subscriptions(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.list_journal_subscriptions()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_journal_subscriptions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.list_journal_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_journal_subscriptions(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.webhooks.webhook_subscriptions.with_streaming_response.list_journal_subscriptions()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.list_subscriptions(
            0,
        )
        assert_matches_type(SubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.list_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.list_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionListResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SettingsResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_subscription(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.update_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_subscription_with_all_params(self, async_client: AsyncHubspot) -> None:
        webhook_subscription = await async_client.webhooks.webhook_subscriptions.update_subscription(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_subscription(self, async_client: AsyncHubspot) -> None:
        response = await async_client.webhooks.webhook_subscriptions.with_raw_response.update_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_subscription(self, async_client: AsyncHubspot) -> None:
        async with async_client.webhooks.webhook_subscriptions.with_streaming_response.update_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(SubscriptionResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
