# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriberState:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_record_by_email(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/email-upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscriber_state = client.marketing.marketing_events.subscriber_state.record_by_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "contact_properties": {"foo": "string"},
                    "email": "email",
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert subscriber_state.is_closed
        assert subscriber_state.json() == {"foo": "bar"}
        assert cast(Any, subscriber_state.is_closed) is True
        assert isinstance(subscriber_state, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_record_by_email(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/email-upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscriber_state = client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "contact_properties": {"foo": "string"},
                    "email": "email",
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert subscriber_state.is_closed is True
        assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"
        assert subscriber_state.json() == {"foo": "bar"}
        assert isinstance(subscriber_state, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_record_by_email(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/email-upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.marketing.marketing_events.subscriber_state.with_streaming_response.record_by_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "contact_properties": {"foo": "string"},
                    "email": "email",
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                }
            ],
        ) as subscriber_state:
            assert not subscriber_state.is_closed
            assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"

            assert subscriber_state.json() == {"foo": "bar"}
            assert cast(Any, subscriber_state.is_closed) is True
            assert isinstance(subscriber_state, StreamedBinaryAPIResponse)

        assert cast(Any, subscriber_state.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_record_by_email(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_email(
                subscriber_state="subscriberState",
                external_event_id="",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "contact_properties": {"foo": "string"},
                        "email": "email",
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_email(
                subscriber_state="",
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "contact_properties": {"foo": "string"},
                        "email": "email",
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                    }
                ],
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_record_by_id(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscriber_state = client.marketing.marketing_events.subscriber_state.record_by_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
        )
        assert subscriber_state.is_closed
        assert subscriber_state.json() == {"foo": "bar"}
        assert cast(Any, subscriber_state.is_closed) is True
        assert isinstance(subscriber_state, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_record_by_id(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscriber_state = client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
        )

        assert subscriber_state.is_closed is True
        assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"
        assert subscriber_state.json() == {"foo": "bar"}
        assert isinstance(subscriber_state, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_record_by_id(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.marketing.marketing_events.subscriber_state.with_streaming_response.record_by_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
        ) as subscriber_state:
            assert not subscriber_state.is_closed
            assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"

            assert subscriber_state.json() == {"foo": "bar"}
            assert cast(Any, subscriber_state.is_closed) is True
            assert isinstance(subscriber_state, StreamedBinaryAPIResponse)

        assert cast(Any, subscriber_state.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_record_by_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_id(
                subscriber_state="subscriberState",
                external_event_id="",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                        "vid": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_id(
                subscriber_state="",
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                        "vid": 0,
                    }
                ],
            )


class TestAsyncSubscriberState:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_record_by_email(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/email-upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscriber_state = await async_client.marketing.marketing_events.subscriber_state.record_by_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "contact_properties": {"foo": "string"},
                    "email": "email",
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert subscriber_state.is_closed
        assert await subscriber_state.json() == {"foo": "bar"}
        assert cast(Any, subscriber_state.is_closed) is True
        assert isinstance(subscriber_state, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_record_by_email(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/email-upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscriber_state = (
            await async_client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_email(
                subscriber_state="subscriberState",
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "contact_properties": {"foo": "string"},
                        "email": "email",
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                    }
                ],
            )
        )

        assert subscriber_state.is_closed is True
        assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await subscriber_state.json() == {"foo": "bar"}
        assert isinstance(subscriber_state, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_record_by_email(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/email-upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.marketing.marketing_events.subscriber_state.with_streaming_response.record_by_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "contact_properties": {"foo": "string"},
                    "email": "email",
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                }
            ],
        ) as subscriber_state:
            assert not subscriber_state.is_closed
            assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await subscriber_state.json() == {"foo": "bar"}
            assert cast(Any, subscriber_state.is_closed) is True
            assert isinstance(subscriber_state, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, subscriber_state.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_record_by_email(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_email(
                subscriber_state="subscriberState",
                external_event_id="",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "contact_properties": {"foo": "string"},
                        "email": "email",
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            await async_client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_email(
                subscriber_state="",
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "contact_properties": {"foo": "string"},
                        "email": "email",
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                    }
                ],
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_record_by_id(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscriber_state = await async_client.marketing.marketing_events.subscriber_state.record_by_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
        )
        assert subscriber_state.is_closed
        assert await subscriber_state.json() == {"foo": "bar"}
        assert cast(Any, subscriber_state.is_closed) is True
        assert isinstance(subscriber_state, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_record_by_id(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscriber_state = (
            await async_client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_id(
                subscriber_state="subscriberState",
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                        "vid": 0,
                    }
                ],
            )
        )

        assert subscriber_state.is_closed is True
        assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await subscriber_state.json() == {"foo": "bar"}
        assert isinstance(subscriber_state, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_record_by_id(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/marketing/marketing-events/2026-03/events/externalEventId/subscriberState/upsert").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.marketing.marketing_events.subscriber_state.with_streaming_response.record_by_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
        ) as subscriber_state:
            assert not subscriber_state.is_closed
            assert subscriber_state.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await subscriber_state.json() == {"foo": "bar"}
            assert cast(Any, subscriber_state.is_closed) is True
            assert isinstance(subscriber_state, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, subscriber_state.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_record_by_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_id(
                subscriber_state="subscriberState",
                external_event_id="",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                        "vid": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            await async_client.marketing.marketing_events.subscriber_state.with_raw_response.record_by_id(
                subscriber_state="",
                external_event_id="externalEventId",
                external_account_id="externalAccountId",
                inputs=[
                    {
                        "interaction_date_time": 0,
                        "properties": {"foo": "string"},
                        "vid": 0,
                    }
                ],
            )
