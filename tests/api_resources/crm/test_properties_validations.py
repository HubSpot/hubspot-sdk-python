# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    PublicPropertyValidationRule,
    CollectionResponsePublicPropertyValidationRuleNoPaging,
    CollectionResponsePublicPropertyValidationRuleMapNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPropertiesValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id(self, client: HubSpot) -> None:
        properties_validation = client.crm.properties_validations.get_by_object_type_id(
            "objectTypeId",
        )
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleMapNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.properties_validations.with_raw_response.get_by_object_type_id(
            "objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = response.parse()
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleMapNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.properties_validations.with_streaming_response.get_by_object_type_id(
            "objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = response.parse()
            assert_matches_type(
                CollectionResponsePublicPropertyValidationRuleMapNoPaging, properties_validation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_object_type_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.properties_validations.with_raw_response.get_by_object_type_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id_and_property_name(self, client: HubSpot) -> None:
        properties_validation = client.crm.properties_validations.get_by_object_type_id_and_property_name(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_type_id_and_property_name(self, client: HubSpot) -> None:
        response = client.crm.properties_validations.with_raw_response.get_by_object_type_id_and_property_name(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = response.parse()
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_type_id_and_property_name(self, client: HubSpot) -> None:
        with client.crm.properties_validations.with_streaming_response.get_by_object_type_id_and_property_name(
            property_name="propertyName",
            object_type_id="objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = response.parse()
            assert_matches_type(
                CollectionResponsePublicPropertyValidationRuleNoPaging, properties_validation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_object_type_id_and_property_name(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.properties_validations.with_raw_response.get_by_object_type_id_and_property_name(
                property_name="propertyName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties_validations.with_raw_response.get_by_object_type_id_and_property_name(
                property_name="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        properties_validation = client.crm.properties_validations.get_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(PublicPropertyValidationRule, properties_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        response = (
            client.crm.properties_validations.with_raw_response.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="propertyName",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = response.parse()
        assert_matches_type(PublicPropertyValidationRule, properties_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        with (
            client.crm.properties_validations.with_streaming_response.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="propertyName",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = response.parse()
            assert_matches_type(PublicPropertyValidationRule, properties_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.properties_validations.with_raw_response.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="",
                property_name="propertyName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties_validations.with_raw_response.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        properties_validation = client.crm.properties_validations.update_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
            rule_arguments=["string"],
        )
        assert properties_validation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_object_type_id_property_name_and_rule_type_with_all_params(self, client: HubSpot) -> None:
        properties_validation = client.crm.properties_validations.update_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
            rule_arguments=["string"],
            should_apply_normalization=True,
        )
        assert properties_validation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        response = (
            client.crm.properties_validations.with_raw_response.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="propertyName",
                rule_arguments=["string"],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = response.parse()
        assert properties_validation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        with client.crm.properties_validations.with_streaming_response.update_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
            rule_arguments=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = response.parse()
            assert properties_validation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_by_object_type_id_property_name_and_rule_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.properties_validations.with_raw_response.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="",
                property_name="propertyName",
                rule_arguments=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties_validations.with_raw_response.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="",
                rule_arguments=["string"],
            )


class TestAsyncPropertiesValidations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        properties_validation = await async_client.crm.properties_validations.get_by_object_type_id(
            "objectTypeId",
        )
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleMapNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id(
            "objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = await response.parse()
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleMapNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties_validations.with_streaming_response.get_by_object_type_id(
            "objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = await response.parse()
            assert_matches_type(
                CollectionResponsePublicPropertyValidationRuleMapNoPaging, properties_validation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id_and_property_name(self, async_client: AsyncHubSpot) -> None:
        properties_validation = await async_client.crm.properties_validations.get_by_object_type_id_and_property_name(
            property_name="propertyName",
            object_type_id="objectTypeId",
        )
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_type_id_and_property_name(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id_and_property_name(
                property_name="propertyName",
                object_type_id="objectTypeId",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = await response.parse()
        assert_matches_type(
            CollectionResponsePublicPropertyValidationRuleNoPaging, properties_validation, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_type_id_and_property_name(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.crm.properties_validations.with_streaming_response.get_by_object_type_id_and_property_name(
                property_name="propertyName",
                object_type_id="objectTypeId",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = await response.parse()
            assert_matches_type(
                CollectionResponsePublicPropertyValidationRuleNoPaging, properties_validation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_type_id_and_property_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id_and_property_name(
                property_name="propertyName",
                object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id_and_property_name(
                property_name="",
                object_type_id="objectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id_property_name_and_rule_type(self, async_client: AsyncHubSpot) -> None:
        properties_validation = (
            await async_client.crm.properties_validations.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="propertyName",
            )
        )
        assert_matches_type(PublicPropertyValidationRule, properties_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        response = await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = await response.parse()
        assert_matches_type(PublicPropertyValidationRule, properties_validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        async with async_client.crm.properties_validations.with_streaming_response.get_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = await response.parse()
            assert_matches_type(PublicPropertyValidationRule, properties_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="",
                property_name="propertyName",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.get_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        properties_validation = (
            await async_client.crm.properties_validations.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="propertyName",
                rule_arguments=["string"],
            )
        )
        assert properties_validation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_object_type_id_property_name_and_rule_type_with_all_params(
        self, async_client: AsyncHubSpot
    ) -> None:
        properties_validation = (
            await async_client.crm.properties_validations.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="propertyName",
                rule_arguments=["string"],
                should_apply_normalization=True,
            )
        )
        assert properties_validation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        response = await async_client.crm.properties_validations.with_raw_response.update_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
            rule_arguments=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        properties_validation = await response.parse()
        assert properties_validation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        async with async_client.crm.properties_validations.with_streaming_response.update_by_object_type_id_property_name_and_rule_type(
            rule_type="AFTER_DATETIME_DURATION",
            object_type_id="objectTypeId",
            property_name="propertyName",
            rule_arguments=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            properties_validation = await response.parse()
            assert properties_validation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_by_object_type_id_property_name_and_rule_type(
        self, async_client: AsyncHubSpot
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="",
                property_name="propertyName",
                rule_arguments=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties_validations.with_raw_response.update_by_object_type_id_property_name_and_rule_type(
                rule_type="AFTER_DATETIME_DURATION",
                object_type_id="objectTypeId",
                property_name="",
                rule_arguments=["string"],
            )
