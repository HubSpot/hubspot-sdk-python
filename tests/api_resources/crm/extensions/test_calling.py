# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.crm.extensions import (
    RecordingSettingsResponse,
    CompletedThirdPartyCallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.create(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.with_raw_response.create(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.with_streaming_response.create(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.update(
            app_id=0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.update(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.with_raw_response.update(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.with_streaming_response.update(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.delete(
            0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inbound_call(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
        )
        assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inbound_call_with_all_params(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
                "extension": "extension",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
                "extension": "extension",
            },
            call_started_timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            duration_seconds=0,
            user_id=0,
        )
        assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_inbound_call(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.with_raw_response.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_inbound_call(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.with_streaming_response.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.get(
            0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_ready(self, client: Hubspot) -> None:
        calling = client.crm.extensions.calling.mark_ready(
            engagement_id=0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_ready(self, client: Hubspot) -> None:
        response = client.crm.extensions.calling.with_raw_response.mark_ready(
            engagement_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_ready(self, client: Hubspot) -> None:
        with client.crm.extensions.calling.with_streaming_response.mark_ready(
            engagement_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCalling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.create(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.create(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.create(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.update(
            app_id=0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.update(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.update(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.update(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.delete(
            0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inbound_call(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
        )
        assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inbound_call_with_all_params(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
                "extension": "extension",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
                "extension": "extension",
            },
            call_started_timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            duration_seconds=0,
            user_id=0,
        )
        assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_inbound_call(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_inbound_call(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.create_inbound_call(
            create_engagement=True,
            engagement_properties={"foo": "string"},
            external_call_id="externalCallId",
            final_call_status="BUSY",
            from_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
            potential_recipient_user_ids=[0],
            to_number={
                "e164_number": "e164Number",
                "phone_number_type": "FIXED_LINE",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(CompletedThirdPartyCallResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.get(
            0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.get(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.get(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_ready(self, async_client: AsyncHubspot) -> None:
        calling = await async_client.crm.extensions.calling.mark_ready(
            engagement_id=0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_ready(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.mark_ready(
            engagement_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_ready(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.mark_ready(
            engagement_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True
