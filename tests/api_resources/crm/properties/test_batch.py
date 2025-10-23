# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import BatchResponseProperty

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        batch = client.crm.properties.batch.create(
            object_type="objectType",
            inputs=[
                {
                    "field_type": "select",
                    "group_name": "contactinformation",
                    "label": "My Contact Property",
                    "name": "my_contact_property",
                    "type": "enumeration",
                }
            ],
        )
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.properties.batch.with_raw_response.create(
            object_type="objectType",
            inputs=[
                {
                    "field_type": "select",
                    "group_name": "contactinformation",
                    "label": "My Contact Property",
                    "name": "my_contact_property",
                    "type": "enumeration",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.properties.batch.with_streaming_response.create(
            object_type="objectType",
            inputs=[
                {
                    "field_type": "select",
                    "group_name": "contactinformation",
                    "label": "My Contact Property",
                    "name": "my_contact_property",
                    "type": "enumeration",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseProperty, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.batch.with_raw_response.create(
                object_type="",
                inputs=[
                    {
                        "field_type": "select",
                        "group_name": "contactinformation",
                        "label": "My Contact Property",
                        "name": "my_contact_property",
                        "type": "enumeration",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        batch = client.crm.properties.batch.delete(
            object_type="objectType",
            inputs=[{"name": "my_custom_property"}],
        )
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.properties.batch.with_raw_response.delete(
            object_type="objectType",
            inputs=[{"name": "my_custom_property"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.properties.batch.with_streaming_response.delete(
            object_type="objectType",
            inputs=[{"name": "my_custom_property"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.batch.with_raw_response.delete(
                object_type="",
                inputs=[{"name": "my_custom_property"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        batch = client.crm.properties.batch.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        batch = client.crm.properties.batch.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
            data_sensitivity="non_sensitive",
        )
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.crm.properties.batch.with_raw_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.crm.properties.batch.with_streaming_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseProperty, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.batch.with_raw_response.read(
                object_type="",
                archived=True,
                inputs=[{"name": "my_custom_property"}],
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.properties.batch.create(
            object_type="objectType",
            inputs=[
                {
                    "field_type": "select",
                    "group_name": "contactinformation",
                    "label": "My Contact Property",
                    "name": "my_contact_property",
                    "type": "enumeration",
                }
            ],
        )
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.batch.with_raw_response.create(
            object_type="objectType",
            inputs=[
                {
                    "field_type": "select",
                    "group_name": "contactinformation",
                    "label": "My Contact Property",
                    "name": "my_contact_property",
                    "type": "enumeration",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.batch.with_streaming_response.create(
            object_type="objectType",
            inputs=[
                {
                    "field_type": "select",
                    "group_name": "contactinformation",
                    "label": "My Contact Property",
                    "name": "my_contact_property",
                    "type": "enumeration",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseProperty, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.batch.with_raw_response.create(
                object_type="",
                inputs=[
                    {
                        "field_type": "select",
                        "group_name": "contactinformation",
                        "label": "My Contact Property",
                        "name": "my_contact_property",
                        "type": "enumeration",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.properties.batch.delete(
            object_type="objectType",
            inputs=[{"name": "my_custom_property"}],
        )
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.batch.with_raw_response.delete(
            object_type="objectType",
            inputs=[{"name": "my_custom_property"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.batch.with_streaming_response.delete(
            object_type="objectType",
            inputs=[{"name": "my_custom_property"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.batch.with_raw_response.delete(
                object_type="",
                inputs=[{"name": "my_custom_property"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.properties.batch.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.properties.batch.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
            data_sensitivity="non_sensitive",
        )
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.batch.with_raw_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseProperty, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.batch.with_streaming_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseProperty, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.batch.with_raw_response.read(
                object_type="",
                archived=True,
                inputs=[{"name": "my_custom_property"}],
            )
