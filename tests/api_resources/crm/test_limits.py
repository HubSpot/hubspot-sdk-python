# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    RecordLimitResponse,
    PipelineLimitResponse,
    CustomObjectLimitResponse,
    CustomPropertyLimitResponse,
    AssociationRecordLimitResponse,
    CalculatedPropertyLimitResponse,
    CollectionResponseAssociationLabelLimitResponseNoPaging,
    CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_association_label_limits(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_association_label_limits()
        assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_association_label_limits_with_all_params(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_association_label_limits(
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_association_label_limits(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_association_label_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_association_label_limits(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_association_label_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_association_records_limits_by_object_type(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_association_records_limits_by_object_type(
            to_object_type_id="toObjectTypeId",
            from_object_type_id="fromObjectTypeId",
        )
        assert_matches_type(AssociationRecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_association_records_limits_by_object_type(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_association_records_limits_by_object_type(
            to_object_type_id="toObjectTypeId",
            from_object_type_id="fromObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(AssociationRecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_association_records_limits_by_object_type(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_association_records_limits_by_object_type(
            to_object_type_id="toObjectTypeId",
            from_object_type_id="fromObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(AssociationRecordLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_association_records_limits_by_object_type(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type_id` but received ''"):
            client.crm.limits.with_raw_response.get_association_records_limits_by_object_type(
                to_object_type_id="toObjectTypeId",
                from_object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type_id` but received ''"):
            client.crm.limits.with_raw_response.get_association_records_limits_by_object_type(
                to_object_type_id="",
                from_object_type_id="fromObjectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_association_records_limits_from_objects(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_association_records_limits_from_objects()
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_association_records_limits_from_objects(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_association_records_limits_from_objects()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_association_records_limits_from_objects(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_association_records_limits_from_objects() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_association_records_limits_to_objects(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_association_records_limits_to_objects(
            "fromObjectTypeId",
        )
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_association_records_limits_to_objects(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_association_records_limits_to_objects(
            "fromObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_association_records_limits_to_objects(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_association_records_limits_to_objects(
            "fromObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_association_records_limits_to_objects(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type_id` but received ''"):
            client.crm.limits.with_raw_response.get_association_records_limits_to_objects(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_calculated_property_limits(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_calculated_property_limits()
        assert_matches_type(CalculatedPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_calculated_property_limits(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_calculated_property_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(CalculatedPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_calculated_property_limits(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_calculated_property_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(CalculatedPropertyLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_custom_object_type_limits(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_custom_object_type_limits()
        assert_matches_type(CustomObjectLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_custom_object_type_limits(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_custom_object_type_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(CustomObjectLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_custom_object_type_limits(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_custom_object_type_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(CustomObjectLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_custom_property_limits(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_custom_property_limits()
        assert_matches_type(CustomPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_custom_property_limits(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_custom_property_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(CustomPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_custom_property_limits(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_custom_property_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(CustomPropertyLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pipeline_limits(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_pipeline_limits()
        assert_matches_type(PipelineLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_pipeline_limits(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_pipeline_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(PipelineLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_pipeline_limits(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_pipeline_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(PipelineLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_record_limits(self, client: Hubspot) -> None:
        limit = client.crm.limits.get_record_limits()
        assert_matches_type(RecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_record_limits(self, client: Hubspot) -> None:
        response = client.crm.limits.with_raw_response.get_record_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(RecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_record_limits(self, client: Hubspot) -> None:
        with client.crm.limits.with_streaming_response.get_record_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(RecordLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_association_label_limits(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_association_label_limits()
        assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_association_label_limits_with_all_params(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_association_label_limits(
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_association_label_limits(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_association_label_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_association_label_limits(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.limits.with_streaming_response.get_association_label_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(CollectionResponseAssociationLabelLimitResponseNoPaging, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_association_records_limits_by_object_type(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_association_records_limits_by_object_type(
            to_object_type_id="toObjectTypeId",
            from_object_type_id="fromObjectTypeId",
        )
        assert_matches_type(AssociationRecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_association_records_limits_by_object_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_association_records_limits_by_object_type(
            to_object_type_id="toObjectTypeId",
            from_object_type_id="fromObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(AssociationRecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_association_records_limits_by_object_type(
        self, async_client: AsyncHubspot
    ) -> None:
        async with async_client.crm.limits.with_streaming_response.get_association_records_limits_by_object_type(
            to_object_type_id="toObjectTypeId",
            from_object_type_id="fromObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(AssociationRecordLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_association_records_limits_by_object_type(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type_id` but received ''"):
            await async_client.crm.limits.with_raw_response.get_association_records_limits_by_object_type(
                to_object_type_id="toObjectTypeId",
                from_object_type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type_id` but received ''"):
            await async_client.crm.limits.with_raw_response.get_association_records_limits_by_object_type(
                to_object_type_id="",
                from_object_type_id="fromObjectTypeId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_association_records_limits_from_objects(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_association_records_limits_from_objects()
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_association_records_limits_from_objects(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_association_records_limits_from_objects()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_association_records_limits_from_objects(
        self, async_client: AsyncHubspot
    ) -> None:
        async with (
            async_client.crm.limits.with_streaming_response.get_association_records_limits_from_objects()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_association_records_limits_to_objects(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_association_records_limits_to_objects(
            "fromObjectTypeId",
        )
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_association_records_limits_to_objects(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_association_records_limits_to_objects(
            "fromObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_association_records_limits_to_objects(
        self, async_client: AsyncHubspot
    ) -> None:
        async with async_client.crm.limits.with_streaming_response.get_association_records_limits_to_objects(
            "fromObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_association_records_limits_to_objects(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type_id` but received ''"):
            await async_client.crm.limits.with_raw_response.get_association_records_limits_to_objects(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_calculated_property_limits(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_calculated_property_limits()
        assert_matches_type(CalculatedPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_calculated_property_limits(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_calculated_property_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(CalculatedPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_calculated_property_limits(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.limits.with_streaming_response.get_calculated_property_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(CalculatedPropertyLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_custom_object_type_limits(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_custom_object_type_limits()
        assert_matches_type(CustomObjectLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_custom_object_type_limits(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_custom_object_type_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(CustomObjectLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_custom_object_type_limits(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.limits.with_streaming_response.get_custom_object_type_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(CustomObjectLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_custom_property_limits(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_custom_property_limits()
        assert_matches_type(CustomPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_custom_property_limits(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_custom_property_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(CustomPropertyLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_custom_property_limits(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.limits.with_streaming_response.get_custom_property_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(CustomPropertyLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pipeline_limits(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_pipeline_limits()
        assert_matches_type(PipelineLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_pipeline_limits(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_pipeline_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(PipelineLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_pipeline_limits(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.limits.with_streaming_response.get_pipeline_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(PipelineLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_record_limits(self, async_client: AsyncHubspot) -> None:
        limit = await async_client.crm.limits.get_record_limits()
        assert_matches_type(RecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_record_limits(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.limits.with_raw_response.get_record_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(RecordLimitResponse, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_record_limits(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.limits.with_streaming_response.get_record_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(RecordLimitResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True
