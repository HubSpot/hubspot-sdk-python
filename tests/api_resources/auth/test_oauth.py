# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.auth import (
    TokenInfoResponseBaseIf,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_token(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = client.auth.oauth.create_token()
        assert oauth.is_closed
        assert oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_token_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = client.auth.oauth.create_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            grant_type="authorization_code",
            redirect_uri="redirect_uri",
            refresh_token="refresh_token",
            scope="scope",
        )
        assert oauth.is_closed
        assert oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_token(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        oauth = client.auth.oauth.with_raw_response.create_token()

        assert oauth.is_closed is True
        assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"
        assert oauth.json() == {"foo": "bar"}
        assert isinstance(oauth, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_token(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.auth.oauth.with_streaming_response.create_token() as oauth:
            assert not oauth.is_closed
            assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"

            assert oauth.json() == {"foo": "bar"}
            assert cast(Any, oauth.is_closed) is True
            assert isinstance(oauth, StreamedBinaryAPIResponse)

        assert cast(Any, oauth.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_introspect_token(self, client: Hubspot) -> None:
        oauth = client.auth.oauth.introspect_token()
        assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_introspect_token_with_all_params(self, client: Hubspot) -> None:
        oauth = client.auth.oauth.introspect_token(
            token="token",
            client_id="client_id",
            client_secret="client_secret",
            token_type_hint="token_type_hint",
        )
        assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_introspect_token(self, client: Hubspot) -> None:
        response = client.auth.oauth.with_raw_response.introspect_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_introspect_token(self, client: Hubspot) -> None:
        with client.auth.oauth.with_streaming_response.introspect_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_revoke_token(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = client.auth.oauth.revoke_token()
        assert oauth.is_closed
        assert oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_revoke_token_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = client.auth.oauth.revoke_token(
            token="token",
            client_id="client_id",
            client_secret="client_secret",
            token_type_hint="token_type_hint",
        )
        assert oauth.is_closed
        assert oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_revoke_token(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        oauth = client.auth.oauth.with_raw_response.revoke_token()

        assert oauth.is_closed is True
        assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"
        assert oauth.json() == {"foo": "bar"}
        assert isinstance(oauth, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_revoke_token(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.auth.oauth.with_streaming_response.revoke_token() as oauth:
            assert not oauth.is_closed
            assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"

            assert oauth.json() == {"foo": "bar"}
            assert cast(Any, oauth.is_closed) is True
            assert isinstance(oauth, StreamedBinaryAPIResponse)

        assert cast(Any, oauth.is_closed) is True


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_token(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = await async_client.auth.oauth.create_token()
        assert oauth.is_closed
        assert await oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_token_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = await async_client.auth.oauth.create_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            grant_type="authorization_code",
            redirect_uri="redirect_uri",
            refresh_token="refresh_token",
            scope="scope",
        )
        assert oauth.is_closed
        assert await oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_token(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        oauth = await async_client.auth.oauth.with_raw_response.create_token()

        assert oauth.is_closed is True
        assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await oauth.json() == {"foo": "bar"}
        assert isinstance(oauth, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_token(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.auth.oauth.with_streaming_response.create_token() as oauth:
            assert not oauth.is_closed
            assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await oauth.json() == {"foo": "bar"}
            assert cast(Any, oauth.is_closed) is True
            assert isinstance(oauth, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, oauth.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_introspect_token(self, async_client: AsyncHubspot) -> None:
        oauth = await async_client.auth.oauth.introspect_token()
        assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_introspect_token_with_all_params(self, async_client: AsyncHubspot) -> None:
        oauth = await async_client.auth.oauth.introspect_token(
            token="token",
            client_id="client_id",
            client_secret="client_secret",
            token_type_hint="token_type_hint",
        )
        assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_introspect_token(self, async_client: AsyncHubspot) -> None:
        response = await async_client.auth.oauth.with_raw_response.introspect_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_introspect_token(self, async_client: AsyncHubspot) -> None:
        async with async_client.auth.oauth.with_streaming_response.introspect_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(TokenInfoResponseBaseIf, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_revoke_token(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = await async_client.auth.oauth.revoke_token()
        assert oauth.is_closed
        assert await oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_revoke_token_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        oauth = await async_client.auth.oauth.revoke_token(
            token="token",
            client_id="client_id",
            client_secret="client_secret",
            token_type_hint="token_type_hint",
        )
        assert oauth.is_closed
        assert await oauth.json() == {"foo": "bar"}
        assert cast(Any, oauth.is_closed) is True
        assert isinstance(oauth, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_revoke_token(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        oauth = await async_client.auth.oauth.with_raw_response.revoke_token()

        assert oauth.is_closed is True
        assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await oauth.json() == {"foo": "bar"}
        assert isinstance(oauth, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_revoke_token(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/oauth/2026-03/token/revoke").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.auth.oauth.with_streaming_response.revoke_token() as oauth:
            assert not oauth.is_closed
            assert oauth.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await oauth.json() == {"foo": "bar"}
            assert cast(Any, oauth.is_closed) is True
            assert isinstance(oauth, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, oauth.is_closed) is True
