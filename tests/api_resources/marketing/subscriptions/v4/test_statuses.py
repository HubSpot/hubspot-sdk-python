# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing.subscriptions import (
    BatchResponsePublicStatus,
    ActionResponseWithResultsPublicStatus,
    BatchResponsePublicStatusBulkResponse,
    ActionResponseWithResultsPublicWideStatus,
    BatchResponsePublicWideStatusBulkResponse,
    BatchResponsePublicBulkOptOutFromAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
            legal_basis="CONSENT_WITH_NOTICE",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.update(
                subscriber_id_string="",
                channel="EMAIL",
                status_state="NOT_SPECIFIED",
                subscription_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_get(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_get(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_get(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.batch_get(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_get(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_get(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_get_unsubscribe_all_status(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get_unsubscribe_all_status_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_get_unsubscribe_all_status(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.batch_get_unsubscribe_all_status(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_get_unsubscribe_all_status(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_unsubscribe_all(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_unsubscribe_all_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_unsubscribe_all(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_unsubscribe_all(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_update(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.batch_update(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_update(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.batch_update(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_update(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_update(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.get(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_all(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_all_with_all_params(self, client: Hubspot) -> None:
        status = client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe_all(self, client: Hubspot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe_all(self, client: Hubspot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unsubscribe_all(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
                subscriber_id_string="",
                channel="EMAIL",
            )


class TestAsyncStatuses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
            legal_basis="CONSENT_WITH_NOTICE",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.update(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.update(
                subscriber_id_string="",
                channel="EMAIL",
                status_state="NOT_SPECIFIED",
                subscription_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_get(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_get(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.batch_get(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_get(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_get_unsubscribe_all_status(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get_unsubscribe_all_status_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_get_unsubscribe_all_status(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        response = (
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.batch_get_unsubscribe_all_status(
                channel="EMAIL",
                inputs=["string"],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_get_unsubscribe_all_status(
                channel="EMAIL",
                inputs=["string"],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_unsubscribe_all_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_unsubscribe_all(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_update(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.batch_update(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.batch_update(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.batch_update(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "NOT_SPECIFIED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all_with_all_params(self, async_client: AsyncHubspot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
                subscriber_id_string="",
                channel="EMAIL",
            )
