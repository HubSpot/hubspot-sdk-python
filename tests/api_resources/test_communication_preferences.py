# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.communication_preferences import (
    LinkGenerationResponse,
    ActionResponseWithResultsPublicStatus,
    ActionResponseWithResultsPublicWideStatus,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommunicationPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_links(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )
        assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_links_with_all_params(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
            business_unit_id=0,
            language="language",
            subscription_id=0,
        )
        assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_links(self, client: Hubspot) -> None:
        response = client.communication_preferences.with_raw_response.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = response.parse()
        assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_links(self, client: Hubspot) -> None:
        with client.communication_preferences.with_streaming_response.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = response.parse()
            assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_statuses(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_statuses_with_all_params(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_statuses(self, client: Hubspot) -> None:
        response = client.communication_preferences.with_raw_response.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_statuses(self, client: Hubspot) -> None:
        with client.communication_preferences.with_streaming_response.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_statuses(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.communication_preferences.with_raw_response.get_statuses(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status_with_all_params(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        response = client.communication_preferences.with_raw_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        with client.communication_preferences.with_streaming_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_unsubscribe_all_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.communication_preferences.with_raw_response.get_unsubscribe_all_status(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unsubscribe_all(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unsubscribe_all_with_all_params(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe_all(self, client: Hubspot) -> None:
        response = client.communication_preferences.with_raw_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe_all(self, client: Hubspot) -> None:
        with client.communication_preferences.with_streaming_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unsubscribe_all(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.communication_preferences.with_raw_response.unsubscribe_all(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: Hubspot) -> None:
        communication_preference = client.communication_preferences.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
            legal_basis="CONSENT_WITH_NOTICE",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Hubspot) -> None:
        response = client.communication_preferences.with_raw_response.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Hubspot) -> None:
        with client.communication_preferences.with_streaming_response.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.communication_preferences.with_raw_response.update_status(
                subscriber_id_string="",
                channel="EMAIL",
                status_state="NOT_SPECIFIED",
                subscription_id=0,
            )


class TestAsyncCommunicationPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_links(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )
        assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_links_with_all_params(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
            business_unit_id=0,
            language="language",
            subscription_id=0,
        )
        assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_links(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.with_raw_response.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = await response.parse()
        assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_links(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.with_streaming_response.generate_links(
            channel="EMAIL",
            subscriber_id_string="subscriberIdString",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = await response.parse()
            assert_matches_type(LinkGenerationResponse, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_statuses(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_statuses_with_all_params(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_statuses(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.with_raw_response.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_statuses(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.with_streaming_response.get_statuses(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_statuses(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.communication_preferences.with_raw_response.get_statuses(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status_with_all_params(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.with_raw_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.with_streaming_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicWideStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_unsubscribe_all_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.communication_preferences.with_raw_response.get_unsubscribe_all_status(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all_with_all_params(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.with_raw_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.with_streaming_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unsubscribe_all(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.communication_preferences.with_raw_response.unsubscribe_all(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncHubspot) -> None:
        communication_preference = await async_client.communication_preferences.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
            legal_basis="CONSENT_WITH_NOTICE",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.communication_preferences.with_raw_response.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        communication_preference = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.communication_preferences.with_streaming_response.update_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="NOT_SPECIFIED",
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            communication_preference = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, communication_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.communication_preferences.with_raw_response.update_status(
                subscriber_id_string="",
                channel="EMAIL",
                status_state="NOT_SPECIFIED",
                subscription_id=0,
            )
