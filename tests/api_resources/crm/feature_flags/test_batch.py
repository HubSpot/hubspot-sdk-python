# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import PortalFlagStateBatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        batch = client.crm.feature_flags.batch.delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.batch.with_raw_response.delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.feature_flags.batch.with_streaming_response.delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.batch.with_raw_response.delete(
                flag_name="",
                app_id=0,
                portal_ids=[0],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Hubspot) -> None:
        batch = client.crm.feature_flags.batch.upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "ABSENT",
                    "portal_id": 0,
                }
            ],
        )
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.batch.with_raw_response.upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "ABSENT",
                    "portal_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Hubspot) -> None:
        with client.crm.feature_flags.batch.with_streaming_response.upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "ABSENT",
                    "portal_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.batch.with_raw_response.upsert(
                flag_name="",
                app_id=0,
                portal_states=[
                    {
                        "flag_state": "ABSENT",
                        "portal_id": 0,
                    }
                ],
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.feature_flags.batch.delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.batch.with_raw_response.delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.batch.with_streaming_response.delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.batch.with_raw_response.delete(
                flag_name="",
                app_id=0,
                portal_ids=[0],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.feature_flags.batch.upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "ABSENT",
                    "portal_id": 0,
                }
            ],
        )
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.batch.with_raw_response.upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "ABSENT",
                    "portal_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.batch.with_streaming_response.upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "ABSENT",
                    "portal_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.batch.with_raw_response.upsert(
                flag_name="",
                app_id=0,
                portal_states=[
                    {
                        "flag_state": "ABSENT",
                        "portal_id": 0,
                    }
                ],
            )
