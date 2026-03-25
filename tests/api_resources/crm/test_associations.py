# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    ReportCreationResponse,
    LabelsBetweenObjectPair,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_associations(self, client: Hubspot) -> None:
        association = client.crm.associations.delete_associations(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_associations(self, client: Hubspot) -> None:
        response = client.crm.associations.with_raw_response.delete_associations(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_associations(self, client: Hubspot) -> None:
        with client.crm.associations.with_streaming_response.delete_associations(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_associations(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.with_raw_response.delete_associations(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.with_raw_response.delete_associations(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.delete_associations(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.with_raw_response.delete_associations(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_high_usage_report(self, client: Hubspot) -> None:
        association = client.crm.associations.request_high_usage_report(
            0,
        )
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_high_usage_report(self, client: Hubspot) -> None:
        response = client.crm.associations.with_raw_response.request_high_usage_report(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_high_usage_report(self, client: Hubspot) -> None:
        with client.crm.associations.with_streaming_response.request_high_usage_report(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(ReportCreationResponse, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_association_labels(self, client: Hubspot) -> None:
        association = client.crm.associations.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_association_labels(self, client: Hubspot) -> None:
        response = client.crm.associations.with_raw_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_association_labels(self, client: Hubspot) -> None:
        with client.crm.associations.with_streaming_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_association_labels(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )


class TestAsyncAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_associations(self, async_client: AsyncHubspot) -> None:
        association = await async_client.crm.associations.delete_associations(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_associations(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.with_raw_response.delete_associations(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_associations(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.with_streaming_response.delete_associations(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_associations(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.delete_associations(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.delete_associations(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.delete_associations(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.delete_associations(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_high_usage_report(self, async_client: AsyncHubspot) -> None:
        association = await async_client.crm.associations.request_high_usage_report(
            0,
        )
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_high_usage_report(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.with_raw_response.request_high_usage_report(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(ReportCreationResponse, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_high_usage_report(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.with_streaming_response.request_high_usage_report(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(ReportCreationResponse, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_association_labels(self, async_client: AsyncHubspot) -> None:
        association = await async_client.crm.associations.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_association_labels(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.with_raw_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_association_labels(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.with_streaming_response.update_association_labels(
            to_object_id="toObjectId",
            object_type="objectType",
            object_id="objectId",
            to_object_type="toObjectType",
            body=[
                {
                    "association_category": "HUBSPOT_DEFINED",
                    "association_type_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(LabelsBetweenObjectPair, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_association_labels(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="toObjectId",
                object_type="objectType",
                object_id="objectId",
                to_object_type="",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_id` but received ''"):
            await async_client.crm.associations.with_raw_response.update_association_labels(
                to_object_id="",
                object_type="objectType",
                object_id="objectId",
                to_object_type="toObjectType",
                body=[
                    {
                        "association_category": "HUBSPOT_DEFINED",
                        "association_type_id": 0,
                    }
                ],
            )
