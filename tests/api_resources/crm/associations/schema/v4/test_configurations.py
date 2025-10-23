# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.associations.schema import (
    BatchResponsePublicAssociationDefinitionUserConfiguration,
    BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
    CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        configuration = client.crm.associations.schema.v4.configurations.list()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_create_by_object_types(self, client: HubSpot) -> None:
        configuration = client.crm.associations.schema.v4.configurations.batch_create_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_create_by_object_types(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.configurations.with_raw_response.batch_create_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_create_by_object_types(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.configurations.with_streaming_response.batch_create_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                BatchResponsePublicAssociationDefinitionUserConfiguration, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch_create_by_object_types(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.batch_create_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.batch_create_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_delete_by_object_types(self, client: HubSpot) -> None:
        configuration = client.crm.associations.schema.v4.configurations.batch_delete_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "category",
                    "type_id": 0,
                }
            ],
        )
        assert configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_delete_by_object_types(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.configurations.with_raw_response.batch_delete_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "category",
                    "type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_delete_by_object_types(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.configurations.with_streaming_response.batch_delete_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "category",
                    "type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch_delete_by_object_types(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.batch_delete_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.batch_delete_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_update_by_object_types(self, client: HubSpot) -> None:
        configuration = client.crm.associations.schema.v4.configurations.batch_update_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        )
        assert_matches_type(
            BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_update_by_object_types(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.configurations.with_raw_response.batch_update_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_update_by_object_types(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.configurations.with_streaming_response.batch_update_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_batch_update_by_object_types(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.batch_update_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.batch_update_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_object_types(self, client: HubSpot) -> None:
        configuration = client.crm.associations.schema.v4.configurations.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_types(self, client: HubSpot) -> None:
        response = client.crm.associations.schema.v4.configurations.with_raw_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_types(self, client: HubSpot) -> None:
        with client.crm.associations.schema.v4.configurations.with_streaming_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_object_types(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.get_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.schema.v4.configurations.with_raw_response.get_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        configuration = await async_client.crm.associations.schema.v4.configurations.list()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.schema.v4.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.schema.v4.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_create_by_object_types(self, async_client: AsyncHubSpot) -> None:
        configuration = await async_client.crm.associations.schema.v4.configurations.batch_create_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_create_by_object_types(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_create_by_object_types(
                to_object_type="toObjectType",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_create_by_object_types(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.crm.associations.schema.v4.configurations.with_streaming_response.batch_create_by_object_types(
                to_object_type="toObjectType",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                BatchResponsePublicAssociationDefinitionUserConfiguration, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch_create_by_object_types(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_create_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_create_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_delete_by_object_types(self, async_client: AsyncHubSpot) -> None:
        configuration = await async_client.crm.associations.schema.v4.configurations.batch_delete_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "category",
                    "type_id": 0,
                }
            ],
        )
        assert configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_delete_by_object_types(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_delete_by_object_types(
                to_object_type="toObjectType",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_delete_by_object_types(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.crm.associations.schema.v4.configurations.with_streaming_response.batch_delete_by_object_types(
                to_object_type="toObjectType",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch_delete_by_object_types(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_delete_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_delete_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_update_by_object_types(self, async_client: AsyncHubSpot) -> None:
        configuration = await async_client.crm.associations.schema.v4.configurations.batch_update_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "HUBSPOT_DEFINED",
                    "max_to_object_ids": 0,
                    "type_id": 0,
                }
            ],
        )
        assert_matches_type(
            BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_update_by_object_types(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_update_by_object_types(
                to_object_type="toObjectType",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_update_by_object_types(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.crm.associations.schema.v4.configurations.with_streaming_response.batch_update_by_object_types(
                to_object_type="toObjectType",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_batch_update_by_object_types(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_update_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.batch_update_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "HUBSPOT_DEFINED",
                        "max_to_object_ids": 0,
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_object_types(self, async_client: AsyncHubSpot) -> None:
        configuration = await async_client.crm.associations.schema.v4.configurations.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_types(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.schema.v4.configurations.with_raw_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_types(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.schema.v4.configurations.with_streaming_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_types(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.get_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.schema.v4.configurations.with_raw_response.get_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
            )
