# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    CollectionResponseAssociationSpecWithLabelNoPaging,
    BatchResponsePublicAssociationDefinitionUserConfiguration,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_create(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.batch_create(
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
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_create(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.labels.with_raw_response.batch_create(
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
        label = response.parse()
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_create(self, client: Hubspot) -> None:
        with client.crm.associations_schema.labels.with_streaming_response.batch_create(
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

            label = response.parse()
            assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_batch_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.batch_create(
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
            client.crm.associations_schema.labels.with_raw_response.batch_create(
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
    def test_method_create_label(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_label_with_all_params(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
            inverse_label="inverseLabel",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_label(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.labels.with_raw_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_label(self, client: Hubspot) -> None:
        with client.crm.associations_schema.labels.with_streaming_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_label(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.create_label(
                to_object_type="toObjectType",
                from_object_type="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.create_label(
                to_object_type="",
                from_object_type="fromObjectType",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_label(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_label(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.labels.with_raw_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_label(self, client: Hubspot) -> None:
        with client.crm.associations_schema.labels.with_streaming_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_label(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="fromObjectType",
                to_object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_labels(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_labels(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.labels.with_raw_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_labels(self, client: Hubspot) -> None:
        with client.crm.associations_schema.labels.with_streaming_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_labels(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.list_labels(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.list_labels(
                to_object_type="",
                from_object_type="fromObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_label(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_label_with_all_params(self, client: Hubspot) -> None:
        label = client.crm.associations_schema.labels.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
            inverse_label="inverseLabel",
        )
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_label(self, client: Hubspot) -> None:
        response = client.crm.associations_schema.labels.with_raw_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_label(self, client: Hubspot) -> None:
        with client.crm.associations_schema.labels.with_streaming_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_label(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.update_label(
                to_object_type="toObjectType",
                from_object_type="",
                association_type_id=0,
                label="label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations_schema.labels.with_raw_response.update_label(
                to_object_type="",
                from_object_type="fromObjectType",
                association_type_id=0,
                label="label",
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_create(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.batch_create(
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
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.labels.with_raw_response.batch_create(
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
        label = await response.parse()
        assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.labels.with_streaming_response.batch_create(
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

            label = await response.parse()
            assert_matches_type(BatchResponsePublicAssociationDefinitionUserConfiguration, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_batch_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.batch_create(
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
            await async_client.crm.associations_schema.labels.with_raw_response.batch_create(
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
    async def test_method_create_label(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_label_with_all_params(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
            inverse_label="inverseLabel",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_label(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.labels.with_raw_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_label(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.labels.with_streaming_response.create_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_label(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.create_label(
                to_object_type="toObjectType",
                from_object_type="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.create_label(
                to_object_type="",
                from_object_type="fromObjectType",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_label(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_label(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.labels.with_raw_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_label(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.labels.with_streaming_response.delete_label(
            association_type_id=0,
            from_object_type="fromObjectType",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_label(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.delete_label(
                association_type_id=0,
                from_object_type="fromObjectType",
                to_object_type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_labels(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_labels(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.labels.with_raw_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_labels(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.labels.with_streaming_response.list_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(CollectionResponseAssociationSpecWithLabelNoPaging, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_labels(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.list_labels(
                to_object_type="toObjectType",
                from_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.list_labels(
                to_object_type="",
                from_object_type="fromObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_label(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_label_with_all_params(self, async_client: AsyncHubspot) -> None:
        label = await async_client.crm.associations_schema.labels.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
            inverse_label="inverseLabel",
        )
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_label(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations_schema.labels.with_raw_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert label is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_label(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations_schema.labels.with_streaming_response.update_label(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            association_type_id=0,
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert label is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_label(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.update_label(
                to_object_type="toObjectType",
                from_object_type="",
                association_type_id=0,
                label="label",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations_schema.labels.with_raw_response.update_label(
                to_object_type="",
                from_object_type="fromObjectType",
                association_type_id=0,
                label="label",
            )
