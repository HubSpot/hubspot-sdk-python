# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.marketing import (
    MarketingEventDefaultResponse,
    MarketingEventPublicReadResponse,
    MarketingEventPublicReadResponseV2,
    MarketingEventPublicDefaultResponse,
    MarketingEventPublicDefaultResponseV2,
    BatchResponseMarketingEventPublicDefaultResponse,
    BatchResponseMarketingEventPublicDefaultResponseV2,
    CollectionResponseSearchPublicResponseWrapperNoPaging,
    CollectionResponseWithTotalMarketingEventIdentifiersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketingEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )
        assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_completed=True,
            event_description="eventDescription",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_description="eventDescription",
            event_name="eventName",
            event_organizer="eventOrganizer",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.update(
                object_id="",
                custom_properties=[
                    {
                        "data_sensitivity": "high",
                        "is_encrypted": True,
                        "is_large_value": True,
                        "name": "name",
                        "persistence_timestamp": 0,
                        "request_id": "requestId",
                        "selected_by_user": True,
                        "selected_by_user_timestamp": 0,
                        "source": "ACADEMY",
                        "source_id": "sourceId",
                        "source_label": "sourceLabel",
                        "source_metadata": "sourceMetadata",
                        "source_upstream_deployable": "sourceUpstreamDeployable",
                        "source_vid": [0],
                        "timestamp": 0,
                        "unit": "unit",
                        "updated_by_user_id": 0,
                        "use_timestamp_as_persistence_timestamp": True,
                        "value": "value",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.list()
        assert_matches_type(SyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.list(
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(SyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(SyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.delete(
            "objectId",
        )
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.delete(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.delete(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert marketing_event is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete_batch(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/batch/archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        marketing_event = client.marketing.marketing_events.delete_batch(
            inputs=[{"object_id": "objectId"}],
        )
        assert marketing_event.is_closed
        assert marketing_event.json() == {"foo": "bar"}
        assert cast(Any, marketing_event.is_closed) is True
        assert isinstance(marketing_event, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete_batch(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/batch/archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        marketing_event = client.marketing.marketing_events.with_raw_response.delete_batch(
            inputs=[{"object_id": "objectId"}],
        )

        assert marketing_event.is_closed is True
        assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"
        assert marketing_event.json() == {"foo": "bar"}
        assert isinstance(marketing_event, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete_batch(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/batch/archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.marketing.marketing_events.with_streaming_response.delete_batch(
            inputs=[{"object_id": "objectId"}],
        ) as marketing_event:
            assert not marketing_event.is_closed
            assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"

            assert marketing_event.json() == {"foo": "bar"}
            assert cast(Any, marketing_event.is_closed) is True
            assert isinstance(marketing_event, StreamedBinaryAPIResponse)

        assert cast(Any, marketing_event.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete_batch_by_external_event_id(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/delete").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        marketing_event = client.marketing.marketing_events.delete_batch_by_external_event_id(
            inputs=[
                {
                    "app_id": 0,
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )
        assert marketing_event.is_closed
        assert marketing_event.json() == {"foo": "bar"}
        assert cast(Any, marketing_event.is_closed) is True
        assert isinstance(marketing_event, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete_batch_by_external_event_id(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/delete").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        marketing_event = client.marketing.marketing_events.with_raw_response.delete_batch_by_external_event_id(
            inputs=[
                {
                    "app_id": 0,
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )

        assert marketing_event.is_closed is True
        assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"
        assert marketing_event.json() == {"foo": "bar"}
        assert isinstance(marketing_event, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete_batch_by_external_event_id(
        self, client: HubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/delete").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.marketing.marketing_events.with_streaming_response.delete_batch_by_external_event_id(
            inputs=[
                {
                    "app_id": 0,
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        ) as marketing_event:
            assert not marketing_event.is_closed
            assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"

            assert marketing_event.json() == {"foo": "bar"}
            assert cast(Any, marketing_event.is_closed) is True
            assert isinstance(marketing_event, StreamedBinaryAPIResponse)

        assert cast(Any, marketing_event.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_external_event_id(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.delete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_external_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.delete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_external_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.delete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert marketing_event is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_by_external_event_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.delete_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.get(
            "objectId",
        )
        assert_matches_type(MarketingEventPublicReadResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.get(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(MarketingEventPublicReadResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.get(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(MarketingEventPublicReadResponseV2, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_external_event_id(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.get_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(MarketingEventPublicReadResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_external_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.get_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(MarketingEventPublicReadResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_external_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.get_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(MarketingEventPublicReadResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_external_event_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.get_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_by_external_event_id(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.search_by_external_event_id(
            q="q",
        )
        assert_matches_type(CollectionResponseSearchPublicResponseWrapperNoPaging, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_by_external_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.search_by_external_event_id(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(CollectionResponseSearchPublicResponseWrapperNoPaging, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_by_external_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.search_by_external_event_id(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(
                CollectionResponseSearchPublicResponseWrapperNoPaging, marketing_event, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_identifiers_by_external_event_id(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.search_identifiers_by_external_event_id(
            "externalEventId",
        )
        assert_matches_type(
            CollectionResponseWithTotalMarketingEventIdentifiersResponse, marketing_event, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_identifiers_by_external_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.search_identifiers_by_external_event_id(
            "externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(
            CollectionResponseWithTotalMarketingEventIdentifiersResponse, marketing_event, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_identifiers_by_external_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.search_identifiers_by_external_event_id(
            "externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(
                CollectionResponseWithTotalMarketingEventIdentifiersResponse, marketing_event, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search_identifiers_by_external_event_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.search_identifiers_by_external_event_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.update_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "object_id": "objectId",
                }
            ],
        )
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.update_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "object_id": "objectId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.update_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "object_id": "objectId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(BatchResponseMarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_external_event_id(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_external_event_id_with_all_params(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_completed=True,
            event_description="eventDescription",
            event_name="eventName",
            event_organizer="eventOrganizer",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_by_external_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_by_external_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_by_external_event_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.with_raw_response.update_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
                custom_properties=[
                    {
                        "data_sensitivity": "high",
                        "is_encrypted": True,
                        "is_large_value": True,
                        "name": "name",
                        "persistence_timestamp": 0,
                        "request_id": "requestId",
                        "selected_by_user": True,
                        "selected_by_user_timestamp": 0,
                        "source": "ACADEMY",
                        "source_id": "sourceId",
                        "source_label": "sourceLabel",
                        "source_metadata": "sourceMetadata",
                        "source_upstream_deployable": "sourceUpstreamDeployable",
                        "source_vid": [0],
                        "timestamp": 0,
                        "unit": "unit",
                        "updated_by_user_id": 0,
                        "use_timestamp_as_persistence_timestamp": True,
                        "value": "value",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_batch(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.upsert_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "event_name": "eventName",
                    "event_organizer": "eventOrganizer",
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert_batch(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.upsert_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "event_name": "eventName",
                    "event_organizer": "eventOrganizer",
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert_batch(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.upsert_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "event_name": "eventName",
                    "event_organizer": "eventOrganizer",
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(BatchResponseMarketingEventPublicDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_by_external_event_id(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_by_external_event_id_with_all_params(self, client: HubSpot) -> None:
        marketing_event = client.marketing.marketing_events.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_completed=True,
            event_description="eventDescription",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert_by_external_event_id(self, client: HubSpot) -> None:
        response = client.marketing.marketing_events.with_raw_response.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = response.parse()
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert_by_external_event_id(self, client: HubSpot) -> None:
        with client.marketing.marketing_events.with_streaming_response.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = response.parse()
            assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert_by_external_event_id(self, client: HubSpot) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_external_event_id` but received ''"
        ):
            client.marketing.marketing_events.with_raw_response.upsert_by_external_event_id(
                path_external_event_id="",
                custom_properties=[
                    {
                        "data_sensitivity": "high",
                        "is_encrypted": True,
                        "is_large_value": True,
                        "name": "name",
                        "persistence_timestamp": 0,
                        "request_id": "requestId",
                        "selected_by_user": True,
                        "selected_by_user_timestamp": 0,
                        "source": "ACADEMY",
                        "source_id": "sourceId",
                        "source_label": "sourceLabel",
                        "source_metadata": "sourceMetadata",
                        "source_upstream_deployable": "sourceUpstreamDeployable",
                        "source_vid": [0],
                        "timestamp": 0,
                        "unit": "unit",
                        "updated_by_user_id": 0,
                        "use_timestamp_as_persistence_timestamp": True,
                        "value": "value",
                    }
                ],
                event_name="eventName",
                event_organizer="eventOrganizer",
                external_account_id="externalAccountId",
                body_external_event_id="externalEventId",
            )


class TestAsyncMarketingEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )
        assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_completed=True,
            event_description="eventDescription",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.create(
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(MarketingEventDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_description="eventDescription",
            event_name="eventName",
            event_organizer="eventOrganizer",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.update(
            object_id="objectId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(MarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.update(
                object_id="",
                custom_properties=[
                    {
                        "data_sensitivity": "high",
                        "is_encrypted": True,
                        "is_large_value": True,
                        "name": "name",
                        "persistence_timestamp": 0,
                        "request_id": "requestId",
                        "selected_by_user": True,
                        "selected_by_user_timestamp": 0,
                        "source": "ACADEMY",
                        "source_id": "sourceId",
                        "source_label": "sourceLabel",
                        "source_metadata": "sourceMetadata",
                        "source_upstream_deployable": "sourceUpstreamDeployable",
                        "source_vid": [0],
                        "timestamp": 0,
                        "unit": "unit",
                        "updated_by_user_id": 0,
                        "use_timestamp_as_persistence_timestamp": True,
                        "value": "value",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.list()
        assert_matches_type(AsyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.list(
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(AsyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(AsyncPage[MarketingEventPublicReadResponseV2], marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.delete(
            "objectId",
        )
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.delete(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.delete(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert marketing_event is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete_batch(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/batch/archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        marketing_event = await async_client.marketing.marketing_events.delete_batch(
            inputs=[{"object_id": "objectId"}],
        )
        assert marketing_event.is_closed
        assert await marketing_event.json() == {"foo": "bar"}
        assert cast(Any, marketing_event.is_closed) is True
        assert isinstance(marketing_event, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete_batch(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/batch/archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        marketing_event = await async_client.marketing.marketing_events.with_raw_response.delete_batch(
            inputs=[{"object_id": "objectId"}],
        )

        assert marketing_event.is_closed is True
        assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await marketing_event.json() == {"foo": "bar"}
        assert isinstance(marketing_event, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete_batch(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/batch/archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.marketing.marketing_events.with_streaming_response.delete_batch(
            inputs=[{"object_id": "objectId"}],
        ) as marketing_event:
            assert not marketing_event.is_closed
            assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await marketing_event.json() == {"foo": "bar"}
            assert cast(Any, marketing_event.is_closed) is True
            assert isinstance(marketing_event, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, marketing_event.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete_batch_by_external_event_id(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/delete").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        marketing_event = await async_client.marketing.marketing_events.delete_batch_by_external_event_id(
            inputs=[
                {
                    "app_id": 0,
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )
        assert marketing_event.is_closed
        assert await marketing_event.json() == {"foo": "bar"}
        assert cast(Any, marketing_event.is_closed) is True
        assert isinstance(marketing_event, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete_batch_by_external_event_id(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/delete").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        marketing_event = (
            await async_client.marketing.marketing_events.with_raw_response.delete_batch_by_external_event_id(
                inputs=[
                    {
                        "app_id": 0,
                        "external_account_id": "externalAccountId",
                        "external_event_id": "externalEventId",
                    }
                ],
            )
        )

        assert marketing_event.is_closed is True
        assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await marketing_event.json() == {"foo": "bar"}
        assert isinstance(marketing_event, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete_batch_by_external_event_id(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/delete").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.marketing.marketing_events.with_streaming_response.delete_batch_by_external_event_id(
            inputs=[
                {
                    "app_id": 0,
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        ) as marketing_event:
            assert not marketing_event.is_closed
            assert marketing_event.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await marketing_event.json() == {"foo": "bar"}
            assert cast(Any, marketing_event.is_closed) is True
            assert isinstance(marketing_event, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, marketing_event.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.delete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.delete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert marketing_event is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.delete_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert marketing_event is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.delete_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.get(
            "objectId",
        )
        assert_matches_type(MarketingEventPublicReadResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.get(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(MarketingEventPublicReadResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.get(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(MarketingEventPublicReadResponseV2, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.get_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(MarketingEventPublicReadResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.get_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(MarketingEventPublicReadResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.get_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(MarketingEventPublicReadResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.get_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.search_by_external_event_id(
            q="q",
        )
        assert_matches_type(CollectionResponseSearchPublicResponseWrapperNoPaging, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.search_by_external_event_id(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(CollectionResponseSearchPublicResponseWrapperNoPaging, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.search_by_external_event_id(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(
                CollectionResponseSearchPublicResponseWrapperNoPaging, marketing_event, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_identifiers_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.search_identifiers_by_external_event_id(
            "externalEventId",
        )
        assert_matches_type(
            CollectionResponseWithTotalMarketingEventIdentifiersResponse, marketing_event, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_identifiers_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.marketing.marketing_events.with_raw_response.search_identifiers_by_external_event_id(
                "externalEventId",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(
            CollectionResponseWithTotalMarketingEventIdentifiersResponse, marketing_event, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_identifiers_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.marketing.marketing_events.with_streaming_response.search_identifiers_by_external_event_id(
                "externalEventId",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(
                CollectionResponseWithTotalMarketingEventIdentifiersResponse, marketing_event, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search_identifiers_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.search_identifiers_by_external_event_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.update_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "object_id": "objectId",
                }
            ],
        )
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.update_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "object_id": "objectId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.update_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "object_id": "objectId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(BatchResponseMarketingEventPublicDefaultResponseV2, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_external_event_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_completed=True,
            event_description="eventDescription",
            event_name="eventName",
            event_organizer="eventOrganizer",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.update_by_external_event_id(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.with_raw_response.update_by_external_event_id(
                external_event_id="",
                external_account_id="externalAccountId",
                custom_properties=[
                    {
                        "data_sensitivity": "high",
                        "is_encrypted": True,
                        "is_large_value": True,
                        "name": "name",
                        "persistence_timestamp": 0,
                        "request_id": "requestId",
                        "selected_by_user": True,
                        "selected_by_user_timestamp": 0,
                        "source": "ACADEMY",
                        "source_id": "sourceId",
                        "source_label": "sourceLabel",
                        "source_metadata": "sourceMetadata",
                        "source_upstream_deployable": "sourceUpstreamDeployable",
                        "source_vid": [0],
                        "timestamp": 0,
                        "unit": "unit",
                        "updated_by_user_id": 0,
                        "use_timestamp_as_persistence_timestamp": True,
                        "value": "value",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_batch(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.upsert_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "event_name": "eventName",
                    "event_organizer": "eventOrganizer",
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.upsert_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "event_name": "eventName",
                    "event_organizer": "eventOrganizer",
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(BatchResponseMarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.upsert_batch(
            inputs=[
                {
                    "custom_properties": [
                        {
                            "data_sensitivity": "high",
                            "is_encrypted": True,
                            "is_large_value": True,
                            "name": "name",
                            "persistence_timestamp": 0,
                            "request_id": "requestId",
                            "selected_by_user": True,
                            "selected_by_user_timestamp": 0,
                            "source": "ACADEMY",
                            "source_id": "sourceId",
                            "source_label": "sourceLabel",
                            "source_metadata": "sourceMetadata",
                            "source_upstream_deployable": "sourceUpstreamDeployable",
                            "source_vid": [0],
                            "timestamp": 0,
                            "unit": "unit",
                            "updated_by_user_id": 0,
                            "use_timestamp_as_persistence_timestamp": True,
                            "value": "value",
                        }
                    ],
                    "event_name": "eventName",
                    "event_organizer": "eventOrganizer",
                    "external_account_id": "externalAccountId",
                    "external_event_id": "externalEventId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(BatchResponseMarketingEventPublicDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_by_external_event_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        marketing_event = await async_client.marketing.marketing_events.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
            end_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_cancelled=True,
            event_completed=True,
            event_description="eventDescription",
            event_type="eventType",
            event_url="eventUrl",
            start_date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.marketing_events.with_raw_response.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketing_event = await response.parse()
        assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.marketing_events.with_streaming_response.upsert_by_external_event_id(
            path_external_event_id="externalEventId",
            custom_properties=[
                {
                    "data_sensitivity": "high",
                    "is_encrypted": True,
                    "is_large_value": True,
                    "name": "name",
                    "persistence_timestamp": 0,
                    "request_id": "requestId",
                    "selected_by_user": True,
                    "selected_by_user_timestamp": 0,
                    "source": "ACADEMY",
                    "source_id": "sourceId",
                    "source_label": "sourceLabel",
                    "source_metadata": "sourceMetadata",
                    "source_upstream_deployable": "sourceUpstreamDeployable",
                    "source_vid": [0],
                    "timestamp": 0,
                    "unit": "unit",
                    "updated_by_user_id": 0,
                    "use_timestamp_as_persistence_timestamp": True,
                    "value": "value",
                }
            ],
            event_name="eventName",
            event_organizer="eventOrganizer",
            external_account_id="externalAccountId",
            body_external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketing_event = await response.parse()
            assert_matches_type(MarketingEventPublicDefaultResponse, marketing_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert_by_external_event_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `path_external_event_id` but received ''"
        ):
            await async_client.marketing.marketing_events.with_raw_response.upsert_by_external_event_id(
                path_external_event_id="",
                custom_properties=[
                    {
                        "data_sensitivity": "high",
                        "is_encrypted": True,
                        "is_large_value": True,
                        "name": "name",
                        "persistence_timestamp": 0,
                        "request_id": "requestId",
                        "selected_by_user": True,
                        "selected_by_user_timestamp": 0,
                        "source": "ACADEMY",
                        "source_id": "sourceId",
                        "source_label": "sourceLabel",
                        "source_metadata": "sourceMetadata",
                        "source_upstream_deployable": "sourceUpstreamDeployable",
                        "source_vid": [0],
                        "timestamp": 0,
                        "unit": "unit",
                        "updated_by_user_id": 0,
                        "use_timestamp_as_persistence_timestamp": True,
                        "value": "value",
                    }
                ],
                event_name="eventName",
                event_organizer="eventOrganizer",
                external_account_id="externalAccountId",
                body_external_event_id="externalEventId",
            )
