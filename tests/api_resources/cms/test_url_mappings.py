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


class TestURLMappings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/url-mappings/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_mapping = client.cms.url_mappings.create(
            id=0,
            cdn_purge_embargo_time=0,
            content_group_id=0,
            cos_object_type="ACCESS_GROUP_MEMBERSHIP",
            created=0,
            created_by_id=0,
            deleted_at=0,
            destination="destination",
            internally_created=True,
            is_active=True,
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_regex=True,
            is_trailing_slash_optional=True,
            label="label",
            name="name",
            note="note",
            portal_id=0,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=0,
            updated_by_id=0,
        )
        assert url_mapping.is_closed
        assert url_mapping.json() == {"foo": "bar"}
        assert cast(Any, url_mapping.is_closed) is True
        assert isinstance(url_mapping, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/url-mappings/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_mapping = client.cms.url_mappings.with_raw_response.create(
            id=0,
            cdn_purge_embargo_time=0,
            content_group_id=0,
            cos_object_type="ACCESS_GROUP_MEMBERSHIP",
            created=0,
            created_by_id=0,
            deleted_at=0,
            destination="destination",
            internally_created=True,
            is_active=True,
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_regex=True,
            is_trailing_slash_optional=True,
            label="label",
            name="name",
            note="note",
            portal_id=0,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=0,
            updated_by_id=0,
        )

        assert url_mapping.is_closed is True
        assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"
        assert url_mapping.json() == {"foo": "bar"}
        assert isinstance(url_mapping, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/url-mappings/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.url_mappings.with_streaming_response.create(
            id=0,
            cdn_purge_embargo_time=0,
            content_group_id=0,
            cos_object_type="ACCESS_GROUP_MEMBERSHIP",
            created=0,
            created_by_id=0,
            deleted_at=0,
            destination="destination",
            internally_created=True,
            is_active=True,
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_regex=True,
            is_trailing_slash_optional=True,
            label="label",
            name="name",
            note="note",
            portal_id=0,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=0,
            updated_by_id=0,
        ) as url_mapping:
            assert not url_mapping.is_closed
            assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"

            assert url_mapping.json() == {"foo": "bar"}
            assert cast(Any, url_mapping.is_closed) is True
            assert isinstance(url_mapping, StreamedBinaryAPIResponse)

        assert cast(Any, url_mapping.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        url_mapping = client.cms.url_mappings.list()
        assert url_mapping.is_closed
        assert url_mapping.json() == {"foo": "bar"}
        assert cast(Any, url_mapping.is_closed) is True
        assert isinstance(url_mapping, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        url_mapping = client.cms.url_mappings.with_raw_response.list()

        assert url_mapping.is_closed is True
        assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"
        assert url_mapping.json() == {"foo": "bar"}
        assert isinstance(url_mapping, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.url_mappings.with_streaming_response.list() as url_mapping:
            assert not url_mapping.is_closed
            assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"

            assert url_mapping.json() == {"foo": "bar"}
            assert cast(Any, url_mapping.is_closed) is True
            assert isinstance(url_mapping, StreamedBinaryAPIResponse)

        assert cast(Any, url_mapping.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        url_mapping = client.cms.url_mappings.delete(
            0,
        )
        assert url_mapping is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.url_mappings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_mapping = response.parse()
        assert url_mapping is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.url_mappings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_mapping = response.parse()
            assert url_mapping is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_mapping = client.cms.url_mappings.get(
            0,
        )
        assert url_mapping.is_closed
        assert url_mapping.json() == {"foo": "bar"}
        assert cast(Any, url_mapping.is_closed) is True
        assert isinstance(url_mapping, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_mapping = client.cms.url_mappings.with_raw_response.get(
            0,
        )

        assert url_mapping.is_closed is True
        assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"
        assert url_mapping.json() == {"foo": "bar"}
        assert isinstance(url_mapping, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.url_mappings.with_streaming_response.get(
            0,
        ) as url_mapping:
            assert not url_mapping.is_closed
            assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"

            assert url_mapping.json() == {"foo": "bar"}
            assert cast(Any, url_mapping.is_closed) is True
            assert isinstance(url_mapping, StreamedBinaryAPIResponse)

        assert cast(Any, url_mapping.is_closed) is True


class TestAsyncURLMappings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/url-mappings/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_mapping = await async_client.cms.url_mappings.create(
            id=0,
            cdn_purge_embargo_time=0,
            content_group_id=0,
            cos_object_type="ACCESS_GROUP_MEMBERSHIP",
            created=0,
            created_by_id=0,
            deleted_at=0,
            destination="destination",
            internally_created=True,
            is_active=True,
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_regex=True,
            is_trailing_slash_optional=True,
            label="label",
            name="name",
            note="note",
            portal_id=0,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=0,
            updated_by_id=0,
        )
        assert url_mapping.is_closed
        assert await url_mapping.json() == {"foo": "bar"}
        assert cast(Any, url_mapping.is_closed) is True
        assert isinstance(url_mapping, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/url-mappings/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_mapping = await async_client.cms.url_mappings.with_raw_response.create(
            id=0,
            cdn_purge_embargo_time=0,
            content_group_id=0,
            cos_object_type="ACCESS_GROUP_MEMBERSHIP",
            created=0,
            created_by_id=0,
            deleted_at=0,
            destination="destination",
            internally_created=True,
            is_active=True,
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_regex=True,
            is_trailing_slash_optional=True,
            label="label",
            name="name",
            note="note",
            portal_id=0,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=0,
            updated_by_id=0,
        )

        assert url_mapping.is_closed is True
        assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await url_mapping.json() == {"foo": "bar"}
        assert isinstance(url_mapping, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/url-mappings/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.url_mappings.with_streaming_response.create(
            id=0,
            cdn_purge_embargo_time=0,
            content_group_id=0,
            cos_object_type="ACCESS_GROUP_MEMBERSHIP",
            created=0,
            created_by_id=0,
            deleted_at=0,
            destination="destination",
            internally_created=True,
            is_active=True,
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_regex=True,
            is_trailing_slash_optional=True,
            label="label",
            name="name",
            note="note",
            portal_id=0,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=0,
            updated_by_id=0,
        ) as url_mapping:
            assert not url_mapping.is_closed
            assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await url_mapping.json() == {"foo": "bar"}
            assert cast(Any, url_mapping.is_closed) is True
            assert isinstance(url_mapping, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, url_mapping.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        url_mapping = await async_client.cms.url_mappings.list()
        assert url_mapping.is_closed
        assert await url_mapping.json() == {"foo": "bar"}
        assert cast(Any, url_mapping.is_closed) is True
        assert isinstance(url_mapping, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        url_mapping = await async_client.cms.url_mappings.with_raw_response.list()

        assert url_mapping.is_closed is True
        assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await url_mapping.json() == {"foo": "bar"}
        assert isinstance(url_mapping, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.url_mappings.with_streaming_response.list() as url_mapping:
            assert not url_mapping.is_closed
            assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await url_mapping.json() == {"foo": "bar"}
            assert cast(Any, url_mapping.is_closed) is True
            assert isinstance(url_mapping, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, url_mapping.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        url_mapping = await async_client.cms.url_mappings.delete(
            0,
        )
        assert url_mapping is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.url_mappings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_mapping = await response.parse()
        assert url_mapping is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.url_mappings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_mapping = await response.parse()
            assert url_mapping is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_mapping = await async_client.cms.url_mappings.get(
            0,
        )
        assert url_mapping.is_closed
        assert await url_mapping.json() == {"foo": "bar"}
        assert cast(Any, url_mapping.is_closed) is True
        assert isinstance(url_mapping, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_mapping = await async_client.cms.url_mappings.with_raw_response.get(
            0,
        )

        assert url_mapping.is_closed is True
        assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await url_mapping.json() == {"foo": "bar"}
        assert isinstance(url_mapping, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/url-mappings/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.url_mappings.with_streaming_response.get(
            0,
        ) as url_mapping:
            assert not url_mapping.is_closed
            assert url_mapping.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await url_mapping.json() == {"foo": "bar"}
            assert cast(Any, url_mapping.is_closed) is True
            assert isinstance(url_mapping, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, url_mapping.is_closed) is True
