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


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_cancel(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/cancel").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = client.crm.subscriptions.cancel(
            0,
        )
        assert subscription.is_closed
        assert subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_cancel(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/cancel").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscription = client.crm.subscriptions.with_raw_response.cancel(
            0,
        )

        assert subscription.is_closed is True
        assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert subscription.json() == {"foo": "bar"}
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_cancel(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/cancel").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.crm.subscriptions.with_streaming_response.cancel(
            0,
        ) as subscription:
            assert not subscription.is_closed
            assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert subscription.json() == {"foo": "bar"}
            assert cast(Any, subscription.is_closed) is True
            assert isinstance(subscription, StreamedBinaryAPIResponse)

        assert cast(Any, subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pause(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = client.crm.subscriptions.pause(
            object_id=0,
        )
        assert subscription.is_closed
        assert subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pause_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = client.crm.subscriptions.pause(
            object_id=0,
            pause_reason="pauseReason",
        )
        assert subscription.is_closed
        assert subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_pause(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscription = client.crm.subscriptions.with_raw_response.pause(
            object_id=0,
        )

        assert subscription.is_closed is True
        assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert subscription.json() == {"foo": "bar"}
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_pause(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.crm.subscriptions.with_streaming_response.pause(
            object_id=0,
        ) as subscription:
            assert not subscription.is_closed
            assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert subscription.json() == {"foo": "bar"}
            assert cast(Any, subscription.is_closed) is True
            assert isinstance(subscription, StreamedBinaryAPIResponse)

        assert cast(Any, subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_unpause(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/unpause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = client.crm.subscriptions.unpause(
            object_id=0,
            proposed_next_billing_date=0,
        )
        assert subscription.is_closed
        assert subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_unpause(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/unpause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscription = client.crm.subscriptions.with_raw_response.unpause(
            object_id=0,
            proposed_next_billing_date=0,
        )

        assert subscription.is_closed is True
        assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert subscription.json() == {"foo": "bar"}
        assert isinstance(subscription, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_unpause(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/unpause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.crm.subscriptions.with_streaming_response.unpause(
            object_id=0,
            proposed_next_billing_date=0,
        ) as subscription:
            assert not subscription.is_closed
            assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert subscription.json() == {"foo": "bar"}
            assert cast(Any, subscription.is_closed) is True
            assert isinstance(subscription, StreamedBinaryAPIResponse)

        assert cast(Any, subscription.is_closed) is True


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_cancel(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/cancel").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = await async_client.crm.subscriptions.cancel(
            0,
        )
        assert subscription.is_closed
        assert await subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_cancel(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/cancel").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscription = await async_client.crm.subscriptions.with_raw_response.cancel(
            0,
        )

        assert subscription.is_closed is True
        assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await subscription.json() == {"foo": "bar"}
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_cancel(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/cancel").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.crm.subscriptions.with_streaming_response.cancel(
            0,
        ) as subscription:
            assert not subscription.is_closed
            assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await subscription.json() == {"foo": "bar"}
            assert cast(Any, subscription.is_closed) is True
            assert isinstance(subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pause(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = await async_client.crm.subscriptions.pause(
            object_id=0,
        )
        assert subscription.is_closed
        assert await subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pause_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = await async_client.crm.subscriptions.pause(
            object_id=0,
            pause_reason="pauseReason",
        )
        assert subscription.is_closed
        assert await subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_pause(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscription = await async_client.crm.subscriptions.with_raw_response.pause(
            object_id=0,
        )

        assert subscription.is_closed is True
        assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await subscription.json() == {"foo": "bar"}
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_pause(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/pause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.crm.subscriptions.with_streaming_response.pause(
            object_id=0,
        ) as subscription:
            assert not subscription.is_closed
            assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await subscription.json() == {"foo": "bar"}
            assert cast(Any, subscription.is_closed) is True
            assert isinstance(subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, subscription.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_unpause(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/unpause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        subscription = await async_client.crm.subscriptions.unpause(
            object_id=0,
            proposed_next_billing_date=0,
        )
        assert subscription.is_closed
        assert await subscription.json() == {"foo": "bar"}
        assert cast(Any, subscription.is_closed) is True
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_unpause(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/unpause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        subscription = await async_client.crm.subscriptions.with_raw_response.unpause(
            object_id=0,
            proposed_next_billing_date=0,
        )

        assert subscription.is_closed is True
        assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await subscription.json() == {"foo": "bar"}
        assert isinstance(subscription, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_unpause(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/payments-subscriptions/v1/subscriptions/crm/0/unpause").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.crm.subscriptions.with_streaming_response.unpause(
            object_id=0,
            proposed_next_billing_date=0,
        ) as subscription:
            assert not subscription.is_closed
            assert subscription.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await subscription.json() == {"foo": "bar"}
            assert cast(Any, subscription.is_closed) is True
            assert isinstance(subscription, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, subscription.is_closed) is True
