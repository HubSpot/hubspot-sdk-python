# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.shared import (
    FilterResponse,
    FilterCreateResponse,
    SnapshotStatusResponse,
    CrmObjectSnapshotBatchResponse,
    BatchResponseJournalFetchResponse,
)
from hubspot_sdk.types.webhooks import (
    SettingsResponse,
    SubscriptionResponse as WebhooksSubscriptionResponse,
    SubscriptionListResponse,
    BatchResponseSubscriptionResponse,
    WebhookListSubscriptionFiltersResponse,
)
from hubspot_sdk.types.webhooks_journal import (
    SubscriptionResponse as WebhooksJournalSubscriptionResponse,
    CollectionResponseSubscriptionResponseNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_batch_event_subscriptions(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_batch_event_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_batch_event_subscriptions(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_batch_event_subscriptions(
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
        webhook = response.parse()
        assert_matches_type(BatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_batch_event_subscriptions(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_batch_event_subscriptions(
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

            webhook = response.parse()
            assert_matches_type(BatchResponseSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_crm_snapshots(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_crm_snapshots(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        )
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_crm_snapshots(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_crm_snapshots(
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
        webhook = response.parse()
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_crm_snapshots(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_crm_snapshots(
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

            webhook = response.parse()
            assert_matches_type(CrmObjectSnapshotBatchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_subscription(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_event_subscription_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
            event_type_name="eventTypeName",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_event_subscription(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_event_subscription(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_1(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_1(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_1(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_2(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_2(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_2(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_3(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_journal_subscription(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_3(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_journal_subscription(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_3(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_journal_subscription(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_4(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_4(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_4(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_journal_subscription_overload_5(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_journal_subscription_overload_5(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_journal_subscription_overload_5(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_subscription_filter(self, client: HubSpot) -> None:
        webhook = client.webhooks.create_subscription_filter(
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
        assert_matches_type(FilterCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_subscription_filter(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create_subscription_filter(
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
        webhook = response.parse()
        assert_matches_type(FilterCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_subscription_filter(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create_subscription_filter(
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

            webhook = response.parse()
            assert_matches_type(FilterCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_event_subscription(self, client: HubSpot) -> None:
        webhook = client.webhooks.delete_event_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_event_subscription(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.delete_event_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_event_subscription(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.delete_event_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_journal_subscription(self, client: HubSpot) -> None:
        webhook = client.webhooks.delete_journal_subscription(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_journal_subscription(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.delete_journal_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_journal_subscription(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.delete_journal_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_journal_subscription_for_portal(self, client: HubSpot) -> None:
        webhook = client.webhooks.delete_journal_subscription_for_portal(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_journal_subscription_for_portal(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.delete_journal_subscription_for_portal(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_journal_subscription_for_portal(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.delete_journal_subscription_for_portal(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_settings(self, client: HubSpot) -> None:
        webhook = client.webhooks.delete_settings(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_settings(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.delete_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_settings(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.delete_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_subscription_filter(self, client: HubSpot) -> None:
        webhook = client.webhooks.delete_subscription_filter(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_subscription_filter(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.delete_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_subscription_filter(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.delete_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest_journal_batch(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_earliest_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest_journal_batch_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_earliest_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earliest_journal_batch(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_earliest_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earliest_journal_batch(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_earliest_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_earliest_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_earliest_journal_entry()
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_earliest_journal_entry_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_earliest_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_earliest_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = client.webhooks.with_raw_response.get_earliest_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_earliest_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.with_streaming_response.get_earliest_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, StreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest_local_journal_batch(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_earliest_local_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earliest_local_journal_batch_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_earliest_local_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earliest_local_journal_batch(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_earliest_local_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earliest_local_journal_batch(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_earliest_local_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_earliest_local_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_earliest_local_journal_entry()
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_earliest_local_journal_entry_with_all_params(
        self, client: HubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_earliest_local_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_earliest_local_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = client.webhooks.with_raw_response.get_earliest_local_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_earliest_local_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.with_streaming_response.get_earliest_local_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, StreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_event_subscription(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_event_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_event_subscription(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_event_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_event_subscription(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_event_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_batch_by_request(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_journal_batch_by_request(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_batch_by_request_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_journal_batch_by_request(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_journal_batch_by_request(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_journal_batch_by_request(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_journal_batch_by_request(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_journal_batch_by_request(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_batch_from_offset(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_journal_batch_from_offset(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_batch_from_offset_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_journal_batch_from_offset(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_journal_batch_from_offset(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_journal_batch_from_offset(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_journal_batch_from_offset(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_journal_batch_from_offset(
            count=1,
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_journal_batch_from_offset(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.with_raw_response.get_journal_batch_from_offset(
                count=1,
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_status(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_journal_status(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_journal_status(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_journal_status(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            client.webhooks.with_raw_response.get_journal_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_journal_subscription(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_journal_subscription(
            0,
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_journal_subscription(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_journal_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_journal_subscription(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_journal_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_latest_journal_batch(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_latest_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_latest_journal_batch_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_latest_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_latest_journal_batch(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_latest_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_latest_journal_batch(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_latest_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_latest_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_latest_journal_entry()
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_latest_journal_entry_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_latest_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_latest_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = client.webhooks.with_raw_response.get_latest_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_latest_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.with_streaming_response.get_latest_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, StreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_latest_local_journal_batch(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_latest_local_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_latest_local_journal_batch_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_latest_local_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_latest_local_journal_batch(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_latest_local_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_latest_local_journal_batch(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_latest_local_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_latest_local_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_latest_local_journal_entry()
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_latest_local_journal_entry_with_all_params(
        self, client: HubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_latest_local_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_latest_local_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = client.webhooks.with_raw_response.get_latest_local_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_latest_local_journal_entry(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.with_streaming_response.get_latest_local_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, StreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_local_journal_batch_by_request(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_local_journal_batch_by_request(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_local_journal_batch_by_request_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_local_journal_batch_by_request(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_local_journal_batch_by_request(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_local_journal_batch_by_request(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_local_journal_batch_by_request(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_local_journal_batch_by_request(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_local_journal_batch_from_offset(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_local_journal_batch_from_offset_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_local_journal_batch_from_offset(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_local_journal_batch_from_offset(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_local_journal_batch_from_offset(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.with_raw_response.get_local_journal_batch_from_offset(
                count=1,
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_local_journal_status(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_local_journal_status(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_local_journal_status(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_local_journal_status(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            client.webhooks.with_raw_response.get_local_journal_status(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_next_journal_entries(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_next_journal_entries(
            offset="offset",
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_next_journal_entries_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_next_journal_entries(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_next_journal_entries(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = client.webhooks.with_raw_response.get_next_journal_entries(
            offset="offset",
        )

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_next_journal_entries(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.with_streaming_response.get_next_journal_entries(
            offset="offset",
        ) as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, StreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_next_journal_entries(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.with_raw_response.get_next_journal_entries(
                offset="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_next_local_journal_entries(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_next_local_journal_entries(
            offset="offset",
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_next_local_journal_entries_with_all_params(
        self, client: HubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = client.webhooks.get_next_local_journal_entries(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_next_local_journal_entries(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = client.webhooks.with_raw_response.get_next_local_journal_entries(
            offset="offset",
        )

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_next_local_journal_entries(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks.with_streaming_response.get_next_local_journal_entries(
            offset="offset",
        ) as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, StreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_next_local_journal_entries(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks.with_raw_response.get_next_local_journal_entries(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_settings(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_settings(
            0,
        )
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_settings(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_settings(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SettingsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscription_filter(self, client: HubSpot) -> None:
        webhook = client.webhooks.get_subscription_filter(
            0,
        )
        assert_matches_type(FilterResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscription_filter(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.get_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(FilterResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscription_filter(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.get_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(FilterResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_event_subscriptions(self, client: HubSpot) -> None:
        webhook = client.webhooks.list_event_subscriptions(
            0,
        )
        assert_matches_type(SubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_event_subscriptions(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.list_event_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_event_subscriptions(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.list_event_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SubscriptionListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_journal_subscriptions(self, client: HubSpot) -> None:
        webhook = client.webhooks.list_journal_subscriptions()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_journal_subscriptions(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.list_journal_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_journal_subscriptions(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.list_journal_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscription_filters(self, client: HubSpot) -> None:
        webhook = client.webhooks.list_subscription_filters(
            0,
        )
        assert_matches_type(WebhookListSubscriptionFiltersResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscription_filters(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.list_subscription_filters(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListSubscriptionFiltersResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscription_filters(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.list_subscription_filters(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListSubscriptionFiltersResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_subscription(self, client: HubSpot) -> None:
        webhook = client.webhooks.update_event_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_subscription_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.update_event_subscription(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_event_subscription(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.update_event_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_event_subscription(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.update_event_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: HubSpot) -> None:
        webhook = client.webhooks.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SettingsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_batch_event_subscriptions(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_batch_event_subscriptions(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_batch_event_subscriptions(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_batch_event_subscriptions(
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
        webhook = await response.parse()
        assert_matches_type(BatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch_event_subscriptions(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_batch_event_subscriptions(
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

            webhook = await response.parse()
            assert_matches_type(BatchResponseSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_crm_snapshots(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_crm_snapshots(
            snapshot_requests=[
                {
                    "object_id": 0,
                    "object_type_id": "objectTypeId",
                    "portal_id": 0,
                    "properties": ["string"],
                }
            ],
        )
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_crm_snapshots(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_crm_snapshots(
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
        webhook = await response.parse()
        assert_matches_type(CrmObjectSnapshotBatchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_crm_snapshots(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_crm_snapshots(
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

            webhook = await response.parse()
            assert_matches_type(CrmObjectSnapshotBatchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_subscription(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_event_subscription_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
            event_type_name="eventTypeName",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_event_subscription(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_event_subscription(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_event_subscription(
            app_id=0,
            active=True,
            event_type="company.associationChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_1(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_1(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_1(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            properties=["string"],
            subscription_type="OBJECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_2(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_2(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_2(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            associated_object_type_ids=["string"],
            object_ids=[0],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="ASSOCIATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_3(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_journal_subscription(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_3(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_journal_subscription(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_3(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_journal_subscription(
            event_type_id="eventTypeId",
            properties=["string"],
            subscription_type="APP_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_4(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_4(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_4(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            list_ids=[0],
            object_ids=[0],
            portal_id=0,
            subscription_type="LIST_MEMBERSHIP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_journal_subscription_overload_5(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_journal_subscription(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_journal_subscription_overload_5(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_journal_subscription(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_journal_subscription_overload_5(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_journal_subscription(
            actions=["CREATE"],
            object_type_id="objectTypeId",
            portal_id=0,
            subscription_type="GDPR_PRIVACY_DELETION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create_subscription_filter(
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
        assert_matches_type(FilterCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create_subscription_filter(
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
        webhook = await response.parse()
        assert_matches_type(FilterCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create_subscription_filter(
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

            webhook = await response.parse()
            assert_matches_type(FilterCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_event_subscription(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.delete_event_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_event_subscription(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.delete_event_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_event_subscription(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.delete_event_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_journal_subscription(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.delete_journal_subscription(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_journal_subscription(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.delete_journal_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_journal_subscription(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.delete_journal_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_journal_subscription_for_portal(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.delete_journal_subscription_for_portal(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_journal_subscription_for_portal(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.delete_journal_subscription_for_portal(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_journal_subscription_for_portal(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.delete_journal_subscription_for_portal(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_settings(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.delete_settings(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_settings(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.delete_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_settings(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.delete_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.delete_subscription_filter(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.delete_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.delete_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest_journal_batch(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_earliest_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest_journal_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_earliest_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earliest_journal_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_earliest_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earliest_journal_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_earliest_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_earliest_journal_entry(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_earliest_journal_entry()
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_earliest_journal_entry_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_earliest_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_earliest_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = await async_client.webhooks.with_raw_response.get_earliest_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_earliest_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.with_streaming_response.get_earliest_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest_local_journal_batch(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_earliest_local_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earliest_local_journal_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_earliest_local_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earliest_local_journal_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_earliest_local_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earliest_local_journal_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_earliest_local_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_earliest_local_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_earliest_local_journal_entry()
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_earliest_local_journal_entry_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_earliest_local_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_earliest_local_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = await async_client.webhooks.with_raw_response.get_earliest_local_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_earliest_local_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.with_streaming_response.get_earliest_local_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_event_subscription(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_event_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_event_subscription(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_event_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_event_subscription(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_event_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_batch_by_request(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_journal_batch_by_request(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_batch_by_request_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_journal_batch_by_request(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_journal_batch_by_request(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_journal_batch_by_request(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_journal_batch_by_request(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_journal_batch_by_request(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_journal_batch_from_offset(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_batch_from_offset_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_journal_batch_from_offset(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_journal_batch_from_offset(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_journal_batch_from_offset(
            count=1,
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.with_raw_response.get_journal_batch_from_offset(
                count=1,
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_status(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_journal_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_journal_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_journal_status(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            await async_client.webhooks.with_raw_response.get_journal_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_journal_subscription(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_journal_subscription(
            0,
        )
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_journal_subscription(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_journal_subscription(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_journal_subscription(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_journal_subscription(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksJournalSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_latest_journal_batch(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_latest_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_latest_journal_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_latest_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_latest_journal_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_latest_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_latest_journal_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_latest_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_latest_journal_entry(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_latest_journal_entry()
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_latest_journal_entry_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_latest_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_latest_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = await async_client.webhooks.with_raw_response.get_latest_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_latest_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.with_streaming_response.get_latest_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_latest_local_journal_batch(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_latest_local_journal_batch(
            count=1,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_latest_local_journal_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_latest_local_journal_batch(
            count=1,
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_latest_local_journal_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_latest_local_journal_batch(
            count=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_latest_local_journal_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_latest_local_journal_batch(
            count=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_latest_local_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_latest_local_journal_entry()
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_latest_local_journal_entry_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_latest_local_journal_entry(
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_latest_local_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = await async_client.webhooks.with_raw_response.get_latest_local_journal_entry()

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_latest_local_journal_entry(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/latest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.with_streaming_response.get_latest_local_journal_entry() as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_local_journal_batch_by_request(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_local_journal_batch_by_request(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_local_journal_batch_by_request_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_local_journal_batch_by_request(
            inputs=["string"],
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_local_journal_batch_by_request(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_local_journal_batch_by_request(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_local_journal_batch_by_request(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_local_journal_batch_by_request(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_local_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_local_journal_batch_from_offset_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
            install_portal_id=0,
        )
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_local_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_local_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_local_journal_batch_from_offset(
            count=1,
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(BatchResponseJournalFetchResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_local_journal_batch_from_offset(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.with_raw_response.get_local_journal_batch_from_offset(
                count=1,
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_local_journal_status(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_local_journal_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_local_journal_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_local_journal_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(SnapshotStatusResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_local_journal_status(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            await async_client.webhooks.with_raw_response.get_local_journal_status(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_next_journal_entries(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_next_journal_entries(
            offset="offset",
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_next_journal_entries_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_next_journal_entries(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_next_journal_entries(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = await async_client.webhooks.with_raw_response.get_next_journal_entries(
            offset="offset",
        )

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_next_journal_entries(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.with_streaming_response.get_next_journal_entries(
            offset="offset",
        ) as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_next_journal_entries(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.with_raw_response.get_next_journal_entries(
                offset="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_next_local_journal_entries(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_next_local_journal_entries(
            offset="offset",
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_next_local_journal_entries_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        webhook = await async_client.webhooks.get_next_local_journal_entries(
            offset="offset",
            install_portal_id=0,
        )
        assert webhook.is_closed
        assert await webhook.json() == {"foo": "bar"}
        assert cast(Any, webhook.is_closed) is True
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_next_local_journal_entries(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        webhook = await async_client.webhooks.with_raw_response.get_next_local_journal_entries(
            offset="offset",
        )

        assert webhook.is_closed is True
        assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await webhook.json() == {"foo": "bar"}
        assert isinstance(webhook, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_next_local_journal_entries(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal-local/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks.with_streaming_response.get_next_local_journal_entries(
            offset="offset",
        ) as webhook:
            assert not webhook.is_closed
            assert webhook.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await webhook.json() == {"foo": "bar"}
            assert cast(Any, webhook.is_closed) is True
            assert isinstance(webhook, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, webhook.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_next_local_journal_entries(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks.with_raw_response.get_next_local_journal_entries(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_settings(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_settings(
            0,
        )
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_settings(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_settings(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(SettingsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.get_subscription_filter(
            0,
        )
        assert_matches_type(FilterResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.get_subscription_filter(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(FilterResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscription_filter(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.get_subscription_filter(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(FilterResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_event_subscriptions(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.list_event_subscriptions(
            0,
        )
        assert_matches_type(SubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_event_subscriptions(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.list_event_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(SubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_event_subscriptions(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.list_event_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(SubscriptionListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_journal_subscriptions(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.list_journal_subscriptions()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_journal_subscriptions(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.list_journal_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_journal_subscriptions(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.list_journal_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(CollectionResponseSubscriptionResponseNoPaging, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscription_filters(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.list_subscription_filters(
            0,
        )
        assert_matches_type(WebhookListSubscriptionFiltersResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscription_filters(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.list_subscription_filters(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListSubscriptionFiltersResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscription_filters(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.list_subscription_filters(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListSubscriptionFiltersResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_subscription(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.update_event_subscription(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_subscription_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.update_event_subscription(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_event_subscription(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.update_event_subscription(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_event_subscription(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.update_event_subscription(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(SettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.update_settings(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(SettingsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
