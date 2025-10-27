# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.extensions.calling import (
    TranscriptResponse,
    TranscriptCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscripts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        transcript = client.crm.extensions.calling.transcripts.create(
            engagement_id=0,
            transcript_create_utterances=[
                {
                    "end_time_millis": 0,
                    "speaker": {
                        "id": "id",
                        "name": "name",
                    },
                    "start_time_millis": 0,
                    "text": "text",
                }
            ],
        )
        assert_matches_type(TranscriptCreateResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.transcripts.with_raw_response.create(
            engagement_id=0,
            transcript_create_utterances=[
                {
                    "end_time_millis": 0,
                    "speaker": {
                        "id": "id",
                        "name": "name",
                    },
                    "start_time_millis": 0,
                    "text": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcript = response.parse()
        assert_matches_type(TranscriptCreateResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.transcripts.with_streaming_response.create(
            engagement_id=0,
            transcript_create_utterances=[
                {
                    "end_time_millis": 0,
                    "speaker": {
                        "id": "id",
                        "name": "name",
                    },
                    "start_time_millis": 0,
                    "text": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcript = response.parse()
            assert_matches_type(TranscriptCreateResponse, transcript, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        transcript = client.crm.extensions.calling.transcripts.delete(
            "transcriptId",
        )
        assert transcript is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.transcripts.with_raw_response.delete(
            "transcriptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcript = response.parse()
        assert transcript is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.transcripts.with_streaming_response.delete(
            "transcriptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcript = response.parse()
            assert transcript is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcript_id` but received ''"):
            client.crm.extensions.calling.transcripts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        transcript = client.crm.extensions.calling.transcripts.get(
            "transcriptId",
        )
        assert_matches_type(TranscriptResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.transcripts.with_raw_response.get(
            "transcriptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcript = response.parse()
        assert_matches_type(TranscriptResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.transcripts.with_streaming_response.get(
            "transcriptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcript = response.parse()
            assert_matches_type(TranscriptResponse, transcript, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcript_id` but received ''"):
            client.crm.extensions.calling.transcripts.with_raw_response.get(
                "",
            )


class TestAsyncTranscripts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        transcript = await async_client.crm.extensions.calling.transcripts.create(
            engagement_id=0,
            transcript_create_utterances=[
                {
                    "end_time_millis": 0,
                    "speaker": {
                        "id": "id",
                        "name": "name",
                    },
                    "start_time_millis": 0,
                    "text": "text",
                }
            ],
        )
        assert_matches_type(TranscriptCreateResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.transcripts.with_raw_response.create(
            engagement_id=0,
            transcript_create_utterances=[
                {
                    "end_time_millis": 0,
                    "speaker": {
                        "id": "id",
                        "name": "name",
                    },
                    "start_time_millis": 0,
                    "text": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcript = await response.parse()
        assert_matches_type(TranscriptCreateResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.transcripts.with_streaming_response.create(
            engagement_id=0,
            transcript_create_utterances=[
                {
                    "end_time_millis": 0,
                    "speaker": {
                        "id": "id",
                        "name": "name",
                    },
                    "start_time_millis": 0,
                    "text": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcript = await response.parse()
            assert_matches_type(TranscriptCreateResponse, transcript, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        transcript = await async_client.crm.extensions.calling.transcripts.delete(
            "transcriptId",
        )
        assert transcript is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.transcripts.with_raw_response.delete(
            "transcriptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcript = await response.parse()
        assert transcript is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.transcripts.with_streaming_response.delete(
            "transcriptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcript = await response.parse()
            assert transcript is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcript_id` but received ''"):
            await async_client.crm.extensions.calling.transcripts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        transcript = await async_client.crm.extensions.calling.transcripts.get(
            "transcriptId",
        )
        assert_matches_type(TranscriptResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.transcripts.with_raw_response.get(
            "transcriptId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcript = await response.parse()
        assert_matches_type(TranscriptResponse, transcript, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.transcripts.with_streaming_response.get(
            "transcriptId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcript = await response.parse()
            assert_matches_type(TranscriptResponse, transcript, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcript_id` but received ''"):
            await async_client.crm.extensions.calling.transcripts.with_raw_response.get(
                "",
            )
