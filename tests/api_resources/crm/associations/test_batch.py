# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import BatchResponsePublicAssociation, BatchResponsePublicAssociationMulti

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        batch = client.crm.associations.batch.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert_matches_type(BatchResponsePublicAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.associations.batch.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.associations.batch.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicAssociation, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.batch.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.batch.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        batch = client.crm.associations.batch.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.associations.batch.with_raw_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.associations.batch.with_streaming_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.batch.with_raw_response.delete(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.batch.with_raw_response.delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        batch = client.crm.associations.batch.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )
        assert_matches_type(BatchResponsePublicAssociationMulti, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.associations.batch.with_raw_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicAssociationMulti, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.associations.batch.with_streaming_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicAssociationMulti, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.batch.with_raw_response.get(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[{"id": "37295"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.batch.with_raw_response.get(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[{"id": "37295"}],
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.associations.batch.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert_matches_type(BatchResponsePublicAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.batch.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.batch.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicAssociation, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.batch.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.batch.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.associations.batch.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.batch.with_raw_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.batch.with_streaming_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.batch.with_raw_response.delete(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.batch.with_raw_response.delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        batch = await async_client.crm.associations.batch.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )
        assert_matches_type(BatchResponsePublicAssociationMulti, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.batch.with_raw_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicAssociationMulti, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.batch.with_streaming_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicAssociationMulti, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.batch.with_raw_response.get(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[{"id": "37295"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.batch.with_raw_response.get(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[{"id": "37295"}],
            )
