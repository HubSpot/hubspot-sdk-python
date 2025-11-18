# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.automation import (
    PublicSequenceResponse,
    PublicSequenceLiteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSequences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        sequence = client.automation.sequences.list(
            user_id="userId",
        )
        assert_matches_type(SyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        sequence = client.automation.sequences.list(
            user_id="userId",
            after="after",
            limit=0,
            name="name",
        )
        assert_matches_type(SyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.automation.sequences.with_raw_response.list(
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sequence = response.parse()
        assert_matches_type(SyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.automation.sequences.with_streaming_response.list(
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sequence = response.parse()
            assert_matches_type(SyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        sequence = client.automation.sequences.get(
            sequence_id="sequenceId",
            user_id="userId",
        )
        assert_matches_type(PublicSequenceResponse, sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.automation.sequences.with_raw_response.get(
            sequence_id="sequenceId",
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sequence = response.parse()
        assert_matches_type(PublicSequenceResponse, sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.automation.sequences.with_streaming_response.get(
            sequence_id="sequenceId",
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sequence = response.parse()
            assert_matches_type(PublicSequenceResponse, sequence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            client.automation.sequences.with_raw_response.get(
                sequence_id="",
                user_id="userId",
            )


class TestAsyncSequences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        sequence = await async_client.automation.sequences.list(
            user_id="userId",
        )
        assert_matches_type(AsyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        sequence = await async_client.automation.sequences.list(
            user_id="userId",
            after="after",
            limit=0,
            name="name",
        )
        assert_matches_type(AsyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.sequences.with_raw_response.list(
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sequence = await response.parse()
        assert_matches_type(AsyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.sequences.with_streaming_response.list(
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sequence = await response.parse()
            assert_matches_type(AsyncPage[PublicSequenceLiteResponse], sequence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        sequence = await async_client.automation.sequences.get(
            sequence_id="sequenceId",
            user_id="userId",
        )
        assert_matches_type(PublicSequenceResponse, sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.sequences.with_raw_response.get(
            sequence_id="sequenceId",
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sequence = await response.parse()
        assert_matches_type(PublicSequenceResponse, sequence, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.sequences.with_streaming_response.get(
            sequence_id="sequenceId",
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sequence = await response.parse()
            assert_matches_type(PublicSequenceResponse, sequence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sequence_id` but received ''"):
            await async_client.automation.sequences.with_raw_response.get(
                sequence_id="",
                user_id="userId",
            )
