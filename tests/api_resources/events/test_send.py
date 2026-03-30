# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from hubspot_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_send(self, client: Hubspot) -> None:
        send = client.events.send.batch_send(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_send(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.batch_send(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_send(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.batch_send(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Hubspot) -> None:
        send = client.events.send.send(
            event_name="eventName",
            properties={"foo": "string"},
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.send(
            event_name="eventName",
            properties={"foo": "string"},
            email="email",
            object_id="objectId",
            occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            utk="utk",
            uuid="uuid",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.send(
            event_name="eventName",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.send(
            event_name="eventName",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_send(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.batch_send(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_send(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.batch_send(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_send(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.batch_send(
            inputs=[
                {
                    "event_name": "eventName",
                    "properties": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send(
            event_name="eventName",
            properties={"foo": "string"},
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send(
            event_name="eventName",
            properties={"foo": "string"},
            email="email",
            object_id="objectId",
            occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            utk="utk",
            uuid="uuid",
        )
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.send(
            event_name="eventName",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.send(
            event_name="eventName",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True
