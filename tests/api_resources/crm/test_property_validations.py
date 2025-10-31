# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import PropertyValidationGetResponse, PropertyValidationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPropertyValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        property_validation = client.crm.property_validations.list(
            "objectTypeId",
        )
        assert_matches_type(PropertyValidationListResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.property_validations.with_raw_response.list(
            "objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property_validation = response.parse()
        assert_matches_type(PropertyValidationListResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.property_validations.with_streaming_response.list(
            "objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property_validation = response.parse()
            assert_matches_type(PropertyValidationListResponse, property_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.property_validations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        property_validation = client.crm.property_validations.get(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(PropertyValidationGetResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.property_validations.with_raw_response.get(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property_validation = response.parse()
        assert_matches_type(PropertyValidationGetResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.property_validations.with_streaming_response.get(
            property_name="propertyName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property_validation = response.parse()
            assert_matches_type(PropertyValidationGetResponse, property_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.property_validations.with_raw_response.get(
                property_name="propertyName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.property_validations.with_raw_response.get(
                property_name="",
                object_type_id="objectTypeId",
            )


class TestAsyncPropertyValidations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        property_validation = await async_client.crm.property_validations.list(
            "objectTypeId",
        )
        assert_matches_type(PropertyValidationListResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.property_validations.with_raw_response.list(
            "objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property_validation = await response.parse()
        assert_matches_type(PropertyValidationListResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.property_validations.with_streaming_response.list(
            "objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property_validation = await response.parse()
            assert_matches_type(PropertyValidationListResponse, property_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.property_validations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        property_validation = await async_client.crm.property_validations.get(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(PropertyValidationGetResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.property_validations.with_raw_response.get(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property_validation = await response.parse()
        assert_matches_type(PropertyValidationGetResponse, property_validation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.property_validations.with_streaming_response.get(
            property_name="propertyName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property_validation = await response.parse()
            assert_matches_type(PropertyValidationGetResponse, property_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.property_validations.with_raw_response.get(
                property_name="propertyName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.property_validations.with_raw_response.get(
                property_name="",
                object_type_id="objectTypeId",
            )
