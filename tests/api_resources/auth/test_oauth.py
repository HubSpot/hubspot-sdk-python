# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.auth import (
    TokenResponseIf,
    AccessTokenInfoResponse,
    RefreshTokenInfoResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_access_token(self, client: Hubspot) -> None:
        oauth = client.auth.oauth.create_access_token()
        assert_matches_type(TokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_access_token_with_all_params(self, client: Hubspot) -> None:
        oauth = client.auth.oauth.create_access_token(
            query_client_secret="client_secret",
            query_refresh_token="refresh_token",
            client_id="client_id",
            body_client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            grant_type="authorization_code",
            redirect_uri="redirect_uri",
            body_refresh_token="refresh_token",
            scope="scope",
        )
        assert_matches_type(TokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_access_token(self, client: Hubspot) -> None:
        response = client.auth.oauth.with_raw_response.create_access_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(TokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_access_token(self, client: Hubspot) -> None:
        with client.auth.oauth.with_streaming_response.create_access_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(TokenResponseIf, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            oauth = client.auth.oauth.delete_refresh_token(
                "token",
            )

        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.auth.oauth.with_raw_response.delete_refresh_token(
                "token",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with client.auth.oauth.with_streaming_response.delete_refresh_token(
                "token",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                oauth = response.parse()
                assert oauth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
                client.auth.oauth.with_raw_response.delete_refresh_token(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_access_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            oauth = client.auth.oauth.get_access_token(
                "token",
            )

        assert_matches_type(AccessTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_access_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.auth.oauth.with_raw_response.get_access_token(
                "token",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(AccessTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_access_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with client.auth.oauth.with_streaming_response.get_access_token(
                "token",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                oauth = response.parse()
                assert_matches_type(AccessTokenInfoResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_access_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
                client.auth.oauth.with_raw_response.get_access_token(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            oauth = client.auth.oauth.get_refresh_token(
                "token",
            )

        assert_matches_type(RefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.auth.oauth.with_raw_response.get_refresh_token(
                "token",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(RefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with client.auth.oauth.with_streaming_response.get_refresh_token(
                "token",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                oauth = response.parse()
                assert_matches_type(RefreshTokenInfoResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_refresh_token(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
                client.auth.oauth.with_raw_response.get_refresh_token(
                    "",
                )


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_access_token(self, async_client: AsyncHubspot) -> None:
        oauth = await async_client.auth.oauth.create_access_token()
        assert_matches_type(TokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_access_token_with_all_params(self, async_client: AsyncHubspot) -> None:
        oauth = await async_client.auth.oauth.create_access_token(
            query_client_secret="client_secret",
            query_refresh_token="refresh_token",
            client_id="client_id",
            body_client_secret="client_secret",
            code="code",
            code_verifier="code_verifier",
            grant_type="authorization_code",
            redirect_uri="redirect_uri",
            body_refresh_token="refresh_token",
            scope="scope",
        )
        assert_matches_type(TokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_access_token(self, async_client: AsyncHubspot) -> None:
        response = await async_client.auth.oauth.with_raw_response.create_access_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(TokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_access_token(self, async_client: AsyncHubspot) -> None:
        async with async_client.auth.oauth.with_streaming_response.create_access_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(TokenResponseIf, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            oauth = await async_client.auth.oauth.delete_refresh_token(
                "token",
            )

        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.auth.oauth.with_raw_response.delete_refresh_token(
                "token",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.auth.oauth.with_streaming_response.delete_refresh_token(
                "token",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                oauth = await response.parse()
                assert oauth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
                await async_client.auth.oauth.with_raw_response.delete_refresh_token(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_access_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            oauth = await async_client.auth.oauth.get_access_token(
                "token",
            )

        assert_matches_type(AccessTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_access_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.auth.oauth.with_raw_response.get_access_token(
                "token",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(AccessTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_access_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.auth.oauth.with_streaming_response.get_access_token(
                "token",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                oauth = await response.parse()
                assert_matches_type(AccessTokenInfoResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_access_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
                await async_client.auth.oauth.with_raw_response.get_access_token(
                    "",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            oauth = await async_client.auth.oauth.get_refresh_token(
                "token",
            )

        assert_matches_type(RefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.auth.oauth.with_raw_response.get_refresh_token(
                "token",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(RefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.auth.oauth.with_streaming_response.get_refresh_token(
                "token",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                oauth = await response.parse()
                assert_matches_type(RefreshTokenInfoResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_refresh_token(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
                await async_client.auth.oauth.with_raw_response.get_refresh_token(
                    "",
                )
