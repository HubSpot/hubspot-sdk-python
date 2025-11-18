# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import CollectionResponsePropertyGroupNoPaging
from hubspot_sdk.types.crm import PropertyGroup

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
            display_order=0,
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.groups.with_raw_response.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.cms.media_bridge.groups.with_streaming_response.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(PropertyGroup, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.create(
                object_type="",
                app_id=0,
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.list(
            object_type="objectType",
            app_id=0,
        )
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.groups.with_raw_response.list(
            object_type="objectType",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.media_bridge.groups.with_streaming_response.list(
            object_type="objectType",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(CollectionResponsePropertyGroupNoPaging, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.list(
                object_type="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_name(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.delete_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )
        assert group is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_by_name(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.groups.with_raw_response.delete_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert group is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_name(self, client: Hubspot) -> None:
        with client.cms.media_bridge.groups.with_streaming_response.delete_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_by_name(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.delete_by_name(
                group_name="groupName",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.delete_by_name(
                group_name="",
                app_id=0,
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_name(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.get_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_name(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.groups.with_raw_response.get_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_name(self, client: Hubspot) -> None:
        with client.cms.media_bridge.groups.with_streaming_response.get_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(PropertyGroup, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_name(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.get_by_name(
                group_name="groupName",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.get_by_name(
                group_name="",
                app_id=0,
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_by_name(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_by_name_with_all_params(self, client: Hubspot) -> None:
        group = client.cms.media_bridge.groups.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
            display_order=0,
            label="label",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_by_name(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.groups.with_raw_response.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_by_name(self, client: Hubspot) -> None:
        with client.cms.media_bridge.groups.with_streaming_response.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(PropertyGroup, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_by_name(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.update_by_name(
                group_name="groupName",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            client.cms.media_bridge.groups.with_raw_response.update_by_name(
                group_name="",
                app_id=0,
                object_type="objectType",
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
            display_order=0,
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.groups.with_raw_response.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.groups.with_streaming_response.create(
            object_type="objectType",
            app_id=0,
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(PropertyGroup, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.create(
                object_type="",
                app_id=0,
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.list(
            object_type="objectType",
            app_id=0,
        )
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.groups.with_raw_response.list(
            object_type="objectType",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.groups.with_streaming_response.list(
            object_type="objectType",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(CollectionResponsePropertyGroupNoPaging, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.list(
                object_type="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_name(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.delete_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )
        assert group is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_name(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.groups.with_raw_response.delete_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert group is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_name(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.groups.with_streaming_response.delete_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_by_name(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.delete_by_name(
                group_name="groupName",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.delete_by_name(
                group_name="",
                app_id=0,
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.get_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.groups.with_raw_response.get_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.groups.with_streaming_response.get_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(PropertyGroup, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.get_by_name(
                group_name="groupName",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.get_by_name(
                group_name="",
                app_id=0,
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_by_name(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_by_name_with_all_params(self, async_client: AsyncHubspot) -> None:
        group = await async_client.cms.media_bridge.groups.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
            display_order=0,
            label="label",
        )
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_by_name(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.groups.with_raw_response.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(PropertyGroup, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_by_name(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.groups.with_streaming_response.update_by_name(
            group_name="groupName",
            app_id=0,
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(PropertyGroup, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_by_name(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.update_by_name(
                group_name="groupName",
                app_id=0,
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            await async_client.cms.media_bridge.groups.with_raw_response.update_by_name(
                group_name="",
                app_id=0,
                object_type="objectType",
            )
