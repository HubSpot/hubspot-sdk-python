# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.conversations import PublicActor, BatchResponsePublicActor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_read(self, client: Hubspot) -> None:
        actor = client.conversations.actors.batch_read(
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_read(self, client: Hubspot) -> None:
        response = client.conversations.actors.with_raw_response.batch_read(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        actor = response.parse()
        assert_matches_type(BatchResponsePublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_read(self, client: Hubspot) -> None:
        with client.conversations.actors.with_streaming_response.batch_read(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            actor = response.parse()
            assert_matches_type(BatchResponsePublicActor, actor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        actor = client.conversations.actors.get(
            "actorId",
        )
        assert_matches_type(PublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.conversations.actors.with_raw_response.get(
            "actorId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        actor = response.parse()
        assert_matches_type(PublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.conversations.actors.with_streaming_response.get(
            "actorId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            actor = response.parse()
            assert_matches_type(PublicActor, actor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `actor_id` but received ''"):
            client.conversations.actors.with_raw_response.get(
                "",
            )


class TestAsyncActors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_read(self, async_client: AsyncHubspot) -> None:
        actor = await async_client.conversations.actors.batch_read(
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_read(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.actors.with_raw_response.batch_read(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        actor = await response.parse()
        assert_matches_type(BatchResponsePublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_read(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.actors.with_streaming_response.batch_read(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            actor = await response.parse()
            assert_matches_type(BatchResponsePublicActor, actor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        actor = await async_client.conversations.actors.get(
            "actorId",
        )
        assert_matches_type(PublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.actors.with_raw_response.get(
            "actorId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        actor = await response.parse()
        assert_matches_type(PublicActor, actor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.actors.with_streaming_response.get(
            "actorId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            actor = await response.parse()
            assert_matches_type(PublicActor, actor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `actor_id` but received ''"):
            await async_client.conversations.actors.with_raw_response.get(
                "",
            )
