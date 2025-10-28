# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import BatchResponsePublicDefaultAssociation
from hubspot_sdk.types.crm.associations import (
    BatchResponseVoid,
    BatchResponseLabelsBetweenObjectPair,
    BatchResponsePublicAssociationMultiWithLabel,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        batch = client.crm.associations.v4.batch.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(BatchResponseLabelsBetweenObjectPair, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.batch.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseLabelsBetweenObjectPair, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.associations.v4.batch.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseLabelsBetweenObjectPair, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        batch = client.crm.associations.v4.batch.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": [{"id": "37295"}],
                }
            ],
        )
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.batch.with_raw_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": [{"id": "37295"}],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.associations.v4.batch.with_streaming_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": [{"id": "37295"}],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseVoid, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.delete(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": [{"id": "37295"}],
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": [{"id": "37295"}],
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_default(self, client: HubSpot) -> None:
        batch = client.crm.associations.v4.batch.create_default(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                }
            ],
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_default(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.batch.with_raw_response.create_default(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_default(self, client: HubSpot) -> None:
        with client.crm.associations.v4.batch.with_streaming_response.create_default(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_default(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.create_default(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.create_default(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_labels(self, client: HubSpot) -> None:
        batch = client.crm.associations.v4.batch.delete_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_labels(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.batch.with_raw_response.delete_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_labels(self, client: HubSpot) -> None:
        with client.crm.associations.v4.batch.with_streaming_response.delete_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseVoid, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_labels(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.delete_labels(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.delete_labels(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        batch = client.crm.associations.v4.batch.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponsePublicAssociationMultiWithLabel, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.associations.v4.batch.with_raw_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponsePublicAssociationMultiWithLabel, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.associations.v4.batch.with_streaming_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponsePublicAssociationMultiWithLabel, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.get(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[{"id": "id"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.v4.batch.with_raw_response.get(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[{"id": "id"}],
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.associations.v4.batch.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(BatchResponseLabelsBetweenObjectPair, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.batch.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseLabelsBetweenObjectPair, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.batch.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseLabelsBetweenObjectPair, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.associations.v4.batch.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": [{"id": "37295"}],
                }
            ],
        )
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.batch.with_raw_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": [{"id": "37295"}],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.batch.with_streaming_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": [{"id": "37295"}],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseVoid, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.delete(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": [{"id": "37295"}],
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": [{"id": "37295"}],
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_default(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.associations.v4.batch.create_default(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                }
            ],
        )
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_default(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.batch.with_raw_response.create_default(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_default(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.batch.with_streaming_response.create_default(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicDefaultAssociation, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_default(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.create_default(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.create_default(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_labels(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.associations.v4.batch.delete_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_labels(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.batch.with_raw_response.delete_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseVoid, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_labels(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.batch.with_streaming_response.delete_labels(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "37295"},
                    "to": {"id": "37295"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseVoid, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_labels(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.delete_labels(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.delete_labels(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "37295"},
                        "to": {"id": "37295"},
                        "types": [
                            {
                                "association_category": "HUBSPOT_DEFINED",
                                "association_type_id": 0,
                            }
                        ],
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.crm.associations.v4.batch.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponsePublicAssociationMultiWithLabel, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.v4.batch.with_raw_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponsePublicAssociationMultiWithLabel, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.v4.batch.with_streaming_response.get(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponsePublicAssociationMultiWithLabel, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.get(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[{"id": "id"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.v4.batch.with_raw_response.get(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[{"id": "id"}],
            )
