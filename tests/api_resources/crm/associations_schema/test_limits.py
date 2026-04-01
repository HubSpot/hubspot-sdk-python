# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
    CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        limit = client.crm.associations_schema.limits.list()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.limits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.associations_schema.limits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_delete(self, client: Hubspot) -> None:
        limit = client.crm.associations_schema.limits.batch_delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "category",
                    "type_id": 0,
                }
            ],
        )
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_delete(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.limits.with_raw_response.batch_delete(
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
        limit = response.parse()
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_delete(self, client: Hubspot) -> None:
        with client.crm.associations_schema.limits.with_streaming_response.batch_delete(
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

            limit = response.parse()
            assert limit is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_batch_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.limits.with_raw_response.batch_delete(
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
            client.crm.associations_schema.limits.with_raw_response.batch_delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_update(self, client: Hubspot) -> None:
        limit = client.crm.associations_schema.limits.batch_update(
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
        assert_matches_type(BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_update(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.limits.with_raw_response.batch_update(
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
        limit = response.parse()
        assert_matches_type(BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_update(self, client: Hubspot) -> None:
        with client.crm.associations_schema.limits.with_streaming_response.batch_update(
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

            limit = response.parse()
            assert_matches_type(
                BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, limit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_batch_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.limits.with_raw_response.batch_update(
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
            client.crm.associations_schema.limits.with_raw_response.batch_update(
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_object_types(self, client: Hubspot) -> None:
        limit = client.crm.associations_schema.limits.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_types(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.limits.with_raw_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_types(self, client: Hubspot) -> None:
        with client.crm.associations_schema.limits.with_streaming_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_object_types(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.limits.with_raw_response.get_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations_schema.limits.with_raw_response.get_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
            )


class TestAsyncLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.associations_schema.limits.list()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.limits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.limits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_delete(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.associations_schema.limits.batch_delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "category": "category",
                    "type_id": 0,
                }
            ],
        )
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.limits.with_raw_response.batch_delete(
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
        limit = await response.parse()
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.limits.with_streaming_response.batch_delete(
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

            limit = await response.parse()
            assert limit is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_batch_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.limits.with_raw_response.batch_delete(
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
            await async_client.crm.associations_schema.limits.with_raw_response.batch_delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "category": "category",
                        "type_id": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_update(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.associations_schema.limits.batch_update(
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
        assert_matches_type(BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.limits.with_raw_response.batch_update(
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
        limit = await response.parse()
        assert_matches_type(BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.limits.with_streaming_response.batch_update(
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

            limit = await response.parse()
            assert_matches_type(
                BatchResponsePublicAssociationDefinitionConfigurationUpdateResult, limit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_batch_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.limits.with_raw_response.batch_update(
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
            await async_client.crm.associations_schema.limits.with_raw_response.batch_update(
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_object_types(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.associations_schema.limits.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_types(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.limits.with_raw_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(
            CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_types(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.limits.with_streaming_response.get_by_object_types(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(
                CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging, limit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_types(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.limits.with_raw_response.get_by_object_types(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations_schema.limits.with_raw_response.get_by_object_types(
                to_object_type="",
                from_object_type="fromObjectType",
            )
