# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import PortalFlagStateResponse, PortalFlagStateBatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        portal = client.crm.feature_flags.portals.update(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
            flag_state="OFF",
        )
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.portals.with_raw_response.update(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
            flag_state="OFF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.feature_flags.portals.with_streaming_response.update(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
            flag_state="OFF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.portals.with_raw_response.update(
                portal_id=0,
                app_id=0,
                flag_name="",
                flag_state="OFF",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        portal = client.crm.feature_flags.portals.delete(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.portals.with_raw_response.delete(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.feature_flags.portals.with_streaming_response.delete(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.portals.with_raw_response.delete(
                portal_id=0,
                app_id=0,
                flag_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_delete(self, client: Hubspot) -> None:
        portal = client.crm.feature_flags.portals.batch_delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_delete(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.portals.with_raw_response.batch_delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_delete(self, client: Hubspot) -> None:
        with client.crm.feature_flags.portals.with_streaming_response.batch_delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.portals.with_raw_response.batch_delete(
                flag_name="",
                app_id=0,
                portal_ids=[0],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_upsert(self, client: Hubspot) -> None:
        portal = client.crm.feature_flags.portals.batch_upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "OFF",
                    "portal_id": 0,
                }
            ],
        )
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_upsert(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.portals.with_raw_response.batch_upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "OFF",
                    "portal_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_upsert(self, client: Hubspot) -> None:
        with client.crm.feature_flags.portals.with_streaming_response.batch_upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "OFF",
                    "portal_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch_upsert(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.portals.with_raw_response.batch_upsert(
                flag_name="",
                app_id=0,
                portal_states=[
                    {
                        "flag_state": "OFF",
                        "portal_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        portal = client.crm.feature_flags.portals.get(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.portals.with_raw_response.get(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.feature_flags.portals.with_streaming_response.get(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.portals.with_raw_response.get(
                portal_id=0,
                app_id=0,
                flag_name="",
            )


class TestAsyncPortals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        portal = await async_client.crm.feature_flags.portals.update(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
            flag_state="OFF",
        )
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.portals.with_raw_response.update(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
            flag_state="OFF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.portals.with_streaming_response.update(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
            flag_state="OFF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.portals.with_raw_response.update(
                portal_id=0,
                app_id=0,
                flag_name="",
                flag_state="OFF",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        portal = await async_client.crm.feature_flags.portals.delete(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.portals.with_raw_response.delete(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.portals.with_streaming_response.delete(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.portals.with_raw_response.delete(
                portal_id=0,
                app_id=0,
                flag_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_delete(self, async_client: AsyncHubspot) -> None:
        portal = await async_client.crm.feature_flags.portals.batch_delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.portals.with_raw_response.batch_delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.portals.with_streaming_response.batch_delete(
            flag_name="flagName",
            app_id=0,
            portal_ids=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.portals.with_raw_response.batch_delete(
                flag_name="",
                app_id=0,
                portal_ids=[0],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_upsert(self, async_client: AsyncHubspot) -> None:
        portal = await async_client.crm.feature_flags.portals.batch_upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "OFF",
                    "portal_id": 0,
                }
            ],
        )
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_upsert(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.portals.with_raw_response.batch_upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "OFF",
                    "portal_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_upsert(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.portals.with_streaming_response.batch_upsert(
            flag_name="flagName",
            app_id=0,
            portal_states=[
                {
                    "flag_state": "OFF",
                    "portal_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch_upsert(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.portals.with_raw_response.batch_upsert(
                flag_name="",
                app_id=0,
                portal_states=[
                    {
                        "flag_state": "OFF",
                        "portal_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        portal = await async_client.crm.feature_flags.portals.get(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.portals.with_raw_response.get(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.portals.with_streaming_response.get(
            portal_id=0,
            app_id=0,
            flag_name="flagName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalFlagStateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.portals.with_raw_response.get(
                portal_id=0,
                app_id=0,
                flag_name="",
            )
