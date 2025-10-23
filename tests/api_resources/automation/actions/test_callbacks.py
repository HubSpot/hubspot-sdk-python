# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallbacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete(self, client: HubSpot) -> None:
        callback = client.automation.actions.callbacks.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
        )
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: HubSpot) -> None:
        response = client.automation.actions.callbacks.with_raw_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: HubSpot) -> None:
        with client.automation.actions.callbacks.with_streaming_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `callback_id` but received ''"):
            client.automation.actions.callbacks.with_raw_response.complete(
                callback_id="",
                output_fields={"foo": "string"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete_batch(self, client: HubSpot) -> None:
        callback = client.automation.actions.callbacks.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                }
            ],
        )
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete_batch(self, client: HubSpot) -> None:
        response = client.automation.actions.callbacks.with_raw_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete_batch(self, client: HubSpot) -> None:
        with client.automation.actions.callbacks.with_streaming_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCallbacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncHubSpot) -> None:
        callback = await async_client.automation.actions.callbacks.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
        )
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.callbacks.with_raw_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.callbacks.with_streaming_response.complete(
            callback_id="callbackId",
            output_fields={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `callback_id` but received ''"):
            await async_client.automation.actions.callbacks.with_raw_response.complete(
                callback_id="",
                output_fields={"foo": "string"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete_batch(self, async_client: AsyncHubSpot) -> None:
        callback = await async_client.automation.actions.callbacks.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                }
            ],
        )
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.callbacks.with_raw_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert callback is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.callbacks.with_streaming_response.complete_batch(
            inputs=[
                {
                    "callback_id": "callbackId",
                    "output_fields": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True
