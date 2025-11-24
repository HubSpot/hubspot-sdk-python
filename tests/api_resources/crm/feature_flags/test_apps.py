# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import FlagResponse, PortalFlagStateBatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        app = client.crm.feature_flags.apps.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        app = client.crm.feature_flags.apps.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
            override_state="ABSENT",
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.apps.with_raw_response.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.feature_flags.apps.with_streaming_response.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(FlagResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.apps.with_raw_response.update(
                flag_name="",
                app_id=0,
                default_state="ABSENT",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        app = client.crm.feature_flags.apps.delete(
            flag_name="flagName",
            app_id=0,
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.apps.with_raw_response.delete(
            flag_name="flagName",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.feature_flags.apps.with_streaming_response.delete(
            flag_name="flagName",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(FlagResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.apps.with_raw_response.delete(
                flag_name="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        app = client.crm.feature_flags.apps.get(
            flag_name="flagName",
            app_id=0,
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.apps.with_raw_response.get(
            flag_name="flagName",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.feature_flags.apps.with_streaming_response.get(
            flag_name="flagName",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(FlagResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.apps.with_raw_response.get(
                flag_name="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_portals(self, client: Hubspot) -> None:
        app = client.crm.feature_flags.apps.list_portals(
            flag_name="flagName",
            app_id=0,
        )
        assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_portals_with_all_params(self, client: Hubspot) -> None:
        app = client.crm.feature_flags.apps.list_portals(
            flag_name="flagName",
            app_id=0,
            limit=0,
            start_portal_id=0,
        )
        assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_portals(self, client: Hubspot) -> None:
        response = client.crm.feature_flags.apps.with_raw_response.list_portals(
            flag_name="flagName",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_portals(self, client: Hubspot) -> None:
        with client.crm.feature_flags.apps.with_streaming_response.list_portals(
            flag_name="flagName",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_portals(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            client.crm.feature_flags.apps.with_raw_response.list_portals(
                flag_name="",
                app_id=0,
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        app = await async_client.crm.feature_flags.apps.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        app = await async_client.crm.feature_flags.apps.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
            override_state="ABSENT",
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.apps.with_raw_response.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.apps.with_streaming_response.update(
            flag_name="flagName",
            app_id=0,
            default_state="ABSENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(FlagResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.apps.with_raw_response.update(
                flag_name="",
                app_id=0,
                default_state="ABSENT",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        app = await async_client.crm.feature_flags.apps.delete(
            flag_name="flagName",
            app_id=0,
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.apps.with_raw_response.delete(
            flag_name="flagName",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.apps.with_streaming_response.delete(
            flag_name="flagName",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(FlagResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.apps.with_raw_response.delete(
                flag_name="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        app = await async_client.crm.feature_flags.apps.get(
            flag_name="flagName",
            app_id=0,
        )
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.apps.with_raw_response.get(
            flag_name="flagName",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(FlagResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.apps.with_streaming_response.get(
            flag_name="flagName",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(FlagResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.apps.with_raw_response.get(
                flag_name="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_portals(self, async_client: AsyncHubspot) -> None:
        app = await async_client.crm.feature_flags.apps.list_portals(
            flag_name="flagName",
            app_id=0,
        )
        assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_portals_with_all_params(self, async_client: AsyncHubspot) -> None:
        app = await async_client.crm.feature_flags.apps.list_portals(
            flag_name="flagName",
            app_id=0,
            limit=0,
            start_portal_id=0,
        )
        assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_portals(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.feature_flags.apps.with_raw_response.list_portals(
            flag_name="flagName",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_portals(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.feature_flags.apps.with_streaming_response.list_portals(
            flag_name="flagName",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(PortalFlagStateBatchResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_portals(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flag_name` but received ''"):
            await async_client.crm.feature_flags.apps.with_raw_response.list_portals(
                flag_name="",
                app_id=0,
            )
