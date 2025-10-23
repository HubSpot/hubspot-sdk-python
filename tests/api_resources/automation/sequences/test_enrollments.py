# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.automation import PublicSequenceEnrollmentResponse, PublicSequenceEnrollmentLiteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrollments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enroll(self, client: HubSpot) -> None:
        enrollment = client.automation.sequences.enrollments.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
        )
        assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enroll_with_all_params(self, client: HubSpot) -> None:
        enrollment = client.automation.sequences.enrollments.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
            sender_alias_address="senderAliasAddress",
        )
        assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enroll(self, client: HubSpot) -> None:
        response = client.automation.sequences.enrollments.with_raw_response.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enroll(self, client: HubSpot) -> None:
        with client.automation.sequences.enrollments.with_streaming_response.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_contact_id(self, client: HubSpot) -> None:
        enrollment = client.automation.sequences.enrollments.get_by_contact_id(
            "contactId",
        )
        assert_matches_type(PublicSequenceEnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_contact_id(self, client: HubSpot) -> None:
        response = client.automation.sequences.enrollments.with_raw_response.get_by_contact_id(
            "contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(PublicSequenceEnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_contact_id(self, client: HubSpot) -> None:
        with client.automation.sequences.enrollments.with_streaming_response.get_by_contact_id(
            "contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(PublicSequenceEnrollmentResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_contact_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.automation.sequences.enrollments.with_raw_response.get_by_contact_id(
                "",
            )


class TestAsyncEnrollments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enroll(self, async_client: AsyncHubSpot) -> None:
        enrollment = await async_client.automation.sequences.enrollments.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
        )
        assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enroll_with_all_params(self, async_client: AsyncHubSpot) -> None:
        enrollment = await async_client.automation.sequences.enrollments.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
            sender_alias_address="senderAliasAddress",
        )
        assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enroll(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.sequences.enrollments.with_raw_response.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enroll(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.sequences.enrollments.with_streaming_response.enroll(
            contact_id="contactId",
            sender_email="senderEmail",
            sequence_id="sequenceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(PublicSequenceEnrollmentLiteResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_contact_id(self, async_client: AsyncHubSpot) -> None:
        enrollment = await async_client.automation.sequences.enrollments.get_by_contact_id(
            "contactId",
        )
        assert_matches_type(PublicSequenceEnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_contact_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.sequences.enrollments.with_raw_response.get_by_contact_id(
            "contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(PublicSequenceEnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_contact_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.sequences.enrollments.with_streaming_response.get_by_contact_id(
            "contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(PublicSequenceEnrollmentResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_contact_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.automation.sequences.enrollments.with_raw_response.get_by_contact_id(
                "",
            )
