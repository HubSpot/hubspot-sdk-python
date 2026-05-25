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
from hubspot_sdk.types.shared import SnapshotStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJournal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_earliest(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = client.webhooks_journal.journal.get_earliest()
        assert journal.is_closed
        assert journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_earliest_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = client.webhooks_journal.journal.get_earliest(
            install_portal_id=0,
        )
        assert journal.is_closed
        assert journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_earliest(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        journal = client.webhooks_journal.journal.with_raw_response.get_earliest()

        assert journal.is_closed is True
        assert journal.http_request.headers.get("X-Stainless-Lang") == "python"
        assert journal.json() == {"foo": "bar"}
        assert isinstance(journal, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_earliest(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks_journal.journal.with_streaming_response.get_earliest() as journal:
            assert not journal.is_closed
            assert journal.http_request.headers.get("X-Stainless-Lang") == "python"

            assert journal.json() == {"foo": "bar"}
            assert cast(Any, journal.is_closed) is True
            assert isinstance(journal, StreamedBinaryAPIResponse)

        assert cast(Any, journal.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_next_from_offset(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = client.webhooks_journal.journal.get_next_from_offset(
            offset="offset",
        )
        assert journal.is_closed
        assert journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_next_from_offset_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = client.webhooks_journal.journal.get_next_from_offset(
            offset="offset",
            install_portal_id=0,
        )
        assert journal.is_closed
        assert journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_next_from_offset(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        journal = client.webhooks_journal.journal.with_raw_response.get_next_from_offset(
            offset="offset",
        )

        assert journal.is_closed is True
        assert journal.http_request.headers.get("X-Stainless-Lang") == "python"
        assert journal.json() == {"foo": "bar"}
        assert isinstance(journal, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_next_from_offset(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.webhooks_journal.journal.with_streaming_response.get_next_from_offset(
            offset="offset",
        ) as journal:
            assert not journal.is_closed
            assert journal.http_request.headers.get("X-Stainless-Lang") == "python"

            assert journal.json() == {"foo": "bar"}
            assert cast(Any, journal.is_closed) is True
            assert isinstance(journal, StreamedBinaryAPIResponse)

        assert cast(Any, journal.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_next_from_offset(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.webhooks_journal.journal.with_raw_response.get_next_from_offset(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: HubSpot) -> None:
        journal = client.webhooks_journal.journal.get_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: HubSpot) -> None:
        response = client.webhooks_journal.journal.with_raw_response.get_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal = response.parse()
        assert_matches_type(SnapshotStatusResponse, journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: HubSpot) -> None:
        with client.webhooks_journal.journal.with_streaming_response.get_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal = response.parse()
            assert_matches_type(SnapshotStatusResponse, journal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            client.webhooks_journal.journal.with_raw_response.get_status(
                "",
            )


class TestAsyncJournal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_earliest(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = await async_client.webhooks_journal.journal.get_earliest()
        assert journal.is_closed
        assert await journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_earliest_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = await async_client.webhooks_journal.journal.get_earliest(
            install_portal_id=0,
        )
        assert journal.is_closed
        assert await journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_earliest(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        journal = await async_client.webhooks_journal.journal.with_raw_response.get_earliest()

        assert journal.is_closed is True
        assert journal.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await journal.json() == {"foo": "bar"}
        assert isinstance(journal, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_earliest(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/earliest").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks_journal.journal.with_streaming_response.get_earliest() as journal:
            assert not journal.is_closed
            assert journal.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await journal.json() == {"foo": "bar"}
            assert cast(Any, journal.is_closed) is True
            assert isinstance(journal, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, journal.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_next_from_offset(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = await async_client.webhooks_journal.journal.get_next_from_offset(
            offset="offset",
        )
        assert journal.is_closed
        assert await journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_next_from_offset_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        journal = await async_client.webhooks_journal.journal.get_next_from_offset(
            offset="offset",
            install_portal_id=0,
        )
        assert journal.is_closed
        assert await journal.json() == {"foo": "bar"}
        assert cast(Any, journal.is_closed) is True
        assert isinstance(journal, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_next_from_offset(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        journal = await async_client.webhooks_journal.journal.with_raw_response.get_next_from_offset(
            offset="offset",
        )

        assert journal.is_closed is True
        assert journal.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await journal.json() == {"foo": "bar"}
        assert isinstance(journal, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_next_from_offset(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/webhooks-journal/journal/2026-03/offset/offset/next").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.webhooks_journal.journal.with_streaming_response.get_next_from_offset(
            offset="offset",
        ) as journal:
            assert not journal.is_closed
            assert journal.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await journal.json() == {"foo": "bar"}
            assert cast(Any, journal.is_closed) is True
            assert isinstance(journal, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, journal.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_next_from_offset(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.webhooks_journal.journal.with_raw_response.get_next_from_offset(
                offset="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncHubSpot) -> None:
        journal = await async_client.webhooks_journal.journal.get_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotStatusResponse, journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks_journal.journal.with_raw_response.get_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journal = await response.parse()
        assert_matches_type(SnapshotStatusResponse, journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks_journal.journal.with_streaming_response.get_status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journal = await response.parse()
            assert_matches_type(SnapshotStatusResponse, journal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_id` but received ''"):
            await async_client.webhooks_journal.journal.with_raw_response.get_status(
                "",
            )
